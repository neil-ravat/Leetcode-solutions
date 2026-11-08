<!-- leetcode-notes-sync:start -->
# 977. Squares of a Sorted Array

[Open on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192123444](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192123444/).

# LeetCode 977 — Squares of a Sorted Array (C++)

**Difficulty:** Easy  
**Topics:** Arrays, Sorting

### Intuition
Square every element, then sort the squared values in ascending order.

### Approach
1. Traverse `nums` and square every element.
2. Sort the array using `sort(nums.begin(), nums.end())`.
3. Return `nums`.

### Example
**Input:** `[-4,-1,0,3,10]`  
**Output:** `[0,1,9,16,100]`

### Complexity
- **Time:** O(n log n) — Sorting dominates.
- **Space:** O(log n) typical auxiliary stack space for `std::sort`; no separate output vector.

### Key Learning
Squaring negative values can change their ordering. Sorting gives a simple correct solution, but Two Pointers can improve the time to O(n).

**Pattern:** Array Transformation + Sorting

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192123444](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192123444/) | 2026-11-08 20:31:52 | cpp | [Source](submissions/2192123444.cpp) |
<!-- leetcode-notes-sync:end -->
