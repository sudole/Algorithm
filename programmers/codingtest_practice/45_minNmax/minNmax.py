def solution(s):
    arr = s.split(' ')
    arr = [int(x) for x in arr]
    answer = f'{min(arr)} {max(arr)}'
    return answer

# answer: "1 4"
print(solution("1 2 3 4"))
# answer: "-4 -1"
print(solution("-1 -2 -3 -4"))
# answer: "-1 -1"
print(solution("-1 -1"))

'''
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
'''