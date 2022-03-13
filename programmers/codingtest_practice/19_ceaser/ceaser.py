def solution(s, n):
    answer = ''
    for c in list(s):
        if c == " ": answer += c
        else:
            end=90
            ordnum=ord(c)
            if ordnum >= 97: end=122
            ceaser = (ordnum+n)%end
            
            if ceaser == 0: ceaser = end
            elif ceaser < (end-26): ceaser += (end-26)
            answer+=chr(ceaser)
    
    return answer

print(solution('AB',1))
print(solution('z',1))
print(solution('a B z',4))