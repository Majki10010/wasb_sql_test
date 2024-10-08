SELECT
    E.employee_id AS employee_id,
    CONCAT(E.first_name, ' ', E.last_name) AS employee_name,
    E.manager_id AS manager_id,
    (SELECT CONCAT(M.first_name, ' ', M.last_name)
     FROM EMPLOYEES M WHERE M.employee_id = E.manager_id) AS manager_name,
    SUM(EXP.quantity * EXP.unit_price) AS total_expensed_amount
FROM
    EMPLOYEES E
        JOIN EXPENSES EXP ON E.employee_id = EXP.employee_id
GROUP BY
    E.employee_id, E.first_name, E.last_name, E.manager_id
HAVING
    SUM(EXP.quantity * EXP.unit_price) > 1000
ORDER BY
    total_expensed_amount DESC