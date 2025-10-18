#https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}

        for sc, tc in zip(s,t):
            if sc in map:
                if map[sc] != tc:
                    return False
            elif tc in map.values():
                    return False
            map[sc] = tc
        return True
