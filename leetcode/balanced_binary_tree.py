from leetcode.libs.binary_tree import TreeNode


class Solution:
    def getDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        if self.getDepth(root.left) <= 1 and self.getDepth(root.right) <= 1:
            return True
        elif self.getDepth(root.left) <= 1 or self.getDepth(root.right) <= 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        