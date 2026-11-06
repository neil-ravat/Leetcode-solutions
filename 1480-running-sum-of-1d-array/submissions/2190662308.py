class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rs = []
        sum = 0 
        for i in range(len(nums)):
            total = sum + nums[i]
            rs.append(total)
            sum = total


        return rs