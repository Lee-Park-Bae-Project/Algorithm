def solution(land):
    answer = 0
    dp = [land[0]]

    for i in range(1, len(land)):
        temp = []
        temp.append(max([dp[i-1][1], dp[i-1][2], dp[i-1][3]])+land[i][0])
        temp.append(max([dp[i-1][0], dp[i-1][2], dp[i-1][3]])+land[i][1])
        temp.append(max([dp[i-1][0], dp[i-1][1], dp[i-1][3]])+land[i][2])
        temp.append(max([dp[i-1][0], dp[i-1][1], dp[i-1][2]])+land[i][3])
        dp.append(temp)
    answer = max(dp[len(land)-1])
    return answer
