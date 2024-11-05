class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #special cases for empty list, bigger than all of list, or smaller than all list items
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        
        #initialize left and right pointers
        left = 0
        right = len(nums) -1

        #now search for middle of list positions
        while left <= right:
            mid = right + left //2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else:  #target is greater than midpoint to shift left point just past mid
                left = mid + 1 

        return left #if the number is not in the list, insert it

"""
35. Search Insert Position
Solved
Easy
Topics
Companies

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

"""
