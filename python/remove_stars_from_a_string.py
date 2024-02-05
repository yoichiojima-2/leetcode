class Solution:
    def removeStars(self, s: str) -> str:
        print({"s": s})

        while s[0] == "*":
            s = s[1:]
            print({"message": "first letter is deleted", "s": s})

        cur = 0
        while cur < len(s) - 1 and len(s) > 0: # refering s[i + 1] in the loop
            print({"cur": cur, "s[cur]": s[cur]})
            if s[cur + 1] == "*": # look a letter a head
                s = s[:cur] + s[cur + 2:]
                cur -= 3
                print({"message": "s[cur + 1] == '*'", "s": s})

            print({"s": s, "message": "cursor is going to be increased"})
            cur += 1

        print({"message": "end of process", "s": s})
        return s

testcases = [
    "leet**cod*e",
    "***erase*****"
]

results = []
for i in testcases:
    res = Solution().removeStars(i)
    results.append({"input": i, "output": res})

from pprint import pprint
pprint(results)