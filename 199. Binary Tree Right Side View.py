# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        level = 0
        self.bfs(root, res, level)
        return res
    
    def bfs(self, node, res, level):
        if node == None: return
        if level == len(res):
            res.append(node.val)
        self.bfs(node.right, res, level+1)
        self.bfs(node.left, res, level+1)
        