<!-- leetcode-notes-sync:start -->
# 1251. Average Selling Price

[Open on LeetCode](https://leetcode.com/problems/average-selling-price/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2194843546](https://leetcode.com/problems/average-selling-price/submissions/2194843546/).

# 1251. Average Selling Price

## Intuition
We need to calculate the average selling price of each product.

Since products can have different prices during different
time periods, we must match each sale to the correct price.

We use a weighted average because different quantities
are sold at different prices.

## Approach
1. Use LEFT JOIN to keep all products, including those
   with no sales.
2. Match product_id between Prices and UnitsSold.
3. Use BETWEEN to match each purchase_date to the
   correct price period.
4. Calculate total revenue using SUM(price * units).
5. Calculate total units sold using SUM(units).
6. Divide total revenue by total units.
7. Use ROUND(..., 2) to round to two decimal places.
8. Use COALESCE(..., 0) to handle products without sales.
9. GROUP BY product_id to get one result per product.

## Complexity
Time: O(P × U) for a naive nested-loop join, where P
is the number of price records and U is the number
of sales records. Indexes and optimization can improve this.

Space: Depends on the database's join and grouping
execution plan.

## MySQL Solution

```sql
SELECT
    p.product_id,
    COALESCE(
        ROUND(
            SUM(p.price * u.units) / SUM(u.units),
            2
        ),
        0
    ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
   AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
```

## Key Takeaways
- BETWEEN includes both endpoints.
- LEFT JOIN preserves products without sales.
- Weighted average = SUM(price * units) / SUM(units).
- ROUND(value, 2) rounds to two decimal places.
- COALESCE(value, 0) replaces NULL with 0.
- Qualify column names when both tables share a column.
- GROUP BY p.product_id produces one row per product.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2194843546](https://leetcode.com/problems/average-selling-price/submissions/2194843546/) | 2026-11-12 18:28:06 | mysql | [Source](submissions/2194843546.sql) |
<!-- leetcode-notes-sync:end -->
