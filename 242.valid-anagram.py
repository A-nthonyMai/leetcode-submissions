#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram

# @lc code=start

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Solution 1 (Hash Map)

        # if len(s) != len(t):
        #     return False

        # charsInS, charsInT = {}, {}

        # # Loop through each char in s
        # # Increment the letter at s[i] by 1 (default to 0+1 if not in map)
        # # Increment the letter at t[i] by 1 (default to 0+1 if not in map)
        # for i in range(len(s)):
        #     charsInS[s[i]] = charsInS.get(s[i], 0) + 1
        #     charsInT[t[i]] = charsInT.get(t[i], 0) + 1

        # # Loop through each char in s map
        # # Check that the value of letter matches the value in t map
        # for c in charsInS:
        #     if charsInS[c] != charsInT.get(c, 0):
        #         return False

        # return True
    
        # Solution 2 (Sort)

        # Sort teach string, if they're an anagram then the
        # each resulting string should be equal
        #
        # Complexity depends on which sorting algorithm is used
        return sorted(s) == sorted(t)


# @lc code=end

