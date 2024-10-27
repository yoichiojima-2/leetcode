from dataclasses import dataclass


@dataclass
class TreeNode:
    val = 0
    left = None
    right = None


TreeNode(
    val=3,
    left=TreeNode(val=9),
    right=TreeNode(val=21, left=TreeNode(val=15), right=TreeNode(val=1)),
)
