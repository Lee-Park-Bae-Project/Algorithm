s = list(input())
bomb = input()
i = 0
stack = []
for c in s:
    stack.append(c)
    if stack[-len(bomb):] == list(bomb):
        for i in range(len(bomb)):
            stack.pop()
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
