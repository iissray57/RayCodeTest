# Concept
# 원하는 목록이 Discount와 각각 매칭해서 WantList의 항목을 제거.
# 만약 10일이 초과하는 경우 
from collections import Counter

def solution(want, number, discount):
    discountGroup = Counter(discount)
    answer = 0

    for i in range(len(want)) :
        if discountGroup[want[i]] < number[i] :
            return answer
    
    for i in range(len(discount)) :
        answer = 0
        if(i+11 > len(discount)) :
            return answer
        if discount[i] in want :
            discountGroup = Counter(discount[i:i+10])
            for j in range(len(want)) :
                if discountGroup[want[j]] < number[j] :
                    answer += 1
                    break
            if answer == 0 :
                return i + 1

# 어떤케이스에서 불가능한지 찾지 못함..
# 어쩔 수 없이 다른사람 풀이 참고.