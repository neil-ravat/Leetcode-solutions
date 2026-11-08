<!-- leetcode-notes-sync:start -->
# 977. Squares of a Sorted Array

[Open on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192129427](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192129427/).

Problems needing attention
classes-more-than-5-students: LeetCode submissions query failed. Its API may have changed; no files were changed for this request.

---

### Submission notes

From accepted submission [#2192127741](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192127741/).

# LeetCode 977 — Squares of a Sorted Array (Optimized C++)

**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers

### Intuition
Since the array is sorted, the largest square must come from either end. Compare both ends and fill the result from right to left.

### Approach
1. Create `ans` of size `n`.
2. Initialize `left = 0`, `right = n-1`, `pos = n-1`.
3. Compare the squares at `left` and `right`.
4. Store the larger square at `ans[pos]`.
5. Move only the selected pointer and decrement `pos`.
6. Repeat until `left > right`.

### Example
**Input:** `[-4,-1,0,3,10]`  
**Output:** `[0,1,9,16,100]`

### Complexity
- **Time:** O(n) — Each element is processed once.
- **Space:** O(n) — Additional output vector.

### Key Learning
Move only the pointer whose value was used. Filling the output from the end maintains sorted order.

**Pattern:** Two Pointers + Reverse Filling

---

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
| [2192129427](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192129427/) | 2026-11-08 20:51:47 | python3 | [Source](submissions/2192129427.py) |
| [2192127741](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192127741/) | 2026-11-08 20:46:02 | cpp | [Source](submissions/2192127741.cpp) |
| [2192123444](https://leetcode.com/problems/squares-of-a-sorted-array/submissions/2192123444/) | 2026-11-08 20:31:52 | cpp | [Source](submissions/2192123444.cpp) |
<!-- leetcode-notes-sync:end -->
