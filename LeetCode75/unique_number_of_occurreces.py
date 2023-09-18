def solution(arr):
    count = {}
    print({"arr": arr})
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        print({"count": count, "num": num})
    occurences = set(count.values())
    return len(count) == len(occurences)


testcases = [
    [1, 2, 2, 1, 1, 3],
    [1, 2],
    [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
    [1, 2, 2, 1, 1, 3],
]

for i in testcases:
    result = {}
    result["testcase"] = i
    result["output"] = solution(i)
    print(result)
