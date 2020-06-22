n, l = map(int, input().split())
holes = sorted(map(int, input().split()))
answer = 0
tape = -1001
for hole in holes:
    if tape + l < hole + 0.5:
        answer += 1
        tape = hole - 0.5

print(answer)
