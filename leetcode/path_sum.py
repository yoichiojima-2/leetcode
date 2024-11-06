from leetcode.libs.binary_tree import TreeNode


class Solution:
    def getSum(self, root: TreeNode | None) -> int:
        ...
        

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        return self.getSum(root.left) == targetSum or self.getSum(root.right) == targetSum