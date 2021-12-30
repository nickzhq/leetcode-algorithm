# 1028. Recover a Tree From Preorder Traversal
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
整体思路是用单方向栈，有点像字符串四则运算
一个数据栈，一个操作栈(这里既是层数栈)，层数栈保持单向递增
"""
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S) <= 0: return None
        
        idx = 0
        data = [] # 保存数字
        level = [] # 记录层数
        while idx < len(S) :
            # 若遇多个数字，则处理为一个数
            if S[idx].isdigit():
                beg = idx
                while idx+1 < len(S) and S[idx+1].isdigit() :
                    idx += 1
                data.append( TreeNode( int(S[beg:idx+1]) ) )
            
            # 若遇多个-，则处理层数
            elif S[idx] is '-':
                beg = idx
                while idx + 1 < len(S) and S[idx+1] is '-':
                    idx += 1
                temp_level = idx - beg
                
                """
                这里最初的版本是做判断
                if 若层数栈为空 或者 当前层数>=栈顶的层，直接入栈
                else 弹出层数栈顶层元素并配合数据栈进行计算，直到当前层数=栈顶的层
                但是写完后，有重复代码，就简化成如下：
                弹出层数栈顶层元素并配合数据栈进行计算，直到当前层数=栈顶的层，然后再入栈
                """
                while len(level) >= 2 and level[-1] > temp_level:
                    """
                    此处有两种结果：
                    1. 有左右两个子节点
                    2. 仅有一个节点，即左子节点
                    """
                    if level[-1] == level[-2]:
                        level.pop()
                        level.pop()
                            
                        right = data.pop()
                        left  = data.pop()
                            
                        data[-1].right = right
                        data[-1].left  = left
                    else:
                        level.pop()
                        left = data.pop()
                        data[-1].left = left
                        
                level.append( temp_level )
            idx += 1
                
        # 若层数栈里有遗留，则继续处理
        while len(level) > 0:
            """
            此处有两种结果：
            1. 有左右两个子节点
            2. 仅有一个节点，即左子节点
            """
            if len(level) >= 2 and level[-1] == level[-2]:
                level.pop()
                level.pop()
                            
                right = data.pop()
                left  = data.pop()
                            
                data[-1].right = right
                data[-1].left  = left
            else:
                level.pop()
                left = data.pop()
                data[-1].left = left    
        
        return data[-1]


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
#整体思路是是递归，用当前层数来确定当前节点
#re.findall('-*\d+', S)将字符串分割成list，再list反转，开始处理
#有多少个-就代表多少层
"""
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def get_depth(ss):
            return ss.rfind('-') + 1
        
        def dfs(s, depth):
            if not s:
                return None
            last = s[-1]
            if get_depth(last) == depth:
                n = TreeNode(last[depth:])
                s.pop()
                n.left = dfs(s, depth + 1)
                n.right = dfs(s, depth + 1)
                return n
            return None
            
        s = re.findall('-*\d+', S)
        return dfs(s[::-1], 0)
"""