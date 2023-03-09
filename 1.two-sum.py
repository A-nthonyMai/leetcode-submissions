#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums[index+1:], index+1):
                if num + num2 == target:
                    return [index, index2]
# @lc code=end

