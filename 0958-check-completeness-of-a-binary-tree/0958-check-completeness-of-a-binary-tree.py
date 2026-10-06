# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return []
        qu=[root]
        past=False
        while qu:
            curr=qu.pop(0)   
            if curr==None:
                past=True
            else:
                if past==True:
                    return False
                qu.append(curr.left)
                qu.append(curr.right)
        return True