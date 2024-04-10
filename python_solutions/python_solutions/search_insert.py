def searchInsert(nums: list[int], target: int) -> int:
    for idx, num in enumerate(nums):
        if num >= target:
            return idx
    return len(nums)


def test_searchInsert():
    assert searchInsert([1, 3, 5, 6], 5) == 2
