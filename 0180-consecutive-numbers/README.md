<!-- leetcode-notes-sync:start -->
# 180. Consecutive Numbers

[Open on LeetCode](https://leetcode.com/problems/consecutive-numbers/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2193078139](https://leetcode.com/problems/consecutive-numbers/submissions/2193078139/).

# 180. Consecutive Numbers

## Intuition
We need to find numbers appearing at least 3 times consecutively.

If the previous, current, and next numbers are equal, we have found 3 consecutive occurrences.

## Approach
1. Use LAG() to get the previous number.
2. Use LEAD() to get the next number.
3. ORDER BY id to preserve the original sequence.
4. Store the results in a CTE.
5. Filter where prev = num AND next = prev.
6. Use DISTINCT to avoid duplicate results.

## Complexity
Time: O(n log n) in the worst case due to ordering.
Space: O(n) for intermediate results.
Actual performance depends on the SQL execution plan.

## MySQL Solution

```sql
WITH cn AS (
    SELECT num,
           LAG(num) OVER (ORDER BY id) AS prev,
           LEAD(num) OVER (ORDER BY id) AS next
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM cn
WHERE prev = num AND next = prev;
```

## Key Takeaways
- LAG() accesses the previous row.
- LEAD() accesses the next row.
- ORDER BY inside OVER() controls the window sequence.
- CTEs help filter window-function results.
- DISTINCT removes duplicate outputs.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2193078139](https://leetcode.com/problems/consecutive-numbers/submissions/2193078139/) | 2026-11-10 09:57:06 | mysql | [Source](submissions/2193078139.sql) |
<!-- leetcode-notes-sync:end -->
