class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sums=0;max_sum=0
        for i in range(len(accounts)):
            sums=sum(accounts[i])
            if sums>max_sum:
                max_sum=sums
               
        return max_sum

        