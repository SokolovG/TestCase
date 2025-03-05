from typing import Final, TypedDict


HOST: Final[str] = "db"
PORT: Final[int] = 5432
DATABASE: Final[str] = "tasks_db"
USER: Final[str] = "postgres"
PASSWORD: Final[str] = "postgres"

class Employee(TypedDict):
    name: str
    position: str
    salary: int

EMPLOYEES_TASK_1: Final[list[Employee]] = [
    {"name": "Иван", "position": "разработчик", "salary": 55000},
    {"name": "Анна", "position": "аналитик", "salary": 48000},
    {"name": "Григорий", "position": "тестировщик", "salary": 100000},
    {"name": "Дарья", "position": "тестировщик", "salary": 52000},
    {"name": "Анастасия", "position": "тестировщик", "salary": 52000},
]

EMPLOYEES_TASK_2: Final[list[Employee]] = [
    {"name": "Иван", "position": "разработчик", "salary": 55000},
    {"name": "Анна", "position": "аналитик", "salary": 48000},
    {"name": "Петр", "position": "тестировщик", "salary": 52000},
]
