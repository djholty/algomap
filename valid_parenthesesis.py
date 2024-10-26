class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stk = []

        for c in s:
            if c not in hashmap: #c is an open bracket, not a closed one
                stk.append(c)
            else: # c is a closing bracket
                if not stk: #if nothing in stack, ie. no open bracket
                    return False
                else: # c is a closing bracket, and we pop off an opening bracket from stack, check for match
                    popped = stk.pop() #open bracket
                    if popped != hashmap[c]:
                        return False
        if stk: #if stack still has open brackets that are unmatched return False
            return False
        else:
            return True 

"""
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""
