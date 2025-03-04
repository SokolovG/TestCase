import os
from pathlib import Path
import csv

from constants import get_cursor


def read_csv(path: Path) -> list[list[str]]:
    with open(path) as file:
        csv_reader = csv.reader(file)
        csv_data = []
        for row in csv_reader:
            # Удаляем лишние пробелы.
            clean_row = [item.strip() for item in row]
            csv_data.append(clean_row)
    print(f"Прочитанные данные: {csv_data}")
    return csv_data


def write_to_db(csv_data: list[list[str]]) -> None:
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
                print(f"Добавлена запись: {name}, {position}, {salary}")
            except print as e:
                print(f"Ошибка при добавлении записи {row}: {e}")


def find_employees_by_position(position: str) -> tuple[str]:
    with get_cursor() as cur:
        cur.execute("SELECT name FROM employees WHERE position = %s", (position,))
        data = cur.fetchall()
        return data


def update_salary_by_name(name: str, new_salary: int) -> None:
    with get_cursor() as cur:
        cur.execute(
            "UPDATE employees SET salary = %s WHERE name = %s", (new_salary, name)
        )


def main() -> None:
    env_path = os.environ.get("CSV_PATH", "employees.csv")
    path = Path(env_path)
    data = read_csv(path)
    write_to_db(data)


if __name__ == "__main__":
    main()
