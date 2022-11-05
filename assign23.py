array = []
size = int(input("Enter the size of array"))

class ArrayFunction:
    def get_array(self):
        print("Enter the values of Array ")
        for i in range(size):
            row = [] * size
            for j in range(size):
                row.append(int(input()))
            array.append(row)

    def display_array(self):
        print("Array elements are")
        for i in range(size):
            for j in range(size):
                print(array[i][j], end=" ")
            print()

array_operation = ArrayFunction()
array_operation.get_array()
array_operation.display_array()




