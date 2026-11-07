# Write your MySQL query statement below
SELECT v.customer_id, Count(V.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.Visit_id is null
Group By v.customer_id