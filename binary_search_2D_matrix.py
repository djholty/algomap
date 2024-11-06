class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #to find the number do binary search twice, first for the row, then for the column
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows*cols

        #binary search through rows to find the right row
        left = 0
        right = total - 1

        while left <= right:
            mid = (right+left)//2
            midrow_idx = mid//cols
            midcol_idx = mid%cols
            if matrix[midrow_idx][midcol_idx] == target:
                return True
            elif target < matrix[midrow_idx][midcol_idx]:
                right = mid -1
            else:
                left = mid + 1

        return False

  """
  74. Search a 2D Matrix
Solved
Medium
Topics
Companies

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

"""
