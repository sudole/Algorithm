def solution(x, n):
    if x < -10000000 or x > 10000000:
        print("x values range from -10000000 to 10000000.")
        return []
    if n > 1000:
        print("The value of n must be entered as 1000 or less.")
        return []
    
    return [(i+1)*x for i in range(n)]


a, b = map(int, input("Enter two number: ").strip().split(' '))
print(solution(a, b))