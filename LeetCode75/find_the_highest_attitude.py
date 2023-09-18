# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude
# between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.


def solution(gain):
    idx = 0
    attitude = gain[0]
    max_attitude = gain[0]
    print({"attitude": attitude, "max_attitude": max_attitude})
    for i in gain[1:]:
        idx += 1
        attitude += i
        max_attitude = max(attitude, max_attitude)
        print(
            {"idx": idx, "gain": i, "attitude": attitude, "max_attitude": max_attitude}
        )
    return max_attitude


testcases = [[-5, 1, 5, 0, -7], [-4, -3, -2, -1, 4, 3, 2]]

results = []
for i in testcases:
    res = {}
    res["testcase"] = i
    res["output"] = solution(i)
    results.append(res)

print(results)
