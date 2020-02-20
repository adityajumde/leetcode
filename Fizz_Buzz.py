# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:19:28 2020

@author: ajumde
"""

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n):
        op_list = []
        for i in range(1,n+1):
            if i%3==0 and i%15!=0:
                op_list.append("Fizz")
            elif i % 5==0 and i%15!=0:
                op_list.append("Buzz")
            elif i%15==0:
                op_list.append("FizzBuzz")
            else:
                op_list.append(str(i))
        return op_list

if __name__ == "__main__":
    s =  Solution()
    print(s.fizzBuzz(15))
