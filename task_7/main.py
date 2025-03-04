from typing import Optional

from constants import get_cursor


def list_products_less_10() -> Optional[list[tuple[str]]]:
    try:
        with get_cursor() as cur:
            cur.execute("SELECT * FROM products WHERE quantity < 10;")
            data = cur.fetchall()
            return data

    except Exception as e:
        print(f"Ошибка при получении продуктов: {e}")
        return []


def update_price_by_name(new_price: int, name: str) -> None:
    if new_price < 0:
        print("Цена не может быть отрицательной")
        return

    try:
        with get_cursor() as cur:
            cur.execute(
                "UPDATE products SET price = %s WHERE name = %s", (new_price, name)
            )

    except Exception as e:
        print(f"Ошибка при обновлении цены: {e}")
        return


def main() -> None:
    data = list_products_less_10()
    print(data)


if __name__ == "__main__":
    main()
