def printSquareStar(a, b):
    for i in range(b):
        s = ''
        for j in range(a):
            s += '*'
        print(s)

a, b = map(int, input("Enter two number: ").strip().split(' '))
printSquareStar(a, b)
