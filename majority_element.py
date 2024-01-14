def solution(nums: list[int]) -> int:
    elem_cnt = {}
    for i in nums:
        if i in elem_cnt:
            elem_cnt[i] += 1
        else:
            elem_cnt[i] = 0

    most_appeared_cnt = 0
    for num, count in elem_cnt.items():
        if count > most_appeared_cnt:
            most_appeared_key = num
    print(most_appeared_cnt, most_appeared_key)
    return most_appeared_key

def test_solution():
    assert solution([3,2,3]) == 3
    assert solution([2,2,1,1,1,2,2]) == 2

test_solution()