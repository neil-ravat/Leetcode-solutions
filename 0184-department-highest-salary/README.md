<!-- leetcode-notes-sync:start -->
# 184. Department Highest Salary

[Open on LeetCode](https://leetcode.com/problems/department-highest-salary/)

**Difficulty:** Medium

## My notes

### Submission notes

From accepted submission [#2194501087](https://leetcode.com/problems/department-highest-salary/submissions/2194501087/).

LeetCode #184 — Department Highest Salary
Difficulty: Medium
Pattern: GroupBy + Transform + Filtering + Merge

Approach:
1. Group employees by departmentId.
2. Use transform("max") to calculate each row's
   department maximum salary.
3. Filter where employee salary equals department maximum.
4. Merge with Department to retrieve department names.
5. Rename columns and return Department, Employee, Salary.

Key Learnings:
- groupby().max() gives one result per department.
- groupby().transform("max") returns one result per employee.
- transform() preserves the original row indices.
- Equality filtering keeps all employees tied for highest salary.
- pd.merge() combines employee and department information.
- Column names are case-sensitive.

Time Complexity: O(n + m) average
Space Complexity: O(n + m)

n = number of employees
m = number of departments

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2194501087](https://leetcode.com/problems/department-highest-salary/submissions/2194501087/) | 2026-11-12 09:31:15 | pythondata | [Source](submissions/2194501087.py) |
<!-- leetcode-notes-sync:end -->
