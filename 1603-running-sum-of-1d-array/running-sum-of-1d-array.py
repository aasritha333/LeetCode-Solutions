class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum=0;result=[]
            
        for i in range(len(nums)):
            sum+=nums[i]
            result.append(sum)
        return result
        