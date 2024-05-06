def add_binary(a, b):
    a = a[::-1]
    b = b[::-1]

    a_int = 0
    b_int = 0

    for i in range(len(a)):
        a_int += (2 ** i) * int(a[i])

    for i in range(len(b)):
        b_int += (2 ** i) * int(b[i])

    sum_i = a_int + b_int

    if sum_i == 0:
        return "0"

    res = ""
    while sum_i > 0:
        res += str(sum_i % 2)
        sum_i = sum_i // 2

    return res[::-1]
