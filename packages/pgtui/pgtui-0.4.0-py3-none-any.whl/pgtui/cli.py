import logging
import os
import pwd

import click
from textual.logging import TextualHandler

from pgtui.app import PgTuiApp
from pgtui.completer import QueryCompleter
from pgtui.entities import DbContext

DEFAULT_USER = pwd.getpwuid(os.getuid()).pw_name

# Tweak the Click context
# https://click.palletsprojects.com/en/8.1.x/api/#context
CONTEXT = dict(show_default=True)


@click.command(context_settings=CONTEXT)
@click.option(
    "-h",
    "--host",
    help="Database server host",
    default="localhost",
    envvar="PGHOST",
)
@click.option(
    "-p",
    "--port",
    help="Database server port",
    default="5432",
    envvar="PGPORT",
)
@click.option(
    "-U",
    "--username",
    help="Database user name",
    default=os.getlogin(),
    envvar="PGUSER",
)
@click.option(
    "-d",
    "--dbname",
    help="Database name to connect to",
    envvar="PGDATABASE",
)
@click.option(
    "-W",
    "--password",
    "force_password_prompt",
    is_flag=True,
    default=False,
    help="Force password prompt",
)
@click.option(
    "-w",
    "--no-password",
    "never_prompt_password",
    is_flag=True,
    default=False,
    help="Never prompt for password",
)
@click.argument(
    "sql_file",
    type=click.Path(dir_okay=False, writable=True),
    required=False,
)
def pgtui(
    host: str,
    port: str,
    username: str,
    dbname: str | None,
    force_password_prompt: bool,
    never_prompt_password: bool,
    sql_file: str | None,
):
    password = os.environ.get("PGPASSWORD", None)
    if force_password_prompt or (not password and not never_prompt_password):
        password = click.prompt("Password", hide_input=True)

    db_context = DbContext(
        host=host,
        port=port,
        dbname=dbname,
        username=username,
        password=password,
    )

    completer = QueryCompleter(
        database=dbname,
        user=username,
        password=password,
        host=host,
        port=port,
    )

    PgTuiApp(db_context, completer, sql_file).run()


def main():
    logging.basicConfig(level="NOTSET", handlers=[TextualHandler()])
    pgtui()
