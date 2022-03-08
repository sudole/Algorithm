def solution(s):
    if s=="": return s
    arr = str(s).split()
    for word in arr:
        rp=""
        for i, char in enumerate(list(word)):
            rp += char.upper() if i % 2 == 0 else char.lower()
            
        s = s.replace(word,rp)
    
    return s
  
print(solution("try hello world"))
