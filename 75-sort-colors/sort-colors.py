class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l=0;m=0;h=len(nums)-1
        while l<h and m<=h:
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                m+=1;l+=1
            elif nums[m]==2:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
            else:
                m+=1
