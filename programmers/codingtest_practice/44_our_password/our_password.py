def update_word(word, i):
    return chr((ord(word) + i - ord('a')) % 26 + ord('a'))

def calc(word, index, skip):
    u1 = word
    for i in range(1, index+1):
        u1 = update_word(u1, 1)
        while u1 in skip:
            u1 = update_word(u1, 1)
    return u1


def solution(s, skip, index):
    answer = ''

    for w in s:
        answer += calc(w, index, skip)

    return answer
# answer "happy"
print(solution("aukks", "wbqd", 5))