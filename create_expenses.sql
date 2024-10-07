-- Set schema for the session
USE memory.default;

CREATE TABLE expenses
(
    employee_id TINYINT,
    unit_price  DECIMAL(8, 2),
    quantity    TINYINT
);

INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 13.0, 75 from employees where first_name = 'Alex' and last_name = 'Jacobson';
INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 22.0, 18 from employees where first_name = 'Alex' and last_name = 'Jacobson';
INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 40.0, 9 from employees where first_name = 'Darren' and last_name = 'Poynton';
INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 300.0, 1 from employees where first_name = 'Andrea' and last_name = 'Ghibaudi';
INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 17.5, 4 from employees where first_name = 'Umberto' and last_name = 'Torrielli';
INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 11.0, 20 from employees where first_name = 'Alex' and last_name = 'Jacobson';
INSERT INTO expenses (employee_id, unit_price, quantity) select employee_id, 6.5, 14 from employees where first_name = 'Alex' and last_name = 'Jacobson';