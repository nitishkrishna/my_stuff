"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set()
        set2 = set()
        for n1 in nums1:
            set1.add(n1)
        for n2 in nums2:
            set2.add(n2)
        
        return list(set1.intersection(set2))

#26.35%
