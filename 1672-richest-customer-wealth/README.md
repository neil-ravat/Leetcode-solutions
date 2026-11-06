<!-- leetcode-notes-sync:start -->
# 1672. Richest Customer Wealth

[Open on LeetCode](https://leetcode.com/problems/richest-customer-wealth/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2190968750](https://leetcode.com/problems/richest-customer-wealth/submissions/2190968750/).

# LeetCode 1672 — Richest Customer Wealth (C++)

**Difficulty:** Easy  
**Topics:** 2D Arrays, Nested Loops, Running Sum, Maximum

### 1. Intuition
Each row in the 2D array represents a customer, and each element represents their bank balance.

We need to calculate the total wealth of each customer and return the highest wealth among all customers.

### 2. Approach
1. Initialize `largest = 0` to track the maximum wealth.
2. Use an outer loop to visit each customer (row).
3. Initialize `sum = 0` inside the outer loop to calculate each customer's wealth separately.
4. Use an inner loop to add all bank balances using `sum += accounts[i][j]`.
5. After the inner loop, compare `sum` with `largest`.
6. Update `largest` if the current customer's wealth is greater.
7. Return `largest`.

### 3. Example
**Input:** `accounts = [[1,5],[7,3],[3,5]]`

**Calculations:**
- Customer 1: 1 + 5 = 6
- Customer 2: 7 + 3 = 10
- Customer 3: 3 + 5 = 8

**Output:** `10`

### 4. Complexity Analysis
- **Time Complexity: O(m × n)** — We visit every bank balance once, where `m` is the number of customers and `n` is the number of banks per customer.
- **Space Complexity: O(1)** — We use only two variables, `sum` and `largest`, regardless of input size.

### 5. Key Learnings
- `vector<vector<int>>` represents a 2D vector.
- `accounts[i][j]` accesses the balance at row `i` and column `j`.
- `accounts.size()` gives the number of customers.
- `accounts[i].size()` gives the number of banks belonging to customer `i`.
- Reset `sum = 0` for every new customer, not every bank.
- Update `largest` only after calculating the complete row sum.
- Never access an element outside the vector's valid indices.

**Pattern to Remember:** Nested Loops + Row Sum + Running Maximum

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2190970408](https://leetcode.com/problems/richest-customer-wealth/submissions/2190970408/) | 2026-11-06 21:42:37 | python3 | [Source](submissions/2190970408.py) |
| [2190968750](https://leetcode.com/problems/richest-customer-wealth/submissions/2190968750/) | 2026-11-06 21:35:52 | cpp | [Source](submissions/2190968750.cpp) |
<!-- leetcode-notes-sync:end -->
