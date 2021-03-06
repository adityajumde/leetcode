# -*- coding: utf-8 -*-
"""

@author: ajumde

"""

'''

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.


'''

#This is a simple 2-pointer problem

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        p1= 0
        
        if not nums:
            return 0
        
        return_var = 1
        for i in range(1,len(nums)):
            if nums[p1]!=nums[i]:
                p1+=1
                #nums[i], nums[p1]  = nums[p1] , nums[i]
                nums[p1] = nums[i]
                return_var+=1
                
                
        return return_var
    

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,3,4]))
    