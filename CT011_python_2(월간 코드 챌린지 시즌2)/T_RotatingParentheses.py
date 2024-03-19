from collections import deque

## Concept
# 스트링을 덱으로 변환하여 하나씩 뒤로 옮겨가며 점검
# 페어를 찾는 식으로 값을 치환하는 것을 고려했으나 리스트 순환을 많이 해야함.
# 괄호가 열렸을때를 1 닫혔을때를 -1로 연산하는 방법을 선정
def solution3(s):
    answer = 0
    myQ = deque(s)
    for i in range(0,len(myQ)) :
        checkValue = 0
        for item in myQ :
            if (item == "[" or item == "{" or item == "(") :
                checkValue += 1
            else :
                checkValue -= 1
            if checkValue < 0 :
                break
                
        if checkValue == 0 :
            answer += 1

        myQ.append(myQ.popleft())       
        print(myQ)
    return answer

# 몇가지 케이스는 통과하였으나
# 양쪽 페어가 맞지 않은경우에도 0으로 연산되는 케이스가 발생.
# "[)(]" == 0
# 각각 괄호들에 고유값이 필요할것으로 생각이 됨.
def solution2(s):
    answer = 0
    myQ = deque(s)
    for i in range(0,len(myQ)) :
        checkValue = 0
        for item in myQ :
            if (item == "[" ) :
                checkValue += 1
            if (item == "{") :
                checkValue += 2
            if (item == "(") :
                checkValue += 3
            if (item == "]" ) :
                checkValue -= 1
            if (item == "}") :
                checkValue -= 2
            if (item == ")") :
                checkValue -= 3
            if checkValue < 0 :
                break                
        if checkValue == 0 :
            answer += 1

        myQ.append(myQ.popleft())       
        print(myQ)
    return answer

# 이렇게 고유값을 부여하는 경우 루프도 이상해지고 좀 무식한 방법인거 같아
# 역방향이 나왔을 때 이전 값이 페어인지 확인하는 방법을 선택
# 열리는 방향이면 누적으로 스택으로 저장
# 역방향이 나왔을 때 이전에 넣은 괄호와 같은 페어의 괄호인지 확인
def check(sList):
    stack = []
    for s in sList:
        if s in ('[', '(', '{'):
            stack.append(s)
        else:
            if not stack: return False
            x = stack.pop()
            if s == ']' and x != '[':
                return False
            elif s == ')' and x != '(':
                return False
            elif s == '}' and x != '{':
                return False
    if stack: return False
    return True


def solution(s):
    answer = 0
    myQ = deque(s)
    for i in range(len(s)):
        if check(myQ):
            answer +=1
        myQ.append(myQ.popleft())   
    return answer

print(solution("[()]"))