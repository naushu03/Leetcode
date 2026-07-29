# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder.pop(0))
        index=inorder.index(root.val)
        root.left=self.buildTree(preorder[:index],inorder[:index])
        root.right=self.buildTree(preorder[index:],inorder[index+1:])
        return root      