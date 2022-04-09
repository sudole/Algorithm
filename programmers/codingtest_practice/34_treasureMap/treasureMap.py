def solution(n, arr1, arr2):
    answer = []
    for x in range(n):
        b1 = bin(arr1[x])
        b2 = bin(arr2[x])
        print(arr1[x], b1, len(b1))
        print(arr2[x], b2)
        print(str(b1 and b2), b1 and b2)
        
        #answer[x] = b1 or b2
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

#print(format(9, 'b'))