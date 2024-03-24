## Conept
## 1단계 올라가면 N이 N/2로 줄어드는 것을 생각
## 몫을 계산하는 방법을 생각
def solution(n,a,b):
    answer = 1

    while True:
        a = (a + 1) // 2
        b = (b + 1) // 2
        print("a = ",a)
        print("b = ",b)
        if a == b:
            return answer

        answer += 1

print(solution(8,4,7))