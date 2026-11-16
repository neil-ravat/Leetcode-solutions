<!-- leetcode-notes-sync:start -->
# 1164. Product Price at a Given Date

[Open on LeetCode](https://leetcode.com/problems/product-price-at-a-given-date/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2197255023](https://leetcode.com/problems/product-price-at-a-given-date/submissions/2197255023/).

# 1164. Product Price at a Given Date

## Intuition
We need to find the price of every product on August 16, 2019.

Each product initially costs 10. If its price changes,
we must select the most recent change on or before
the target date.

We can use ROW_NUMBER() to find the latest valid price
for each product and LEFT JOIN to include products
that have no qualifying price changes.

## Approach
1. Use a CTE to filter price changes on or before
   August 16, 2019.
2. Apply ROW_NUMBER() partitioned by product_id.
3. Order by change_date DESC so the latest price
   receives rn = 1.
4. Get all distinct product IDs from the Products table.
5. LEFT JOIN the latest prices using product_id
   and rn = 1.
6. Use COALESCE(new_price, 10) to assign the default
   price to products with no qualifying changes.

## Complexity
Time: O(n log n) for sorting and ranking n price records.
Space: O(n) for intermediate ranking and join results.

Actual performance depends on the database execution plan.

## MySQL Solution

```sql
WITH latest_price AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT
    p.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM Products
) p
LEFT JOIN latest_price lp
    ON p.product_id = lp.product_id
   AND lp.rn = 1;
```

## Key Takeaways
- ROW_NUMBER() assigns a unique number to each row.
- PARTITION BY restarts numbering for each product.
- ORDER BY change_date DESC selects the latest record.
- Filter by the target date before ranking.
- SELECT DISTINCT retrieves all product IDs.
- LEFT JOIN keeps products without earlier price changes.
- COALESCE() replaces missing prices with the default 10.
- Put rn = 1 inside the JOIN condition to preserve
  unmatched products.
- The latest price is not necessarily the highest price.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2197255023](https://leetcode.com/problems/product-price-at-a-given-date/submissions/2197255023/) | 2026-11-16 11:18:38 | mysql | [Source](submissions/2197255023.sql) |
<!-- leetcode-notes-sync:end -->
