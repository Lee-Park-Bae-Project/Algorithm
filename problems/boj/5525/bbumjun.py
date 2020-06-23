n = int(input())
m = int(input())
s = input()
p = []
continuous = 0
for i in range(len(s)):
    if s[i] == 'I':
        if s[i-2:i+1] == 'IOI':
            continuous += 1
        else:
            if continuous != 0:
                p.append(continuous)
            continuous = 0
if continuous != 0:
    p.append(continuous)
ans = 0
for x in p:
    if x >= n:
        ans += x-n + 1
print(ans)
