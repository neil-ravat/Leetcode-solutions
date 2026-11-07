<!-- leetcode-notes-sync:start -->
# 2880. Select Data

[Open on LeetCode](https://leetcode.com/problems/select-data/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191172148](https://leetcode.com/problems/select-data/submissions/2191172148/).

LeetCode 2880 — Select Data
Difficulty: Easy
Topic: Pandas, Filtering, loc[]

Intuition:
Find a specific student and retrieve selected columns.

Approach:
1. Filter rows where student_id == 101.
2. Use .loc[] to select matching rows.
3. Return only the name and age columns.

Example:
Input: student_id = [101, 102]
Output: Name and age of student 101.

Complexity:
Time: O(n) — checks each row.
Space: O(n) — temporary Boolean mask.

Key Learnings:
- .loc[rows, columns] selects data.
- == checks equality.
- Conditions filter matching rows.
- A list selects multiple columns.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191172148](https://leetcode.com/problems/select-data/submissions/2191172148/) | 2026-11-07 08:51:29 | pythondata | [Source](submissions/2191172148.py) |
<!-- leetcode-notes-sync:end -->
