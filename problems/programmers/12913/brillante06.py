def solution(land):
    answer = 0
    rst = [[0] * 4 for _ in range(len(land))]
    for i in range(1):
        rst[i] = land[i]
    for i in range(1, len(land)):
        rst[i][0] = land[i][0] + max(rst[i-1][1], rst[i-1][2], rst[i-1][3])
        rst[i][1] = land[i][1] + max(rst[i-1][0], rst[i-1][2], rst[i-1][3])
        rst[i][2] = land[i][2] + max(rst[i-1][0], rst[i-1][1], rst[i-1][3])
        rst[i][3] = land[i][3] + max(rst[i-1][0], rst[i-1][1], rst[i-1][2])
    answer = max(rst[len(land)-1])
    return answer
