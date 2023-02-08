def solution(number):
    answer = 0
    _max = len(number)
    for i in range(_max-2):
        for j in range(i+1, _max-1):
            for k in range(j+1, _max):
                answer+= 1 if number[i] + number[j] + number[k] == 0 else 0
    return answer

# answer: 2
print(solution([-2, 3, 0, 2, -5]))
# answer: 5
print(solution([-3, -2, -1, 0, 1, 2, 3]))
# answer: 0
print(solution([-1, 1, -1, 1]))