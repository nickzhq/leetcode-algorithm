# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        """
        if root == None:
            return None
        
        self.dfs(root.left, root, 1, target)
        self.dfs(root.right, root, 0, target)
        
        if root.val == target and root.left == None and root.right == None:
            return None
        
        return root
        
    def dfs(self, node, parent, left_child, target):
        if node != None:
            if node.left != None:
                self.dfs(node.left, node, 1, target)
            if node.right != None:
                self.dfs(node.right, node, 0, target)

            if node.val == target and node.left == None and node.right == None:
                if left_child == 1:
                    parent.left = None
                else:
                    parent.right = None
        """
        if not root:
            return None
        
        root.left  = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        if root.val == target and not root.left and not root.right:
            return None
        
        return root