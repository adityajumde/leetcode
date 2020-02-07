# -*- coding: utf-8 -*-
"""

@author: ajumde

"""

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
#Get the sign, get the reversed absolute integer, and return their product if r didn't "overflow".


class Solution(object):
    def reverse(self, x):
        if x<0:
            negative = True
            x *= -1
        elif x>0:
            negative = False
        else:
            return 0
        
        stack = []
        while x != 0:
            stack.append(x%10)
            x = int(x/10)
            
        strOut = ""
        for i in stack:
            strOut+=str(i)
        
        if negative:
            final =  -1*int(strOut)
        else:
            final = int(strOut)
        if abs(final) > (2 ** 31 -1):
            return 0
        else:
            return final
                        
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1002))
        
        
        
