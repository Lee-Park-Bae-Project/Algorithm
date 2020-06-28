t = int(input())
while t != 0:
    walf = list(map(str, input().split()))
    inp = ''
    while True:
        inp = input()
        if inp == 'what does the fox say?':
            break
        animal = inp.split()
        for j in range(len(walf)):
            if walf[j] == animal[2]:
                walf[j] = -1
    for q in range(len(walf)):
        if walf[q] != -1:
            print(walf[q], end=' ')
    t -= 1
