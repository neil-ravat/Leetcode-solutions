<!-- leetcode-notes-sync:start -->
# 26. Remove Duplicates from Sorted Array

[Open on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191588476](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2191588476/).

# LeetCode 26 — Remove Duplicates from Sorted Array (Python)

**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers

### Intuition
Since the array is sorted, duplicates are adjacent. Use two pointers to keep unique elements at the beginning.

### Approach
1. Initialize `j = 0` for the last unique index.
2. Traverse from `i = 1`.
3. If `nums[i] != nums[j]`, increment `j`.
4. Assign `nums[j] = nums[i]`.
5. Return `j + 1`.

### Example
**Input:** `[1,1,2,2,3]`  
**Output:** `3`, first 3 elements `[1,2,3]`

### Complexity
- **Time:** O(n) — Single traversal.
- **Space:** O(1) — In-place modification.

### Key Learning
The slow pointer tracks the last unique index, while the fast pointer searches for new values.

**Pattern:** Two Pointers + In-Place Modification

---

### Submission notes

From accepted submission [#2191588161](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2191588161/).

# LeetCode 26 — Remove Duplicates from Sorted Array (C++)

**Difficulty:** Easy  
**Topics:** Arrays, Two Pointers

### Intuition
Since the array is sorted, duplicates are adjacent. Use two pointers to keep unique elements at the beginning.

### Approach
1. Initialize `j = 0` for the last unique element.
2. Traverse from `i = 1`.
3. If `nums[i] != nums[j]`, increment `j`.
4. Copy `nums[i]` to `nums[j]`.
5. Return `j + 1`.

### Example
**Input:** `[1,1,2,2,3]`  
**Output:** `3`, first 3 elements `[1,2,3]`

### Complexity
- **Time:** O(n) — Single traversal.
- **Space:** O(1) — In-place modification.

### Key Learning
`j` tracks the last unique index. Use assignment rather than swapping with `j` to preserve the unique prefix.

**Pattern:** Two Pointers + In-Place Array Modification

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191588476](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2191588476/) | 2026-11-07 21:46:59 | python3 | [Source](submissions/2191588476.py) |
| [2191588161](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2191588161/) | 2026-11-07 21:45:46 | cpp | [Source](submissions/2191588161.cpp) |
<!-- leetcode-notes-sync:end -->
