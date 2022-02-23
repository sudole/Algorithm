def solution(x):
    return True if x % sum([int(x) for x in str(x)]) == 0 else False

def inputNumber():
    return int(input("Enter number>"))
a = inputNumber()
while a > -1:
    if solution(a):
        print("%d is harshad number." % a)
    else:
        print("%d is not harshad number." % a)

    a = inputNumber()