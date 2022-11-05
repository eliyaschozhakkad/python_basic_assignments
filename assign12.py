size = int(input("Enter the size of array"))
array = []
for i in range(0, size):
    array.append(int(input()))
for i in range(0, size - 1):

    for j in range(i+1, size):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
print("The sorted array is")
print(array)
