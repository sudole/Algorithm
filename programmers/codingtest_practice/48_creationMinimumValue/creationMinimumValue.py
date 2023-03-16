def solution(A,B):
    answer = 0

    sum_list = A + B
    while len(sum_list) != 0:
        min_i = min(sum_list)
        max_i = max(sum_list)
        answer += min_i * max_i
        sum_list.pop(sum_list.index(min_i))
        sum_list.pop(sum_list.index(max_i))

    return answer

# answer: 29
print(solution([1, 4, 2], [5, 4, 4]))
# answer: 10
print(solution([1,2], [3,4]))