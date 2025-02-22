from leetcode.libs.binary_tree import TreeNode


class Solution:
    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)

        if left_depth == -1 or right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.getDepth(root) != -1
