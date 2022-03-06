def gcd(a, b):
    # Euclidean algorithm
    while b != 0:
        r = a % b
        a = b
        b = int(r)
    return a

def solution(a, b):
    n_gcd = gcd(max(a,b), min(a,b))
    return [n_gcd, int((a * b) / n_gcd)]

print(solution(3, 12))
print(solution(2, 5))