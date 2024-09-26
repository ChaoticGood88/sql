-- Query 1: Find the app with ID 1880
SELECT *
FROM analytics
WHERE id = 1880;

-- Query 2: Find apps last updated on August 01, 2018
SELECT id, app_name
FROM analytics
WHERE last_updated = '2018-08-01';

-- Query 3: Count the number of apps in each category
SELECT category, COUNT(*) AS app_count
FROM analytics
GROUP BY category
ORDER BY app_count DESC;

-- Query 4: Find the top 5 most-reviewed apps
SELECT app_name, reviews
FROM analytics
ORDER BY reviews DESC
LIMIT 5;

-- Query 5: Find the app with the most reviews and rating >= 4.8
SELECT app_name, reviews, rating
FROM analytics
WHERE rating >= 4.8
ORDER BY reviews DESC
LIMIT 1;

-- Query 6: Find average rating for each category ordered from highest to lowest
SELECT category, AVG(rating) AS average_rating
FROM analytics
GROUP BY category
ORDER BY average_rating DESC;

-- Query 7: Find the most expensive app with a rating less than 3
SELECT app_name, price, rating
FROM analytics
WHERE rating < 3
ORDER BY price DESC
LIMIT 1;

-- Query 8: Find apps with min_installs <= 50 that have a rating, ordered by highest rating first
SELECT *
FROM analytics
WHERE min_installs <= 50 AND rating IS NOT NULL
ORDER BY rating DESC;

-- Query 9: Find app names rated less than 3 with at least 10,000 reviews
SELECT app_name
FROM analytics
WHERE rating < 3 AND reviews >= 10000;

-- Query 10: Find top 10 most-reviewed apps costing between $0.10 and $1.00
SELECT app_name, reviews, price
FROM analytics
WHERE price BETWEEN 0.10 AND 1.00
ORDER BY reviews DESC
LIMIT 10;

-- Query 11: Find the most out of date app
SELECT *
FROM analytics
WHERE last_updated = (
    SELECT MIN(last_updated)
    FROM analytics);

    -- Query 12: Find the most expensive app
SELECT *
FROM analytics
WHERE price = (
    SELECT MAX(price)
    FROM analytics);

    -- Query 13: Count total number of reviews
SELECT SUM(reviews) AS total_reviews
FROM analytics;

-- Query 14: Find categories with more than 300 apps
SELECT category, COUNT(*) AS app_count
FROM analytics
GROUP BY category
HAVING COUNT(*) > 300;

-- Query 15: Find the app with the highest min_installs to reviews proportion
SELECT app_name, reviews, min_installs, (min_installs::float / reviews) AS proportion
FROM analytics
WHERE min_installs >= 100000 AND reviews > 0
ORDER BY proportion DESC
LIMIT 1;