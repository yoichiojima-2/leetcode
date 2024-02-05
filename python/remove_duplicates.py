def solution(nums: list[int]):
    cur = 0
    for i in range(len(nums)):
        if nums[cur] != nums[i]:
            cur += 1
            nums[cur] = nums[i]
    return cur

nums = [0,0,1,1,1,2,2,3,3,4]
index = solution(nums)
print(nums, index)