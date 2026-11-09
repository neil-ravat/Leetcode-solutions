<!-- leetcode-notes-sync:start -->
# 584. Find Customer Referee

[Open on LeetCode](https://leetcode.com/problems/find-customer-referee/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192711654](https://leetcode.com/problems/find-customer-referee/submissions/2192711654/).

Pattern: Boolean Filtering + Missing Values

Approach:
1. Check referee_id != 2.
2. Check referee_id.isna() for missing values.
3. Combine both conditions with OR (|).
4. Return only the name column using .loc.

Key Learning:
- .isna() detects missing values.
- .notna() detects non-missing values.
- | combines two Boolean conditions.
- NULL handling in SQL and Pandas differs.

Time Complexity: O(n)
Space Complexity: O(n)

---

### Submission notes

From accepted submission [#2191318087](https://leetcode.com/problems/find-customer-referee/submissions/2191318087/).

LeetCode 584 — Find Customer Referee
Difficulty: Easy
Topic: WHERE, OR, NULL

Intuition:
Find customers who were not referred by
customer 2 or were not referred by anyone.

Approach:
1. SELECT retrieves customer names.
2. WHERE filters the records.
3. != 2 excludes customers referred by ID 2.
4. OR IS NULL includes customers without a referee.

Example:
Output: Will, Jane, Bill, Zack

Complexity:
Time: O(n) — Full table scan.
Space: O(1) — Excluding output.

Key Learnings:
- != and <> mean not equal.
- IS NULL checks missing values.
- OR requires at least one condition to be true.
- Comparing NULL using != does not return TRUE.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192711654](https://leetcode.com/problems/find-customer-referee/submissions/2192711654/) | 2026-11-09 18:53:14 | pythondata | [Source](submissions/2192711654.py) |
| [2191318087](https://leetcode.com/problems/find-customer-referee/submissions/2191318087/) | 2026-11-07 14:32:02 | mysql | [Source](submissions/2191318087.sql) |
| [2045951298](https://leetcode.com/problems/find-customer-referee/submissions/2045951298/) | 2026-06-25 15:48:09 | mysql | [Source](submissions/2045951298.sql) |
<!-- leetcode-notes-sync:end -->
