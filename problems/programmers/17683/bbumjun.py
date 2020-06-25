import math


def pre(score):
    i = 0
    scoreLst = []
    while i < len(score):
        if i+1 < len(score) and score[i+1] == '#':
            scoreLst.append(score[i:i+2])
            i += 2
        else:
            scoreLst.append(score[i])
            i += 1
    return scoreLst


def solution(m, musicinfos):
    answer = ''
    songs = []
    for music in musicinfos:
        start, end, songName, score = music.split(',')
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        time = (h2-h1) * 60 + (m2-m1)
        scoreLst = pre(score)
        if time < len(scoreLst):
            scoreLst = scoreLst[:time]
        elif time > len(scoreLst):
            scoreLst *= math.ceil(time/len(scoreLst))
            if time % len(scoreLst) != 0:
                scoreLst = scoreLst[:-(len(scoreLst) - time % len(scoreLst))]
        songs.append((songName, scoreLst))
    melody = pre(m)
    candidates = []
    for songInfo in songs:
        song = songInfo[1]
        for i in range(len(song)):
            if song[i] == melody[-1]:
                if song[i-len(melody)+1:i+1] == melody:
                    candidates.append(songInfo)
                    break
    if len(candidates) == 0:
        return "(None)"
    answer = sorted(candidates, key=lambda item: len(
        item[1]), reverse=True)[0][0]
    return answer
