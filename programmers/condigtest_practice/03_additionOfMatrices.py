def solution(arr1, arr2):
    answer = []
    print(arr1, arr2)
    
    
    for x in range(len(arr1)):
        item = []
        for y in range(len(arr1[x])):
            item.append(arr1[x][y] + arr2[x][y])
        answer.append(item)
    return answer

a, b = 	[[1, 2], [2, 3]], [[3, 4], [5, 6]]
print(solution(a, b))

x, y = 	[[1], [2]], [[3], [4]]
print(solution(x, y))
