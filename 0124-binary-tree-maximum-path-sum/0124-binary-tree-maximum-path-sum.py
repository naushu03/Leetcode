class Solution(object):

    def maxPathSum(self, root):

        self.maximum = float("-inf")

        def postorder(node):

            if not node:
                return 0

            l = max(postorder(node.left), 0)
            r = max(postorder(node.right), 0)

            # Update answer for every node
            self.maximum = max(self.maximum, node.val + l + r)

            # Return best path going upward
            return node.val + max(l, r)

        postorder(root)

        return self.maximum