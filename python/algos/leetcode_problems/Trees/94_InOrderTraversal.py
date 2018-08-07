# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_list = []
        if not root:
            return inorder_list
        inorder_list += self.inorderTraversal(root.left)
        inorder_list.append(root.val)
        inorder_list += self.inorderTraversal(root.right)
        
        return inorder_list
