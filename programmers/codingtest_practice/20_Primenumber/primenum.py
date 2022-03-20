def solution(n):
    answer = [x for x in range(2, n+1)]
    index=0
    p = answer[index]
    i = 2
    while True:
        if p * i > n:
            index+=1
            if index >= len(answer)-1: break 
            p = answer[index]
            i=2
            continue

        if p*i in answer:
            answer.remove(p*i)
        i+=1
    return len(answer)

print(solution(10))
print(solution(100))
print(solution(1000))
print(solution(10000))
# ..
print(solution(100000))
# ..
print(solution(1000000))