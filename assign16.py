number = int(input("Enter a number: "))
flag = 0
if number == 0 or number == 1:
    flag = 1

for i in range(2, number):
    if number % i == 0:
        flag = 1

if flag == 1:
    print("The number is not prime")
else:
    print("The number is prime")
