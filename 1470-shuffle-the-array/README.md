<!-- leetcode-notes-sync:start -->
# 1470. Shuffle the Array

[Open on LeetCode](https://leetcode.com/problems/shuffle-the-array/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2190972632](https://leetcode.com/problems/shuffle-the-array/submissions/2190972632/).

# LeetCode 1470 — Shuffle the Array (C++)

**Difficulty:** Easy  
**Topic:** Arrays, Indexing

### Intuition
We need to rearrange the array by alternately taking elements from its first and second halves.

### Approach
1. Create an output vector `ans` of size `2*n`.
2. Traverse the first `n` elements.
3. Place `nums[i]` at `ans[2*i]`.
4. Place `nums[i+n]` at `ans[2*i+1]`.
5. Return `ans`.

### Example
**Input:** `[2,5,1,3,4,7]`, `n = 3`  
**Output:** `[2,3,5,4,1,7]`

### Complexity
- **Time:** O(n) — Single loop.
- **Space:** O(n) — Additional output vector.

### Key Learning
Use `2*i` and `2*i+1` to place elements at alternating positions.

**Pattern:**

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2190972632](https://leetcode.com/problems/shuffle-the-array/submissions/2190972632/) | 2026-11-06 21:51:38 | cpp | [Source](submissions/2190972632.cpp) |
<!-- leetcode-notes-sync:end -->
