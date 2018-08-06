"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        mid = 0
        while (start<end):
            # Since we discard half the search space in each iteration it is O(logn)
            mid = (start+end)/2
            if (mid%2) == 1:
                mid = mid-1
            if nums[mid] == nums[mid+1]:
                # Answer is on the right hand side (since mid is even index)
                start = mid+2
            else:
                # Answer is on left hand side ending at mid
                end = mid
        return nums[start]
        
#100%
