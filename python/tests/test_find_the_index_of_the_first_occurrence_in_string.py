from python.find_the_index_of_the_first_occurrence_in_string import solution

def test_1():
    res = solution(haystack = 'sadbutsad', needle = 'sad')
    assert res == 0

def test_2():
    res = solution(haystack = 'leetcode', needle = 'leeto')
    assert res == -1
