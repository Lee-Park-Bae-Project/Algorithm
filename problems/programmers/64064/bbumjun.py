banLists = set([])


def dfs(idx, restIds, banned_id, selectedIds):
    global banLists
    candidates = []
    for id in restIds:
        if len(id) == len(banned_id[idx]):
            for i in range(len(id)):
                if id[i] != banned_id[idx][i] and banned_id[idx][i] != '*':
                    break
            else:
                candidates.append(id)
    if idx == len(banned_id)-1:
        for candidate in candidates:
            lst = selectedIds[:]
            lst.append(candidate)
            lst.sort()
            banLists.add(tuple(lst))
    else:
        for candidate in candidates:
            lst = selectedIds[:]
            lst.append(candidate)
            nextIds = list(filter(lambda item: item != candidate, restIds))
            dfs(idx+1, nextIds, banned_id, lst)


def solution(user_id, banned_id):
    dfs(0, user_id, banned_id, [])
    global banLists
    return len(banLists)
