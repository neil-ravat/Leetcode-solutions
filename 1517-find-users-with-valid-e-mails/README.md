<!-- leetcode-notes-sync:start -->
# 1517. Find Users With Valid E-Mails

[Open on LeetCode](https://leetcode.com/problems/find-users-with-valid-e-mails/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2193000159](https://leetcode.com/problems/find-users-with-valid-e-mails/submissions/2193000159/).

LeetCode #1517 — Find Users With Valid E-Mails

Pattern: Regex + String Filtering

Approach:
1. Build a regex for a permitted email prefix.
2. Require the exact @leetcode.com domain.
3. Use .str.match(pattern) to create a Boolean mask.
4. Return matching rows using .loc.

Key Learning:
- ^ checks the start; $ checks the end.
- [...] defines allowed characters.
- * means zero or more repetitions.
- \. matches a literal period.
- .str.match() applies regex matching to a Pandas column.

Time: O(total email characters) for matching
Space: O(n) for the Boolean mask, excluding output

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2193000159](https://leetcode.com/problems/find-users-with-valid-e-mails/submissions/2193000159/) | 2026-11-10 07:29:40 | pythondata | [Source](submissions/2193000159.py) |
<!-- leetcode-notes-sync:end -->
