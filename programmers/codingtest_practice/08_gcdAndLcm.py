def gcd(a, b):
    # Euclidean algorithm
    while b != 0:
        r = a % b
        a = b
        b = int(r)
    return a

def lcm(a, b):
    return int((a * b) / gcd(a,b))

def solution(a, b):
    return [gcd(max(a,b), min(a,b)), lcm(max(a,b), min(a,b))]

print(solution(3, 12))
print(solution(2, 5))