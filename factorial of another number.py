number = int(input("Enter the number: "))
fact = 1
counter = 1
if number == 0:
    print("0 != 1")
elif number < 0:
    print("The number must be greater than zero.")
else:
    while True:
        if fact == number:
            print("0! = 1")
            break
        elif number < fact:
            print(number  , "is not the factorial of another number.")
            break
        else:
            fact *= counter
            counter += 1
