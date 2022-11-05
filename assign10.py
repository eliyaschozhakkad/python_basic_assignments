size=int(input("Enter the size of array:"))
array1=[]
array2=[]
print("Enter the values of Array1")
for i in range(0,size):
    array1.append(input())

print("Enter the values of Array2")
for i in range(0,size):
    array2.append(input())

print("First array")
for i in array1:
    print(i,end=" ")
print("\nSecond array")
for i in array2:
    print(i,end=" ")

for i in range(0,size):
    temp=array1[i]
    array1[i]=array2[i]
    array2[i]=temp

print("\nAfter swapping")
print("Array 1")
for i in array1:
    print(i,end=" ")
print("\nArray 2")
for i in array2:
    print(i,end=" ")