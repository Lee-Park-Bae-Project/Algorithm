def solution(n, results):
    answer = 0
    val = [[False] * (n+1) for _ in range(n+1)]
    res = []
    for t in results:
        val[t[0]][t[1]] = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if val[j][i] and val[i][k]:
                    val[j][k] = True
    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            if val[i][j] or val[j][i]:
                tmp += 1
        if tmp == n-1:
            answer += 1

    return answer
