# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:15:46 2020

@author: ajumde
"""
'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
class Solution:
    def maxSubArray(self, nums) -> int:
        # Basically it checks in every iteration if curr_sum + current number is greater or the current number is greater
        max_sum = curr_sum = nums[0]
        
        for num in nums:
            print("curr_sum + num : ", curr_sum+num)
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            print("Num : ",num, "curr_sum : ", curr_sum, "max_sum : ", max_sum, '\n-----')
        return max_sum
            
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,-1,-3,4,-1,2,1,-5,4]))