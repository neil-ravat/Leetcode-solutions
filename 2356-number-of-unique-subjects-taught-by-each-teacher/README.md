<!-- leetcode-notes-sync:start -->
# 2356. Number of Unique Subjects Taught by Each Teacher

[Open on LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191494485](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/submissions/2191494485/).

LeetCode 2356 — Number of Unique Subjects
Taught by Each Teacher

Difficulty: Easy
Topic: COUNT, DISTINCT, GROUP BY

Intuition:
Count the number of different subjects
taught by each teacher.

Approach:
1. SELECT retrieves teacher_id.
2. GROUP BY creates groups for each teacher.
3. COUNT(DISTINCT subject_id) counts unique subjects.
4. AS cnt names the result column.

Example:
Teacher 1: 2, 2, 3 → 2 unique subjects
Teacher 2: 1, 2, 3, 4 → 4 unique subjects

Complexity:
Time: O(n) expected with hash-based aggregation.
Space: O(u) for unique teacher-subject combinations.
Actual performance depends on the database engine.

Key Learnings:
- GROUP BY groups rows by a column.
- COUNT(*) counts all rows.
- COUNT(DISTINCT column) counts unique values.
- Aggregate functions operate on each group.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191494485](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/submissions/2191494485/) | 2026-11-07 17:57:32 | mysql | [Source](submissions/2191494485.sql) |
<!-- leetcode-notes-sync:end -->
