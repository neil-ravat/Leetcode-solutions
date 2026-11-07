<!-- leetcode-notes-sync:start -->
# 283. Move Zeroes

[Open on LeetCode](https://leetcode.com/problems/move-zeroes/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191581008](https://leetcode.com/problems/move-zeroes/submissions/2191581008/).

# LeetCode 283 — Move Zeroes (Python)

**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers

### Intuition
Use a fast pointer to find non-zero elements and a slow pointer to move them to the beginning while maintaining their order.

### Approach
1. Initialize `j = 0` as the slow pointer.
2. Traverse the array using `i`.
3. If `nums[i] != 0`, swap `nums[i]` and `nums[j]`.
4. Increment `j` after each swap.
5. Modify the original array in place.

### Example
**Input:** `[0,1,0,3,12]`  
**Output:** `[1,3,12,0,0]`

### Complexity
- **Time:** O(n) — Single traversal.
- **Space:** O(1) — No additional array.

### Key Learning
The fast pointer visits every element, while the slow pointer advances only when a non-zero element is found.

**Pattern:** Two Pointers (Slow & Fast)

---

### Submission notes

From accepted submission [#2191580266](https://leetcode.com/problems/move-zeroes/submissions/2191580266/).

# LeetCode 283 — Move Zeroes (C++)

**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers

### Intuition
Use a fast pointer to find non-zero elements and a slow pointer to position them at the beginning while preserving their order.

### Approach
1. Initialize slow pointer `j = 0`.
2. Traverse the array using fast pointer `i`.
3. If `nums[i] != 0`, swap `nums[i]` with `nums[j]`.
4. Increment `j` after each swap.
5. Modify the original array directly.

### Example
**Input:** `[0,1,0,3,12]`  
**Output:** `[1,3,12,0,0]`

### Complexity
- **Time:** O(n) — Single traversal.
- **Space:** O(1) — In-place modification.

### Key Learning
The fast pointer scans every element, while the slow pointer advances only for non-zero values.

**Pattern:** Two Pointers (Slow & Fast)

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191581008](https://leetcode.com/problems/move-zeroes/submissions/2191581008/) | 2026-11-07 21:18:08 | python3 | [Source](submissions/2191581008.py) |
| [2191580266](https://leetcode.com/problems/move-zeroes/submissions/2191580266/) | 2026-11-07 21:15:31 | cpp | [Source](submissions/2191580266.cpp) |
<!-- leetcode-notes-sync:end -->
