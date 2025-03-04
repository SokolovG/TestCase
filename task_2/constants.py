from typing import Final, TypedDict


class Employee(TypedDict):
    name: str
    position: str
    salary: int


EMPLOYEES: Final[list[Employee]] = [
    {"name": "Иван", "position": "разработчик", "salary": 55000},
    {"name": "Анна", "position": "аналитик", "salary": 48000},
    {"name": "Петр", "position": "тестировщик", "salary": 52000},
]

HIGH_SALARY_EMPLOYEES: Final[int] = 50_000
