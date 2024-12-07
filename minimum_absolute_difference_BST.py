# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        previous = None
        minabsdiff = float('inf')

        def dfs(root):
            nonlocal previous
            nonlocal minabsdiff

            if not root:
                return

            dfs(root.left)
            if previous is None: #if you only do 'not previous' then if the node value is 0 the code may not be correct, therefore you need the 'is' keyword
                previous = root.val
            else:
                diff = root.val - previous #subsequent nodes are always greater in inorder traversal so this will be positive
                minabsdiff = min(minabsdiff, diff)
                previous = root.val
            dfs(root.right)

        dfs(root)
        return minabsdiff

  '''

  530. Minimum Absolute Difference in BST
Solved
Easy
Topics
Companies

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 104].
    0 <= Node.val <= 105

'''
