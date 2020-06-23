r, c = map(int, input().split())
matrixA = []
matrixB = []
for i in range(r):
    line = input()
    row = []
    for j in range(c):
        row.append(int(line[j]))
    matrixA.append(row)
for i in range(r):
    line = input()
    row = []
    for j in range(c):
        row.append(int(line[j]))
    matrixB.append(row)


def flip(a, b):
    global matrixA
    for i in range(3):
        for j in range(3):
            matrixA[a+i][b+j] = 0 if matrixA[a+i][b+j] == 1 else 1


answer = 0
for i in range(r-2):
    for j in range(c-2):
        if matrixA[i][j] != matrixB[i][j]:
            answer += 1
            flip(i, j)
print(answer if matrixA == matrixB else -1)
