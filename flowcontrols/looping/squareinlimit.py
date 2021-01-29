num=int(input("enter the number:"))
lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
for i in range(1,upper):
    pow=(i**num)
    for pow in range(lower,upper):
        print(pow)
