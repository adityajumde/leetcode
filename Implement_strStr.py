# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:11:52 2020

@author: ajumde
"""

'''

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        if needle==haystack:
            return 0
        window_size = len(needle)
        for i in range(0,len(haystack) - window_size+1):
            #print(haystack[i:window_size+i])
            if needle == haystack[i:window_size+i]:
                return i
        return -1
            
if __name__ == "__main__":
    s = Solution()
    print(s.strStr("mississippi","pi"))