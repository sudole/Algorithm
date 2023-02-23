def calc(x, index, skips):
    calculating = True
    calc_num = int((ord(x)+index-97) % 26) + 97
    while calculating:
        for n in skips:
            if ord(x) < calc_num and n >= ord(x) and n <= calc_num:
                calc_num += 1
            elif calc_num < ord(x) and n <= ord(x) and n >= calc_num:
                calc_num += 1
            else:
                calculating = False
        calc_num = int((calc_num-97) % 26) + 97
    return chr(calc_num)

def solution(s, skip, index):
    arr_skip = [ord(x) for x in skip]
    answer = ''.join([calc(x, index, arr_skip) for x in s])
    return answer