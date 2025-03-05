from typing import Any

from .constants import HIGH_SALARY_EMPLOYEES
from ..constants import EMPLOYEES_TASK_2, Employee
from core import Logger


logger = Logger("Task_2")


def filter_employees_and_return(employees_list: list[Employee]) -> dict[str, Any]:
    """
    Фильтрует список сотрудников и выполняет различные операции с данными.

    Функция вычисляет среднюю зарплату, находит сотрудников с зарплатой выше
    установленного порога и сортирует список сотрудников по размеру зарплаты.

    Args:
        employees_list: Список объектов сотрудников.

    Returns:
        Словарь, содержащий:
        - 'salary_more_than_50': список имен сотрудников с зарплатой выше порога.
        - 'sorted_list': отсортированный по убыванию зарплаты список сотрудников.
        - 'avg_salary': средняя зарплата всех сотрудников.
    """
    employees_above_threshold = []
    result = {}
    avg_salary = 0
    employees_count = len(employees_list)
    sorted_list = sorted(employees_list, key=lambda x: x.get("salary", 0), reverse=True)

    for employee in employees_list:  # Проходимся по каждому сотруднику.
        avg_salary += employee.get("salary", 0)
        if employee.get("salary") > HIGH_SALARY_EMPLOYEES:
            # Если зарплата больше установленной, то добавляем в список.
            employees_above_threshold.append(employee.get("name"))

    result["salary_more_than_50"] = employees_above_threshold
    result["sorted_list"] = sorted_list

    if employees_count > 0:
        result["avg_salary"] = avg_salary / employees_count
    else:
        result["avg_salary"] = 0

    return result


def main() -> None:
    """
    Основная логика программы.

    Вызывает функцию filter_employees_and_return с константой EMPLOYEES
    и логирует результат на экран.
    """
    logger.info(filter_employees_and_return(EMPLOYEES_TASK_2))


if __name__ == "__main__":
    main()
