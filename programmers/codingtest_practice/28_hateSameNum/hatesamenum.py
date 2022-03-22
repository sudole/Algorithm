def solution(arr):
    answer = []
    for num in arr:
        length = len(answer)
        if length == 0: answer.append(num)
        elif num != answer[length-1]:
            answer.append(num)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))