from python_solutions.isomorphic_string import solution


def test_solution_1():
    assert solution("egg", "add") == True

def test_solution_2():
    assert solution("foo", "bar") == False

def test_solution_3():
    assert solution("paper", "title") == True