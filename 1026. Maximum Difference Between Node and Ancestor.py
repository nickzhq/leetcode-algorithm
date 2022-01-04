# coding=utf-8
# @Time     : 04th January, 2022  19:45
# @Author   : Nick Z
# @Email    : nick_zz@qq.com
# @File     : 1026. Maximum Difference Between Node and Ancestor.py
# @Software : PyCharm 
# =======================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(node, cmax, cmin):
            if not node:
                return cmax - cmin

            cmax = max(cmax, node.val)
            cmin = min(cmin, node.val)
            left = helper(node.left, cmax, cmin)
            right = helper(node.right, cmax, cmin)
            return max(left, right)

        return helper(root, root.val, root.val)