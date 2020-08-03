
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
def solution(cacheSize, cities):
    answer = 0
    lst={}
    cnt=0
    if cacheSize!=0:
        for a in range(0,len(cities)):
            cities[a]=cities[a].lower()
        for city in cities:
            if city in lst.keys():
                answer+=1
                lst[city]=cnt
                #print(city,answer)
            else:
                answer+=5
               # print(city,answer)
                if len(lst)>=cacheSize:
                    key_min=min(lst.keys(), key=(lambda k: lst[k]))
                   # print("delete?",key_min)
                    del lst[key_min]
                    lst[city]=cnt
                   # print(city," in ")
                    #print(lst)
                else:
                    lst[city]=cnt
            cnt+=1

    else :
        answer=len(cities)*5
