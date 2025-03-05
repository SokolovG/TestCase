from contextlib import contextmanager
import logging
import sys

from colorama import init, Fore, Style
import psycopg2

from constants import HOST, PORT, DATABASE, USER, PASSWORD


init()


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


class Logger:
    def __init__(self, name: str = None):
        logger_name = name or "Logger"
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # Очищаем существующие обработчики.
        if self.logger.handlers:
            self.logger.handlers.clear()

        # Создаем консольный вывод.
        console = logging.StreamHandler(sys.stdout)

        # Настраиваем формат с цветным именем логгера.
        formatter = logging.Formatter(
            f"{Fore.GREEN}%(name)s{Style.RESET_ALL} - %(message)s"
        )
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def info(self, message):
        # Обычные информационные сообщения - белым цветом.
        colored_message = f"{Fore.WHITE}{message}{Style.RESET_ALL}"
        self.logger.info(colored_message)

    def error(self, message):
        # Сообщения об ошибках - красным цветом.
        colored_message = f"{Fore.RED}{message}{Style.RESET_ALL}"
        self.logger.error(colored_message)

    def warning(self, message):
        # Предупреждения - желтым цветом.
        colored_message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
        self.logger.warning(colored_message)

    def success(self, message):
        # Сообщения об успехе - зеленым цветом.
        colored_message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
        self.logger.info(colored_message)
