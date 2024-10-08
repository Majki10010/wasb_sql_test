USE memory.default;
INSERT INTO invoice (supplier_id, id, invoice_amount, due_date) select supplier.id, 1,1500.0, CAST('2025-01-08' AS DATE) from supplier where name = 'Catering Plus';
INSERT INTO invoice (supplier_id, id, invoice_amount, due_date) select supplier.id, 2,500.0, CAST('2024-11-08' AS DATE) from supplier where name = 'Dave''s Discos';
INSERT INTO invoice (supplier_id, id, invoice_amount, due_date) select supplier.id, 3,4000.0, CAST('2025-04-08' AS DATE) from supplier where name = 'Ice Ice Baby';
INSERT INTO invoice (supplier_id, id, invoice_amount, due_date) select supplier.id, 4,2000.0, CAST('2024-12-08' AS DATE) from supplier where name = 'Catering Plus';
INSERT INTO invoice (supplier_id, id, invoice_amount, due_date) select supplier.id, 5,6000.0, CAST('2025-01-08' AS DATE) from supplier where name = 'Entertainment tonight';
INSERT INTO invoice (supplier_id, id, invoice_amount, due_date) select supplier.id, 6,6000.0, CAST('2025-01-08' AS DATE) from supplier where name = 'Party Animals';
