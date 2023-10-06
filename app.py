#Tapsiriq1
number = int(input("Enter a number (maximum 4 digits): "))

if 0 <= number <= 9999:
   
    num_str = str(number)
    num_digits = len(num_str)
    
    print(f"The number {number} has {num_digits} digit(s).")
else:
    print("Please enter a number with a maximum of 4 digits.")
    
#Tapsiriq2
number = int(input("Enter a number: "))

count_3 = 0
count_5 = 0
count_7 = 0


for i in range(3):
    if number % 3 == 0:
        count_3 += 1
    if number % 5 == 0:
        count_5 += 1
    if number % 7 == 0:
        count_7 += 1


if count_3 >= 3:
    print(f"{number} is divisible by 3 for at least 3 divisions.")
else:
    print(f"{number} is not divisible by 3 for at least 3 divisions.")
    
if count_5 >= 3:
    print(f"{number} is divisible by 5 for at least 3 divisions.")
else:
    print(f"{number} is not divisible by 5 for at least 3 divisions.")
    
if count_7 >= 3:
    print(f"{number} is divisible by 7 for at least 3 divisions.")
else:
    print(f"{number} is not divisible by 7 for at least 3 divisions.")
    
#Tapsiriq3
X = int(input("Enter the first number (X): "))
Y = int(input("Enter the second number (Y): "))


if X % Y == 0:
    print("Yes")
else:
    print("No")