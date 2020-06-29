def rep(q):
    q = q.replace("C#", "T")
    q = q.replace("D#", "V")
    q = q.replace("F#", "X")
    q = q.replace("G#", "Z")
    q = q.replace("A#", "R")
    return q


def solution(m, musicinfos):
    cor = None
    m = rep(m)
    lst = {}
    for i, val in enumerate(musicinfos):
        arr = val.split(',')
        t1 = arr[0].split(':')
        t2 = arr[1].split(':')
        music_time = (int(t2[0])-int(t1[0]))*60+int(t2[1])-int(t1[1])
        music_name = arr[2]
        code = []
        comp = []
        music_code = rep(arr[3])
        music_code = music_code * \
            (music_time//len(music_code)) + \
            music_code[0:music_time % len(music_code)]
        lst[music_code] = music_name
    for q in lst.keys():
        if m in q:
            # print("?")
            if cor == None:
                cor = q
            else:
                if len(cor) < len(q):
                    cor = q

    if cor != None:
        return lst[cor]
    else:
        return "(None)"
