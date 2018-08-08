class Solution(object):
    max_ans = 0
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        while(left<right):
            vol = (right-left)*min(height[right],height[left])
            self.max_ans = max(self.max_ans,vol)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return self.max_ans
            
# 7.31%
