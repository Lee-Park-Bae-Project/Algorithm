n = int(input())
dic = {}
ans = ''
for i in range(n):
    password = input()
    if password[::-1] in dic:
        ans = password
        break
    else:
        k = password[len(password)//2+1:]
        if k[::-1] == password[0:len(password)//2]:
            ans = password
            break
        dic[password] = 1
print(len(ans), password[len(ans)//2])
