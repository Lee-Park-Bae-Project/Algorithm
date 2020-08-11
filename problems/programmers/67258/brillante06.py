from collections import defaultdict


def solution(gems):
    answer, minVal, dic = [1, len(gems)], len(gems)-1, defaultdict(int)
    start, end, leng, gemLength = 0, 0, len(set(gems)), len(gems)
    dic[gems[0]] = 1
    while start < gemLength and end < gemLength:
        if len(dic) == leng:
            if (end-start) < answer[1]-answer[0]:
                answer = [start+1, end+1]
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            dic[gems[end]] += 1

    return answer
