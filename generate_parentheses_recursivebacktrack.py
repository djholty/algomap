class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers, solution = [],[]
        counter = 0
        def backtrack(open, close):
            nonlocal counter
            counter +=1
            if len(solution) == 2*n:
                answers.append(''.join(solution))
                return
            
            if open < n:
                solution.append('(')
                backtrack(open+1, close)
                solution.pop()
            
            if open > close:
                solution.append(')')
                backtrack(open, close +1)
                solution.pop()

        backtrack(0,0)
        print(counter)
        return answers

"""
22. Generate Parentheses
Solved
Medium
Topics
Companies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""
