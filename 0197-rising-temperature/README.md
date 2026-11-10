<!-- leetcode-notes-sync:start -->
# 197. Rising Temperature

[Open on LeetCode](https://leetcode.com/problems/rising-temperature/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2046903671](https://leetcode.com/problems/rising-temperature/submissions/2046903671/).

# 197. Rising Temperature

## Intuition
We need to find days when the temperature is higher than the previous calendar day's temperature.

A self-join lets us compare two records from the same table.

## Approach
1. Join the Weather table with itself using aliases w1 and w2.
2. Treat w1 as the current day and w2 as the previous day.
3. Use DATEDIFF() = 1 to match dates exactly one day apart.
4. Keep rows where w1.temperature > w2.temperature.
5. Return the current day's id.

## Complexity
Time: O(n²) for a naive pairwise self-join.
Space: Depends on the database execution plan.
Actual performance depends on the optimizer and indexes.

## MySQL Solution

```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```

## Key Takeaways
- SELF JOIN compares rows from the same table.
- DATEDIFF(date1, date2) returns date1 minus date2 in days.
- DATEDIFF() = 1 ensures the dates are exactly one day apart.
- The direction of the DATEDIFF arguments matters.
- Comparing only adjacent rows can be wrong when dates are missing.

Status: Accepted ✅

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2046903671](https://leetcode.com/problems/rising-temperature/submissions/2046903671/) | 2026-06-26 14:22:11 | mysql | [Source](submissions/2046903671.sql) |
<!-- leetcode-notes-sync:end -->
