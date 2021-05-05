-- SHOW DATABASES;
-- use sql_store;

#SELECT * FROM sql_store.customers where customer_id = 6;
/*
select 
	last_name, 
	first_name, 
    points, 
    points * 10 +100 as `discount points`
 from sql_store.customers 
 where points > 1486
 order by points desc;
 
 */

/*
SELECT * 
FROM sql_store.customers
WHERE birth_date > '1990-01-01' OR 
	(points > 1000 AND state <> 'FL');
    
*/
 
 /*
SELECT *
FROM sql_store.customers
WHERE last_name LIKE 'B%y';
*/

/*
SELECT *
FROM sql_store.customers
#WHERE last_name REGEXP 'field$|mac|rose'
WHERE last_name REGEXP '[gim]e'
*/

/*
SELECT *
FROM sql_store.customers
#WHERE first_name in ('ELKA', 'AMBUR') AND
WHERE first_name REGEXP 'ELKA|AMBUR' OR
	#last_name REGEXP 'EY$|ON$'
    #last_name REGEXP '^my|se'
    last_name REGEXP 'br|bu'
    */

/* 
-- NULL operation
SELECT *
FROM sql_store.customers
WHERE phone is  NULL


SELECT *
FROM sql_store.orders
WHERE shipped_date IS NULL
LIMIT 3


SELECT  *
FROM sql_store.customers
LIMIT 6, 3
*/
/*
-- Get the top three loyal customers
SELECT *
FROM sql_store.customers
ORDER BY points DESC
LIMIT 3

*/
/*
-- JOIN 
SELECT order_id, orders.customer_id, first_name, last_name
FROM sql_store.orders
JOIN sql_store.customers
	ON sql_store.orders.customer_id = sql_store.customers.customer_id
*/

/*
SELECT order_id, oi.product_id, quantity, oi.unit_price
FROM sql_store.order_items oi
JOIN sql_store.products p ON oi.product_id = p.product_id
*/

/*
-- use different database
SELECT *
FROM sql_store.order_items oi
JOIN sql_inventory.products p
	ON oi.product_id = p.product_id
*/

/*
USE sql_hr;
SELECT
	e.employee_id,
    e.first_name,
    m.first_name AS manager
FROM employees e
JOIN employees m
	ON e.reports_to = m.employee_id
*/

/*
-- JOIN three tables
USE sql_store;

SELECT 
	o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    os.name AS status
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id
*/

/*
USE sql_invoicing;

SELECT 
	p.date,
    p.amount,
    pm.name
    
FROM payments p
JOIN clients c
	ON p.client_id = c.client_id
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
*/

USE sql_store;

/*
SELECT *
FROM order_items
LIMIT 10;
*/

/*
SELECT *
FROM order_items oi
JOIN order_item_notes oin
	USING (order_id, product_id)
    #ON oi.order_id = oin.order_id 
    #oi.product_id = oin.product_id

*/

/*
USE sql_store;

SELECT
	c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date,
	os.name as 'Status',
    sh.name as 'Shipper'
FROM customers c
LEFT JOIN orders o
	-- ON c.customer_id = o.customer_id
    USING (customer_id)
LEFT JOIN order_statuses os
 	ON o.status = os.order_status_id
JOIN shippers sh
	-- ON sh.shipper_id = o.shipper_id
    USING (shipper_id)
ORDER BY c.customer_id
*/

/*
USE sql_hr;

SELECT 
	e.employee_id,
    e.first_name,
    m.first_name AS manager
FROM employees e
LEFT JOIN employees m
	ON e.reports_to = m.employee_id
*/

/*
USE sql_invoicing;

SELECT 
	p.date,
    c.name AS client,
    p.amount,
    pm.name as payment_method
FROM payments p
JOIN clients c USING (client_id)
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id

  */
  /*
  SELECT 
	o.order_id,
    c.first_name
  FROM orders o
  -- NATURAL JOIN customers c
  -- JOIN customers c
  CROSS JOIN customers c
 */
 
 /*
 SELECT 
	customer_id, 
	first_name, 
    points, 
    'Bronze' as type
FROM customers
WHERE points < 2000
UNION
 SELECT 
	customer_id, 
	first_name, 
    points, 
    'Silver' as type
FROM customers
WHERE points  BETWEEN 2000 AND 3000
UNION
 SELECT 
	customer_id, 
	first_name, 
    points, 
    'Golden' as type
FROM customers
WHERE points > 3000
*/

/*
INSERT INTO orders_archived
#CREATE TABLE orders_archived AS
SELECT *
FROM orders
WHERE order_date < '2019-01-01'
*/

/*
-- update a single row
USE sql_invoicing;

UPDATE invoices
SET 
	payment_total = payment_total + 1
	#payment_date = due_date
WHERE client_id = 1
*/

USE sql_store;

UPDATE customers
SET points = points + 50
WHERE birth_date < '1990-01-01'


