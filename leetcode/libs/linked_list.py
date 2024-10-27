from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None
