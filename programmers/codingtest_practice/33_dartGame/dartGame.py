def solution(dartResult):
    answer = 0

    while len(dartResult)>0:
        idx = findChar(dartResult)

        chkstr=''
        if idx != 0:
            chkstr = dartResult[0:idx]
        else:
            chkstr = dartResult[idx]
        
        dartResult = dartResult.replace(chkstr, '')
        print(idx, chkstr, dartResult)
        
    # for x in dartResult:
    #     print(x)
    return answer

def findChar(strWord):
    index = -1
    for x in ['S', 'D', 'T']:
        index = strWord.find(x)
        if index > -1:
            break
    return index

print(solution('1S2D*3T'))
print(ord('0'))
print(ord('1'))
print(ord('9'))
