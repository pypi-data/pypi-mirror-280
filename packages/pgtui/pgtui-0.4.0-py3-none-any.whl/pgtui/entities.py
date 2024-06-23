from dataclasses import dataclass
from datetime import timedelta
from typing import NamedTuple


class ResultMeta(NamedTuple):
    """Information about an executed query"""

    rows: int
    duration: timedelta


@dataclass
class DbInfo:
    """Database info loaded from the server"""

    database: str
    host: str
    host_address: str
    port: str
    schema: str
    user: str


@dataclass
class DbContext:
    """Credentials used to connect to the database"""

    dbname: str | None
    host: str
    password: str | None
    port: str
    username: str
