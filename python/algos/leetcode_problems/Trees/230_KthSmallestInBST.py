"""
[31,30,48,3,null,38,49,0,16,35,47,null,null,null,2,15,27,33,37,39,null,1,null,5,null,22,28,32,34,36,null,null,43,null,null,4,11,19,23,null,29,null,null,null,null,null,null,40,46,null,null,7,14,17,21,null,26,null,null,null,41,44,null,6,10,13,null,null,18,20,null,25,null,null,42,null,45,null,null,8,null,12,null,null,null,null,null,24,null,null,null,null,null,null,9]
1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    stack = list()
    count = 0
    res = None
    
    def InorderTraversal(self, root):
        if not root:
            return
        self.InorderTraversal(root.left)
        self.stack.append(root.val)
        self.count +=1
        if self.count == self.k:
            self.res = root.val
        self.InorderTraversal(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.InorderTraversal(root)
        return self.res

# 11.61% -> Iterative will be faster
