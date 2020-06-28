n = int(input())
expect = []
for i in range(n):
    expect.append(int(input()))
expect.sort()
answer = 0
for i in range(len(expect)):
    answer += abs(expect[i] - (i+1))
print(answer)
