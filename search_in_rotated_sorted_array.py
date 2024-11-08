class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n -1

        #check which side is the sorted side
        while left <= right:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            m =  (right +left)//2
            if nums[m] == target:
                return m
            #check if right side is sorted    
            if nums[m] < nums[right]:
                #check if target is in the sorted side:
                if nums[m] <= target < nums[right]: # target on sorted R side
                    left = m + 1
                else: #target is on left side then
                    right = m - 1


            else: #if right isn't sorted then left side is
                #check if target is in sorted Left side
                if nums[left] <= target < nums[m]: #target is on left sorted side
                    right = m -1
                else: #target is on right side
                    left = m + 1
        return -1

  """
  33. Search in Rotated Sorted Array
Solved
Medium
Topics
Companies

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104

"""
