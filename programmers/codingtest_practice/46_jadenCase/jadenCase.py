def solution(s):
    arr = []
    for word in s.split(" "):
        a = word[0]
        if type(a) == str and a != ' ' and ord(a) >= ord('a'):
            b = word[1:]
            arr.append(a.upper() + b.lower())
        else:
            arr.append(word)

    return ' '.join(arr)