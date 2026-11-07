<!-- leetcode-notes-sync:start -->
# 1068. Product Sales Analysis I

[Open on LeetCode](https://leetcode.com/problems/product-sales-analysis-i/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191573384](https://leetcode.com/problems/product-sales-analysis-i/submissions/2191573384/).

LeetCode 1068 — Product Sales Analysis I
Difficulty: Easy
Topic: INNER JOIN, Table Aliases

Intuition:
Combine sales records with product details
to retrieve product names for each sale.

Approach:
1. FROM selects the Sales table.
2. JOIN connects the Product table.
3. ON matches records using product_id.
4. SELECT returns product_name, year, and price.

Example:
Nokia → 2008, 5000
Nokia → 2009, 5000
Apple → 2011, 9000

Complexity:
Time: O(n + m) expected with a hash join.
Space: O(m) for the hash table.
Actual cost depends on the database engine.

Key Learnings:
- JOIN is equivalent to INNER JOIN.
- ON specifies the matching condition.
- Table aliases make queries easier to read.
- INNER JOIN returns matching records only.
- Multiple sales of one product remain separate.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191573384](https://leetcode.com/problems/product-sales-analysis-i/submissions/2191573384/) | 2026-11-07 20:51:12 | mysql | [Source](submissions/2191573384.sql) |
| [2046073471](https://leetcode.com/problems/product-sales-analysis-i/submissions/2046073471/) | 2026-06-25 17:43:42 | mysql | [Source](submissions/2046073471.sql) |
<!-- leetcode-notes-sync:end -->
