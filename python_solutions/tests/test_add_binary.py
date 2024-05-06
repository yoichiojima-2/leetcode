from python_solutions.add_binary import add_binary

def test_add_binary_1():
    a = "11"
    b = "1"
    assert add_binary(a, b) == "100"


def test_add_binary_2():
    a = "1010"
    b = "1011"
    assert add_binary(a, b) == "10101"
