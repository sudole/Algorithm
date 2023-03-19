def solution(s):
    answer = True

    if s.count('(') != s.count(')'): return False
    if s[0] == ')': return False

    for x in s:
        if x == '(':
            answer = False
        if answer == False and x == ')':
            answer = True
        if answer == True and x == '(':
            answer = False

    return True

# answer true
print(solution("()()"))
# answer true
print(solution("(())()"))
# answer false
print(solution(")()("))
# answer false
print(solution("(()("))