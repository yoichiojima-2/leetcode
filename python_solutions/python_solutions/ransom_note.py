# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter


def solution(ransom_note: str, magazine: str) -> bool:
    letter_count = dict(Counter(magazine))

    for i in ransom_note:
        if i not in letter_count:
            return False

        if letter_count[i] == 0:
            return False

        letter_count[i] -= 1

    return True