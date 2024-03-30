def solution(numbers):
    answer = [-1] * len(numbers)                    
    for i, n in enumerate(numbers):                 
        for j in numbers[ i + 1 : len(numbers) ]:   
            if n < j:                               
                answer[i] = j                       
                break                               
    return answer                                   