<!-- leetcode-notes-sync:start -->
# 2878. Get the Size of a DataFrame

[Open on LeetCode](https://leetcode.com/problems/get-the-size-of-a-dataframe/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191169246](https://leetcode.com/problems/get-the-size-of-a-dataframe/submissions/2191169246/).

LeetCode 2878 — Get the Size of a DataFrame
Difficulty: Easy
Topic: Pandas, DataFrame Attributes

Intuition:
Find the number of rows and columns in a DataFrame.

Approach:
1. Use .shape to get (rows, columns).
2. Convert the tuple into a list.
3. Return the list.

Example:
DataFrame with 4 rows and 3 columns
Output: [4, 3]

Complexity (Optimized):
Time: O(1)
Space: O(1)

Key Learnings:
- .shape returns (rows, columns).
- .shape is an attribute, not a method.
- list() converts a tuple into a list.
- Avoid unnecessary DataFrame creation.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191169246](https://leetcode.com/problems/get-the-size-of-a-dataframe/submissions/2191169246/) | 2026-11-07 08:43:54 | pythondata | [Source](submissions/2191169246.py) |
<!-- leetcode-notes-sync:end -->
