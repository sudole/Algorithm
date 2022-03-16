def solution(s):
    lowS=s.lower()
    cntY=lowS.count('y')
    cntP=lowS.count('p')
    if cntY > 25 or cntP > 25 or cntY != cntP:
            return False
    return True

print(solution("pPoooyY"))
print(solution("Pyy"))
