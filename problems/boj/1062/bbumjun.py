from itertools import combinations
import sys
n, k = map(int, input().split())
words = []
defaultC = set(['a', 'c', 'i', 'n', 't'])
for i in range(n):
    string = list(input()[4:-4])
    word = set([])
    for c in string:
        if c not in defaultC:
            word.add(c)
    words.append(word)
if k < 5:
    print(0)
    sys.exit()
words.sort(key=lambda words: len(words))
candidates = set([])
for word in words:
    for c in word:
        candidates.add(c)
cb = combinations(candidates, k-5 if k-5 <
                  len(candidates) else len(candidates))
ans = 0
for x in cb:
    res = 0
    for word in words:
        for c in word:
            if c not in x:
                break
        else:
            res += 1
    if res > ans:
        ans = res
print(ans)
