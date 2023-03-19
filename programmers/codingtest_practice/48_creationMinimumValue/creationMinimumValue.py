def solution(A,B):
    answer = 0

    while len(A) != 0 and len(B) != 0:
        val_a = max(A)
        val_b = max(B)
        if val_a < val_b:
            val_a = min(A)
        else:
            val_b = min(B)
        answer += val_a * val_b
        A.pop(A.index(val_a))
        B.pop(B.index(val_b))

    return answer

# answer: 29
print(solution([1, 4, 2], [5, 4, 4]))
# answer: 10
print(solution([1,2], [3,4]))