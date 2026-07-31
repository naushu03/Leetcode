# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        def insert(node,val):
            if not node:
                node=TreeNode(val)
                return node
            elif val>node.val:
                node.right=insert(node.right,val)
            elif val<node.val:
                node.left=insert(node.left,val)
            return node
        for i in range(1,len(preorder)):
            if preorder[i]>root.val:
                root.right=insert(root.right,preorder[i])
            elif preorder[i]<root.val:
                root.left=insert(root.left,preorder[i])
        return root 