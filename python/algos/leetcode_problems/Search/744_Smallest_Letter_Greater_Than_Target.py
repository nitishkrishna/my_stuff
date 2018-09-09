class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        if target >= letters[n-1]:
            return letters[0]
        
        lo = 0
        hi = n
        
        while (lo<hi):
            mid = lo + (hi-lo)/2
            if target < letters[mid]:
                hi = mid
            else:
                lo = mid+1
            
        return letters[lo]
