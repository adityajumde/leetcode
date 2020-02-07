# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:23:45 2020

@author: ajumde
"""

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
class Solution:
    def searchInsert(self, nums,target) -> int:
        for i in range(len(nums)):
            if target - nums[i] == 0:
                return i
            if target - nums[i] < 0:
                return i
        return len(nums)
    
        '''
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)/2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l
        '''

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,1,1,2,3,4],4))