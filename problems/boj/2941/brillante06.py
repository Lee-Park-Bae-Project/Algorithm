t = input()
i, ans = 0, 0
dic = {}
dic['c='], dic['c-'], dic['dz='], dic['d-'], dic['lj'], dic['nj'], dic['s='], dic['z='] = 1, 1, 1, 1, 1, 1, 1, 1

while len(t) > i:
    if t[i:i+2] in dic:
        ans += 1
        i += 2
    else:
        if t[i:i+2] == 'dz' and t[i:i+3] == 'dz=':
            i += 3
            ans += 1
        else:
            dic[t[i:i+1]] = 1
            ans += 1
            i += 1

print(ans)
