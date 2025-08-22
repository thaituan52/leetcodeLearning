#https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
#Solution:
#   Using Greedy Search to first find all occurrence with higher points
#   The twist here to make it easier is to create a stack - list of char in s, then
#   we gonna go through the string and append if it is not a - b/ b - a, else pop the stack[-1] out and count it to the point
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        #work on the highest point first then to the lower one

        def remove_pair(s, first, second, point):
            stack = []
            score = 0
            for char in s:
                if stack and char == second and stack[-1] == first:
                    stack.pop()
                    score += point
                else:
                    stack.append(char)
            return ''.join(stack), score

        if (x > y):
            new_s, score1 = remove_pair(s, "a", "b", x)
            _, score2 = remove_pair(new_s, "b", "a", y)
        else:
            new_s, score1 = remove_pair(s, "b", "a", y)
            _, score2 = remove_pair(new_s, "a", "b", x)            
        return score1 + score2


        

