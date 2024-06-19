import pytest
from click.testing import CliRunner
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from poaster.access import cli


@pytest.fixture
async def add_user(db_session: AsyncSession) -> None:
    qry = "INSERT OR IGNORE INTO users (username, password) VALUES ('testuser', 'password');"
    await db_session.execute(text(qry))


def test_users_help(cli_runner: CliRunner):
    expected_help_text = """\
Usage: users [OPTIONS] COMMAND [ARGS]...

  Control panel for managing users.

Options:
  -h, --help  Show this message and exit.

Commands:
  add     Add new user.
  delete  Delete existing user.
  list    List stored usernames.
  update  Update existing user.
"""
    result = cli_runner.invoke(cli.users, ["--help"])

    assert result.exit_code == 0
    assert result.output == expected_help_text


def test_users_add(cli_runner: CliRunner):
    add_user_args = ["add", "--username", "testuser", "--password", "password"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert result.output == "`testuser` successfully added.\n"


def test_users_add_validation_failed(cli_runner: CliRunner):
    add_user_args = ["add", "--username", "testuser" * 100, "--password", "password"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert "Input validation failed:" in result.output


@pytest.mark.usefixtures("add_user")
def test_users_add_already_exists(cli_runner: CliRunner):
    add_user_args = ["add", "--username", "testuser", "--password", "password"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert result.output == "User 'testuser' exists.\n"


@pytest.mark.usefixtures("add_user")
def test_users_update(cli_runner: CliRunner):
    add_user_args = ["update", "--username", "testuser", "--password", "newpassword"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert result.output == "User `testuser` successfully updated.\n"


def test_users_update_does_not_exist(cli_runner: CliRunner):
    add_user_args = ["update", "--username", "testuser", "--password", "newpassword"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert result.output == "User 'testuser' does not exist.\n"


def test_users_update_validation_failed(cli_runner: CliRunner):
    add_user_args = ["update", "--username", "testuser" * 100, "--password", "password"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert "Input validation failed:" in result.output


@pytest.mark.usefixtures("add_user")
def test_users_delete(cli_runner: CliRunner):
    add_user_args = ["delete", "--username", "testuser"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert result.output == "User `testuser` successfully deleted.\n"


def test_users_delete_does_not_exist(cli_runner: CliRunner):
    add_user_args = ["delete", "--username", "testuser"]
    result = cli_runner.invoke(cli.users, add_user_args)

    assert result.exit_code == 0
    assert result.output == "User 'testuser' does not exist.\n"


@pytest.mark.usefixtures("add_user")
def test_users_list(cli_runner: CliRunner):
    result = cli_runner.invoke(cli.users, ["list"])

    assert result.exit_code == 0
    assert result.output == "Stored users:\n- testuser\n"


def test_users_list_no_users(cli_runner: CliRunner):
    result = cli_runner.invoke(cli.users, ["list"])

    assert result.exit_code == 0
    assert result.output == "No users found.\n"
