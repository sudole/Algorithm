def solution(s):
    length = len(s)
    center = int(length / 2)
    answer = s[center-1:center+1] if length % 2 == 0 else s[center]
    return answer

print(solution("qwer"))
print(solution("abcde"))