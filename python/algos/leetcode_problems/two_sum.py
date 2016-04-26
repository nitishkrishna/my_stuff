# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup_dict = dict(((v, i) for i, v in enumerate(nums)))
        return next(((i+1, lookup_dict.get(target-v)+1) for i, v in enumerate(nums)
                     if lookup_dict.get(target-v, i) != i), None)
    """
    Logic:
    1. Create a dict of number, index as lookup_dict from list of nums
    2. Search for index of dict[target-num] while iterative list of nums
    """
# 55.44 percentile