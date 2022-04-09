def solution(n, arr1, arr2):
    answer = []
    for x in range(n):
        b = bin(arr1[x] | arr2[x])
        b = b[2:].zfill(n)
        answer.append(b.replace('1', '#').replace('0', ' '))
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

# print(format(9, '010b'))
# print(format(30, '010b'))