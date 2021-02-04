arr=[10,11,12,13,14,15]
ele=int(input("enter element:"))
flag=0
for i in arr:
    if(i==ele):
          flag=1
          break
    else:
        flag=0
if(flag==0):
    print("not found")
else:
    print("found")

#print(ele in arr)