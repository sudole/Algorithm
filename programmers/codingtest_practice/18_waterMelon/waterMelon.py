def solution(n):
    word = ['수','박']
    return ''.join([word[x%2] for x in range(n)])

print(solution(3))
print(solution(4))