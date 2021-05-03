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



    
 