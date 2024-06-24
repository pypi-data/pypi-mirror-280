import json
import os
from typing import Any, Dict, Optional, Union
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Gist:
    # read from VERSION file
    with open("VERSION") as f:
        VERSION = f.read().strip()
    # A list of clipboard commands with copy and paste support.
    CLIPBOARD_COMMANDS = {
        "pbcopy": "pbpaste",
        "xclip": "xclip -o",
        "xsel -i": "xsel -o",
        "putclip": "getclip",
    }

    GITHUB_API_URL = "https://api.github.com/"
    GITHUB_URL = "https://github.com/"
    GIT_IO_URL = "https://git.io"

    GITHUB_BASE_PATH = ""
    GHE_BASE_PATH = "/api/v3"

    GITHUB_CLIENT_ID = "4f7ec0d4eab38e74384e"

    URL_ENV_NAME = "GITHUB_URL"
    CLIENT_ID_ENV_NAME = "GIST_CLIENT_ID"
    TOKEN_ENV_NAME = "GITHUB_TOKEN"

    USER_AGENT = f"gist/{VERSION} (requests, {os.uname()})"

    class Error(Exception):
        """Base class for exceptions in this module."""

        pass

    class ClipboardError(Error):
        """Exception raised for errors related to clipboard operations."""

        pass

    @staticmethod
    def auth_token() -> Optional[str]:
        """Read the authentication token from the environment variable or file."""
        token = os.getenv(Gist.TOKEN_ENV_NAME)
        if token:
            return token

        try:
            return Gist.AuthTokenFile.read()
        except FileNotFoundError:
            return None

    class AuthTokenFile:
        """Helper class for handling authentication token file."""

        @staticmethod
        def filename() -> str:
            """Return the filename for the auth token file."""
            if Gist.URL_ENV_NAME in os.environ:
                return os.path.expanduser(
                    f"~/.gist.{os.environ[Gist.URL_ENV_NAME].replace(':', '.').replace('[^a-z0-9.-]', '')}"
                )
            else:
                return os.path.expanduser("~/.gist")

        @staticmethod
        def read() -> str:
            """Read the auth token from the file."""
            with open(Gist.AuthTokenFile.filename(), "r") as f:
                return f.read().strip()

        @staticmethod
        def write(token: str) -> None:
            """Write the auth token to the file."""
            with open(Gist.AuthTokenFile.filename(), "w", 0o600) as f:
                f.write(token)

    @staticmethod
    def default_filename() -> str:
        """Return the default filename for gists."""
        return "gistfile1.txt"

    @staticmethod
    def gist(
        content: str, options: Optional[Dict[str, Any]] = None
    ) -> Optional[Union[Dict[str, Any], str]]:
        """Create a new gist with the given content and options."""
        options = options or {}
        filename = options.get("filename", Gist.default_filename())
        return Gist.multi_gist({filename: content}, options)

    @staticmethod
    def multi_gist(
        files: Dict[str, str], options: Optional[Dict[str, Any]] = None
    ) -> Optional[Union[Dict[str, Any], str]]:
        """Create a new gist with multiple files."""
        options = options or {}
        if options.get("anonymous"):
            raise Exception(
                "Anonymous gists are no longer supported. Please log in with `gist --login`."
            )

        access_token = options.get("access_token", Gist.auth_token())
        json_data = {
            "description": options.get("description"),
            "public": options.get("public", False),
            "files": {
                name: {"content": content}
                for name, content in files.items()
                if content.strip() or not options.get("skip_empty")
            },
        }

        if not json_data["files"] and options.get("skip_empty"):
            raise ValueError("No files to gist")

        existing_gist = options.get("update", "").split("/")[-1]
        url = urljoin(
            Gist.GITHUB_API_URL,
            f"/gists/{existing_gist}" if existing_gist else "/gists",
        )
        headers = {"Authorization": f"token {access_token}"} if access_token else {}
        response = requests.post(url, headers=headers, json=json_data)

        if response.ok:
            return Gist.on_success(response.json(), options)
        else:
            response.raise_for_status()

        return None

    @staticmethod
    def on_success(
        response_json: Dict[str, Any], options: Dict[str, Any]
    ) -> Optional[Union[Dict[str, Any], str]]:
        """Handle the success response from creating a gist."""
        output_type = options.get("output", "all")
        output = {
            "javascript": f'<script src="{response_json["html_url"]}.js"></script>',
            "html_url": response_json["html_url"],
            "short_url": Gist.shorten(response_json["html_url"]),
            "raw_url": Gist.rawify(response_json["html_url"]),
            "short_raw_url": Gist.shorten(Gist.rawify(response_json["html_url"])),
            "all": response_json,
        }.get(output_type, response_json)

        if options.get("copy"):
            Gist.copy(output)
        if options.get("open"):
            Gist.open(response_json["html_url"])

        return output

    @staticmethod
    def shorten(url: str) -> str:
        """Shorten a given URL using git.io."""
        response = requests.post(f"{Gist.GIT_IO_URL}/create", data={"url": url})
        return response.text if response.ok else url

    @staticmethod
    def rawify(url: str) -> str:
        """Convert a GitHub URL into a raw file URL."""
        response = requests.head(url)
        if response.ok:
            return f"{url}/raw"
        elif response.is_redirect:
            return Gist.rawify(response.headers["Location"])
        else:
            return url

    @staticmethod
    def copy(content: str) -> None:
        """Copy content to the clipboard."""
        import subprocess

        command = next(
            (cmd for cmd in Gist.CLIPBOARD_COMMANDS if Gist.which(cmd)), None
        )
        if not command:
            raise Gist.ClipboardError(
                f"Could not find copy command, tried: {', '.join(Gist.CLIPBOARD_COMMANDS.keys())}"
            )

        subprocess.run(command, input=content.encode(), check=True)

        if Gist.paste() != content:
            raise Gist.ClipboardError("Copying to clipboard failed.")

    @staticmethod
    def paste() -> str:
        """Get content from the clipboard."""
        import subprocess

        command = next(
            (cmd for cmd in Gist.CLIPBOARD_COMMANDS.values() if Gist.which(cmd)), None
        )
        if not command:
            raise Gist.ClipboardError("Could not find paste command.")
        return subprocess.run(command, capture_output=True, text=True).stdout

    @staticmethod
    def which(cmd: str) -> Optional[str]:
        """Check if a command exists in the system."""
        import shutil

        return shutil.which(cmd)

    @staticmethod
    def open(url: str) -> None:
        """Open a URL in the default web browser."""
        import webbrowser

        webbrowser.open(url)

    @staticmethod
    def base_path() -> str:
        """Return the base path for the GitHub API."""
        return (
            Gist.GHE_BASE_PATH
            if Gist.URL_ENV_NAME in os.environ
            else Gist.GITHUB_BASE_PATH
        )

    @staticmethod
    def login_url() -> str:
        """Return the login URL for GitHub."""
        return os.environ.get(Gist.URL_ENV_NAME, Gist.GITHUB_URL)

    @staticmethod
    def api_url() -> str:
        """Return the API URL for GitHub."""
        return os.environ.get(Gist.URL_ENV_NAME, Gist.GITHUB_API_URL)

    @staticmethod
    def client_id() -> str:
        """Return the GitHub client ID."""
        return os.environ.get(Gist.CLIENT_ID_ENV_NAME, Gist.GITHUB_CLIENT_ID)

    @staticmethod
    def list_all_gists() -> Any:
        """List all gists for the authenticated user."""
        url = urljoin(Gist.api_url(), "/gists")
        access_token = Gist.auth_token()
        headers = {"Authorization": f"token {access_token}"} if access_token else {}
        response = requests.get(url, headers=headers)

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def read_gist(gist_id: str) -> Optional[str]:
        """Read the content of a specific gist by its ID."""
        url = urljoin(Gist.api_url(), f"/gists/{gist_id}")
        access_token = Gist.auth_token()
        headers = {"Authorization": f"token {access_token}"} if access_token else {}
        response = requests.get(url, headers=headers)

        if response.ok:
            body = response.json()
            files = body.get("files", {})
            if not files:
                return None
            file_name, file_data = next(iter(files.items()))
            return file_data.get("content")
        else:
            response.raise_for_status()

        return None

    @staticmethod
    def delete_gist(gist_id: str) -> None:
        """Delete a specific gist by its ID."""
        url = urljoin(Gist.api_url(), f"/gists/{gist_id}")
        access_token = Gist.auth_token()
        headers = {"Authorization": f"token {access_token}"} if access_token else {}
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print("Gist deleted successfully.")
        else:
            response.raise_for_status()

    @staticmethod
    def update_gist(gist_id: str, content: str) -> None:
        """Update a specific gist by its ID."""
        url = urljoin(Gist.api_url(), f"/gists/{gist_id}")
        access_token = Gist.auth_token()
        headers = {"Authorization": f"token {access_token}"} if access_token else {}
        json_data = {"files": {Gist.default_filename(): {"content": content}}}
        response = requests.patch(url, headers=headers, json=json_data)

        if response.status_code == 200:
            print("Gist updated successfully.")
        else:
            response.raise_for_status()
