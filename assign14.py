size = int(input("Enter the size of arrays"))
array1 = []
array2 = []

print("Enter the values of Array 1")
for i in range(size):
    row = [] * size
    for j in range(size):
        row.append(int(input()))
    array1.append(row)
print("Array 1")
for i in range(size):
    for j in range(size):
        print(array1[i][j], end=" ")
    print()

print("Enter the values of Array 2")
for i in range(size):
    row = [] * size
    for j in range(size):
        row.append(int(input()))
    array2.append(row)
print("Array 2")
for i in range(size):
    for j in range(size):
        print(array2[i][j], end=" ")
    print()
print("The sum of 2 Arrays is")
for i in range(size):
    for j in range(size):
        sum = array1[i][j] + array2[i][j]
        print(sum, end=" ")
    print()

