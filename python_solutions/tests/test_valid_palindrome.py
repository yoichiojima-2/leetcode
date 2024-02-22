from python_solutions.valid_palindrome import solution


def test_1():
    assert solution("A man, a plan, a canal: Panama")

def test_2():
    assert not solution("race a car")

def test_3():
    assert solution(" ")

def test_4():
    assert solution("aa")