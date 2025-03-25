SELECT
    w2.id
FROM
    Weather w2
JOIN
    Weather w1
ON
    DATE_ADD(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
WHERE
    w1.temperature < w2.temperature