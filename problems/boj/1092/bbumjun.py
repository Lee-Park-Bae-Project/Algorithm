n = int(input())
ships = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)
answer = 0
if ships[0] < boxes[0]:
    answer = -1
else:
    while len(boxes) >= 1:
        for ship in ships:
            i = 0
            while i < len(boxes):
                if ship >= boxes[i]:
                    boxes.pop(i)
                    break
                i += 1
        answer += 1
print(answer)
