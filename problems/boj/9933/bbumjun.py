n = int(input())
words = []
for i in range(n):
    words.append(list(input()))
for word in words:
    rev = word[:]
    rev.reverse()
    if rev in words:
        print(len(word), word[len(word)//2])
        break
