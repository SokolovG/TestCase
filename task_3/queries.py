# 1. Найти общую сумму заказов для каждого клиента.
TOTAL_ORDER_SUM_BY_CLIENT = """
SELECT customer_id, SUM(amount)
FROM orders
GROUP BY customer_id;
"""

# 2. Найти клиента с максимальной суммой заказов.
MAX_CLIENT_ORDER_SUM = """
SELECT customer_id, SUM(amount)
FROM orders
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 1;
"""
# 3. Найти количество заказов, сделанных в 2023 году.
COUNT_2023_ORDERS_BY_CLIENT = """
SELECT COUNT(id)
FROM orders
WHERE EXTRACT(year FROM order_date) = 2023;
"""
# 4. Найти среднюю сумму заказа для каждого клиента.
AVG_ORDER_SUM_BY_CLIENT = """
SELECT customer_id, AVG(amount)
FROM orders
GROUP BY customer_id;
"""
