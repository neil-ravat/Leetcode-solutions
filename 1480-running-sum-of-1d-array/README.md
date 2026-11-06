<!-- leetcode-notes-sync:start -->
# 1480. Running Sum of 1d Array

[Open on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2190662308](https://leetcode.com/problems/running-sum-of-1d-array/submissions/2190662308/).

# LeetCode 1480 — Running Sum of 1D Array (Python)

**Difficulty:** Easy  
**Topic:** Arrays, Running Sum, Prefix Sum

### 1. Intuition
We need to calculate the cumulative sum of an array. Each position in the result stores the sum of all elements from the beginning up to that position.

### 2. Approach
1. Create an empty list `rs = []`.
2. Initialize `total = 0`.
3. Traverse each number in `nums`.
4. Add the current number to `total`.
5. Append the updated total to `rs`.
6. Return `rs

---

### Submission notes

From accepted submission [#2190660307](https://leetcode.com/problems/running-sum-of-1d-array/submissions/2190660307/).

# LeetCode 1480 — Running Sum of 1D Array

**Difficulty:** Easy  
**Topic:** Arrays, Running Sum / Prefix Sum

### Intuition
We need to calculate the cumulative sum of the array. Each element in the result contains the sum of all elements from index `0` to the current index.

### Approach
1. Create a result vector `rs` of the same size as the input.
2. Initialize `sum = 0`.
3. Traverse the array using a loop.
4. Add the current element to `sum`.
5. Store the updated `sum` in `rs[i]`.
6. Return the result vector.

### Example
Input: `[1, 2, 3, 4]`  
Output: `[1, 3, 6, 10]`

### Complexity
- **Time: O(n)** — We traverse the array once.
- **Space: O(n)** — We create an additional vector of size `n`.

### Key Learning
- `vector<int> rs(n)` creates a vector containing `n` integers.
- Always update the running sum before storing it.
- Running sum is a basic form of the prefix sum technique.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2190662308](https://leetcode.com/problems/running-sum-of-1d-array/submissions/2190662308/) | 2026-11-06 11:32:32 | python3 | [Source](submissions/2190662308.py) |
| [2190660307](https://leetcode.com/problems/running-sum-of-1d-array/submissions/2190660307/) | 2026-11-06 11:27:16 | cpp | [Source](submissions/2190660307.cpp) |
<!-- leetcode-notes-sync:end -->
