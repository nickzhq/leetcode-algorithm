# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# 如果不利用二叉搜索树性质，可以遍历所有节点，然后sort
# 这里面利用了二叉搜索树性质

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        list1 = self.traverse(root1, [])
        list2 = self.traverse(root2, [])
        
        if root1 == None:
            return list2
        elif root2 == None:
            return list1
        
        res = []
        
        first = 0
        second = 0
        while first < len(list1) and second < len(list2):
            if list1[first] < list2[second]:
                res.append( list1[first] )
                first += 1
            else:
                res.append( list2[second] )
                second += 1
        
        if first < len(list1):
            res.extend( list1[first:] )
        else:
            res.extend( list2[second:] )
        
        return res
        
    def traverse(self, root, res):
        if root != None:
            self.traverse(root.left, res)
            res.append(root.val)
            self.traverse(root.right, res)
            
            return res
        
        