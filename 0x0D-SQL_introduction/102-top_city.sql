-- Write a script that displays the top 3 of cities temperature
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY 2 DESC
LIMIT 3;
