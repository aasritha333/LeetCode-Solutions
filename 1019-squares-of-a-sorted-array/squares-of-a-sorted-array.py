class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        f = 0
        l = len(nums) - 1
        result = []

        while f <= l:
            if abs(nums[f]) > abs(nums[l]):
                result.append(nums[f] ** 2)
                f += 1
            else:
                result.append(nums[l] ** 2)
                l -= 1

        return result[::-1]