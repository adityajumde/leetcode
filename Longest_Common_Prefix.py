# -*- coding: utf-8 -*-
"""

@author: ajumde
"""

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        #strs = ["aa","a"]
        '''
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        first =  strs[0]
        print("first : ",first)
        index = 0
        flag = 0
        for i in first:
            for word in strs:
                print("Comparing",i," with ",word[index]," from ",word, " index : ",index)
                if index < len(word) - 1:
                    if i != word[index]:
                        flag = 1
                        break
                else:
                    print("going here")
                    flag = 1
                    break
                   
            if flag ==1:
                break
            index+=1 
            
            print("---> iteration done :",index)
            
        if index > 0:    
            return first[0:index]
        else:
            return ""
        '''
        
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        '''
        #This is a brilliant solution!! 
        # x = ["abcd", "abcdpqr","abcsd"]
        # min(x) = 'abcd' max(X) = 'abcsd'
        
        
        m = strs
        if not m: return ''
	    #since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
        '''

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['abcd','abc']))
