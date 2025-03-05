import csv
import os
from pathlib import Path

from core import get_cursor, Logger


logger = Logger("Task_4")


def read_csv(path: Path) -> list[list[str]]:
    """
    Читает данные из CSV файл построчно.

    Args:
        path: Путь к файлу.

    Returns:
        Список списков со строками.
    """
    try:
        with open(path) as file:
            csv_reader = csv.reader(file)
            csv_data = []
            for row in csv_reader:
                # Удаляем лишние пробелы.
                clean_row = [item.strip() for item in row]
                csv_data.append(clean_row)
        logger.success(f"Прочитанные данные: {csv_data}")
        return csv_data

    except Exception as error:
        logger.error(f"Ошибка с чтением файла: {error}")

    return None


def write_to_db(csv_data: list[list[str]]) -> None:
    """
    Принимает данные из CSV и записывает их в БД.

    Args:
        csv_data: Данные из CSV файла.
    """
    if csv_data is None:
        logger.error(f"Данные пусты")
        return
    with get_cursor() as cur:
        cur.execute("TRUNCATE TABLE employees;")
        data = csv_data[1:]  # Пропускаем заголовки.
        for row in data:
            try:
                name, position, salary = row
                cur.execute(
                    "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)",
                    (name, position, salary),
                )
                logger.success(f"Добавлена запись: {name}, {position}, {salary}")
            except Exception as e:
                logger.error(f"Ошибка при добавлении записи {row}: {e}")


def find_employees_by_position(position: str) -> list[tuple[str]]:
    """
    Находит сотрудника по его должности.

    Args:
        position: Позиция должности.

    Returns:
        Список кортежей строк.
    """
    with get_cursor() as cur:
        cur.execute("SELECT name FROM employees WHERE position = %s", (position,))
        data = cur.fetchall()
        return data


def update_salary_by_name(name: str, new_salary: int) -> None:
    """
    Обновляет зарплату сотрудника по имени.

    Args:
        name: Имя сотрудника.
        new_salary: Новая зарплата.
    """
    with get_cursor() as cur:
        cur.execute(
            "UPDATE employees SET salary = %s WHERE name = %s", (new_salary, name)
        )


def main() -> None:
    """
    Основная логика программы.

    Вызывает функцию read_csv с путем к файлу и логирует данные.
    Вызывает функцию write_to_db с данными из CSV
    и записывает их в базу данных.
    """
    env_path = os.environ.get("CSV_PATH", "employees.csv")
    path = Path(env_path)
    data = read_csv(path)
    write_to_db(data)


if __name__ == "__main__":
    main()
