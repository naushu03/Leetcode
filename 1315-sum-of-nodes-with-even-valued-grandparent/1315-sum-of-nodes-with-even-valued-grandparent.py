# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def pre(root,parent,grandparent):
            total=0
            if not root:
                return 0
            if grandparent and grandparent.val%2==0:
                total+=root.val
            total+= pre(root.left,root,parent)
            total+= pre(root.right,root,parent)
            return total
        return pre(root,None,None)
        