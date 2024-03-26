## Concept
## 다리위에 트럭 ㅣ올라갈 수 있는수가 다리의 길이와같음 문제를 좌표식으로 보면
## 트럭 한대가 2의 길이의 다리를 완전히 지나는데 걸리는시간은 3임.
## 큐에 트럭을 넣고 무게 합산을 확인. 초과 되었다면 큐의 합계를 확인하며 다음 타임을 지속적으로 확인
## 다리의 길이와 큐의 길이를 항상 확인.
## 큐로 하려 하였으나 현재 다리 위의 트럭의 위치를 알아야 할 필요가 있음.
## 딕셔너리로 변경
## 딕셔너리 사용시 고유 Key가 필요한데 이때 키중복 발생 문제가 있을 수 있음
## 길이가 2인 데이터 큐로 방향 변경
def solution(bridge_length, weight, truck_weights):
    answer = 0
    curentSituation = []

    while len(truck_weights) != 0 or len(curentSituation) != 0 :
        for item in curentSituation :
            item[1] -= 1        
        for item in curentSituation :
            if item[1] == 0 :
                curentSituation.pop(0)
        sumOfWeight = sum(row[0] for row in curentSituation)
        if len(truck_weights) > 0:
            if  sumOfWeight + truck_weights[0] <= weight:
                curentSituation.append([truck_weights[0], bridge_length])
                truck_weights.pop(0)
        print(curentSituation)
        answer += 1
    return answer

print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# 테스트 1 〉	통과 (2.18ms, 10.2MB)
# 테스트 2 〉	통과 (31.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.16ms, 10.1MB)
# 테스트 4 〉	통과 (109.35ms, 10.2MB)
# 테스트 5 〉	통과 (782.46ms, 10.2MB)
# 테스트 6 〉	통과 (404.18ms, 10.3MB)
# 테스트 7 〉	통과 (1.55ms, 10.2MB)
# 테스트 8 〉	통과 (0.36ms, 10.2MB)
# 테스트 9 〉	통과 (10.11ms, 10.3MB)
# 테스트 10 〉	통과 (0.37ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.56ms, 10.1MB)
# 테스트 13 〉	통과 (2.99ms, 10.2MB)
# 테스트 14 〉	통과 (0.07ms, 10.3MB)