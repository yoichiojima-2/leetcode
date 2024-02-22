from python.ransom_note import solution


def test_solution_1():
    assert solution("a", "b") == False

def test_solution_2():
    assert solution("aa", "ab") == False

def test_solution_3():
    assert solution("aa", "aab") == True