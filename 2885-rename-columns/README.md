<!-- leetcode-notes-sync:start -->
# 2885. Rename Columns

[Open on LeetCode](https://leetcode.com/problems/rename-columns/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191224603](https://leetcode.com/problems/rename-columns/submissions/2191224603/).

LeetCode 2885 — Rename Columns
Difficulty: Easy
Topic: Pandas, Column Renaming

Intuition:
Rename existing DataFrame columns without
changing their values.

Approach:
1. Use rename(columns={}).
2. Map old column names to new names.
3. Return the renamed DataFrame.

Example:
Old: id, first
New: student_id, first_name

Complexity:
Time: O(c) for column labels
Space: O(c) for labels, excluding data copies
(c = number of columns)

Key Learnings:
- rename() changes column names.
- Dictionary keys represent old names.
- Dictionary values represent new names.
- rename() returns a new DataFrame by default.
- Original data values remain unchanged.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191224603](https://leetcode.com/problems/rename-columns/submissions/2191224603/) | 2026-11-07 11:04:35 | pythondata | [Source](submissions/2191224603.py) |
<!-- leetcode-notes-sync:end -->
