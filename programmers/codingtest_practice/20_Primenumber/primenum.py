def solution(n):
    l = [0 for x in range(n+1)]
    for y in range(2, n+1):
        for z in range(2, int(n**1/2)+1):
            if y*z > n:
                break
            l[y*z] = 1

    return sum([1 for x in l[2:n+1] if x == 0])


def ex(n):
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

def ex2(n):
    count=0
    for x in range(2, n+1):
        for y in range(2, x+1):
            if x == 2:
                count+=1
                break
            if x == 3:
                count+=1
                break
            elif x == y:
                count+=1
                break
            elif x%y==0:
                break
            y+=1
    return count

print(solution(10))
print(solution(100))
print(solution(1000))
print(solution(10000))
# # ..
print(solution(100000))
# # ..
print(solution(1000000))