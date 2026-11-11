<!-- leetcode-notes-sync:start -->
# 176. Second Highest Salary

[Open on LeetCode](https://leetcode.com/problems/second-highest-salary/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2192148225](https://leetcode.com/problems/second-highest-salary/submissions/2192148225/).

176. Second Highest Salary
Difficulty: Medium
Topic: Subqueries, Aggregation

Intuition:
Find the highest salary, exclude it, then find the
maximum salary among the remaining employees.

Approach:
1. Inner MAX() finds the highest salary.
2. WHERE removes salaries equal to that maximum.
3. Outer MAX() finds the second-highest distinct salary.

Example:
[100, 300, 200, 300] → 200

Complexity:
Time: O(n) approximately without an index
Space: O(1)

Key Learning:
- Subqueries can calculate values used by WHERE.
- Strictly less than (<) handles duplicate maximum salaries.
- MAX() returns NULL when no qualifying values exist.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2193933000](https://leetcode.com/problems/second-highest-salary/submissions/2193933000/) | 2026-11-11 14:22:33 | pythondata | [Source](submissions/2193933000.py) |
| [2192148225](https://leetcode.com/problems/second-highest-salary/submissions/2192148225/) | 2026-11-08 22:05:49 | mysql | [Source](submissions/2192148225.sql) |
<!-- leetcode-notes-sync:end -->
