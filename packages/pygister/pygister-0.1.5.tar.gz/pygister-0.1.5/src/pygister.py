import os
import signal
import time
from datetime import datetime, timezone

import click
import requests

from gist import Gist  # type: ignore


def get_gist_metadata(gist_id):
    """Get the metadata of a gist including its updated time."""
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {Gist.auth_token()}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_local_file_mod_time(filename):
    """Get the last modification time of the local file."""
    return datetime.fromtimestamp(os.path.getmtime(filename), tz=timezone.utc)


def update_local_file(filename, content):
    """Update the local file with the content from the gist."""
    with open(filename, "w") as file:
        file.write(content)


def signal_handler(sig, frame):
    """Handle graceful shutdown on receiving CTRL-C."""
    print("Exiting gracefully...")
    exit(0)


@click.command()
@click.argument("gist_id")
@click.argument("interval", type=int)
def sync(gist_id, interval):
    """Synchronize a file with a remote gist every <interval> seconds."""
    signal.signal(signal.SIGINT, signal_handler)
    gist_info = get_gist_metadata(gist_id)
    filename = list(gist_info["files"].keys())[0]

    while True:
        try:
            local_mod_time = (
                get_local_file_mod_time(filename) if os.path.exists(filename) else None
            )
            remote_mod_time = datetime.fromisoformat(
                gist_info["updated_at"].replace("Z", "+00:00")
            ).astimezone(timezone.utc)

            if local_mod_time and local_mod_time > remote_mod_time:
                with open(filename, "r") as file:
                    content = file.read()
                Gist.update_gist(gist_id, content)
            elif not local_mod_time or remote_mod_time > local_mod_time:
                content = Gist.read_gist(gist_id)
                update_local_file(filename, content)

            time.sleep(interval)
            gist_info = get_gist_metadata(gist_id)

        except Exception as e:
            click.echo(f"Error syncing gist: {e}", err=True)
            time.sleep(interval)


@click.command()
@click.argument("filename")
@click.argument("gist_id", required=False)
def push(filename, gist_id):
    """Pushes to gist and returns a short URL of the new gist, or updates an existing gist."""
    with open(filename, "r") as file:
        content = file.read()

    if gist_id:
        # Update the existing gist
        try:
            Gist.update_gist(gist_id, content)
        except Exception as e:
            click.echo(f"Error updating gist: {e}", err=True)
    else:
        # Create a new gist
        gist_options = {
            "description": f"Content of {filename}",
            "public": True,
            "filename": filename,
        }
        try:
            result = Gist.gist(content, gist_options)
            short_url = result.get("short_url", result.get("html_url"))
            click.echo(short_url)
        except Exception as e:
            click.echo(f"Error creating gist: {e}", err=True)


@click.command()
@click.argument("gist_id")
def read(gist_id):
    """Reads a gist by its ID and prints the content to stdout."""
    try:
        content = Gist.read_gist(gist_id)
        if content:
            click.echo(content)
        else:
            click.echo("No content found.", err=True)
    except Exception as e:
        click.echo(f"Error reading gist: {e}", err=True)


@click.command()
def version():
    """Print the version of the library."""
    click.echo(f"pygister version {Gist.VERSION}")


@click.group()
def cli():
    pass


cli.add_command(push)
cli.add_command(read)
cli.add_command(sync)
cli.add_command(version)

if __name__ == "__main__":
    cli()
