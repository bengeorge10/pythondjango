num=int(input("enter the number:"))
sum=0
c=0
while(num>0):
    d=num%10
    c=d*d*d
    sum+=c
    num=num//10
print(sum)