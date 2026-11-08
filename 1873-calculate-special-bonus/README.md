<!-- leetcode-notes-sync:start -->
# 1873. Calculate Special Bonus

[Open on LeetCode](https://leetcode.com/problems/calculate-special-bonus/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192136239](https://leetcode.com/problems/calculate-special-bonus/submissions/2192136239/).

LeetCode 1873 — Calculate Special Bonus
Difficulty: Easy
Topic: CASE WHEN, AND, NOT LIKE, ORDER BY

Intuition:
Give employees a bonus equal to their salary
if their ID is odd and name doesn't start with M.

Approach:
1. SELECT retrieves employee_id.
2. CASE WHEN checks the two conditions.
3. % 2 = 1 identifies odd employee IDs.
4. NOT LIKE 'M%' excludes names starting with M.
5. THEN salary gives the bonus; ELSE 0 otherwise.
6. ORDER BY sorts employee IDs ascending.

Example:
ID 3 → 0
ID 7 → 7400
ID 9 → 7700

Performance:
Processes each employee and sorts the results.
Sorting typically costs O(n log n).

Key Learnings:
- CASE WHEN works like if-else.
- END closes the CASE expression.
- AND requires both conditions.
- ORDER BY is necessary when sorting is required.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192136239](https://leetcode.com/problems/calculate-special-bonus/submissions/2192136239/) | 2026-11-08 21:17:11 | mysql | [Source](submissions/2192136239.sql) |
<!-- leetcode-notes-sync:end -->
