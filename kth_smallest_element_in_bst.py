# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k  # Use a class-level variable to track `k`
        self.result = None  # Store the result

        def in_order_traversal(node):
            if not node or self.result is not None:
                return
            
            # Traverse the left subtree
            in_order_traversal(node.left)
            
            # Process the current node
            self.k -= 1
            if self.k == 0:  # If k reaches 0, we found the k-th smallest element
                self.result = node.val
                return
            
            # Traverse the right subtree
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        return self.result

  """
  230. Kth Smallest Element in a BST
Solved
Medium
Topics
Companies
Hint

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

 

Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

"""
