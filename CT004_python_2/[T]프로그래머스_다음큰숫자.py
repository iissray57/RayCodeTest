def solution(n) :
    targetOneCnt = countOne(bin(n))
    while n > 0 :
        n += 1
        if(countOne(bin(n)) == targetOneCnt):
            print(n)
            return n

def countOne(binN):
    count = 0
    for digit in binN:
        if digit == '1':
            count += 1
    return count
        
solution(78)
