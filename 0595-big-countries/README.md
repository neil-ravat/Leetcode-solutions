<!-- leetcode-notes-sync:start -->
# 595. Big Countries

[Open on LeetCode](https://leetcode.com/problems/big-countries/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191332362](https://leetcode.com/problems/big-countries/submissions/2191332362/).

LeetCode 595 — Big Countries
Difficulty: Easy
Topic: SELECT, WHERE, OR, Comparison Operators

Intuition:
Find countries with a large area or population.

Approach:
1. SELECT retrieves name, population, and area.
2. FROM specifies the World table.
3. WHERE filters countries.
4. >= checks the minimum required values.
5. OR includes countries meeting either condition.

Example:
Output: Afghanistan, Algeria

Complexity:
Time: O(n) — Full table scan.
Space: O(1) — Excluding output.

Key Learnings:
- >= means greater than or equal to.
- OR requires at least one true condition.
- AND requires both conditions to be true.
- SELECT column order determines output order.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191332362](https://leetcode.com/problems/big-countries/submissions/2191332362/) | 2026-11-07 14:44:02 | mysql | [Source](submissions/2191332362.sql) |
| [2045966016](https://leetcode.com/problems/big-countries/submissions/2045966016/) | 2026-06-25 16:03:13 | mysql | [Source](submissions/2045966016.sql) |
<!-- leetcode-notes-sync:end -->
