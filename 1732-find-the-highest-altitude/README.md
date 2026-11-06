<!-- leetcode-notes-sync:start -->
# 1732. Find the Highest Altitude

[Open on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)

**Difficulty:** Easy

## My notes

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
<!-- leetcode-notes-sync:end -->
