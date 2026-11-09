<!-- leetcode-notes-sync:start -->
# 1148. Article Views I

[Open on LeetCode](https://leetcode.com/problems/article-views-i/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191325489](https://leetcode.com/problems/article-views-i/submissions/2191325489/).

LeetCode 1148 — Article Views I
Difficulty: Easy
Topic: DISTINCT, WHERE, ORDER BY, AS

Intuition:
Find authors who viewed their own articles
and return their unique IDs in sorted order.

Approach:
1. SELECT retrieves the author IDs.
2. DISTINCT removes duplicate IDs.
3. AS renames author_id to id.
4. WHERE checks author_id = viewer_id.
5. ORDER BY sorts IDs in ascending order.

Example:
Output: 4, 7

Complexity:
Time: O(n log n) — Typical sorting approach.
Space: O(n) — Worst-case intermediate storage.
Actual performance depends on the database engine.

Key Learnings:
- DISTINCT removes duplicate results.
- AS creates a column alias.
- ORDER BY sorts the output.
- ASC is the default sorting order.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192745096](https://leetcode.com/problems/article-views-i/submissions/2192745096/) | 2026-11-09 20:10:32 | pythondata | [Source](submissions/2192745096.py) |
| [2191325489](https://leetcode.com/problems/article-views-i/submissions/2191325489/) | 2026-11-07 14:38:55 | mysql | [Source](submissions/2191325489.sql) |
| [2046049269](https://leetcode.com/problems/article-views-i/submissions/2046049269/) | 2026-06-25 17:22:52 | mysql | [Source](submissions/2046049269.sql) |
<!-- leetcode-notes-sync:end -->
