from typing import Final
from contextlib import contextmanager
import psycopg2


HOST: Final[str] = "db"
PORT: Final[int] = 5432
DATABASE: Final[str] = "tasks_db"
USER: Final[str] = "postgres"
PASSWORD: Final[str] = "postgres"


@contextmanager
def get_cursor():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
    )
