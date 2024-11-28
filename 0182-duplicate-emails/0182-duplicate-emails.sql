# Write your MySQL query statement below
SELECT e.email AS Email
FROM Person e
GROUP BY e.email
HAVING COUNT(*) > 1;