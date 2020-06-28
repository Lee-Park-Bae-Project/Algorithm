n, m = map(int, input().split())
num = list(map(int, list(input())))
ascending = sorted(num)

for i in range(m):
    num[num.index(ascending[i])] = -1

answer = ''
for n in num:
    if n != -1:
        answer += str(n)
print(answer)
