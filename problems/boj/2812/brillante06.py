n, k = map(int, (input().split()))
num = list(map(int, list(input())))
top, lst, temp, res = 0, [], k, ''
for i in range(n):
    while temp > 0 and len(lst) > 0 and lst[len(lst)-1] < num[i]:
        lst.pop()
        temp -= 1
    lst.append(num[i])
for i in range(0, len(lst)):
    res += str(lst[i])
print(int(res[:(n-k)]))
