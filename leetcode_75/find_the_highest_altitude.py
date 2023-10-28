# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude
# between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.


def solution(gain):
    idx = 0
    altitude = 0
    max_altitude = 0
    print({"altitude": altitude, "max_altitude": max_altitude})
    for i in gain:
        idx += 1
        altitude += i
        max_altitude = max(altitude, max_altitude)
        print(
            {"idx": idx, "gain": i, "altitude": altitude, "max_altitude": max_altitude}
        )
    return max_altitude


testcases = [[-5, 1, 5, 0, -7], [0, -4, -3, -2, -1, 4, 3, 2]]

results = []
for i in testcases:
    res = {}
    res["testcase"] = i
    res["output"] = solution(i)
    results.append(res)

print(results)
