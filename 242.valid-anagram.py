#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram

# @lc code=start

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsInS = {}

        for char in s:
            if char in charsInS:
                charsInS[char] = charsInS[char] + 1
            else:
                charsInS[char] = 1

        for char in t:
            if not char in charsInS:
                return False
            else:
                if charsInS[char] > 0:
                    charsInS[char] = charsInS[char] - 1
                else:
                    return False
        
        for key, value in charsInS.items():
            if value > 0:
                return False

        return True


# @lc code=end

