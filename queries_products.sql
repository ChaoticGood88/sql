-- Query 1: Add "chair" product
INSERT INTO products (name, price, can_be_returned)
VALUES ('chair', 44.00, false);

-- Query 2: Add "stool" product
INSERT INTO products (name, price, can_be_returned)
VALUES ('stool', 25.99, true);

-- Query 3: Add "table" product
INSERT INTO products (name, price, can_be_returned)
VALUES ('table', 124.00, false);

-- Query 4: Display all products
SELECT * FROM products;

-- Query 5: Display all product names
SELECT name FROM products;

-- Query 6: Display all product names and prices
SELECT name, price FROM products;

-- Query 7: Add "lamp" product
INSERT INTO products (name, price, can_be_returned)
VALUES ('lamp', 35.50, true);

-- Query 8: Display products that can be returned
SELECT * FROM products
WHERE can_be_returned = true;

-- Query 9: Display products with price less than 44.00
SELECT * FROM products
WHERE price < 44.00;

-- Query 10: Display products with price between 22.50 and 99.99
SELECT * FROM products
WHERE price BETWEEN 22.50 AND 99.99;

-- Query 11: Reduce the price of all products by $20
UPDATE products
SET price = price - 20;

-- Query 12: Delete products with price less than $25
DELETE FROM products
WHERE price < 25;

-- Query 13: Increase the price of remaining products by $20
UPDATE products
SET price = price + 20;

-- Query 14: Set all products to be returnable
UPDATE products
SET can_be_returned = true;