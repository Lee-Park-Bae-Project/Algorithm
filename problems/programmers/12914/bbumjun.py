def solution(n):
    dp = [0, 1, 2]
    for i in range(3, n+1):
        dp.append(dp[i-2]+dp[i-1])
    return dp[n] % 1234567


print(solution(1))
