def solution(n, lost, reserve):
    answer = n
    # 여벌옷이 없는 경우 도난 수를 제외한 값을 리턴
    if len(reserve) == 0:
        answer = answer - len(lost)
    elif len(lost) > 0 and len(reserve) > 0:
        # 여벌옷 인덱스와 도난 인덱스가 동일한 경우를 제외하여 배열 재구성
        _lost = [l for l in lost if l not in reserve]
        _reserve = [l for l in reserve if l not in lost]
        # 도난 수는 큰 값을 먼저 처리하도록 함
        _lost.sort(reverse=True)
        for l in _lost:
            if l+1 in _reserve:
                _reserve.pop(_reserve.index(l+1))
            elif l-1 in _reserve:
                _reserve.pop(_reserve.index(l-1))
            else:
                # 여벌옷으로 처리할 수 없는 경우 -1
                answer+=-1
    return answer

# answer 5
print(solution(5, [2, 4], [1, 3, 5])
# answer 4
print(solution(5, [2, 4], [3])
# answer 2
print(solution(3, [3], [1])