# https://leetcode.com/problems/two-sum/

#My solution:
# Using two-pointer approach in the sorted array to make sure we go through all of the point from first to end 
#This way of doing code make it cost time than usual - time complexity: O(n^2)
# This is brute force approach just the way I use two pointer different
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = 1
        while (nums[start] + nums[end] != target):
            if start == len(nums) - 1:
                return []
            if end == len(nums) - 1:
                start += 1
                end = start + 1
            else:
                end += 1

        return [start, end]

#Faster way to do it is using a hashMap where map[num[i]] = i 
#and check if complement of i (target - nums[i] is actually 
#in the map or not - must be 2 different one)   
# this one take 2n time complexity to finish
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []
#Fastest way is to store the seen number in the hash and actually check the other item in the list until we find one with complement in the list
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # just in case no solution found

