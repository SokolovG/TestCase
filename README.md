**[English](#english) | [Русский](#russian)**
## English
# Backend Developer Test Assignment

This repository contains my solution for the Backend Developer test assignment in Python.

## Installation and Running

1. Clone the repository:
```bash
git clone https://github.com/SokolovG/TestCase.git
```

2. Build the image:
```bash
docker compose build
```

3. Start the database:
```bash
docker compose up -d db
```

4. Run the desired application:
```bash
# To run task 1
docker compose up -d backend_task_1

# To run task 4
docker compose up -d backend_task_4

# To run task 7
docker compose up -d backend_task_7
```

## Viewing Execution Results

To view the results of script execution:

### View Container Logs
```bash
# View logs for task 1
docker compose logs backend_task_1

# View logs for task 4
docker compose logs backend_task_4

# View logs for task 7
docker compose logs backend_task_7
```

## Solutions Description

### Task 1: Python + SQL (basic)

Implemented a script to create an `employees` table, add test data, and perform various data operations using Postgres.

### Task 2: Python (data processing)

Implemented functions for processing employee lists: filtering by salary, calculating average salary, and sorting.

### Task 3: SQL (queries)

Written SQL queries for order data analysis: summation, finding maximum values, date filtering, and calculating averages.

### Task 4: Python (mini-project)

Implemented a script to read a CSV file, write data to a Postgres database, and functions for searching and updating employee data.

### Task 5: Algorithmic (Python)

Implemented functions for analyzing a list of numbers: counting unique numbers, finding the second largest number, and filtering numbers divisible by 3.

### Task 6: Theoretical (SQL)

Provided detailed answers to questions about indexes, JOIN operations, and transactions in SQL.

### Task 7: Practical (Python + SQL)

Implemented a script to create a `products` table, add test data, and functions for analyzing and updating product data.

---
## Russian

# Тестовое задание на позицию Backend разработчика

Это репозиторий содержит мое решение тестового задания на позицию Backend разработчика на Python.

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/SokolovG/TestCase.git
```

2. Собрать образ
```bash
docker compose build
```

3. Запустить базу данных
```bash
docker compose up -d db
```

4. Запустить нужное приложение
```bash
# Для запуска задания 1
docker compose up -d backend_task_1

# Для запуска задания 4
docker compose up -d backend_task_4

# Для запуска задания 7
docker compose up -d backend_task_7
```

## Просмотр результатов выполнения

Для просмотра результатов выполнения скриптов:

### Просмотр логов контейнера
```bash
# Просмотр логов для задания 1
docker compose logs backend_task_1

# Просмотр логов для задания 4
docker compose logs backend_task_4

# Просмотр логов для задания 7
docker compose logs backend_task_7
```
## Описание решений

### Задание 1: Python + SQL (базовое)

Реализован скрипт для создания таблицы `employees`, добавления тестовых данных и выполнения различных операций с данными через Postgres.

### Задание 2: Python (работа с данными)

Реализованы функции для обработки списка сотрудников: фильтрация по зарплате, расчет средней зарплаты и сортировка.

### Задание 3: SQL (запросы)

Написаны SQL-запросы для анализа данных о заказах: суммирование, поиск максимума, фильтрация по дате и расчет средних значений.

### Задание 4: Python (мини-проект)

Реализован скрипт для чтения CSV-файла, записи данных в Postgres базу и функций поиска и обновления данных сотрудников.

### Задание 5: Алгоритмическое (Python)

Реализованы функции для анализа списка чисел: подсчет уникальных чисел, поиск второго по величине числа и фильтрация чисел, делящихся на 3.

### Задание 6: Теоретическое (SQL)

Даны подробные ответы на вопросы об индексах, JOIN-операциях и транзакциях в SQL.

### Задание 7: Практическое (Python + SQL)

Реализован скрипт для создания таблицы `products`, добавления тестовых данных и функций для анализа и обновления данных о продуктах.


