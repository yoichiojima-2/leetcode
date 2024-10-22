class Solution:
    def climbStairs(self, n: int) -> int:
        # return simpler_solution(n)
        return optimized_solution(n)


def optimized_solution(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def simpler_solution(n):
    if n == 0 or n == 1:
        return 1
    else:
        return simpler_solution(n - 1) + simpler_solution(n - 2)
