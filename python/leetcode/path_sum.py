from leetcode.libs.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
