# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        res=[]
        p=head
        while p:
            res.append(p.val)
            p=p.next
        def construct(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            root=TreeNode(res[mid])
            root.left=construct(l,mid-1)
            root.right=construct(mid+1,r)
            return root
        return construct(0,len(res)-1)