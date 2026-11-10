# Write your MySQL query statement below
SELECT score, DENSE_RANK() OVER (ORDER BY SCORE DESC) AS 'Rank'
FROM Scores
ORDER BY score DESC