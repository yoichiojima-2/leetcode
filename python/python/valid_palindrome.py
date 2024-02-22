import re

def solution(s: str) -> bool:
    if match := re.findall(r"[A-Za-z0-9]", s):
        chars = "".join(match).lower()
    else:
        return True

    if len(chars) <= 3:
        return chars == chars[::-1]

    a = chars[:len(chars) // 2]
    b = chars[(len(chars) // 2):]

    if len(a) != len(b):
        b = b[1:]

    return a == b[::-1]

