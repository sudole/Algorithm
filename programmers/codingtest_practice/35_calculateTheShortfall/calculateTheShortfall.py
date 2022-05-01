def solution(price, money, count):
    answer = 0
    for n in range(count):
        answer+= (price*(n+1))
    return 0 if answer-money <= 0 else answer-money

print(solution(3, 20, 4))