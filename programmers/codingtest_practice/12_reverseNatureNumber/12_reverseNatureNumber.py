def solution(n):
    answer = list(str(n))
    answer.reverse()
    return [int(i) for i in answer]
  
print(solution(12345))
