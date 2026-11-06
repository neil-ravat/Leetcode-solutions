# Write your MySQL query statement below
select pt.product_name,p.year,p.price
FROM sales as p
join Product as pt
on p.product_id = pt.product_id
