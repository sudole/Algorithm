def solution(numbers):
    answer = []

    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))

# result => [2,3,4,5,6,7]
print(solution([2, 1, 3, 4, 1]))
# result => [2,5,7,9,12]
print(solution([5, 0, 2, 7]))
# result => [4]
print(solution([2,2]))