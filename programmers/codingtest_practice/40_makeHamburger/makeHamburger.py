def solution(ingredient):
    answer = 0
    str_match = '1231'
    str_ingre = ''.join([str(x) for x in ingredient])
    
    idx = str_ingre.find(str_match)
    while(idx > -1):
        idx = str_ingre.find(str_match)
        answer=answer+1
        str_ingre = str_ingre[0:idx-1] + str_ingre[idx+5:len(str_ingre)]
    return answer
  
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
