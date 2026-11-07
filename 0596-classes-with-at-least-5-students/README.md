<!-- leetcode-notes-sync:start -->
# 596. Classes With at Least 5 Students

[Open on LeetCode](https://leetcode.com/problems/classes-with-at-least-5-students/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191497571](https://leetcode.com/problems/classes-with-at-least-5-students/submissions/2191497571/).

LeetCode 596 — Classes With at Least 5 Students
Difficulty: Easy
Topic: GROUP BY, HAVING, COUNT

Intuition:
Find classes containing at least 5 students.

Approach:
1. SELECT retrieves class names.
2. GROUP BY groups students by class.
3. COUNT() counts students in each group.
4. HAVING filters groups with count >= 5.

Example:
Math: 6 students → Included
English: 1 student → Excluded
Output: Math

Complexity:
Time: O(n) expected with hash-based grouping.
Space: O(k) for k distinct classes.
Actual performance depends on the database engine.

Key Learnings:
- GROUP BY creates groups.
- COUNT(*) counts all rows.
- HAVING filters aggregated groups.
- WHERE filters rows before grouping.
- >= includes the boundary value.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191497571](https://leetcode.com/problems/classes-with-at-least-5-students/submissions/2191497571/) | 2026-11-07 18:02:02 | mysql | [Source](submissions/2191497571.sql) |
<!-- leetcode-notes-sync:end -->
