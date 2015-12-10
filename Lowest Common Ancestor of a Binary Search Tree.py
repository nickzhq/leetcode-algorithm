__author__ = 'Nick'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        # recursion
        if not root:
            return None
        # if root are greater than p and q, then LCA lies in left
        if( root.val > p.val and root.val > q.val ):
            return self.lowestCommonAncestor(root.left,p,q)
        # if root are smaller than p and q, then LCA lies in right
        if( root.val < p.val and root.val < q.val ):
            return self.lowestCommonAncestor(root.right,p,q)

        return root
        '''
        result = root
        while result:
            if result.val > p.val and result.val > q.val and result.left:
                result = result.left
                continue
            elif result.val < p.val and result.val < q.val and result.right:
                result = result.right
                continue
            break

        return result