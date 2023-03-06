def solution(s):
    answer = ''

    while s.find(' ') != -1:
        answer += s[0].upper()
        answer += s[1:s.find(' ')+1].lower()
        s=s.replace(s[:s.find(' ')+1], '')
    answer += s[0].upper() + s[1:].lower()

    return answer