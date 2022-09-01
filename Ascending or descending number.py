numbers = []
sort = True
The_desired_number_to_sort = int(input("The desired number to sort :"))
for i in range(0, The_desired_number_to_sort):
    num = int(input('Enter a number: '))
    numbers.append(num)
for number in range(1, The_desired_number_to_sort):
    if numbers[number -1] < numbers[number] or numbers[-number] < numbers[-number - 1]:
        sort = True
    else:
        sort = False
        break
if sort == True:
    print('Yes!')
else:
    print('No!')