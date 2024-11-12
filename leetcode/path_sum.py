from pprint import pprint
from dataclasses import dataclass
from leetcode.libs.binary_tree import TreeNode


@dataclass
class Solution:
    def get_sums(self, root: TreeNode | None) -> list[int]:
        print(f"visiting...: {root.val}")

        if not root:
            print("root is None")
            return [0]

        elif not root.left and not root.right:
            print("left and right is None")
            return [root.val]

        elif not root.left:
            print("left is None")
            return [
                root.val,
                *[i + root.val for i in self.get_sums(root.right)],
            ]

        elif not root.right:
            print("right is None")
            return [
                *[i + root.val for i in self.get_sums(root.left)],
                root.val
            ]

        return [
            *[i + root.val for i in self.get_sums(root.left)],
            *[i + root.val for i in self.get_sums(root.right)],
        ]

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        pprint(root)  # debug
        print(f"get_sums: {self.get_sums(root)}") # debug
        return targetSum in self.get_sums(root)