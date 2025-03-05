from typing import Final

from core import Logger


logger = Logger("Task_5")
input_list: Final[list[int]] = [10, 20, 30, 40, 50, 30, 20]


def analyze_numbers(numbers: list[int]) -> dict[str, int | list[int]]:
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
    numbers_copy = numbers.copy()

    result["Числа, делящиеся на 3"] = [num for num in numbers if num % 3 == 0]
    result["Уникальные числа"] = len(set(numbers))

    sorted_unique = sorted(set(numbers_copy), reverse=True)
    result["Второе по величине число"] = sorted_unique[1] if len(sorted_unique) > 1 else None


    return result


def main() -> None:
    """Основная логика программы.

    Вызывает функцию analyze_numbers со списком чисел и логирует результат.
    """
    logger.info(analyze_numbers(input_list))


if __name__ == "__main__":
    main()
