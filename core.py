from contextlib import contextmanager
import logging
import sys
from typing import Optional

from colorama import init, Fore, Style
import psycopg2

from constants import HOST, PORT, DATABASE, USER, PASSWORD


@contextmanager
def get_cursor():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
    )
    try:
        cur = conn.cursor()
        yield cur
        conn.commit()
    finally:
        conn.close()


init()


class BaseLogger:
    def __init__(self):
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)

        if logger.handlers:
            logger.handlers.clear()

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            f"{Fore.GREEN}%(name)s{Style.RESET_ALL} - " f"%(message)s",
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        return logger

    def log(self, message: str, level: Optional[str] = "info") -> None:
        """

        Args:
            message:
            level:

        Returns:

        """
        if level == "info":
            message = f"{Fore.WHITE}{message}{Style.RESET_ALL}"
            self.logger.info(message)
        elif level == "error":
            message = f"{Fore.RED}{message}{Style.RESET_ALL}"
            self.logger.error(message)
        elif level == "warning":
            message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
            self.logger.warning(message)
        elif level == "success":
            message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
            self.logger.info(message)


base_logger = BaseLogger()
