import bisect
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        idx = bisect.bisect_left(arr,x)
        left = right = idx
        while(right-left<k):
            if left == 0:
                return arr[0:k]
            if right == len(arr):
                return arr[-k:]
            if (x - arr[left-1] <= arr[right] - x):
                left-=1
            else:
                right+=1
        return arr[left:right]
        
