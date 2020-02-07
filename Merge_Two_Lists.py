# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:03:46 2020

@author: ajumde
"""
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode(-1)
        cur = result
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return result.next



'''
Recursive efficient solution

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = None
        if not l1 and not l2: return temp
        if not l1 and l2: return l2
        if not l2 and l1: return l1
        
        if l1.val<=l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
        else: 
            temp = l2
            temp.next = self.mergeTwoLists(l2.next, l1)
        return temp

'''