import sys
from itertools import accumulate
ip = sys.stdin.readline
pt = sys.stdout.write
n,q = map(int, ip().split())
arr = list(map(int, input().split()))
acc = list(accumulate(arr, initial=0))
shift = 0
for _ in range(q):
    query = list(map(int,ip().split()))
    if query[0] == 1 :
        shift = (shift - query[1])%n
    elif query[0] == 2 :
        shift = (shift + query[1])%n
    elif query[0] == 3 :
        a = query[1]-1
        b = query[2]-1
        a = (a + shift) % n
        b = (b + shift) % n
        if a <= b:
            pt(str(acc[b + 1] - acc[a]) + "\n")
        else:
            pt(str(acc[n] - acc[a] + acc[b + 1]) + "\n")