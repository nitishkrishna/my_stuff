# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not len(preorder) or not len(inorder):
            return None
        
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        
        root.left = self.buildTree(preorder,inorder[0:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
            
        return root
        
