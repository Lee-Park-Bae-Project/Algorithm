from collections import deque


def solution(board):
    answer = 100000000000
    n = len(board)
    res = deque()
    dX = [0, 1, 0, -1]
    dY = [1, 0, -1, 0]
    visited = [[100000000000] * len(board) for _ in range(len(board))]
    visited[0][0] = 0
    if board[0][1] != 1:
        res.append((0, 1, 1, 0, 0))
        visited[0][1] = 100
    if board[1][0] != 1:
        res.append((1, 0, 1, 0, 1))
        visited[1][0] = 100
    while res:
        t = res.popleft()
        price = t[2]*100+t[3]*500
        if t[0] == n-1 and t[1] == n-1:
            if answer > price:
                answer = price
        for i in range(0, 4):
            if 0 <= t[0]+dX[i] < n and 0 <= t[1]+dY[i] < n and visited[t[0]+dX[i]][t[1]+dY[i]] >= price:
                if board[t[0]+dX[i]][t[1]+dY[i]] == 0:
                    visited[t[0]+dX[i]][t[1]+dY[i]] = price
                    if i == t[4]:
                        res.append(
                            (t[0]+dX[i], t[1]+dY[i], t[2]+1, t[3], t[4]))
                    else:
                        res.append((t[0]+dX[i], t[1]+dY[i], t[2]+1, t[3]+1, i))
    return answer
