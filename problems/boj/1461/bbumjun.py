n, m = map(int, input().split())
pos = sorted(map(int, input().split()))
answer = 0


def calRight(books):
    res = 0
    pick = []
    while len(books) > 0:
        pick = books[-m:]
        books = books[:-m]
        res += abs(pick[-1]) * 2
    return res


def calLeft(books):
    res = 0
    pick = []
    while len(books) > 0:
        pick = books[:m]
        books = books[m:]
        res += abs(pick[0]) * 2
    return res


if pos[0] > 0 and pos[-1] > 0:
    answer = calRight(pos)
elif pos[0] < 0 and pos[-1] < 0:
    answer = calLeft(pos)
else:
    for i in range(len(pos)):
        if pos[i] < 0 and pos[i+1] > 0:
            answer = calLeft(pos[:i+1]) + calRight(pos[i+1:])
answer -= abs(pos[0]) if abs(pos[0]) > abs(pos[-1]) else abs(pos[-1])
print(answer)
