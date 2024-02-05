def solution(haystack: str, needle: str) -> int:
    needle_len = len(needle)
    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i
    return -1

def test_1():
    res = solution(haystack = 'sadbutsad', needle = 'sad')
    assert res == 0

def test_2():
    res = solution(haystack = 'leetcode', needle = 'leeto')
    assert res == -1
