def solution(s: str) -> int:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    roman = 0
    for i in range(len(s)):
        if i < len(s) - 1 and symbols[s[i]] < symbols[s[i + 1]]:
            roman -= symbols[s[i]]
        else:
            roman += symbols[s[i]]
    return roman
