from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step

# 테스트 1 〉	통과 (0.41ms, 10.2MB)
# 테스트 2 〉	통과 (6.68ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (11.06ms, 10.3MB)
# 테스트 5 〉	통과 (65.24ms, 10.3MB)
# 테스트 6 〉	통과 (17.40ms, 10.2MB)
# 테스트 7 〉	통과 (0.33ms, 10.3MB)
# 테스트 8 〉	통과 (0.12ms, 10.2MB)
# 테스트 9 〉	통과 (3.65ms, 10.4MB)
# 테스트 10 〉	통과 (0.09ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.4MB)
# 테스트 12 〉	통과 (0.29ms, 10.3MB)
# 테스트 13 〉	통과 (0.56ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)