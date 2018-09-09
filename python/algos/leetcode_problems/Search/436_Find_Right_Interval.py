# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        start_dict = {}
        end_list = []
        
        for idx,val in enumerate(intervals):
            start_dict[val.start] = idx
            end_list.append(val.end)
        
        res_list = []
        
        for end in end_list:
            ret_idx, result = self.BinarySearch(sorted(start_dict.keys()),end)
            if result and ret_idx in start_dict:
                res_list.append(start_dict[ret_idx])
            else:
                res_list.append(-1)

        return res_list
    
    def BinarySearch(self, arr, val):
        lo = 0
        hi = len(arr)-1
        
        while (lo<=hi):
            mid = lo + (hi-lo)/2
            if arr[mid] == val:
                return [arr[mid], 1]
            elif arr[mid] < val:
                lo = mid+1
            else:
                hi = mid-1
            
        
        if lo == len(arr):
            return [-1, 0]
        elif arr[lo] > val:
            return [arr[lo],1]
        else:
            return [arr[lo+1],1]
