from leetcode.libs.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        print(f"root: {root.val}")
        if root.left is None and root.right is None:
            return True
        if root.left is None and root.right is not None:
            if root.right.left is not None or root.right.right is not None:
                return False
        if root.right is None and root.left is not None:
            if root.left.left is not None or root.left.right is not None:
                return False
        else:
            res = self.isBalanced(root.left) and self.isBalanced(root.right)
            print(res)
            return res