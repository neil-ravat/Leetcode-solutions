# Write your MySQL query statement below
WITH total as(
  SELECT person_name, turn, weight,
       SUM(weight) OVER (ORDER BY turn) AS total_weight
FROM Queue
)
SELECT person_name FROM total
where  total_weight <= 1000
order by total_weight DESC
LIMIT 1