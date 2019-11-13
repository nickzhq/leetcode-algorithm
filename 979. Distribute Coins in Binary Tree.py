# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node):
            if not node: return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.res += abs(L) + abs(R)
            return node.val + L + R - 1 # Math.abs(num_coins - 1) 这个是若某一节点硬币数大于1时，由于被计算了但是没有移动，所以必须-1
        
        dfs(root)
        return self.res