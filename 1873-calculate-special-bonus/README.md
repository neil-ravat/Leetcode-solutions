<!-- leetcode-notes-sync:start -->
# 1873. Calculate Special Bonus

[Open on LeetCode](https://leetcode.com/problems/calculate-special-bonus/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192758658](https://leetcode.com/problems/calculate-special-bonus/submissions/2192758658/).

LeetCode #1873 — Calculate Special Bonus

Pattern: Boolean Masking + Conditional Assignment

Approach:
1. Check odd IDs using employee_id % 2 != 0.
2. Exclude names starting with M using ~ and .str.startswith().
3. Initialize bonus = 0 for every employee.
4. Use .loc[condition, 'bonus'] to assign eligible salaries.
5. Sort by employee_id and return employee_id, bonus.

Key Learning:
- ~ negates a Boolean mask.
- .str.startswith() checks string prefixes.
- .loc[mask, column] updates selected rows without
  overwriting the entire column.

Time: O(n log n) including sorting
Space: O(n) for masking and sorting

---

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
| [2192758658](https://leetcode.com/problems/calculate-special-bonus/submissions/2192758658/) | 2026-11-09 20:48:58 | pythondata | [Source](submissions/2192758658.py) |
| [2192136239](https://leetcode.com/problems/calculate-special-bonus/submissions/2192136239/) | 2026-11-08 21:17:11 | mysql | [Source](submissions/2192136239.sql) |
<!-- leetcode-notes-sync:end -->
