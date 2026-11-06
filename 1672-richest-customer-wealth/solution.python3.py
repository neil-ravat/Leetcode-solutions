class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        largest = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum = sum + accounts[i][j]
                if(sum >= largest):
                    largest = sum

        return largest