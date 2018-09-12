# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        first_stack = []
        second_stack = []
        p_o = []
        
        if not root:
            return p_o
        
        first_stack.append(root)
        
        while len(first_stack):
            top = first_stack.pop(-1)
            if top.left:
                first_stack.append(top.left)
            if top.right:
                first_stack.append(top.right)
                
            second_stack.append(top)
        
        while len(second_stack):
            top = second_stack.pop(-1)
            p_o.append(top.val)
            
        return p_o
