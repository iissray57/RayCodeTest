def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer 

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))

#1, 2, 3, 4
#      3, 4, 5, 6, 7
#         4, 5
#         4, 5, 6, 7, 8
#            5, 6, 7, 8, 9, 10, 11, 12
#                               11, 12, 13
#                           10, 11, 12 ,13, 14