-- Set schema for the session
USE memory.default;

-- Create table employees
CREATE TABLE employees
(
    employee_id TINYINT,
    first_name  VARCHAR,
    last_name   VARCHAR,
    job_title   VARCHAR,
    manager_id  INT
);
-- insert values to the table
INSERT INTO employees (employee_id, first_name, last_name, job_title, manager_id)
VALUES (1, 'Ian', 'James', 'CEO', 4),
       (2, 'Umberto', 'Torrielli', 'CSO', 1),
       (3, 'Alex', 'Jacobson', 'MD EMEA', 2),
       (4, 'Darren', 'Poynton', 'CFO', 2),
       (5, 'Tim', 'Beard', 'MD APAC', 2),
       (6, 'Gemma', 'Dodd', 'COS', 1),
       (7, 'Lisa', 'Platten', 'CHR', 6),
       (8, 'Stefano', 'Camisaca', 'GM Activation', 2),
       (9, 'Andrea', 'Ghibaudi', 'MD NAM', 2);
