from python_solutions.length_of_the_word import solution

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