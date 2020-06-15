from sys import stdin

# def binar(lst,op):
#     idx=len(lst)
#     if idx%2==1:
#         idx+=1
#     while True:

#         for a in range(idx):
#             if lst[a]==op:


while True:
    a, b = stdin.readline().split()
    a = int(a); b = int(b)
    if a + b == 0:
        break
    print(a + b)

                

