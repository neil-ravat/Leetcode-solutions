<!-- leetcode-notes-sync:start -->
# 1193. Monthly Transactions I

[Open on LeetCode](https://leetcode.com/problems/monthly-transactions-i/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2194562398](https://leetcode.com/problems/monthly-transactions-i/submissions/2194562398/).

# 1193. Monthly Transactions I

## Intuition
We need monthly transaction statistics for each country,
including total transactions and approved transactions.

Use GROUP BY with conditional aggregation.

## Approach
1. Use DATE_FORMAT() to extract year and month.
2. GROUP BY month and country.
3. COUNT(*) counts all transactions.
4. SUM(CASE WHEN ... THEN 1 ELSE 0 END) counts approvals.
5. SUM(amount) calculates the total amount.
6. SUM(CASE WHEN ... THEN amount ELSE 0 END)
   calculates the approved amount.

## Complexity
Time: O(n) with hash aggregation, or O(n log n)
with sorting-based grouping.
Space: O(k) for k month-country groups.
Actual performance depends on the query execution plan.

## MySQL Solution

```sql
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
       country,
       COUNT(*) AS trans_count,
       SUM(CASE WHEN state = 'approved'
                THEN 1 ELSE 0 END) AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(CASE WHEN state = 'approved'
                THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
```

## Key Takeaways
- DATE_FORMAT() extracts the required month.
- GROUP BY creates one group per month and country.
- CASE WHEN inside SUM() performs conditional aggregation.
- ELSE 0 handles non-approved transactions.
- WHERE state = 'approved' would incorrectly exclude
  declined transactions from overall totals.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2194562398](https://leetcode.com/problems/monthly-transactions-i/submissions/2194562398/) | 2026-11-12 11:22:53 | mysql | [Source](submissions/2194562398.sql) |
<!-- leetcode-notes-sync:end -->
