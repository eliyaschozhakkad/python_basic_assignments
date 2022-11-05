size=int(input("Enter the size of array"))
array=[]*size
result=[]*(size)
print("Enter the values of array")
for i in range(size):
    array.append(int(input()))

for i in range(size-1):
    result.append(array[i]*array[i+1])
print("Output")
for i in result:
    print(i,end=" ")
