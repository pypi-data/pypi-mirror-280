import click

from exponent.core.config import ExponentCloudConfig, Settings


def print_editable_install_forced_prod_warning(settings: Settings) -> None:
    click.secho(
        "Detected local editable install, but this command only works against prod.",
        fg="red",
        bold=True,
    )
    click.secho("Using prod settings:", fg="red", bold=True)
    click.secho("- base_url=", fg="yellow", bold=True, nl=False)
    click.secho(f"{settings.base_url}", fg=(100, 200, 255), bold=False)
    click.secho("- base_api_url=", fg="yellow", bold=True, nl=False)
    click.secho(f"{settings.base_api_url}", fg=(100, 200, 255), bold=False)
    click.secho()


def print_editable_install_warning(settings: Settings) -> None:
    click.secho(
        "Detected local editable install, using local URLs", fg="yellow", bold=True
    )
    click.secho("- base_url=", fg="yellow", bold=True, nl=False)
    click.secho(f"{settings.base_url}", fg=(100, 200, 255), bold=False)
    click.secho("- base_api_url=", fg="yellow", bold=True, nl=False)
    click.secho(f"{settings.base_api_url}", fg=(100, 200, 255), bold=False)
    click.secho()


def print_exponent_message(base_url: str, chat_uuid: str) -> None:
    click.echo()
    click.secho("△ Exponent v1.0.0", fg=(180, 150, 255), bold=True)
    click.echo()
    click.echo(
        " - Link: " + click.style(f"{base_url}/chats/{chat_uuid}", fg=(100, 200, 255))
    )
    click.echo(click.style("  - Shell: /bin/zsh", fg="white"))
    click.echo()
    click.echo(click.style("✓", fg="green", bold=True) + " Ready in 1401ms")


def write_template_exponent_cloud_config(file_path: str) -> None:
    exponent_cloud_config = ExponentCloudConfig(
        repo_name="your_repo_name",
        repo_specific_setup_commands=[
            "cd /home/user",
            "gh repo clone https://github.com/<org>/<repo>.git",
            "cd <repo>",
            "# Any additional setup commands",
        ],
        gh_token="ghp_your_token_here",
        runloop_api_key="ak_your_runloop_api_key_here",
    )
    with open(file_path, "w") as f:
        f.write(exponent_cloud_config.model_dump_json(indent=2))
