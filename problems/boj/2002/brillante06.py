n = int(input())
before, after, answer = {}, [], 0

for i in range(n):
    t = input()
    before[t] = i
for i in range(n):
    t = input()
    after.append(t)

for i in range(n):
    for j in range(i+1, n):
        if before[after[i]] > before[after[j]]:
            answer += 1
            break

print(answer)
