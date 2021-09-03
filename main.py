def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    if a == b:
        return a

    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


while True:
    try:
        num1 = int(input("Enter number 1: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if num1 < 0:
            print("Enter a positive number")
        else:
            break

while True:
    try:
        num2 = int(input("Enter number 2: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if num1 < 0:
            print("Enter a positive number")
        else:
            break

ans = gcd(num1, num2)
print(f"HCF of {num1} and {num2} is {ans}")