def solution(s: str) -> int:
    first_word_found = False
    count = 0
    for i in s[::-1]:
        if first_word_found:
            if i != " ":
                count += 1
            else:
                return count
        elif i != " ":
            first_word_found = True
            count += 1
    return count