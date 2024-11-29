# Write your MySQL query statement below
# DELETE FROM Person
# WHERE id NOT IN (
#     SELECT MIN(id)
#     FROM Person
#     GROUP BY email
# )
WITH CTE AS (
    SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM Person
)
DELETE FROM Person
WHERE id IN (
    SELECT id
    FROM CTE
    WHERE rn > 1
);

# DELETE p1 FROM Person p1, Person p2
# WHERE p1.email = p2.email and p1.id > p2.id