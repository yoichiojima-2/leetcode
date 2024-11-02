from leetcode.libs.binary_tree import TreeNode
from typing import Iterable


class Solution:
    def helper(self, root: TreeNode | None) -> Iterable[int]:
        if root:
            self.helper(root.left)
            yield root.val
            self.helper(root.right)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return list(self.helper(root))
