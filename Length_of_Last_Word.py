# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:20:41 2020

@author: ajumde
"""

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
 
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip().split(' ')
        return len(lst[-1])
        
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello world"))