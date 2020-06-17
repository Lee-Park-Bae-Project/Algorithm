# 1080
n, m = map(int, input().split())
cnt = 0
normal = [list(map(int, list(input()))) for _ in range(n)]
comp = [list(map(int, list(input()))) for _ in range(n)]


def change(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            if normal[i][j] == 1:
                normal[i][j] = 0
            else:
                normal[i][j] = 1


for i in range(0, n-2):
    for j in range(0, m-2):
        if normal[i][j] != comp[i][j]:
            change(i, j)
            cnt += 1

print(normal, comp)

for i in range(0, n):
    for j in range(0, m):
        if normal[i][j] != comp[i][j]:
            cnt = -1
            break
print(cnt)
