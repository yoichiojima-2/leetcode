def solution(strs: list[str]):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    min_len = len(min(strs, key = len))
    for i in range(min_len):
        for str_ in strs:
            if strs[0][i] != str_[i]:
                return strs[0][:i]
    return strs[0][:min_len]
