# https://leetcode.com/problems/add-two-numbers/
# The simple idea is to go through the two linked list and add up and put to the result
# This one takes times to think how to work with linked list a bit - new to python and use chatgpt to refine my idea
# Overall this approach is not hard to think of

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        answer = temp
        carry = 0
        
        while l1 or l2 or carry: #iterate through l1 and l2 with remember of carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            temp.next = ListNode(total % 10)
            temp = temp.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return answer.next
