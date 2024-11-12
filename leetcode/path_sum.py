from pprint import pprint
from dataclasses import dataclass
from leetcode.libs.binary_tree import TreeNode


@dataclass
class Solution:
    def get_sums(self, root: TreeNode | None) -> list[int]:
        print(f"visiting...: {root.val}")

        if not root:
            return [0]

        elif not root.left and not root.right:
            return [root.val]

        elif not root.left:
            return [root.val, root.val + root.right.val]

        elif not root.right:
            return [root.val + root.left.val, root.val]

        return [
            *[i + root.val for i in self.get_sums(root.left)],
            *[i + root.val for i in self.get_sums(root.right)],
        ]

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        pprint(root)  # debug
        print(f"get_sums: {self.get_sums(root)}") # debug
        return targetSum in self.get_sums(root)