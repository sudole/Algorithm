def solution(ingredient):
    answer = 0
    arr_ingre = [1, 2, 3, 1]
    chk_ingre = 0
    for ing in ingredient:
        if chk_ingre == 3:
            answer+=1
            chk_ingre = 0
        if arr_ingre[chk_ingre] == ing:
            chk_ingre+=1
        elif arr_ingre[chk_ingre-1] == ing:
            pass
        else:
            chk_ingre = 0
    return answer
  
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
