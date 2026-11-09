<!-- leetcode-notes-sync:start -->
# 1683. Invalid Tweets

[Open on LeetCode](https://leetcode.com/problems/invalid-tweets/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191338256](https://leetcode.com/problems/invalid-tweets/submissions/2191338256/).

LeetCode 1683 — Invalid Tweets
Difficulty: Easy
Topic: SELECT, WHERE, String Functions

Intuition:
Find tweets whose content exceeds 15 characters.

Approach:
1. SELECT retrieves the tweet_id.
2. FROM specifies the Tweets table.
3. LENGTH() measures the content length.
4. WHERE filters tweets with length > 15.

Example:
Tweet 1: 11 characters → Valid
Tweet 2: 33 characters → Invalid
Output: 2

Complexity:
Time: O(n) — Row scan, plus string-length checks.
Space: O(1) — Excluding output.

Key Learnings:
- LENGTH() returns string length in bytes.
- CHAR_LENGTH() counts characters.
- > means strictly greater than.
- Spaces are included when measuring length.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192750063](https://leetcode.com/problems/invalid-tweets/submissions/2192750063/) | 2026-11-09 20:23:57 | pythondata | [Source](submissions/2192750063.py) |
| [2191338256](https://leetcode.com/problems/invalid-tweets/submissions/2191338256/) | 2026-11-07 14:48:19 | mysql | [Source](submissions/2191338256.sql) |
| [2046051614](https://leetcode.com/problems/invalid-tweets/submissions/2046051614/) | 2026-06-25 17:24:53 | mysql | [Source](submissions/2046051614.sql) |
<!-- leetcode-notes-sync:end -->
