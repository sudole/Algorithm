def solution(dartResult):
    answer = 0
    score_item = []
    
    while len(dartResult)>0:
        chkstr=''
        idx = findBonus(dartResult)
        o_idx = findOption(dartResult)

        if o_idx-idx == 1:
            chkstr = dartResult[0:o_idx+1]
        elif idx > -1:
            chkstr = dartResult[0:idx+1]
            
        score_item.append(chkstr)
        dartResult = dartResult.replace(chkstr, '')

    for score in score_item:
        b_idx=findBonus(score)
        n = score[0:b_idx]
        b = score.replace(n, '')
        o_idx = findOption(b)

        n = int(n)
        o = convertOption(b[o_idx])
        if o_idx > -1 and o > -1:
            b = convertBonus(b[0:o_idx])
            answer = answer * o + (n ** b) * o
        else:
            answer = answer + (n ** convertBonus(b))

    return answer

def findBonus(strWord):
    index = -1
    for x in ['S', 'D', 'T']:
        index = strWord.find(x)
        if index > -1:
            break
    return index

def findOption(strWord):
    index = -1
    for x in ['*', '#']:
        index = strWord.find(x)
        if index > -1:
            break
    return index

def convertBonus(b):
    if b == 'S':
        return 1
    if b == 'D':
        return 2
    if b == 'T':
        return 3

def convertOption(o):
    if o == '*':
        return 2
    if o == '#':
        return -1

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))