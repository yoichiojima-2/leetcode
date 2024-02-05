def solution(nums: list[int]) -> int:
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    majority_count = 0 
    for key, val in count.items():
        if val > majority_count:
            majority_name = key
            majority_count = val
    
    return majority_name


res = solution([2,2,1,1,1,2,2])
print(res)