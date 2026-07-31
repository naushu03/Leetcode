# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        lst=[]
        def insert(node,val):
            if not node:
                node=TreeNode(val)
                return node
            elif val<node.val:
                node.left=insert(node.left,val)
            else:
                node.right=insert(node.right,val)
            return node
        def preorder(root,low,high):
            if not root:
                return
            if root.val>=low and root.val<=high:
                lst.append(root.val)
            preorder(root.left,low,high)
            preorder(root.right,low,high)
        
        preorder(root,low,high)
        if len(lst)==0:
            return None
        root=TreeNode(lst[0])
        for i in range(1,len(lst)):
            if lst[i]>root.val:
                root.right=insert(root.right,lst[i])
            elif lst[i]<root.val:
                root.left=insert(root.left,lst[i])
        return root
    