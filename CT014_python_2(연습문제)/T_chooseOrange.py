## Concept
## 주어진 오랜지들의 사이즈를 그룹별로 갯수를 확인
## 가장 수가 많은 순서대로 내림차순 정렬
## 그룹의 아이템 순서대로 하나씩 확인하며
## 총량에서 갯수를 줄여나감
## 이때마다 정답에 1씩 더하기.
from collections import Counter
def solution(k, tangerine):
    answer = 0
    sizeCount = Counter(tangerine).most_common()
    for size in sizeCount :
        if k > 0 :
            k -= size[1]
            answer += 1
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))