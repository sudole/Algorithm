def solution(a, b):
    return sum([x for x in range(min(a,b), max(a,b)+1)])


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))