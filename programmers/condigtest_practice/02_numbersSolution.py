def solution(x, n):
    answer = []
    if x < -10000000 or x > 10000000:
        print("x values range from -10000000 to 10000000.")
        return answer
    if n > 1000:
        print("The value of n must be entered as 1000 or less.")
        return answer
    
    for i in range(1, n+1):
        answer.append(x*i)
    return answer


a, b = map(int, input("Enter two number: ").strip().split(' '))
print(solution(a, b))