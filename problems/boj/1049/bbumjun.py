# 1 <= N <= 100 , 1 <= M <= 50 , 0<= price <= 1000
import math
n, m = map(int, input().split())
package = []
piece = []
answer = 0
for i in range(m):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)
cheapest_package = sorted(package)[0]
cheapest_piece = sorted(piece)[0]
if cheapest_piece * 6 <= cheapest_package:
    answer = cheapest_piece * n
elif cheapest_piece * (n % 6) > cheapest_package:
    answer = cheapest_package * math.ceil(n/6)
else:
    answer = cheapest_package * (n//6) + cheapest_piece * (n % 6)
print(answer)
