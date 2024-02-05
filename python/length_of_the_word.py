def solution(s: str) -> int:
    first_word_found = False
    count = 0
    for i in s[::-1]:
        if first_word_found:
            if i != " ":
                count += 1
            else:
                return count
        elif i != " ":
            first_word_found = True
            count += 1
    return count
        

def test_solution_1():
    res = solution("Hello World")
    assert res == 5

def test_solution_2():
    res = solution("   fly me   to   the moon  ")
    assert res == 4


def test_solution_3():
    res = solution("luffy is still joyboy")
    assert res == 6

def test_solution_3():
    res = solution("a ")
    assert res == 1