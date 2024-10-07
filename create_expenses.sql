-- Set schema for the session
USE memory.default;

CREATE TABLE expenses
(
    employee_id TINYINT,
    unit_price  DECIMAL(8, 2),
    quantity    TINYINT
);

