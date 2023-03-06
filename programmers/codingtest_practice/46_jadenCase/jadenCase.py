def solution(s):
    arr = []
    for word in s.split(" "):
        a = word[0]
        b = word[1:len(word)+1]
        arr.append(a.upper() + b.lower())

    return ' '.join(arr)