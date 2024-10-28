from leetcode.libs.binary_tree import TreeNode


class Solution:
    def getDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        else:
            return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        print(f"visiting: {root.val}")

        if root is None:
            return True

        elif root.left is None and root.right is None:
            return True

        elif root.left is None and root.right is not None:
            if root.right.left is not None or root.right.right is not None:
                return False

        elif root.right is None and root.left is not None:
            if root.left.left is not None or root.left.right is not None:
                return False

        elif abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False

        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)