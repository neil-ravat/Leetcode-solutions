class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        count = 0
        for x in nums:
            count = count + freq.get(x,0)
            freq[x]=freq.get(x,0)+1

        return count

        