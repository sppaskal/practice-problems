SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees
WHERE department = 'Engineering' AND salary > 70000