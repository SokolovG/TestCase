from typing import Optional

from core import get_cursor, base_logger


def list_products_less_10() -> Optional[list[tuple[str]]]:
    try:
        with get_cursor() as cur:
            cur.execute("SELECT * FROM products WHERE quantity < 10;")
            data = cur.fetchall()
            return data

    except Exception as e:
        base_logger.log(f"Ошибка при получении продуктов: {e}", level="error")
        return []


def update_price_by_name(new_price: int, name: str) -> None:
    if new_price < 0:
        base_logger.log("Цена не может быть отрицательной", level="error")
        return

    try:
        with get_cursor() as cur:
            cur.execute(
                "UPDATE products SET price = %s WHERE name = %s", (new_price, name)
            )

    except Exception as e:
        base_logger.log(f"Ошибка при обновлении цены: {e}", level="error")
        return


def main() -> None:
    data = list_products_less_10()
    base_logger.log(data, level="info")


if __name__ == "__main__":
    main()
