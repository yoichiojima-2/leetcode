from leetcode.libs.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return [
            *self.inorderTraversal(root.left),
            root.val,
            *self.inorderTraversal(root.right)
        ]