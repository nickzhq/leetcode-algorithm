__author__ = 'Nick'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack,result = [root],[]
        while stack:
            temp = stack.pop()
            result += [temp.val]
            if temp.right:
                stack += [temp.right]
            if temp.left:
                stack += [temp.left]

        return result
