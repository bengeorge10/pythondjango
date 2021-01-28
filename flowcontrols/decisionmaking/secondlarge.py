num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if((num1>num2)&(num2>num3))|((num3>num2)&(num2>num1)):
    print("num2 is second largest")
elif((num2>num1)&(num1>num3))|((num3>num1)&(num1>num2)):
    print("num1 is second largest")
elif((num1>num3)&(num3>num2))|((num2>num3)&(num3>num1)):
    print("num3 is second largest")
else:
    print("they are equal")


#if(num1>num2)&(num2>num3):
#   if(num2>num3):
#       print("second largest is num2")
#   else:
#       print("second largest is num3")
# do the rest