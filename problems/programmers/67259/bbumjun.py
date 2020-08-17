import queue


def isRange(r, c, n):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    return True


def solution(board):
    answer = 9999999999
    n = len(board)
    q = queue.Queue()
    q.put((0, 0, (0, 0), 0))
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    isVisit = [[9999999999 for __ in range(
        len(board))] for _ in range(len(board))]
    while q.empty() == False:
        r, c, d, cost = q.get()
        if r == n-1 and c == n-1:
            if answer > cost:
                answer = cost
        for dirr in dirs:
            tr, tc = r+dirr[0], c+dirr[1]
            if isRange(tr, tc, n) == False or board[tr][tc] == 1:
                continue
            if d != (0, 0) and d != dirr:
                if isVisit[tr][tc] < cost+600:
                    continue
                isVisit[tr][tc] = cost+600
                q.put((tr, tc, dirr, cost+600))
            else:
                if isVisit[tr][tc] < cost+100:
                    continue
                isVisit[tr][tc] = cost+100
                q.put((tr, tc, dirr, cost+100))

    return answer
