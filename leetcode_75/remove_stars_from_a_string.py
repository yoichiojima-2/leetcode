class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        for i in range(1, n):
            if s[i] == "*":
                s = s[: i - 1] + s[i + 1:]
                print(s)

testcases = [
    "leet**cod*e",
    "erase*****"
]

results = []
for i in testcases:
    res = Solution().removeStars(i)
    results.append({"input": i, "output": res})

print(results)