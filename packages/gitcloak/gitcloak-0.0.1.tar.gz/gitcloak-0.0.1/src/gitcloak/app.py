from flask import Flask, render_template, abort, send_from_directory
from .classes.git import Git
from .classes.markdown import RelativeURLRewriter
import logging
import os
import base64
import mimetypes
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory(Path(__file__).parent / "assets", path)


@app.route("/<owner>/<repo>/", methods=["GET"])
@app.route("/<owner>/<repo>/tree/main/", methods=["GET"])
@app.route("/<owner>/<repo>/tree/main/<path:path>", methods=["GET"])
def get_tree(owner, repo, path=""):
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

        if f"README.md" in files:
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
def get_raw(owner, repo, file_path):
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
def preview_file(owner, repo, file_path):
    repo_url = f"https://github.com/{owner}/{repo}.git"
    git = Git(repo_url)
    try:
        file_content = git.get_file_content(file_path)

        content_type, _ = mimetypes.guess_type(file_path)
        is_text = content_type and content_type.startswith("text")
        is_image = content_type and content_type.startswith("image")
        is_safe = False

        if content_type == "text/markdown":
            base_url = f"/{owner}/{repo}/raw/main/{"/".join(file_path.split("/")[:-1])}".rstrip("/")
            file_content = RelativeURLRewriter(base_url).convert(
                file_content.decode("utf-8")
            )
            is_safe = True

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
            is_safe=is_safe
        )
    except Exception as e:
        logger.error(f"Error previewing file {file_path} in {owner}/{repo}: {e}")
        abort(404, description=str(e))


def main():
    port = os.environ.get("PORT", 8107)
    host = os.environ.get("HOST", "127.0.0.1")
    app.run(debug=True, port=port, host=host)


if __name__ == "__main__":
    main()
