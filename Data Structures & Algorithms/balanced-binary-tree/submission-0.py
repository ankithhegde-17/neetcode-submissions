class Solution:
    def isBalanced(self, root):
        return self.height(root) != -1

    def height(self, node):
        if not node:
            return 0
        l = self.height(node.left)
        r = self.height(node.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)