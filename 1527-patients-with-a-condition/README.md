<!-- leetcode-notes-sync:start -->
# 1527. Patients With a Condition

[Open on LeetCode](https://leetcode.com/problems/patients-with-a-condition/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2193069587](https://leetcode.com/problems/patients-with-a-condition/submissions/2193069587/).

LeetCode #1527 — Patients With a Condition

Pattern: String Filtering + Regex + Boolean OR

Approach:
1. Check for DIAB1 at the start using ^DIAB1.
2. Check for DIAB1 after a space using " DIAB1".
3. Combine the conditions with | (OR).
4. Filter matching rows using .loc.

Key Learning:
- .str.contains() searches within each string.
- ^ anchors a match to the start.
- A literal space matches a space in the text.
- | combines Boolean conditions in Pandas.

Time: O(L), where L is total text length
Space: O(n) for Boolean masks, excluding output

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2193069587](https://leetcode.com/problems/patients-with-a-condition/submissions/2193069587/) | 2026-11-10 09:41:24 | pythondata | [Source](submissions/2193069587.py) |
<!-- leetcode-notes-sync:end -->
