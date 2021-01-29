num=int(input("enter the number:"))
c=0
for i in range(1,num+1):
    sum=str(num)*i
    c=c+int(sum)
print(c)