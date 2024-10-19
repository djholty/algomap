class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ransomnoteDict = {}
        magazineDict = {}
        for i in ransomNote:
            ransomnoteDict[i] = ransomnoteDict.get(i,0) + 1
        for i in magazine:
            magazineDict[i] = magazineDict.get(i,0) + 1
        print(ransomnoteDict)
        print(magazineDict)
        for key in ransomnoteDict:
            if magazineDict.get(key,0) < ransomnoteDict.get(key):
                return False
        return True 

"""
383. Ransom Note
Solved
Easy
Topics
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
