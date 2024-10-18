class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) <2:
            return strs[0]
        
        # Find the length of the shortest word
        shortest_length = min(len(word) for word in strs)
        if shortest_length == 0:
            return ""
        prefix = []
        for i in range(shortest_length):
            letterset = set()
            for word in strs:
                letterset.add(word[i])
            if len(letterset) == 1:
                prefix.append(word[i])
            else:
                break
        return "".join(prefix)
"""
14. Longest Common Prefix
Solved
Easy
Topics
Companies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""
            



