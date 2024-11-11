class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left =  0
        max_window = 0
        numzeroes = 0
        

        for r in range(n):
            if nums[r] == 0:
                numzeroes += 1
            while numzeroes > k:
                if nums[left] == 0: 
                    numzeroes -= 1
                left += 1

            w = r - left + 1
            max_window = max(max_window, w)
        return max_window

"""
1004. Max Consecutive Ones III
Solved
Medium
Topics
Companies
Hint

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length


"""
