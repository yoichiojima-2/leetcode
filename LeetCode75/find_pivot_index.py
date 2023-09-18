# 724. Find Pivot Index


# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the
# left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because
# there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.


def solution(nums):
    cur = 0

    if sum(nums[cur + 1 :]) == 0:
        return cur

    if sum(nums[: len(nums) - 1]) == 0:
        return len(nums) - 1

    print({"nums": nums, "cur": cur})

    while cur < len(nums) - 2:
        cur += 1
        if sum(nums[:cur]) == sum(nums[cur + 1 :]):
            return cur

        print({"cur": cur})

    return -1


testcases = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [2, 1, -1], [-1, -1, 1, 1, 0, 0]]

for i in testcases:
    result = {}
    result["input"] = i
    result["output"] = solution(i)
    print(result, "\n")
