def solution(s):
    if len(s) != 4 and len(s) != 6: return False
    check="1234567890"
    for x in list(s):
        if not(x in check):
            return False
    return True

print(solution("a123"))
print(solution("1234"))
