
def copy1Dto2DList(arr1D,arr2D):
     col= len(arr2D)
     #Copying 1D array to 2D array by every col no.of elements in each row
     arr2D = [arr1D[i:i+col] for i in range(0,len(arr1D),col)]
     return arr2D

print("Enter array elements: ")
arr1D= list(map(int,input().split())) #Taking 1D array as input
print("Array in 1D:")
print(arr1D)    #Printing 1D array
n=len(arr1D)
row,col = 0,0
for i in range(2,n//2):    #Finding factors for n #elements
    if n%i==0:
        row=i
        col=n//i
        print("Creating a",row,"X",col,"Matrix") 
        arr2D = [0]*col  #Creating a list with col no.of elements
        break
if row==0: print("Error, Cannot convert to 2D array.") 
else: 
    arr2D = copy1Dto2DList(arr1D,arr2D)
    for i in arr2D:
        print(i)
   