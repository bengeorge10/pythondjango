arr=[2,3,4,5]
ele=int(input("enter the number:"))
for i in arr:
    for j in arr:
        if (i+j==ele)&(i!=j):
            print(i,j)

