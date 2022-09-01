bakery_line = ["Ali", "Atefe", "Reza", "Homa", "Amir", "Fatemeh"]
#### while True:
first_Aghazadeh_name = input("Enter the name of the first Aghazadeh : ")
first_Aghazadeh_spot = int(input("Where do you want to stand?: "))
second_Aghazadeh_name = input("Enter the name of the second Aghazadeh : ")
second_Aghazadeh_spot = int(input("Where do you want to stand?: "))
third_Aghazadeh_name = input("Enter the name of the third Aghazadeh : ")
third_Aghazadeh_spot = int(input("Where do you want to stand?: "))
### Do not use additional items
bakery_line.insert(first_Aghazadeh_spot-1, first_Aghazadeh_name)
bakery_line.insert(second_Aghazadeh_spot-1, second_Aghazadeh_name)
bakery_line.insert(third_Aghazadeh_spot-1, third_Aghazadeh_name)
print("All the people standing in line:" , bakery_line )