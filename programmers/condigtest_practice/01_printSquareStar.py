def printSquareStar(a, b):
    if a > 1000 or b > 1000:
        print("The entered value must not exceed 1000.")
        return
    
    for i in range(b):
        s = ''
        for j in range(a):
            s += '*'
        print(s)

a, b = map(int, input("Enter two number: ").strip().split(' '))
printSquareStar(a, b)
