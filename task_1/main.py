from typing import Optional

from core import get_cursor, Logger
from ..constants import EMPLOYEES_TASK_1, Employee


logger = Logger("Task_1")


def add_data_to_db(data: list[Employee]) -> bool:
    """
    Записывает данные в БД.

    Args:
        data: Список словарей с информацией о сотрудниках.

    Returns:
        True/False
    """
    try:
        with get_cursor() as cur:
            for row in data:
                name, position, salary = row["name"], row["position"], row["salary"]
                cur.execute(
                    "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)",
                    (name, position, salary),
                )
                logger.success(f"Добавлена запись: {name}, {position}, {salary}")
            return True

    except Exception as e:
        logger.error(f"Ошибка при добавлении сотрудников: {e}")
        return False

def get_employee_with_salary(target_salary: int) -> Optional[list[str]]:
    """
    Получает список имен сотрудников с зарплатой выше указанной.

    Args:
        target_salary: Минимальная зарплата для поиска

    Returns:
        Список имен сотрудников или пустой список в случае ошибки
    """
    try:
        with get_cursor() as cur:
            cur.execute(
                "SELECT name FROM employees WHERE salary > %s",
                (target_salary,)
            )
            data = cur.fetchall()
            data = [name[0] for name in data]
            logger.success(f"Работники с зарплатой выше {target_salary}: {data}")
            return data

    except Exception as e:
        logger.error(f"Ошибка вывода сотрудников с зарплатой выше {target_salary}: {e}")
        return []

def update_salary_by_name(new_salary: int, name: str) -> bool:
    """
    Обновляет зарплату сотруднику по имени.

    Args:
        new_salary: Новая зарплата
        name: Имя сотрудника

    Returns:
        True/False
    """
    if new_salary <= 0:
        logger.error("Зарплата должна быть положительным числом")
        return False
    if not name:
        logger.error("Имя сотрудника не может быть пустым")
        return False

    try:
        with get_cursor() as cur:
            cur.execute(
                "UPDATE employees SET salary = %s WHERE name = %s",
                (new_salary, name)
            )
            logger.success(f"Обновлена зарплата {name} на {new_salary}")
            return True

    except Exception as e:
        logger.error(f"Ошибка при обновлении зарплаты сотрудника {name} c новой зарплатой {new_salary}: {e}")
        return False


def delete_by_name(name: str) -> bool:
    """
    Удаляет сотрудника с заданным именем.

    Args:
        name: Имя сотрудника для удаления

    Returns:
        True/False
    """

    if not name:
        logger.error("Имя сотрудника не может быть пустым")
        return False
    try:
        with get_cursor() as cur:
            cur.execute(
                "DELETE FROM employees WHERE name = %s", (name,)
            )
            logger.success(f"Удален сотрудник с именем {name}")
            return True

    except Exception as e:
        logger.error(f"Ошибка при удалении сотрудника {name}: {e}")
        return False


def main() -> None:
    """Основная логика программы, вызов функций."""
    add_data_to_db(EMPLOYEES_TASK_1)
    get_employee_with_salary(target_salary=50000)
    update_salary_by_name(name='Иван', new_salary=60000)
    delete_by_name(name='Анна')


if __name__ == "__main__":
    main()
