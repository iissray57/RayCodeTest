# 컨셉
def FibonacciNumbers (n) :
    number = 0
    if(n == 1) :
        return 1
    elif(n >= 2) :
        number = FibonacciNumbers(n-1) + FibonacciNumbers(n-2)
    return number

# 코드 정리
def FibonacciNumbers2 (n) :
    return 1 if n == 1 else sum(FibonacciNumbers(n-x) for x in range(1,3))\
    
################ RunTime 에러 발생.
# 재귀 호출 제한
def FibonacciNumbers3(n, stack={}):
    if n in stack:
        return stack[n]
    if n <= 2:
        return 1
    stack[n] = FibonacciNumbers3(n-1, stack) + FibonacciNumbers3(n-2, stack)
    return stack[n]

# 절반은 성공 절반은 런타임에러로 실패
######### 힌트참고.. :(
def solution(n):
    FibonacciArray = [0 for c in range(n+1)]
    FibonacciArray[1] = 1
    for i in range(2, n+1):
        FibonacciArray[i] = (FibonacciArray[i-1] + FibonacciArray[i-2]) % 1234567
    return FibonacciArray[i]

solution(5)