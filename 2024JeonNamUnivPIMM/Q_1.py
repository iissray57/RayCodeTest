def solution(M):
    return (M * 0.5) if M <= 30 else 15 + (M - 30) * 1.5

for i in range(0,60) :
    print(solution(i))