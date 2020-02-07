# -*- coding: utf-8 -*-
"""

@author: ajumde

"""

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

#The key is to only reverse the last half of the number and not the entire number, the condition in while very important

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x == 0:
            return True
        
        if x > 0 and x%10 == 0:
            return False
        
        if x < 0:
            return False
        
        reverted = 0
        temp = x
        while x > reverted:
            reverted = (reverted *10) + x%10
            if reverted == x or reverted == int(x/10):
                return True
            x = int(x/10)
        
        
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1002))
