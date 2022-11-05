array1 = []
array2 = []

size = int(input("Enter the size of array"))


def get_array():
    print("Enter the values of Array 1")
    for i in range(size):
        row = [] * size
        for j in range(size):
            row.append(int(input()))
        array1.append(row)
    print("Enter the values of Array 2")
    for i in range(size):
        row = [] * size
        for j in range(size):
            row.append(int(input()))
        array2.append(row)


def display_array():
    print("The first array")
    for i in range(size):
        for j in range(size):
            print(array1[i][j], end=" ")
        print()
    print("The second array")
    for i in range(size):
        for j in range(size):
            print(array2[i][j], end=" ")
        print()


def add_array():
    print("Sum of Array 1 and Array 2")
    for i in range(size):
        for j in range(size):
            sum = array1[i][j] + array2[i][j]
            print(sum, end=" ")
        print()


get_array()
display_array()
add_array()
