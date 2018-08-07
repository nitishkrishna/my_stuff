# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        root = self.rec_flatten(root)
    
    def rec_flatten(self,root):
        
        if not root:
            return root
        flat_left = flat_right = tmp_right = None
        if root.left:
            flat_left = self.rec_flatten(root.left)
        if root.right:
            flat_right =self.rec_flatten(root.right)
        if flat_left:
            tmp_right = flat_left
        if flat_right:
            if tmp_right:
                cur = tmp_right
                while(cur.right is not None):
                    cur = cur.right
                cur.right = flat_right
            else:
                tmp_right = flat_right
        root.right = tmp_right
        root.left = None
        
        return root
        
# 98.83%
