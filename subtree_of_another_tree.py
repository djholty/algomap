# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSame(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def isSub(root, subRoot):
            if root and not subRoot:
                return True
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if isSame(root, subRoot):
                return True
            return isSub(root.left, subRoot ) or isSub(root.right, subRoot)
            
        return isSub(root, subRoot)

"""
572. Subtree of Another Tree
Solved
Easy
Topics
Companies
Hint

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
"""
