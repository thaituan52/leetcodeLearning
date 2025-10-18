#https://leetcode.com/problems/valid-anagram



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return all(c == 0 for c in count)
        
# Sorting (simple, clean):

# class Solution(object):
#     def isAnagram(self, s, t):
#         return sorted(s) == sorted(t)

#Excting solution


# Time: O(n log n) due to sorting

# Space: O(1) or O(n) depending on sorting algorithm implementation

# Hash Map / Counter (most efficient):

# from collections import Counter

# class Solution(object):
#     def isAnagram(self, s, t):
#         return Counter(s) == Counter(t)


# Time: O(n)

# Space: O(1) (since only 26 lowercase letters exist, the hashmap size is bounded)

# Array Count (fastest, since only lowercase letters):

# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#         count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1
#         return all(c == 0 for c in count)


# Time: O(n)

# Space: O(26) → constant