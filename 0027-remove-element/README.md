<!-- leetcode-notes-sync:start -->
# 27. Remove Element

[Open on LeetCode](https://leetcode.com/problems/remove-element/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191592815](https://leetcode.com/problems/remove-element/submissions/2191592815/).

# LeetCode 27 — Remove Element (C++)

**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers

### Intuition
Use two pointers to remove all occurrences of `val` in place while keeping the remaining elements.

### Approach
1. Initialize `j = 0` as the next available position.
2. Traverse the array using `i`.
3. If `nums[i] != val`, copy it to `nums[j]`.
4. Increment `j` after copying.
5. Return `j`.

### Example
**Input:** `[3,2,2,3]`, `val = 3`  
**Output:** `2`, first 2 elements `[2,2]`

### Complexity
- **Time:** O(n) — One traversal.
- **Space:** O(1) — In-place modification.

### Key Learning
`j` represents the number of elements retained, so return `j`, not `j + 1`.

**Pattern:** Two Pointers + In-Place Filtering

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191592815](https://leetcode.com/problems/remove-element/submissions/2191592815/) | 2026-11-07 22:04:40 | cpp | [Source](submissions/2191592815.cpp) |
<!-- leetcode-notes-sync:end -->
