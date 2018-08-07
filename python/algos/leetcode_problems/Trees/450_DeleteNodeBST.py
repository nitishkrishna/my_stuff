# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        else:        
            found_node = root
            # Find next largest number if found_node.right
            # Find next smallest number if found_node.left
            # If neither, set found_node to null
            if not root.right and not root.left:
                return None
            elif not root.right:
                tmp = root.left
                root = None
                return tmp
            elif not root.left:
                tmp = root.right
                root = None
                return tmp
            else:
                cur_node = root.right
                while(cur_node.left is not None):
                    cur_node = cur_node.left
                root.val = cur_node.val
                root.right = self.deleteNode(root.right,root.val)
        
        return root
        
#10.51%
