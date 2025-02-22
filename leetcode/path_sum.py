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
            
        if not root.left and not root.right:
            return root.val == targetSum
            
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))
