orig = input()
comp = input()
i, temp, c, start = 0, 0, '', -1
lst = []
while i < len(orig):
    lst.append(orig[i])
    temp += 1
    i += 1
    if temp >= len(comp):
        m = len(comp)-1
        for t in range(temp-1, temp-len(comp)-1, -1):
            if comp[m] != lst[t]:
                break
            m -= 1
        else:
            z = 0
            while z < len(comp):
                lst.pop()
                z += 1
                temp -= 1
if len(lst) == 0:
    print("FRULA")
else:
    print(''.join(lst))
