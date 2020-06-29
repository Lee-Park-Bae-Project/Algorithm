tc = int(input())
for i in range(tc):
    sounds = input().split()
    barkTypes = []
    ans = []
    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        barkTypes.append(s.split()[2])
    for sound in sounds:
        if sound not in barkTypes:
            ans.append(sound)
    print(' '.join(ans))
