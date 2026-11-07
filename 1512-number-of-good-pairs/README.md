<!-- leetcode-notes-sync:start -->
# 1512. Number of Good Pairs

[Open on LeetCode](https://leetcode.com/problems/number-of-good-pairs/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191153119](https://leetcode.com/problems/number-of-good-pairs/submissions/2191153119/).

# LeetCode 1512 — Number of Good Pairs (Optimized C++)

**Difficulty:** Easy  
**Topics:** Arrays, Hashing, Frequency Map

### Intuition
A good pair has equal values and indices `i < j`. Instead of comparing every pair, we count how many times each number has appeared previously.

### Approach
1. Create an `unordered_map<int, int>` to store frequencies.
2. Initialize `count = 0`.
3. Traverse the array.
4. Add `freq[nums[i]]` to `count`.
5. Increase `freq[nums[i]]` by 1.
6. Return `count`.

### Example
**Input:** `[1,2,1,1]`  
**Output:** `3`

### Complexity
- **Time:** O(n) expected — Hash-map operations are expected O(1).
- **Space:** O(k) — Stores frequencies of k distinct numbers.

### Key Learning
Count previous occurrences before increasing the frequency to avoid counting an element with itself.

**Pattern:** Hashing + Frequency Counting

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191153119](https://leetcode.com/problems/number-of-good-pairs/submissions/2191153119/) | 2026-11-07 08:02:44 | cpp | [Source](submissions/2191153119.cpp) |
| [2190977109](https://leetcode.com/problems/number-of-good-pairs/submissions/2190977109/) | 2026-11-06 22:10:28 | cpp | [Source](submissions/2190977109.cpp) |
<!-- leetcode-notes-sync:end -->
