# 724. Find Pivot Index


# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the
# left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because
# there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.


def solution(nums):
    cur = 0
    print({"nums": nums, "cur": cur})
    if sum(nums[cur + 1 :]) == 0:
        return cur
    while cur < len(nums) - 2:
        cur += 1
        if sum(nums[:cur]) == sum(nums[cur + 1 :]):
            return cur
        print({"cur": cur})
    if sum(nums[: len(nums) - 1]) == 0:
        cur = len(nums) - 1
        while nums[cur] == 0 and nums[cur - 1] == 0:
            cur -= 1
        return cur
    return -1
