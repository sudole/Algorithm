def solution(s):
    answer = ''

    while s.find(' ') != -1:
        if s.find(' ') == 0:
            answer += s[0]
            s = s[1:]
        else:
            answer += s[0].upper()
            answer += s[1:s.find(' ')+1].lower()
            s=s.replace(s[:s.find(' ')+1], '')
    answer += s[0].upper() + s[1:].lower()

    return answer