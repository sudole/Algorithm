def solution(s):
    return len(s) in (4,6) and not(False in [x in "1234567890" for x in s])

print(solution("a123"))
print(solution("1234"))