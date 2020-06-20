def dfs(i, j):
    global ans, check
    if j == c-1:
        ans += 1
        check = True
        return

    flag[i][j] = True
    for m in range(3):
        if i+dX[m] >= 0 and j+1 <= c-1 and i+dX[m] < r and bake[i+dX[m]][j+1] == '.' and flag[i+dX[m]][j+1] == False:

            dfs(i+dX[m], j+1)
            if check:
                return


r, c = map(int, input().split())
bake = [list(map(str, list(input()))) for _ in range(r)]
flag = [[False]*(c+2) for _ in range(r+2)]
dX, ans = [-1, 0, 1], 0
for i in range(r):
    if bake[i][0] == '.':
        flag[i][0] = True
        check = False
        dfs(i, 0)

print(ans)
