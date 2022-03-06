def solution(phone_number):
    return ''.join([n if n == '-' else '*' for n in phone_number[0:-4]]) + phone_number[-4:]

print(solution(input("Enter Phone Number >")))