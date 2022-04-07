def solution(dartResult):
    x_num = -1
    tmp_answer = []
    for x in dartResult:
        x_ord=ord(x)
        if x_ord >= 48 and x_ord <= 57:
            if x_ord == 48 and x_num > -1:
                x_num *= 10
            else:
                x_num = int(x)
        else:
            if x in ('S', 'D', 'T'):
                if x == 'S':
                    tmp_answer.append(x_num**1)
                elif x == 'D':
                    tmp_answer.append(x_num**2)
                elif x == 'T':
                    tmp_answer.append(x_num**3)
            elif x in ('#', '*'):
                last_idx = len(tmp_answer)-1
                if x == '#':
                    tmp_answer[last_idx] = tmp_answer[last_idx]*-1
                elif x == '*':
                    tmp_answer = tmp_answer[:last_idx-1] + [a*2 for a in tmp_answer[last_idx-1:]]
            x_num = -1

    return sum(tmp_answer)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))