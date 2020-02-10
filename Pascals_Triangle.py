# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:43:25 2020

@author: ajumde
"""

'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows):
        op_list = []
        for i in range(numRows):
            op_list.append([1]*(i+1))
            for j in range(1,i):
                if i>1:
                    op_list[i][j] = op_list[i-1][j-1] + op_list[i-1][j]     
        return op_list
            
if __name__ == "__main__":
    numRows = 5
    s = Solution()
    print(s.generate(numRows))
