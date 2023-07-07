number1 = input()
number2 = input()

result = ''
while number1 and number2:
    if number1 >= number2:
        result = number1[0] + result
        number1 = number1[1:]
    else:
        result = number2[0] + result
        number2 = number2[1:]

result = number1 + result + number2

print(result[::-1])
