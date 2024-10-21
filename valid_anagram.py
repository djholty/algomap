class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        for key in s_dict:
            if s_dict[key] != t_dict.get(key, -1):
                return False
        return True

  """
  242. Valid Anagram
Solved
Easy
Topics
Companies

Given two strings s and t, return true if t is an
anagram
of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
