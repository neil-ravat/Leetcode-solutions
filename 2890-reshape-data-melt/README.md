<!-- leetcode-notes-sync:start -->
# 2890. Reshape Data: Melt

[Open on LeetCode](https://leetcode.com/problems/reshape-data-melt/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191232271](https://leetcode.com/problems/reshape-data-melt/submissions/2191232271/).

LeetCode 2890 — Reshape Data: Melt
Difficulty: Easy
Topic: Pandas, Data Reshaping

Intuition:
Convert quarterly sales data from wide to long format.

Approach:
1. Use pd.melt() to reshape the DataFrame.
2. id_vars="product" preserves product names.
3. var_name="quarter" stores original column names.
4. value_name="sales" stores sales values.
5. Return the reshaped DataFrame.

Example:
Input: Product, Q1, Q2
Output: Product, Quarter, Sales

Complexity:
Time: O(n × q)
Space: O(n × q)
(n = input rows, q = melted columns)

Key Learnings:
- melt() converts wide data into long format.
- id_vars identifies columns to preserve.
- var_name names the variable column.
- value_name names the values column.
- melt() is conceptually the opposite of pivot().

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191232271](https://leetcode.com/problems/reshape-data-melt/submissions/2191232271/) | 2026-11-07 11:23:48 | pythondata | [Source](submissions/2191232271.py) |
<!-- leetcode-notes-sync:end -->
