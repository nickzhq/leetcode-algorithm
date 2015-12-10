__author__ = 'Nick'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root
        swapNodes(root)
        return root

def swapNodes(root):
    if not root:
        return
    root.left, root.right = root.right, root.left

    swapNodes(root.left)
    swapNodes(root.right)