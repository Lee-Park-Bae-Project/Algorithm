def solution(genres, plays):
    answer = []
    playList = {}
    playTotal = {}
    q = 0
    for i, j in zip(genres, plays):
        if i not in playList.keys():
            playList[i] = {}
        playList[i][q] = j
        if i not in playTotal.keys():
            playTotal[i] = j
        else:
            playTotal[i] += j
        q += 1
    playTotal = sorted(playTotal.items(),
                       key=lambda item: item[1], reverse=True)
    for i in playList.keys():
        playList[i] = sorted(playList[i].items(),
                             key=lambda x: (x[1], -x[0]), reverse=True)
    for i in playTotal:
        for m, j in enumerate(playList[i[0]]):
            answer.append(j[0])
            if m == 1:
                break
    return answer
