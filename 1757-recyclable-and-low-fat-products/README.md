<!-- leetcode-notes-sync:start -->
# 1757. Recyclable and Low Fat Products

[Open on LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191313360](https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/2191313360/).

LeetCode 1757 — Recyclable and Low Fat Products
Difficulty: Easy
Topic: SELECT, WHERE, AND

Intuition:
Find products that are both low-fat and recyclable.

Approach:
1. SELECT retrieves the product_id.
2. FROM specifies the Products table.
3. WHERE filters records.
4. AND ensures both conditions are true.

Example:
Output: product_id = 1, 3

Complexity:
Time: O(n) — Full table scan.
Space: O(1) — Excluding output.

Key Learnings:
- SELECT chooses columns.
- WHERE filters rows.
- AND requires both conditions to be true.
- Use single quotes for string values.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191313360](https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/2191313360/) | 2026-11-07 14:22:52 | mysql | [Source](submissions/2191313360.sql) |
| [2045924356](https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/2045924356/) | 2026-06-25 15:19:49 | mysql | [Source](submissions/2045924356.sql) |
<!-- leetcode-notes-sync:end -->
