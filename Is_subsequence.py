class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for letter in s:  #loop through the first word and check if each letter is in the second one, if not return false
            if letter in t:
                continue
            else:
                return False
        for i in range(len(s)-1):  #loop through the first word and compare the index of the current letter to the index of the next one.  If the next one is not higher then return false.
            if t.index(s[i]) < t.index(s[i+1]):
                continue
            else:
                return False
        return True




"""
392. Is Subsequence
Easy


Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

 

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
