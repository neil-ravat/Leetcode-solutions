# Write your MySQL query statement below
WITH cn as (
    SELECT num, LAG(num) OVER (order by id ) as prev,
     LEAD(num) OVER (ORDER BY id) as next
    FROM Logs
)
SELECT distinct num as ConsecutiveNums
FROM cn
WHERE prev = num AND next = prev