WITH
  invoice_aggregates AS (
    SELECT
        supplier_id,
        SUM(invoice_amount) AS total_due,
        CAST((year(MAX(due_date)) - year(current_date)) * 12 + month(MAX(due_date)) - month(current_date) + 1 AS INTEGER) AS months_until_due_date,
        MAX(due_date) AS last_due_date
    FROM invoice
    GROUP BY supplier_id
  ),
  calculated_payments AS (
    SELECT
        i.supplier_id,
        i.total_due / i.months_until_due_date AS payment_amount,
        date_add('month', cast(element as int), date_trunc('month', current_date)) - INTERVAL '1' DAY AS payment_date,
        row_number() over (partition by i.supplier_id order by date_add('month', cast(element as int), date_trunc('month', current_date))) as payment_num
    FROM invoice_aggregates i
    CROSS JOIN UNNEST(sequence(0, i.months_until_due_date - 1)) AS t(element)
  )
SELECT
    s.id,
    s.name AS supplier_name,
    DATE_TRUNC('month', cp.payment_date) AS payment_month,
    cp.payment_amount AS total_payment_for_month,
    ia.total_due - cp.payment_amount * cp.payment_num as balance_outstanding,
    MIN(cp.payment_date) AS earliest_payment_date,
    MAX(cp.payment_date) AS latest_payment_date
FROM supplier s
         JOIN calculated_payments cp ON s.id = cp.supplier_id
         JOIN invoice_aggregates ia ON ia.supplier_id = cp.supplier_id
GROUP BY s.id, s.name, DATE_TRUNC('month', cp.payment_date), cp.payment_amount, ia.total_due, cp.payment_num
ORDER BY s.id, payment_month