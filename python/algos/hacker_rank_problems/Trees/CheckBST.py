""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys

def checkBSTrec(root, min_s, max_s):
    if not root:
        return True
    if root.data > min_s and root.data < max_s:
        return (checkBSTrec(root.left,min_s, root.data) and checkBSTrec(root.right,root.data,max_s))
    else:
        return False
    
def checkBST(root):
    min_s = -1*sys.maxsize
    max_s = sys.maxsize
    
    return checkBSTrec(root,min_s, max_s)

