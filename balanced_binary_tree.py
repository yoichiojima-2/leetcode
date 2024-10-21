from typing import Optional
from dataclasses import dataclass
import pytest


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ...


@pytest.fixture
def binary_tree() -> TreeNode:
    return TreeNode(
        val=1,
        right=TreeNode(
            val=2,
            right=TreeNode(
                val=3,
                right=TreeNode(val=4)
            )
        )
    )

def test_solution(binary_tree: TreeNode):
    assert not Solution().isBalanced(binary_tree)
