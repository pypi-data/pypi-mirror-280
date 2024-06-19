import asyncio

import click
import pydantic

from poaster.core import exceptions, sessions

from . import services


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def users() -> None:
    """Control panel for managing users."""


@click.command("add")
@click.option(
    "--username",
    type=str,
    prompt="Username",
    help="Username input. [prompt]",
)
@click.option(
    "--password",
    type=str,
    prompt="Password",
    hide_input=True,
    confirmation_prompt=True,
    help="Password input. [prompt]",
)
def add_user(username: str, password: str) -> None:
    """Add new user."""
    try:
        asyncio.run(add_user_(username, password))
    except exceptions.AlreadyExists as err:
        click.secho(err, fg="yellow")
    except pydantic.ValidationError as err:
        click.secho(f"Input validation failed: {err}", fg="yellow")
    else:
        click.secho(f"`{username}` successfully added.", fg="green")


async def add_user_(username: str, password: str) -> None:
    async with sessions.async_session() as session:
        access_service = services.AccessService.from_session(session)
        await access_service.register_user(username, password)


@click.command("update")
@click.option(
    "--username",
    type=str,
    prompt="Username",
    help="Username input. [prompt]",
)
@click.option(
    "--password",
    type=str,
    prompt="Password",
    hide_input=True,
    confirmation_prompt=True,
    help="Password input. [prompt]",
)
def update_user(username: str, password: str) -> None:
    """Update existing user."""
    try:
        asyncio.run(update_user_(username, password))
    except exceptions.DoesNotExist as err:
        click.secho(err, fg="yellow")
    except pydantic.ValidationError as err:
        click.secho(f"Input validation failed: {err}", fg="yellow")
    else:
        click.secho(f"User `{username}` successfully updated.", fg="green")


async def update_user_(username: str, password: str) -> None:
    async with sessions.async_session() as session:
        access_service = services.AccessService.from_session(session)
        await access_service.update_user_password(username, password)


@click.command("delete")
@click.option(
    "--username",
    type=str,
    prompt="Username",
    help="Username input. [prompt]",
)
def delete_user(username: str) -> None:
    """Delete existing user."""
    try:
        asyncio.run(delete_user_(username))
    except exceptions.DoesNotExist as err:
        click.secho(err, fg="yellow")
    else:
        click.secho(f"User `{username}` successfully deleted.", fg="green")


async def delete_user_(username: str) -> None:
    async with sessions.async_session() as session:
        access_service = services.AccessService.from_session(session)
        await access_service.delete_user(username)


@click.command("list")
def list_usernames() -> None:
    """List stored usernames."""
    if usernames := asyncio.run(list_usernames_()):
        click.secho("Stored users:", fg="green")
        for username in sorted(usernames):
            click.echo(f"- {username}")
    else:
        click.secho("No users found.", fg="yellow")


async def list_usernames_() -> list[str]:
    async with sessions.async_session() as session:
        access_service = services.AccessService.from_session(session)
        return await access_service.list_usernames()


users.add_command(add_user)
users.add_command(update_user)
users.add_command(delete_user)
users.add_command(list_usernames)
