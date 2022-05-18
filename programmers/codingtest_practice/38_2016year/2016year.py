def solution(a, b):
    weeks = ['THU', 'FRI','SAT','SUN','MON','TUE','WED']
    n=0
    for m in range(1, a):
        if m % 2 == 0:
            if m == 2: 
                n += 29
            elif m < 8:
                n += 30
            else:
                n += 31
        else:
            if m < 8:
                n += 31
            else:
                n += 30
    n += b
    print(n, (n % 7))
    return weeks[(n % 7)]

# result > "TUE"
print(solution(5, 24))
# result > "SAT"
print(solution(12, 31))
# result > "SUN"
print(solution(1, 31))