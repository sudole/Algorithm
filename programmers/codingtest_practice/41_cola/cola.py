def solution(a, b, n):
    answer, rem = 0, 0

    while(n >= a):
        # 교환할 수 없는 병의 개수 계산
        rem = int(n % a)
        # 교환된 병의 개수 계산
        n = int(n / a) * b
        answer += n
        n += rem

    return answer

# answer: 19
print(solution(2,1,20))
# answer: 9
print(solution(3,1,20))
# answer: 16
print(solution(3,2,10))