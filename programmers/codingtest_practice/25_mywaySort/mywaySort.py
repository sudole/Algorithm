
def solution(s, n):
    w = {}
    for word in s:
        w[word] = word[n]

    return list(dict(sorted(w.items(), key = lambda s: (s[1], s[0]))))

def solution2(s, n):
    answer=[]
    w=[]
    for i, word in enumerate(s):
        w.append((i, word[n]))
    
    # print(w)
    c_w=sorted(w, key = lambda item: item[1])
    # print(c_w)

    for x in c_w:
        answer.append(s[x[0]])
    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))