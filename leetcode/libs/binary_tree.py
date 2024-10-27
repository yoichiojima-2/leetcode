from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None
