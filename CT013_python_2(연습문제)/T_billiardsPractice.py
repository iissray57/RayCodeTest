def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls :
        vX = 0
        vY = 0
        if startX != ball[0] :
            if startY > n/2 :
                vY = n + (n-startY)
            else :
                vY = 0 - startY
            vX = startX
        elif startY != ball[1] :
            if startX > m/2 :
                vX = m + (m-startX)
            else :
                vX = 0 - startX
            vY = startY
        a = vX - ball[0]
        b = vY - ball[1]
        print(a, " - ", b,  "  ",vX , " - ", ball[0],  "  ",vY, " - ", ball[1])

        answer.append(a*a + b*b)
    
    return answer

print(solution(5,5,1,2,[[3, 4], [1, 3], [2, 2]]))