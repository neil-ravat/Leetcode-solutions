<!-- leetcode-notes-sync:start -->
# 178. Rank Scores

[Open on LeetCode](https://leetcode.com/problems/rank-scores/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2193110024](https://leetcode.com/problems/rank-scores/submissions/2193110024/).

# 178. Rank Scores

## Intuition
We need to rank scores from highest to lowest.

Equal scores must receive the same rank, and ranks must not have gaps.

DENSE_RANK() is ideal because it handles ties without skipping rank numbers.

## Approach
1. Select the score column from Scores.
2. Apply DENSE_RANK() as a window function.
3. Use ORDER BY score DESC inside OVER() to rank highest first.
4. Name the calculated column `rank`.
5. Sort the final output by score descending.

## Complexity
Time: O(n log n) in a sorting-based execution plan.
Space: Depends on the database's window-function execution plan.

## MySQL Solution

```sql
SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
```

## Key Takeaways
- ROW_NUMBER() gives every row a unique number.
- RANK() assigns the same rank to ties but leaves gaps.
- DENSE_RANK() assigns the same rank to ties without gaps.
- ORDER BY inside OVER() controls ranking.
- The final ORDER BY controls result display order.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2194489181](https://leetcode.com/problems/rank-scores/submissions/2194489181/) | 2026-11-12 09:10:52 | pythondata | [Source](submissions/2194489181.py) |
| [2193110024](https://leetcode.com/problems/rank-scores/submissions/2193110024/) | 2026-11-10 10:58:51 | mysql | [Source](submissions/2193110024.sql) |
<!-- leetcode-notes-sync:end -->
