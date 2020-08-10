def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        dic.setdefault(genres[i], {})
        dic[genres[i]].setdefault('count', 0)
        dic[genres[i]].setdefault('songs', [])
        dic[genres[i]]['count'] += plays[i]
        dic[genres[i]]['songs'].append((i, plays[i]))

    lst = sorted(dic.items(), key=lambda item: item[1]['count'], reverse=True)
    for album in lst:
        songList = sorted(album[1]['songs'],
                          key=lambda item: item[1], reverse=True)
        for i in range(len(songList)):
            if i >= 2:
                break
            answer.append(songList[i][0])

    return answer
