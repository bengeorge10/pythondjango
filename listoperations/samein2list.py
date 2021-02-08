lst=[1,2,3,4,5]
lstt=[7,8,5,1,2]
lst.sort()
lstt.sort()
for i in lst:
    if(i==lstt[0]):
        print(i)
        i+=1
        lstt[0]+1
    elif(i>lstt[0]):
        lstt[0]+1
    else:
        i+=1