# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def checkSubtree(self, node, smallest, largest):
        
        if not node:
            return True
        
        if (node.val <= smallest) or (node.val >= largest):
            return False
        if node.left and (node.val<=node.left.val):
            return False
        if node.right and (node.val>=node.right.val):
            return False
        
        return (self.checkSubtree(node.left,smallest,node.val) and self.checkSubtree(node.right,node.val,largest))
                    
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res_left = True
        res_right = True
        if not root:
            return True
        
        min_size = -sys.maxsize -1
        max_size = sys.maxsize

        return self.checkSubtree(root,min_size, max_size)
        

# 38.24%
