from flask import (
    Flask,
    render_template,
    abort,
    send_from_directory,
    Response,
    request,
    redirect,
)
import requests
from .classes.git import Git
from .classes.markdown import RelativeURLRewriter
import logging
import os
import base64
import mimetypes
import html
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)


@app.route("/")
def index() -> Response:
    """Route for the index page.

    Returns:
        str: The rendered template for the index page.
    """
    return render_template("index.html")


@app.route("/assets/<path:path>")
def send_assets(path: str) -> Response:
    """Route for serving static assets.

    Args:
        path (str): The path to the asset file.

    Returns:
        Response: A response containing the asset file.
    """
    return send_from_directory(Path(__file__).parent / "assets", path)


@app.route("/<owner>/<repo>/", methods=["GET"])
@app.route("/<owner>/<repo>/tree/main/", methods=["GET"])
@app.route("/<owner>/<repo>/tree/main/<path:path>", methods=["GET"])
def get_tree(owner: str, repo: str, path: str = "") -> Response:
    """Route for getting the directory structure of a repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        path (str): The path within the repository.

    Returns:
        str: The rendered template for the directory structure.
    """
    path = path.lstrip("/")
    logger.debug(f"Path: {path}")

    repo_url = f"https://github.com/{owner}/{repo}.git"
    git = Git(repo_url)

    try:
        directory_structure = git.get_directory_structure(path)
        filtered_structure = directory_structure

        logger.debug(f"Filtered structure: {filtered_structure}")

        # Separate files and directories
        directories = sorted(
            list(
                set(
                    [
                        entry.split("/")[0]
                        for entry in filtered_structure
                        if "/" in entry
                    ]
                )
            )
        )

        files = [entry for entry in filtered_structure if "/" not in entry]

        # Get README.md content if it exists
        readme_content = None

        if "README.md" in files:
            readme_md = git.get_file_content(f"{path}/README.md")
            base_url = f"/{owner}/{repo}/raw/main/{path}".rstrip("/")
            readme_content = RelativeURLRewriter(base_url).convert(
                readme_md.decode("utf-8")
            )

        return render_template(
            "path.html",
            owner=owner,
            repo=repo,
            path=path,
            directories=directories,
            files=files,
            readme_content=readme_content,
        )
    except Exception as e:
        logger.error(
            f"Error getting directory structure for {path} in {owner}/{repo}: {e}"
        )
        abort(404, description=str(e))


@app.route("/<owner>/<repo>/raw/main/<path:file_path>", methods=["GET"])
def get_raw(owner: str, repo: str, file_path: str) -> Response:
    """Route for getting the raw content of a file.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        file_path (str): The path of the file.

    Returns:
        Response: A response containing the raw content of the file.
    """
    repo_url = f"https://github.com/{owner}/{repo}.git"
    git = Git(repo_url)
    try:
        file_content = git.get_file_content(file_path)
        try:
            file_content = file_content.decode("utf-8")
            content_type = "text/plain"
        except UnicodeDecodeError:
            content_type = "application/octet-stream"

        content_type, _ = mimetypes.guess_type(file_path)

        file_name = file_path.split("/")[-1]

        headers = {
            "Content-Type": content_type,
            "Content-Disposition": f"attachment; filename={file_name}",
        }

        return file_content, 200, headers
    except Exception as e:
        logger.error(
            f"Error getting file content for {file_path} in {owner}/{repo}: {e}"
        )
        abort(404, description=str(e))


@app.route("/<owner>/<repo>/blob/main/<path:file_path>", methods=["GET"])
def preview_file(owner: str, repo: str, file_path: str):
    """Route for previewing a file.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        file_path (str): The path of the file.

    Returns:
        str: The rendered template for the file preview.
    """
    repo_url = f"https://github.com/{owner}/{repo}.git"
    git = Git(repo_url)
    try:
        file_content = git.get_file_content(file_path)

        content_type, _ = mimetypes.guess_type(file_path)

        try:
            file_content.decode("utf-8")
            is_text = True
        except UnicodeDecodeError:
            is_text = False

        is_image = content_type and content_type.startswith("image")
        is_raw = True

        if content_type == "text/markdown":
            base_url = f"/{owner}/{repo}/raw/main/{'/'.join(file_path.split('/')[:-1])}".rstrip(
                "/"
            )
            file_content = RelativeURLRewriter(base_url).convert(
                file_content.decode("utf-8")
            )
            is_raw = False

        elif is_text:
            file_content = file_content.decode("utf-8")
            file_content = html.escape(file_content)

        if is_image:
            file_content = base64.b64encode(file_content).decode("utf-8")

        return render_template(
            "preview.html",
            owner=owner,
            repo=repo,
            file_path=file_path,
            file_content=file_content,
            is_text=is_text,
            is_image=is_image,
            is_raw=is_raw,
        )
    except Exception as e:
        logger.error(f"Error previewing file {file_path} in {owner}/{repo}: {e}")
        abort(404, description=str(e))


@app.route("/<path:subpath>.git", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route(
    "/<path:subpath>.git/<path:extra>",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
)
def proxy_git(subpath, extra=None):
    """Route for proxying Git client requests to GitHub.

    Args:
        subpath (str): The subpath of the request.
        extra (str): An optional extra path after .git.

    Returns:
        Response: A response from the repository on GitHub.
    """
    path = f"{subpath}.git"
    if extra:
        path += f"/{extra}"
    github_url = f"https://github.com/{path}"

    logger.debug(f"Proxying Git request to {github_url}")

    resp = requests.request(
        method=request.method,
        url=github_url,
        headers={
            key: value
            for (key, value) in request.headers.items()
            if key.lower() != "host"
            and not key.lower().startswith("x-forwarded")
            and not key.lower().startswith("forwarded")
        },
        data=request.get_data(),
        cookies=request.cookies,
        params=request.args,
        allow_redirects=False,
        stream=True,
    )

    # Those headers shouldn't be passed directly to the client
    excluded_headers = [
        "content-length",
        "content-encoding",
        "transfer-encoding",
        "connection",
    ]

    headers = [
        (name, value)
        for (name, value) in resp.raw.headers.items()
        if name.lower() not in excluded_headers
    ]

    return Response(resp.raw, status=resp.status_code, headers=dict(headers))


@app.before_request
def catch_git_requests():
    if "git/" in request.headers.get("User-Agent", ""):
        try:
            path = request.path.lstrip("/")
            path = path.split("/")
            return proxy_git("/".join(path[:2]), "/".join(path[2:]) or None)
        except Exception as e:
            logger.error(f"Error proxying Git request: {e}")
            abort(404, description=str(e))


def main():
    """Main function to run the Flask app."""
    port = os.environ.get("PORT", 8107)
    host = os.environ.get("HOST", "127.0.0.1")
    app.run(debug=True, port=port, host=host)


if __name__ == "__main__":
    main()
