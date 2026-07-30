# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res=[]
        def pre(root,s):
            if not root:
                return 
            s+=str(root.val)
            if not root.left and not root.right:
                res.append(s)
            pre(root.left,s+"->")
            pre(root.right,s+"->")  
        pre(root,"")
        return res