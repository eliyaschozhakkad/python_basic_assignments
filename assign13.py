string = input("Enter a string")
flag = 0
length = len(string)

for i in range(0, length):

    if string[i] != string[length - 1 - i]:
        flag = 1
        break
if flag == 0:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")
