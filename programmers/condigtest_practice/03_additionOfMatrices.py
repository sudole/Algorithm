def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]

a, b = 	[[1, 2], [2, 3]], [[3, 4], [5, 6]]
print(a, b)
print(solution(a, b))

x, y = 	[[1], [2]], [[3], [4]]
print(x, y)
print(solution(x, y))
