CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, 
    customer_name VARCHAR(50),
	city VARCHAR (50)
	);
    
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount FLOAT
);

-- Insert data into the Customers table
INSERT INTO Customers (customer_name, city)
VALUES
    ('John Doe','New YORK'),
    ('Jane Smith','Los Angeles'),
    ('David Johnson','Chicago');
    
-- Insert data into the orders table
INSERT INTO orders (customer_id,order_date,total_amount)
VALUES
    (1,'2022-01-10',100.00),
	(1,'2022-02-15',150.00),
	(2,'2022-03-20',200.00),
	(3,'2022-04-25',50.00);
	
begin 

SELECT customers.customer_name, count(orders.order_id) as total_orders
FROM customers
JOIN orders
on customers.customer_id = orders.customer_id
group by 1

commit




drop table Customers;
drop table Orders;

select * from Customers
select * from Orders