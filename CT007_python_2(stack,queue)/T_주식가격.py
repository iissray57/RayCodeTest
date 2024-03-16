def solution (prices) :
    N = len(prices)
    time = [0]*N
    for p in range(N) :
        for q in range(p+1 , N):
            if prices[q] >= prices[p] :
                time[p] += 1
    return(time)

print(solution([1, 2, 3, 2, 3]))