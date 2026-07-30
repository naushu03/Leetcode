# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        def pre(node,row,col):
            if not node:
                return
            res.append([col,row,node.val])
            pre(node.left,row+1,col-1)
            pre(node.right,row+1,col+1)
        pre(root,0,0)
        res.sort()
        op=[]
        prevCol=float('inf')
        for col,row,val in res:
            while col!=prevCol:
                op.append([])
                prevCol=col
            op[-1].append(val)
        return op