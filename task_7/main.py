from typing import Optional

from core import get_cursor, Logger


logger = Logger("Task_7")


def list_products_less_10() -> list[tuple[str]]:
    """Возвращает список продуктов с количеством меньше 10.

    Returns:
        Список кортежей, содержащих информацию о продуктах.
        В случае ошибки возвращает пустой список.
    """
    try:
        with get_cursor() as cur:
            cur.execute("SELECT * FROM products WHERE quantity < 10;")
            data = cur.fetchall()
            return data

    except Exception as e:
        logger.error(f"Ошибка при получении продуктов: {e}")
        return []


def update_price_by_name(new_price: int, name: str) -> None:
    """Обновляет цену продукта по его названию.

    Args:
       new_price: Новая цена продукта. Должна быть неотрицательной.
       name: Название продукта, цену которого нужно обновить.
    """
    if new_price < 0:
        logger.error("Цена не может быть отрицательной")
        return

    try:
        with get_cursor() as cur:
            cur.execute(
                "UPDATE products SET price = %s WHERE name = %s", (new_price, name)
            )

    except Exception as e:
        logger.error(f"Ошибка при обновлении цены: {e}")
        return


def main() -> None:
    """Основная функция программы.

    Получает список продуктов с количеством меньше 10 и выводит информацию в лог.
    """
    data = list_products_less_10()
    logger.info(data)


if __name__ == "__main__":
    main()
