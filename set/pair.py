lst=[1,2,3,4,5]
num=6
st=set(lst)
for i in lst:
    res=i-num
    if st:
        print(i,res)