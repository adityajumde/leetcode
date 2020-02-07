# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:15:46 2020

@author: ajumde
"""

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
'''

class Solution:
    def update(self, start_str):
        print("here")
        return_str = ""
        start_str+='&'
        count = 1
        for i in range(len(start_str)-1):
            if start_str[i] == start_str[i+1]:
                count+=1
            else:
               return_str+=str(count)+str(start_str[i])              
               count = 1
               
        
        return return_str
    
    
    def countAndSay(self, n):
        
        if n == 1:
            return "1"
        
        start_str = "1"
        
        for i in range(2,n+1):
            print("Before : ",start_str)
            start_str = self.update(start_str)
            print("After : ",start_str)
            print("------")
        return start_str
            
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(6))