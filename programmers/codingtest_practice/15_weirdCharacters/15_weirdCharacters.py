def solution(s):
    answer = ''
    i = 0
    for char in list(s):
        if char == " ": 
            i = 0
            answer += char
        else:
            answer += char.upper() if i % 2 == 0 else char.lower()
            i+=1
    return answer
  
print(solution("try hello world"))
