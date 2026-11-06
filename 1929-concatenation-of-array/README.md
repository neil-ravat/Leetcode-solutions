<!-- leetcode-notes-sync:start -->
# 1929. Concatenation of Array

[Open on LeetCode](https://leetcode.com/problems/concatenation-of-array/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2190961305](https://leetcode.com/problems/concatenation-of-array/submissions/2190961305/).

# LeetCode 1929 — Concatenation of Array (C++)

**Difficulty:** Easy  
**Topics:** Arrays, Vectors, Indexing

### 1. Intuition
We are given an array `nums` of size `n`. We need to create a new array containing two copies of `nums`, placed one after another.

We can achieve this using a single loop by copying each element into two positions.

### 2. Approach
1. Store the size of the original array in `n`.
2. Create a result vector `ans` of size `2 * n`.
3. Traverse `nums` using a loop.
4. Copy each element to `ans[i]`.
5. Copy the same element to `ans[i + n]`.
6. Return `ans`.

### 3. Example
**Input:** `nums = [1, 2, 3]`

**Output:** `[1, 2, 3, 1, 2, 3]`

Each element is copied twice:
- `nums[0]` → `ans[0]` and `ans[3]`
- `nums[1]` → `ans[1]` and `ans[4]`
- `nums[2]` → `ans[2]` and `ans[5]`

### 4. Complexity Analysis
- **Time Complexity: O(n)** — We traverse the input array once.
- **Space Complexity: O(n)** — We create an output vector containing `2n` elements.

### 5. Key Learnings
- `vector<int> ans(2 * n)` creates a vector containing `2n` integers.
- `ans[i]` stores the first copy of an element.
- `ans[i + n]` stores its second copy.
- Array indexing starts at 0.
- We can fill both halves of an array using a single loop.
- Always ensure indices remain within the vector's boundaries.

**Pattern to Remember:** Array Construction + Index Offset (`i + n`)

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2190961305](https://leetcode.com/problems/concatenation-of-array/submissions/2190961305/) | 2026-11-06 21:06:52 | cpp | [Source](submissions/2190961305.cpp) |
| [2044588613](https://leetcode.com/problems/concatenation-of-array/submissions/2044588613/) | 2026-06-24 12:21:05 | python3 | [Source](submissions/2044588613.py) |
<!-- leetcode-notes-sync:end -->
