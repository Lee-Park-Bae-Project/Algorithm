def solution(triangle):
    answer = 0

    memo = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        memo.append([])
        for j in range(len(triangle[i])):
            if j == 0:
                memo[i].append(triangle[i][j]+memo[i-1][j])
            elif j == len(triangle[i])-1:
                memo[i].append(triangle[i][j]+memo[i-1][j-1])
            else:
                x = max([memo[i-1][j-1], memo[i-1][j]])
                memo[i].append(triangle[i][j] + x)
    answer = max(memo[len(triangle)-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
