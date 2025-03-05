from typing import Optional

from core import get_cursor, base_logger


def add_data_to_db(data: list[str]) -> None:
    try:
        with get_cursor() as cur:
            for row in range(5):
                name, position, salary = row
                cur.execute(
                    "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)",
                    (name, position, salary),
                )

    except Exception as e:
        base_logger.log(f"Ошибка при добавлении сотрудников: {e}", level="error")
        return


def get_employee_with_salary() -> Optional[list[tuple[str]]]:
    pass


def update_bu_name() -> None:
    pass


def delete_by_name() -> None:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
