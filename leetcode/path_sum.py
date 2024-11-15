from leetcode.libs.binary_tree import TreeNode


class Solution:
    def get_sums(self, root: TreeNode | None) -> list[int]:
        if not root:
            return [0]

        if not root.left and not root.right:
            return [root.val]

        elif not root.left:
            return [
                root.val,
                *[i + root.val for i in self.get_sums(root.right)],
            ]

        elif not root.right:
            return [*[i + root.val for i in self.get_sums(root.left)], root.val]

        return [
            *[i + root.val for i in self.get_sums(root.left)],
            *[i + root.val for i in self.get_sums(root.right)],
        ]

    def get_depth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        if self.get_depth(root) == 1 and root.val == targetSum:
            return True

        return (targetSum in self.get_sums(root.left) and self.get_depth(root.left) > 1) or (
            targetSum in self.get_sums(root.right) and self.get_depth(root.right) > 1
        )
