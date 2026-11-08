<!-- leetcode-notes-sync:start -->
# 183. Customers Who Never Order

[Open on LeetCode](https://leetcode.com/problems/customers-who-never-order/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192150196](https://leetcode.com/problems/customers-who-never-order/submissions/2192150196/).

183. Customers Who Never Order
Difficulty: Easy
Topic: Correlated Subquery, NOT EXISTS

Intuition:
Find customers who have no matching records in Orders.

Approach:
1. Select customer names.
2. Use NOT EXISTS to check for matching orders.
3. Keep customers with zero matching orders.

Example:
Joe → Has order → Exclude
Henry → No order → Include

Performance:
An index on Orders(customerId) can improve lookup speed.

Key Learnings:
- NOT EXISTS checks whether a subquery returns zero rows.
- SELECT 1 is used because only row existence matters.
- A correlated subquery refers to the outer query.
- LEFT JOIN + IS NULL is another possible approach.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192150196](https://leetcode.com/problems/customers-who-never-order/submissions/2192150196/) | 2026-11-08 22:13:52 | mysql | [Source](submissions/2192150196.sql) |
<!-- leetcode-notes-sync:end -->
