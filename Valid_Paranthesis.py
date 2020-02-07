# -*- coding: utf-8 -*-
"""

@author: ajumde

"""

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s: 
            return True
        
        if s[0] == ')' or s[0] == "}" or s[0] == "]":
            return False
        
        len_s = 0
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                
            if char == ')' or char == ']' or char == '}':
                if not stack:
                    return False
                c = stack.pop()
                if char == ')' and c!= '(':
                    return False
                elif char == ']' and c!= '[':
                    return False
                elif char == '}' and c!= '{':
                    return False
                else:
                    pass
            len_s+=1
            
            if len_s == len(s):
                if not stack:
                    return True
        '''
        Another way using lookup.. same logic, beats 70%
        lookup = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in ['(', '[','{']:
                stack.append(c)
            elif c in [']', ')','}']:
                if not stack or stack[-1]!=lookup[c]:
                    return False
                stack.pop()
            else:
                return False
            
        return True if not stack else False
        '''

if __name__ == '__main__':
    s = Solution()
    print(s.isValid(["()"]))

    