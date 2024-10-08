USE memory.default;

CREATE TABLE supplier
(
    id TINYINT NOT NULL ,
    name        VARCHAR
);


CREATE TABLE invoice
(
    supplier_id    TINYINT NOT NULL,
    id    TINYINT NOT NULL,
    invoice_amount DECIMAL(8, 2),
    due_date       DATE
    --PRIMARY KEY (id)
    --FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id) -- just informational as trino does not supprpt foreong key constraaints
);