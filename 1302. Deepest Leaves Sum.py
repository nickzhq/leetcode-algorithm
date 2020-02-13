# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = []
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        self.res.append(0)
        self.helper(root, 0)
        return self.res[-1]
    
    def helper(self, root, level):
        if len(self.res) <= level:
            self.res.append(0)
        if root.left == None and root.right == None:
            self.res[level] += root.val
            return None
        
        if root.left != None:
            self.helper(root.left, level + 1)
        if root.right != None:
            self.helper(root.right, level + 1)