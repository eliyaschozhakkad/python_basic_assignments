size=int(input("Enter the size of array"))
array=[]
count=0
for i in range(0,size):
    array.append(int(input()))
for i in array:
    if i%2==0:
        count+=1
print(f"The number of even numbers in the given array is {count}")
