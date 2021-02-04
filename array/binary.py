arr=[3,4,2,1,8,7,6]
#arr.sort()          : its a method. identify using dot
#str=sorted(arr)     : its a function

arr.sort()
print(arr)
ele=int(input("enter the element:"))
flag=0
low=0
upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2
    if(ele>arr[mid]):
        low=mid+1
    elif(ele<arr[mid]):
        upp=mid-1
    elif(ele==arr[mid]):
        flag=1
        break

if(flag==0):
    print("not found")
else:
    print("found")
