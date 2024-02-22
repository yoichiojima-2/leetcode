# Two strings are considered close if you can attain one from the other using the
# following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do
# the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

from collections import Counter


def solution(word1, word2):
    counter1 = Counter(word1)
    counter2 = Counter(word2)
    print({"counter1": counter1, "counter2": counter2})
    if set(counter1.keys()) != set(counter2.keys()):
        return False
    return sorted(counter1.values()) == sorted(counter2.values())
