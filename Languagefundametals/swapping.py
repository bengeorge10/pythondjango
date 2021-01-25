num1=10
num2=20

print("Values before swapping:")
print("num1:",num1)
print("num2:",num2)s
temp=num1
num1=num2
num2=temp
print("Values after swapping:")
print("num1:",num1)
print("num2:",num2)

#OR WITHOUT USING A THIRD VARIABLE

num1=num1+num2
num2=num1=num2
num1=num1-num2

#Special code works only in python for swapping

num1,num2=num2,num1
