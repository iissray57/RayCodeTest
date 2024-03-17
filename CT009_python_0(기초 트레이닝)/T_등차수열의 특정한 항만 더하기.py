def solution(a, d, included):
    answer = 0
    for i in range(0, len(included)) :
        if (included[i]) :
            answer += a + d*i
    return answer

print(solution(3,4,[True, False, False, True, True]))

