from typing import Optional

from leetcode.libs.binary_tree import TreeNode


class Solution:
    def get_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1
