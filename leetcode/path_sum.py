from pprint import pprint
from leetcode.libs.binary_tree import TreeNode
from pprint import pprint


class Solution:
    def get_sums(self, root: TreeNode | None) -> list[int]:
        if not root:
            return [0]

        elif not root.left and not root.right:
            return [root.val]

        elif not root.left:
            return [
                root.val,
                *[i + root.val for i in self.get_sums(root.right)],
            ]

        elif not root.right:
            return [
                *[i + root.val for i in self.get_sums(root.left)],
                root.val
            ]

        return [
            *[i + root.val for i in self.get_sums(root.left)],
            *[i + root.val for i in self.get_sums(root.right)],
        ]

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        sums = self.get_sums(root)

        # [START debug]
        pprint(root)
        print(f"targetSum: {targetSum}")
        print(f"sums: {sums}")
        # [END debug]

        return targetSum in sums