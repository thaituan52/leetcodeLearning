# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        string = ""
        for char in s:
            m = string.find(char)
            if ( m != -1):
                maximum = max(len(string), maximum)
                string = string[m + 1:] + char
            else:
                string += char
        
        return max(len(string), maximum)