def solution(s):
    answer = [0, 0]
    while s.count("0") > 0 or len(s) > 1:
        answer[1] += s.count("0")
        s = s.replace("0", "")
        len_s = len(s)

        s = ""
        while len_s > 0:
            s = ("1" if len_s % 2 > 0 else "0") + s
            len_s = int(len_s / 2)

        answer[0] += 1

    return answer

# Answer [3, 8]
print(solution("110010101001"))
# Answer [3, 3]
print(solution("01110"))
# Answer [4, 1]
print(solution("1111111"))