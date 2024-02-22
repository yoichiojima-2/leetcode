# Given an array of integers arr, return true if the number of occurrences
# of each value in the array is unique or false otherwise.


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