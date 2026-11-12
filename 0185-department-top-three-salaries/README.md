<!-- leetcode-notes-sync:start -->
# 185. Department Top Three Salaries

[Open on LeetCode](https://leetcode.com/problems/department-top-three-salaries/)

**Difficulty:** Hard

## My notes

### Submission notes

From accepted submission [#2194554563](https://leetcode.com/problems/department-top-three-salaries/submissions/2194554563/).

LeetCode #185 — Department Top Three Salaries
Difficulty: Hard
Pattern: GroupBy + Dense Rank + Filtering + Merge

Approach:
1. Group employees by departmentId.
2. Rank salary within each department using:
   .rank(method="dense", ascending=False)
3. Keep employees whose rank <= 3.
4. Merge with Department to retrieve department names.
5. Rename columns and return Department, Employee, Salary.

Key Learnings:
- groupby() separates data into departments.
- GroupBy.rank() ranks values within each group.
- Dense ranking gives equal salaries the same rank.
- Dense ranking does not skip numbers after ties.
- Filtering rank <= 3 keeps the top 3 distinct salary levels.
- Multiple employees can qualify at the same salary level.

Time Complexity: O(n log n + m)
Space Complexity: O(n + m)

n = number of employees
m = number of departments

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2194554563](https://leetcode.com/problems/department-top-three-salaries/submissions/2194554563/) | 2026-11-12 11:06:51 | pythondata | [Source](submissions/2194554563.py) |
<!-- leetcode-notes-sync:end -->
