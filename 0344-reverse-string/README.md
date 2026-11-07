<!-- leetcode-notes-sync:start -->
# 344. Reverse String

[Open on LeetCode](https://leetcode.com/problems/reverse-string/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191577495](https://leetcode.com/problems/reverse-string/submissions/2191577495/).

# LeetCode 344 — Reverse String (C++)

**Difficulty:** Easy  
**Topics:** Two Pointers, Strings

### Intuition
Use two pointers from opposite ends of the array and swap characters until they meet.

### Approach
1. Initialize `left = 0` and `right = n - 1`.
2. While `left < right`, swap `s[left]` and `s[right]`.
3. Increment `left` and decrement `right`.
4. Modify the original array directly without returning anything.

### Example
**Input:** `['h','e','l','l','o']`  
**Output:** `['o','l','l','e','h']`

### Complexity
- **Time:** O(n) — At most n/2 swaps.
- **Space:** O(1) — No extra array.

### Key Learning
Two pointers can reverse an array in place. Use indices, not element values, and remember that `void` functions don't return a result.

**Pattern:** Two Pointers + In-Place Swapping

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191578213](https://leetcode.com/problems/reverse-string/submissions/2191578213/) | 2026-11-07 21:07:55 | python3 | [Source](submissions/2191578213.py) |
| [2191577495](https://leetcode.com/problems/reverse-string/submissions/2191577495/) | 2026-11-07 21:05:17 | cpp | [Source](submissions/2191577495.cpp) |
<!-- leetcode-notes-sync:end -->
