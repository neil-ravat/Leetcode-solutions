# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary
From employee
where salary < (SELECT MAX(salary)
                FROM employee);