def solution(n):
    answer, x = -1, 1
    
    while (x ** 2) <= n:
        if (x ** 2) == n: answer = (x+1)**2
        x+=1
    return answer
  
print(solution(121))
print(solution(3))
