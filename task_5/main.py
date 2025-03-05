from typing import Final

from core import base_logger


input_list: Final[list[int]] = [10, 20, 30, 40, 50, 30, 20]


def analyze_numbers(numbers: list[int]) -> dict[int | list[int]]:
    """Анализирует список чисел и возвращает статистику.

    Args:
        numbers: Список чисел для анализа.

    Returns:
        Словарь со следующими ключами:
            - "Уникальные числа": количество уникальных чисел в списке
            - "Второе по величине число": второе максимальное число в списке
            - "Числа, делящиеся на 3": список всех чисел, которые делятся на 3
    """
    result = {}
    unique_numbers = len(set(numbers))
    divisible_by_three = [num for num in numbers if num % 3 == 0]
    max_num = max(numbers)
    numbers.pop(numbers.index(max(numbers)))

    result["Уникальные числа"] = unique_numbers
    result["Второе по величине число"] = max(numbers)
    result["Числа, делящиеся на 3"] = divisible_by_three

    return result


def main() -> None:
    """Основная логика программы.

    Вызывает функцию analyze_numbers со списком чисел и логирует результат.
    """
    base_logger.log(analyze_numbers(input_list), level="info")


if __name__ == "__main__":
    main()
