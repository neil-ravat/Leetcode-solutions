<!-- leetcode-notes-sync:start -->
# 1581. Customer Who Visited but Did Not Make Any Transactions

[Open on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191567901](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/2191567901/).

LeetCode 1581 — Customer Who Visited but
Did Not Make Any Transactions

Difficulty: Easy
Topic: LEFT JOIN, IS NULL, GROUP BY, COUNT

Intuition:
Find visits without transactions and count
how many such visits each customer made.

Approach:
1. LEFT JOIN Visits with Transactions.
2. Match records using visit_id.
3. WHERE IS NULL finds visits without transactions.
4. GROUP BY customer_id groups those visits.
5. COUNT() calculates visits per customer.

Example:
Customer 30 → 1 visit
Customer 96 → 1 visit
Customer 54 → 2 visits

Complexity:
Time: O(n + m) expected with a hash join.
Space: O(m + k) for joining and grouping.
Actual performance depends on the database engine.

Key Learnings:
- LEFT JOIN preserves unmatched visits.
- IS NULL identifies missing matches.
- GROUP BY creates one group per customer.
- COUNT() counts records within each group.
- COUNT(column) ignores NULL values.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191567901](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/2191567901/) | 2026-11-07 20:32:30 | mysql | [Source](submissions/2191567901.sql) |
| [2046090822](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/2046090822/) | 2026-06-25 17:58:56 | mysql | [Source](submissions/2046090822.sql) |
<!-- leetcode-notes-sync:end -->
