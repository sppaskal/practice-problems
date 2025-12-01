-- PostgreSQL

-- What % of first orders (for each customer) are immediate

SELECT 
    -- Calculate percentage of immediate first orders
    ROUND(
        SUM(
            CASE 
                -- Immediate order = order_date matches preferred delivery date
                WHEN d.order_date = d.customer_pref_delivery_date
                THEN 1 
                ELSE 0 
            END
        ) * 100.0 / COUNT(*),   -- Divide by total first orders (one per customer)
        2
    ) AS immediate_percentage
FROM Delivery d
JOIN (
    -- Step 1: Find the earliest order_date for each customer
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) f
    -- Step 2: Match each customer’s first order back to the Delivery table
    ON d.customer_id = f.customer_id 
    AND d.order_date = f.first_order_date;
