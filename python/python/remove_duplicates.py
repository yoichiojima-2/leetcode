def solution(nums: list[int]):
    cur = 0
    for i in range(len(nums)):
        if nums[cur] != nums[i]:
            cur += 1
            nums[cur] = nums[i]
    return cur