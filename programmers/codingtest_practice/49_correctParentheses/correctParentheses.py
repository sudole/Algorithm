def solution(s):
    answer = True

    if s.count('(') != s.count(')'): return False
    if s[0] == ')': return False

    check = 0
    for x in s:
        if check == 0 and x == ')': return False
        if x == '(':
            check+=1
        elif x == ')':
            check-=1
    if check != 0: answer = False

    return answer

# answer true
print(solution("()()"))
# answer true
print(solution("(())()"))
# answer false
print(solution(")()("))
# answer false
print(solution("(()("))