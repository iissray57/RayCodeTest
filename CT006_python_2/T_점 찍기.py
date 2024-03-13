# 컨셉
# 2중 for문에서 곱한 값을 d와 비교
# d^2 = 
import math
def dot (k, d) :
    dotCnt = 0
    for x in range(0,d+1) :
        for y in range(0,d+1) :
            print(math.sqrt((k*x)**2 + (k*y)**2))
            if math.sqrt((k*x)**2 + (k*y)**2) < d :
                dotCnt += 1
    return dotCnt

# 시간 초과로 1 회탐색하는 방법으로 수정
# D^2 = X^2 + Y^2
# x가 2일때 가능한 Y의 값을 실수로 계산해서 몫을 구한다.
def dotDot (k, d) :
    dotCnt = 0

    for x in range(0, d + 1, k):
        y = math.floor(math.sqrt(d*d - x*x))
        dotCnt += (y // k) + 1
    return dotCnt

print(dotDot(2,4))