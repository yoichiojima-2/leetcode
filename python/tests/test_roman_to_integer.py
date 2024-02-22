from python.roman_to_integer import solution

def test_solution():
    assert solution("III") == 3
    assert solution("LVIII") == 58
    assert solution("MCMXCIV") == 1994