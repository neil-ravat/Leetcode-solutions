<!-- leetcode-notes-sync:start -->
# 177. Nth Highest Salary

[Open on LeetCode](https://leetcode.com/problems/nth-highest-salary/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2193105486](https://leetcode.com/problems/nth-highest-salary/submissions/2193105486/).

Pattern: Sorting + Deduplication + Indexing

Approach:
1. Remove duplicate salaries using drop_duplicates().
2. Sort salaries in descending order.
3. Check if N is between 1 and the number of distinct salaries.
4. If valid, retrieve the Nth highest salary using .iloc[N - 1].
5. Otherwise, return None.
6. Return a one-row DataFrame with the required column name.

Key Learning:
- drop_duplicates() removes repeated values.
- ascending=False sorts from highest to lowest.
- .iloc[] selects by position, not index label.
- Python uses 0-based indexing, so Nth position = N - 1.
- pd.DataFrame({"column": [value]}) creates a one-row DataFrame.
- Always handle invalid N to avoid IndexError.

Time Complexity: O(n log n) — sorting
Space Complexity: O(n) — processed DataFrame

Important Edge Cases:
- Duplicate salaries count only once.
- N > number of distinct salaries → None.
- N <= 0 → None.
- Only one distinct salary with N = 1 → that salary.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2193105486](https://leetcode.com/problems/nth-highest-salary/submissions/2193105486/) | 2026-11-10 10:49:57 | pythondata | [Source](submissions/2193105486.py) |
<!-- leetcode-notes-sync:end -->
