<!-- leetcode-notes-sync:start -->
# 1732. Find the Highest Altitude

[Open on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2190893562](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190893562/).

# LeetCode 1732 — Find the Highest Altitude (Optimized)

**Difficulty:** Easy  
**Topics:** Arrays, Prefix Sum, Running Maximum

### 1. Intuition
The biker starts at altitude 0. Each value in `gain` represents an increase or decrease in altitude.

Instead of storing all altitudes in a separate array, we can calculate the current altitude and track the highest altitude while traversing the input.

### 2. Approach
1. Initialize `altitude = 0` and `highest = 0`.
2. Traverse the `gain` array once.
3. Update the current altitude using `altitude += gain[i]`.
4. If `altitude >= highest`, update `highest = altitude`.
5. Return `highest`.

### 3. Example
**Input:** `gain = [-5, 1, 5, 0, -7]`

**Altitudes:** `0 → -5 → -4 → 1 → 1 → -6`

**Output:** `1`

### 4. Complexity Analysis
- **Time Complexity: O(n)** — We traverse the array only once.
- **Space Complexity: O(1)** — We use only two variables, regardless of input size.

### 5. Key Learnings
- We don't need to store every intermediate result if only the maximum is required.
- Updating the running sum and maximum in the same loop saves memory.
- Initialize `highest = 0` because the starting altitude is included.
- Both `>` and `>=` work when updating the maximum.
- Optimization can reduce space complexity without changing time complexity.

**Pattern to Remember:** Running Sum + Running Maximum + Constant Space

---

### Submission notes

From accepted submissions [#2190737086](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190737086/), [#2190734628](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190734628/).

# LeetCode 1732 — Find the Highest Altitude

**Difficulty:** Easy  
**Topics:** Arrays, Prefix Sum, Maximum Element

### 1. Intuition
The biker starts at altitude 0. Each element in `gain` represents an increase or decrease in altitude.

We calculate the altitude at every point using a running sum and then find the maximum altitude reached.

### 2. Approach
1. Create a vector `g` of size `gain.size() + 1` to store all altitudes.
2. Initialize `g[0] = 0` because the biker starts at altitude 0.
3. Traverse `gain` and calculate each altitude using:
   `g[i] = g[i-1] + gain[i-1]`
4. Initialize `largest = 0`.
5. Traverse the entire altitude vector and update `largest` whenever a higher altitude is found.
6. Return `largest`.

### 3. Example
**Input:** `gain = [-5, 1, 5, 0, -7]`

**Altitudes:** `[0, -5, -4, 1, 1, -6]`

**Output:** `1`

### 4. Complexity Analysis
- **Time Complexity: O(n)** — Two separate loops traverse the altitude values.
- **Space Complexity: O(n)** — An additional vector stores all `n + 1` altitudes.

### 5. Key Learnings
- Running sum helps calculate cumulative values.
- We must compare each altitude with the maximum found so far, not just the previous altitude.
- Always include the starting altitude of 0.
- Check every element when finding the maximum.
- An additional vector uses O(n) memory.

**Pattern:** Prefix Sum + Running Maximum

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2190924351](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190924351/) | 2026-11-06 19:17:59 | python3 | [Source](submissions/2190924351.py) |
| [2190893562](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190893562/) | 2026-11-06 18:19:52 | cpp | [Source](submissions/2190893562.cpp) |
| [2190737086](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190737086/) | 2026-11-06 14:13:13 | cpp | [Source](submissions/2190737086.cpp) |
| [2190734628](https://leetcode.com/problems/find-the-highest-altitude/submissions/2190734628/) | 2026-11-06 14:08:55 | cpp | [Source](submissions/2190734628.cpp) |
<!-- leetcode-notes-sync:end -->
