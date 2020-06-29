croatiaC = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
ans = 0
for c in croatiaC:
    ans += s.count(c)
    s = s.replace(c, ' ')
s = s.replace(' ', '')
print(ans + len(s))
