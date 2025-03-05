from core import get_cursor, Logger


logger = Logger("Task_1")


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
        logger.error(f"Ошибка при добавлении сотрудников: {e}")
        return


def get_employee_with_salary() -> list[tuple[str]]:
    pass


def update_bu_name() -> None:
    pass


def delete_by_name() -> None:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
