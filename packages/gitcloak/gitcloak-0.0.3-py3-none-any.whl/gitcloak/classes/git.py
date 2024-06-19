import requests

import logging

from typing import Generator, Dict, List, Optional

from dulwich.objects import Tree, Blob
from dulwich.client import HttpGitClient, get_transport_and_path
from dulwich.repo import MemoryRepo


class InMemoryRepo(MemoryRepo):
    """A subclass of MemoryRepo that provides additional methods to interact with the repository."""

    def get_tree(self, commit_sha: bytes) -> Tree:
        """Return the tree object for the given commit.

        Args:
            commit_sha (bytes): The commit hash.

        Returns:
            ShaFile: The tree object.
        """
        commit = self.get_object(commit_sha)
        return self.get_object(commit.tree)

    def list_tree(
        self, tree: Tree, path: str = "", prefix: str = ""
    ) -> Generator[str, None, None]:
        """List the directory structure of the tree object.

        Args:
            tree (Tree): The tree object.
            path (str): The path within the tree object.
            prefix (str): The prefix to be added to the path.

        Yields:
            str: The path of the file or directory.
        """
        logging.debug(f"Listing tree {tree.sha()} with path {path}, prefix {prefix}")

        for entry in tree.items():
            entry_path = (
                f"{prefix}/{entry.path.decode('utf-8')}"
                if prefix
                else entry.path.decode("utf-8")
            )

            if path:
                path_parts = path.split("/")
                if path_parts[0] != entry.path.decode("utf-8"):
                    continue

            if isinstance(self.get_object(entry.sha), Tree):
                if path:
                    for _ in self.list_tree(
                        self.get_object(entry.sha),
                        path="/".join(path_parts[1:]),
                        prefix="/".join(path_parts[1:]),
                    ):
                        yield (_)
                else:
                    for _ in self.list_tree(
                        self.get_object(entry.sha), prefix=entry_path
                    ):
                        yield (_)
            else:
                yield (entry_path)

    def get_file_content(self, tree: Tree, file_path: str) -> bytes:
        """Get the content of a file in the tree object.

        Args:
            tree (Tree): The tree object.
            file_path (str): The path of the file.

        Returns:
            bytes: The content of the file.
        """

        parts = file_path.split("/")
        for entry in tree.items():
            entry_name = entry.path.decode("utf-8")
            if entry_name == parts[0]:
                # If we are already in the last part of the path, return the file content
                if len(parts) == 1:
                    file_obj = self.get_object(entry.sha)
                    if isinstance(file_obj, Blob):
                        return file_obj.data
                    else:
                        raise ValueError(f"Path {file_path} is not a file.")

                # If there are more parts in the path, try the next depth level
                else:
                    if isinstance(self.get_object(entry.sha), Tree):
                        return self.get_file_content(
                            self.get_object(entry.sha), "/".join(parts[1:])
                        )
                    else:
                        raise ValueError(f"Path {file_path} is not a directory.")
        raise ValueError(f"File {file_path} not found in the repository.")


class Git:
    """A class to interact with a remote Git repository.

    This class is not specific to any hosting service and should work with any Git repository.
    """

    def __init__(self, repo_url):
        """Initialize the Git class.

        Args:
            repo_url (str): The URL of the remote Git repository.
        """
        self.repo_url = repo_url.rstrip("/")
        self.client = HttpGitClient(self.repo_url)

    def get_remote_refs(self) -> Dict[bytes, bytes]:
        """Get the remote references of the repository.

        Returns:
            Dict[bytes, bytes]: A dictionary of references.
        """
        client, path = get_transport_and_path(self.repo_url)
        refs = client.fetch(path, self.repo)
        return refs

    def get_head_commit(self, refs) -> bytes:
        """Get the commit hash of the HEAD reference.

        Args:
            refs (Dict[bytes, bytes]): A dictionary of references.

        Returns:
            bytes: The commit hash of the HEAD reference.
        """
        return refs[b"HEAD"]

    def get_pack_data(self, commit_sha: str) -> bytes:
        """Get the pack data for the given commit.

        Args:
            commit_sha (str): The commit hash.

        Returns:
            bytes: The pack data.
        """
        url = f"{self.repo_url}/git-upload-pack"
        request_body = f"0032want {commit_sha} multi_ack_detailed side-band-64k thin-pack ofs-delta agent=git/2.28.0\n00000009done\n"
        response = requests.post(url, data=request_body.encode("utf-8"))
        response.raise_for_status()
        return response.content

    def get_directory_structure(
        self, path: str = "", commit_sha: Optional[bytes] = None
    ) -> List[str]:
        """Get the directory structure of the repository.

        Args:
            path (str): The path within the repository.
            commit_sha (bytes): The commit hash. If not provided, the HEAD commit will be used.

        Returns:
            List[str]: A list of file and directory paths under the given path.
        """
        # Initialize an in-memory repository
        self.repo = InMemoryRepo()

        if not commit_sha:
            # Fetch the remote references and objects into the in-memory repository
            refs = self.get_remote_refs()
            commit_sha = self.get_head_commit(refs)

        # Get the tree object for the given commit
        tree = self.repo.get_tree(commit_sha)

        # List the directory structure
        return list(self.repo.list_tree(tree, path=path))

    def get_file_content(
        self, file_path: str, commit_sha: Optional[bytes] = None
    ) -> bytes:
        """Get the content of a file in the repository.

        Args:
            file_path (str): The path of the file.
            commit_sha (bytes): The commit hash. If not provided, the HEAD commit will be used.

        Returns:
            bytes: The content of the file.
        """

        file_path = file_path.lstrip("/")

        # Initialize an in-memory repository
        self.repo = InMemoryRepo()

        if not commit_sha:
            # Fetch the remote references and objects into the in-memory repository
            refs = self.get_remote_refs()
            commit_sha = self.get_head_commit(refs)

        # Get the tree object for the given commit
        tree = self.repo.get_tree(commit_sha)

        # Get the file content
        return self.repo.get_file_content(tree, file_path)
