def solution(s, n):
    answer = ''
    for c in list(s):
        ordnum = ord(c)
        ceaser = ordnum + n
        
        if ceaser > 122 or (ceaser > 90 and ceaser < 97): ceaser -= 26
        if ceaser < 65 or ceaser > 122 or (ceaser > 90 and ceaser < 97): answer += c
        else:
            answer += chr(ceaser)
    return answer