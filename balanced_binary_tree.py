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
        return True

@pytest.fixture
def balanced_binary_tree() -> TreeNode:
    return TreeNode(
        val=3,
        left=TreeNode(
            val=9
        ),
        right=TreeNode(
            val=20,
            left=TreeNode(val=15),
            right=TreeNode(val=7)
        )
    )

@pytest.fixture
def unbalanced_binary_tree() -> TreeNode:
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

def test_solution(
    balanced_binary_tree:TreeNode,
    unbalanced_binary_tree: TreeNode
):
    assert Solution().isBalanced(balanced_binary_tree)
    assert not Solution().isBalanced(binary_tree)
