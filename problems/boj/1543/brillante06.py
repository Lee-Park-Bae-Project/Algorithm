from sys import stdin
# 1543
strVal = input()
findVal = input()
# print(findVal,strVal)
i, start, res = 0, 0, 0
while i <= len(strVal)-len(findVal):
    if strVal[i:i+len(findVal)] == findVal:
        res += 1
        i += len(findVal)
    else:
        i += 1
print(res)
