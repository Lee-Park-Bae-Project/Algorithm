docs = input()
target = input()
answer = 0
while len(docs) >= len(target):
    if docs.find(target) == -1:
        break
    answer += 1
    idx = docs.find(target)
    docs = docs[idx+len(target):]
print(answer)
