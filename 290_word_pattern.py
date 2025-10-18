#https://leetcode.com/problems/word-pattern

#Like isomorphic strings but with words instead of characters

# We use two hash maps to ensure the one-to-one mapping in both 
# directions thus making it from O(n^2) to O(1) when checking if 
# a word is already mapped to a different character.
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        

        char_to_word = {}
        word_to_char = {}


        for c, w in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w

            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c
        
        return True
        
