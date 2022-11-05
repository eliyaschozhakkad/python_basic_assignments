size = int(input("Enter the size of array"))
array = [] * size


def get_array():
    print("Enter the elements of array")
    for i in range(size):
        array.append(input())


def display_array():
    print("The array is ")
    for i in array:
        print(i, end=" ")


get_array()
display_array()
