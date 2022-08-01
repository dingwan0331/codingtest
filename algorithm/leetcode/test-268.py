# 268. Missing Number
# problem url = https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        try:
            nums.sort()
            if nums[0] != 0:
                return 0
            for i in range(len(nums)):
                if nums[i]+1 != nums[i+1]:
                    return nums[i]+1
        except:
            return nums[-1]+1