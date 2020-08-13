from collections import defaultdict


def solution(gems):

    gemTypes = set(gems)
    gemTypesLen = len(gemTypes)
    gemDict = defaultdict(lambda: 0)
    start, end = 0, 0
    candidates = []
    while True:
        curTypes = len(gemDict)
        if start == len(gems):
            break
        if curTypes == gemTypesLen:
            candidates.append((end-start, start, end))
            gemDict[gems[start]] -= 1
            if gemDict[gems[start]] == 0:
                del gemDict[gems[start]]
            start += 1
            continue
        if end == len(gems):
            break
        gemDict[gems[end]] += 1
        end += 1
    a, b, c = sorted(candidates)[0]
    return [b+1, c]


print(solution(["DIA", "RUBY", "RUBY", "DIA",
                "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
