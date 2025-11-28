-- PostgreSQL

-- What % of first orders (for each customer) are immediate

SELECT
    -- sum up number of immediate first orders and divide
    -- by the number of total first orders (# of customers)
    ROUND(
        SUM(CASE
            WHEN d1.order_date = d1.customer_pref_delivery_date
            THEN 1 ELSE 0 END) * 100 / COUNT(*),
        2) AS immediate_percentage
FROM Delivery d1
WHERE d1.order_date = (
    -- filter for first order for each customer
    SELECT MIN(d2.order_date)
    FROM Delivery d2
    WHERE d1.customer_id = d2.customer_id
)