def solution(nums1, nums2):
    print({"nums1": nums1, "nums2": nums2})
    answer1 = {i for i in nums1 if i not in nums2}
    answer2 = {i for i in nums2 if i not in nums1}
    return list(answer1), list(answer2)


testcases = [([1, 2, 3], [2, 4, 6]), ([1, 2, 3, 3], [1, 1, 2, 2])]

for i in testcases:
    result = {}
    result["input"] = i
    result["output"] = solution(i[0], i[1])
    print(result)
