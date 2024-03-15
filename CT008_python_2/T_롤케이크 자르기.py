#concept
# 자른 시점에서 토핑의 갯수가 같은지 확인.
# List에서 인덱스 단위로 자르는게 가능 => 중복제거 => 갯수확인
# 만약 같다면 Case 증가 Return
def solution(topping):
    answer = 0
    for i in range(1,len(topping)) :
        if len(set(topping[0:i])) == len(set(topping[i:])):
            answer += 1

    return answer

# 케이스 20개 중 2개 통과 시간 초과.
# 리스트를 그룹화 하는 함수를 활용
# 다음에 다시 풀게요

from collections import Counter
 
def solution(topping):
    answer = 0
    toppingGroup = Counter(topping)         
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))