#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List

# Given an array of numbers (ex. [1,2,3,1]), we need this function to
# return true if an number exists at least twice
#
# This solution uses a set to store unique numbers from the input array
#
# We loop through each element in the list, if it's already there 
# in the set then we return early otherwise we add it to the set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existingNums = set()

        for num in nums:
            if num in existingNums:
                return True
            existingNums.add(num)
        
        return False
        
# @lc code=end
