class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr_l = 0
        ptr_r = len(s) - 1
        while ptr_l < ptr_r:
            s[ptr_l], s[ptr_r] = s[ptr_r], s[ptr_l]
            ptr_l +=1
            ptr_r -=1

"""
344. Reverse String
Solved
Easy
Topics
Companies
Hint

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.

"""
