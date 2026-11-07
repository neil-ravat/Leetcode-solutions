<!-- leetcode-notes-sync:start -->
# 1378. Replace Employee ID With The Unique Identifier

[Open on LeetCode](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191501326](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/2191501326/).

LeetCode 1378 — Replace Employee ID
With the Unique Identifier

Difficulty: Easy
Topic: LEFT JOIN, Table Aliases, NULL

Intuition:
Display every employee with their unique ID.
If no unique ID exists, display NULL.

Approach:
1. Use Employees as the left table.
2. LEFT JOIN EmployeeUNI to retain all employees.
3. Match both tables using their id columns.
4. SELECT unique_id and name.
5. Unmatched employees automatically receive NULL.

Example:
Alice → NULL
Bob → NULL
Meir → 2
Winston → 3
Jonathan → 1

Complexity:
Time: O(n + m) with a hash join.
Space: O(m) for the hash table.
Actual cost depends on the database engine.

Key Learnings:
- INNER JOIN returns only matching records.
- LEFT JOIN keeps all rows from the left table.
- Unmatched right-side values become NULL.
- ON defines the matching condition.
- Table aliases improve readability.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191501326](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/2191501326/) | 2026-11-07 18:07:32 | mysql | [Source](submissions/2191501326.sql) |
| [2046057327](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/2046057327/) | 2026-06-25 17:29:50 | mysql | [Source](submissions/2046057327.sql) |
<!-- leetcode-notes-sync:end -->
