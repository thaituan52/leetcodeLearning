# https://leetcode.com/problems/ransom-note

#Time: O(n^2) since using count method inside a loop
#Using set to check each unique letter only once make it faster but still not optimal
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for ch in set(ransomNote):  # check each unique letter
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True
    
#fastest solution Time: O(n+m) since using a single loop
class Solution:
    def canConstruct(self, ransomNote, magazine):
        alphabet = [0] * 26
        for c in ransomNote:
            idx = ord(c) - ord('a')
            i = magazine.find(c, alphabet[idx])
            if i == -1:
                return False
            alphabet[idx] = i + 1
        return True