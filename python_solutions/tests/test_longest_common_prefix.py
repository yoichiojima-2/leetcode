from python.longest_common_prefix import solution

def test_solution_1():
    assert solution(['flower', 'flow', 'flight']) == 'fl'

def test_solution_2():
    assert solution(['dog', 'racecar', 'car']) == ''

def test_solution_3():
    assert solution([""]) == ""

def test_solution_4():
    assert solution(["a"]) == "a"

def test_solution_5():
    assert solution(["ab", "a"]) == "a"

def test_solution_6():
    assert solution(["flower","flower","flower","flower"]) == "flower"

if __name__ == "__main__":
    res = solution(["ab", "a"])
    print(res)