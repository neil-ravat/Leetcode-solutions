<!-- leetcode-notes-sync:start -->
# 2889. Reshape Data: Pivot

[Open on LeetCode](https://leetcode.com/problems/reshape-data-pivot/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191230818](https://leetcode.com/problems/reshape-data-pivot/submissions/2191230818/).

LeetCode 2889 — Reshape Data: Pivot
Difficulty: Easy
Topic: Pandas, Data Reshaping

Intuition:
Convert weather data from long to wide format.

Approach:
1. Use pivot() to reshape the DataFrame.
2. index="month" creates one row per month.
3. columns="city" creates columns for cities.
4. values="temperature" fills the cells.
5. Return the pivoted DataFrame.

Example:
Input: City, Month, Temperature
Output: Month as rows, cities as columns.

Performance:
Output size depends on the number of unique
months and cities.

Key Learnings:
- pivot() converts long data to wide format.
- index determines the row labels.
- columns determines the column headings.
- values determines the cell values.
- pivot() requires unique index-column pairs.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191230818](https://leetcode.com/problems/reshape-data-pivot/submissions/2191230818/) | 2026-11-07 11:20:13 | pythondata | [Source](submissions/2191230818.py) |
<!-- leetcode-notes-sync:end -->
