arr=[10,11,12,13]
ele=int(input("enter the number:"))
# for i in arr:
#     for j in arr:
#         if (i+j==ele)&(i!=j):
#             print(i,j)

low=0
upp=len(arr)-1
for i in arr:
    sum=arr[low]+arr[upp]
    if(sum==ele):
        print("[",arr[low],arr[upp],"]")
        low+=1
    elif(sum<ele):
        low+=1
    else:
        upp-=1