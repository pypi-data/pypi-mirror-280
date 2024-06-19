import os
import subprocess
from datetime import datetime, timezone

import click
import humanize
import yaml
from pr_pilot import Task
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding

from cli.constants import CONFIG_LOCATION, CONFIG_API_KEY


def clean_code_block_with_language_specifier(response):
    lines = response.split("\n")

    # Check if the first line starts with ``` followed by a language specifier
    # and the last line is just ```
    if lines[0].startswith("```") and lines[-1].strip() == "```":
        # Remove the first and last lines
        cleaned_lines = lines[1:-1]
    else:
        cleaned_lines = lines

    clean_response = "\n".join(cleaned_lines)
    return clean_response


def load_config():
    """Load the configuration from the default location. If it doesn't exist,
    ask user to enter API key and save config."""
    if not os.path.exists(CONFIG_LOCATION):
        if os.getenv("PR_PILOT_API_KEY"):
            click.echo("Using API key from environment variable.")
            api_key = os.getenv("PR_PILOT_API_KEY")
        else:
            api_key_url = "https://app.pr-pilot.ai/dashboard/api-keys/"
            click.echo(f"Configuration file not found. Please create an API key at {api_key_url}.")
            api_key = click.prompt("PR Pilot API key")
        with open(CONFIG_LOCATION, "w") as f:
            f.write(f"{CONFIG_API_KEY}: {api_key}")
        click.echo(f"Configuration saved in {CONFIG_LOCATION}")
    with open(CONFIG_LOCATION) as f:
        config = yaml.safe_load(f)
    return config


def pull_branch_changes(status_indicator, console, branch, debug=False):
    status_indicator.update(f"Pull latest changes from {branch}")
    try:
        # Fetch origin and checkout branch
        subprocess_params = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        subprocess.run(["git", "fetch", "origin"], **subprocess_params)
        subprocess.run(["git", "checkout", branch], **subprocess_params)
        # Capture output of git pull
        result = subprocess.run(["git", "pull", "origin", branch], **subprocess_params)
        output = result.stdout
        error = result.stderr
        status_indicator.success()
        if debug:
            console.line()
            console.print(output)
            console.line()
    except Exception as e:
        status_indicator.fail()
        console.print(
            "[bold red]An error occurred:"
            f"[/bold red] {type(e)} {str(e)}\n\n{error if error else ''}"
        )


class TaskFormatter:

    def __init__(self, task: Task):
        self.task = task

    def format_github_project(self):
        return (
            f"[link=https://github.com/{self.task.github_project}]{self.task.github_project}[/link]"
        )

    def format_created_at(self):
        # If task was created less than 23 hours ago, show relative time
        now = datetime.now(timezone.utc)  # Use timezone-aware datetime
        if (now - self.task.created).days == 0:
            return humanize.naturaltime(self.task.created)
        local_time = self.task.created.astimezone()
        return local_time.strftime("%Y-%m-%d %H:%M:%S")

    def format_pr_link(self):
        if self.task.pr_number:
            return (
                f"[link=https://github.com/{self.task.github_project}/pull/"
                f"{self.task.pr_number}]#{self.task.pr_number}[/link]"
            )
        return ""

    def format_status(self):
        if self.task.status == "running":
            return f"[bold yellow]{self.task.status}[/bold yellow]"
        elif self.task.status == "completed":
            return f"[bold green]{self.task.status}[/bold green]"
        elif self.task.status == "failed":
            return f"[bold red]{self.task.status}[/bold red]"

    def format_title(self):
        dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(self.task.id)}/"
        return f"[link={dashboard_url}]{self.task.title}[/link]"

    def format_branch(self):
        return Markdown(f"`{self.task.branch}`")


class PaddedConsole:
    def __init__(self, padding=(1, 1)):
        self.console = Console()
        self.padding = padding

    def print(self, content):
        padded_content = Padding(content, self.padding)
        self.console.print(padded_content)
