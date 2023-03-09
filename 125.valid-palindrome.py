#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        convertedString = ''.join(filter(str.isalnum, s))
        convertedString = convertedString.lower()
        reversedString = convertedString[::-1]
        return convertedString == reversedString

        
# @lc code=end

