num=int(input("enter the number:"))
rev=0                    #rev=""
while(num>0):
    d=num%10
    rev=rev*10+d         #rev+=str(d)
    num=num//10
print(rev)