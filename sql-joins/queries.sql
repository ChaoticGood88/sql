SELECT o.id AS owner_id, o.first_name, o.last_name, v.id 
AS vehicle_id, v.make, v.model, v.year, v.price, v.owner_id
FROM owners o
LEFT JOIN vehicles v ON o.id = v.owner_id
ORDER BY o.id, v.id;

SELECT o.first_name, o.last_name, COUNT(v.id) AS count
FROM owners o
LEFT JOIN vehicles v ON o.id = v.owner_id
GROUP BY o.id, o.first_name, o.last_name
HAVING COUNT(v.id) > 0
ORDER BY o.first_name ASC;

SELECT o.first_name, o.last_name, 
ROUND(AVG(v.price)) AS average_price, 
COUNT(v.id) AS count
FROM owners o
LEFT JOIN vehicles v ON o.id = v.owner_id
GROUP BY o.id, o.first_name, o.last_name
HAVING COUNT(v.id) > 1 AND AVG(v.price) > 10000
ORDER BY o.first_name DESC;