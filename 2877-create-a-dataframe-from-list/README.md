<!-- leetcode-notes-sync:start -->
# 2877. Create a DataFrame from List

[Open on LeetCode](https://leetcode.com/problems/create-a-dataframe-from-list/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191166497](https://leetcode.com/problems/create-a-dataframe-from-list/submissions/2191166497/).

LeetCode 2877 — Create a DataFrame from List
Difficulty: Easy
Topic: Pandas, DataFrame Creation

Intuition:
Convert a 2D list into a DataFrame with specified column names.

Approach:
1. Use pd.DataFrame() to convert the input list.
2. Use columns=[] to assign column names.
3. Return the DataFrame.

Example:
Input: [[1, 15], [2, 11]]
Columns: ["student_id", "age"]

Output:
   student_id  age
0           1   15
1           2   11

Complexity:
Time: O(n)
Space: O(n)

Key Learnings:
- Each inner list represents one row.
- columns=[] assigns column names.
- Return the DataFrame instead of printing it.
- No loops are required.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191166497](https://leetcode.com/problems/create-a-dataframe-from-list/submissions/2191166497/) | 2026-11-07 08:36:30 | pythondata | [Source](submissions/2191166497.py) |
<!-- leetcode-notes-sync:end -->
