class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7: #if the word text has fewer letters than the word balloon return 0 b/c its not possible
            return 0
        text_dict = {}
        for letter in text:
            text_dict[letter] = text_dict.get(letter, 0) + 1
        totalinstances = 0
        balloon_dict = {'b':1, 'a':1, 'l':2,'o':2, 'n':1}
        instance_dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for key in balloon_dict:
            instance_dict[key] = text_dict.get(key, 0)//balloon_dict[key]
        print(instance_dict)
        return min(instance_dict.values())

"""
1189. Maximum Number of Balloons
Solved
Easy
Topics
Companies
Hint

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 

Constraints:

    1 <= text.length <= 104
    text consists of lower case English letters only.

 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
"""
