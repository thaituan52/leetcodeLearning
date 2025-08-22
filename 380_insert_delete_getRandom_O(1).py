#https://leetcode.com/problems/insert-delete-getrandom-o1/

# to get O(1) time complexity for insert, delete and getRandom, we use a combination of a list and a dictionary.

import random

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        - `self.data`: A list to store the elements.
        - `self.pos`: A dictionary to store the index of each element in the list.
        """
        self.data = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        - If the value is already in `self.pos`, return False.
        - Otherwise, add the value to `self.data` and store its index in `self.pos`.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        - If the value is not in `self.pos`, return False.
        - Otherwise, swap the element to remove with the last element in `self.data`.
        - Update the index of the last element in `self.pos`.
        - Remove the last element from `self.data` and delete the value from `self.pos`.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        # get index of element to remove
        idx = self.pos[val]
        last = self.data[-1]

        # move last element into idx position
        self.data[idx] = last
        self.pos[last] = idx

        # remove last element
        self.data.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        - Use `random.choice` to select a random element from `self.data`.
        :rtype: int
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()