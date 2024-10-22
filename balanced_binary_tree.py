from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True
