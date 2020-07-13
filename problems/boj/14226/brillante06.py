s = int(input())
lst, ans = 0, 2000
q = [(1, 0, 0)]
flag = [[False]*(2001) for _ in range(2001)]
flag[1][0] = True
while q:
    cur, m, clip = q.pop(0)

    if cur == s:
        ans = m
        break
    for i in range(3):
        if cur > 0 and cur < 2001 and i == 0 and flag[cur][cur] is False:
            q.append((cur, m+1, cur))
            flag[cur][cur] = True
        elif i == 1:
            if cur > 0 and cur+clip < 2001 and flag[clip+cur][clip] is False:
                flag[clip+cur][clip] = True
                q.append((clip+cur, m+1, clip))
        elif i == 2:
            if cur-1 > 0 and cur < 2001 and flag[cur-1][clip] is False:
                q.append((cur-1, m+1, clip))
                flag[cur-1][clip] = True

print(ans)
