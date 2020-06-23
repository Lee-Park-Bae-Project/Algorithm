r_size, c_size = map(int, input().split())
field = [list(input()) for i in range(r_size)]
answer = 0


def isRange(a, b):
    global r_size, c_size
    if a < 0 or a >= r_size or b < 0 or b >= c_size:
        return False
    return True


dirs = [(-1, 1), (0, 1), (1, 1)]


def dfs(a, b):
    global field, r_size, c_size, answer, dirs
    stack = [(a, b)]
    while len(stack) != 0:
        r, c, = stack[-1]
        if c == c_size-1:
            answer += 1
            return
        field[r][c] = 'x'
        for dir in dirs:
            tr, tc = (r+dir[0], c+dir[1])
            if isRange(tr, tc) is True and field[tr][tc] == '.':
                stack.append((tr, tc))
                break
        else:
            stack.pop()


for i in range(r_size):
    dfs(i, 0)
print(answer)
