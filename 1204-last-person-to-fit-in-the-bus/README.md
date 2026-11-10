<!-- leetcode-notes-sync:start -->
# 1204. Last Person to Fit in the Bus

[Open on LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2193143995](https://leetcode.com/problems/last-person-to-fit-in-the-bus/submissions/2193143995/).

# 1204. Last Person to Fit in the Bus

## Intuition
We need to find the last person who can board a bus without
exceeding its 1000 kg weight limit.

Since people board in turn order, we need a running total
of their weights.

## Approach
1. Use SUM(weight) OVER (ORDER BY turn) to calculate the
   cumulative weight as each person boards.
2. Store the running total in a CTE.
3. Filter people whose cumulative weight is <= 1000.
4. Sort by cumulative weight descending.
5. Use LIMIT 1 to return the last qualifying person.

## Complexity
Time: O(n log n) for a sorting-based execution plan.
Space: O(n) for intermediate window/CTE results.
Actual performance depends on the database optimizer.

## MySQL Solution

```sql
WITH total AS (
    SELECT person_name, turn, weight,
           SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
SELECT person_name
FROM total
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;
```

## Key Takeaways
- SUM() OVER() calculates a running total without collapsing rows.
- ORDER BY inside OVER() determines the accumulation sequence.
- A CTE allows filtering a calculated window-function result.
- LIMIT 1 returns a single row after sorting.
- ORDER BY turn DESC is another way to select the last
  qualifying person and directly reflects boarding order.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2193143995](https://leetcode.com/problems/last-person-to-fit-in-the-bus/submissions/2193143995/) | 2026-11-10 12:07:53 | mysql | [Source](submissions/2193143995.sql) |
<!-- leetcode-notes-sync:end -->
