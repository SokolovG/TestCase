from typing import Final

input_list: Final[list[int]] = [10, 20, 30, 40, 50, 30, 20]


def analyze_numbers(numbers: list[int]) -> dict[int | list[int]]:
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
    print(analyze_numbers(input_list))


if __name__ == "__main__":
    main()
