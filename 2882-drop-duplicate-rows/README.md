<!-- leetcode-notes-sync:start -->
# 2882. Drop Duplicate Rows

[Open on LeetCode](https://leetcode.com/problems/drop-duplicate-rows/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191218308](https://leetcode.com/problems/drop-duplicate-rows/submissions/2191218308/).

LeetCode 2882 — Drop Duplicate Rows
Difficulty: Easy
Topic: Pandas, Data Cleaning

Intuition:
Remove duplicate emails while keeping the first entry.

Approach:
1. Use drop_duplicates() to remove duplicates.
2. Set subset="email" to check only emails.
3. Use keep="first" to retain the first entry.
4. Return the cleaned DataFrame.

Example:
Emails: [a@gmail.com, b@gmail.com, a@gmail.com]
Output: [a@gmail.com, b@gmail.com]

Complexity:
Time: O(n) average
Space: O(n)

Key Learnings:
- drop_duplicates() removes duplicate rows.
- subset specifies which columns to check.
- keep="first" retains the first occurrence.
- By default, the original DataFrame is unchanged.
- Store or return the resulting DataFrame.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191218308](https://leetcode.com/problems/drop-duplicate-rows/submissions/2191218308/) | 2026-11-07 10:48:42 | pythondata | [Source](submissions/2191218308.py) |
<!-- leetcode-notes-sync:end -->
