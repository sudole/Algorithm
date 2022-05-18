def solution(sizes):
    for size in sizes:
        size.sort()
    
    w = -1
    h = -1
    for size in sizes:
        w=size[0] if w < size[0] else w
        h=size[1] if h < size[1] else h
    return w * h

# result > 4000
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# result > 120
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# result > 133
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))