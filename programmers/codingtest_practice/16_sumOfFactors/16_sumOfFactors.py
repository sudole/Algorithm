def solution(n):
    return sum([n/x if n % x == 0 else 0 for x in range(1, n+1)])
  
print(solution(12))
print(solution(5))
