lst=[1,2,3,4,5,6]
lstt=[7,8,5,1,2]
lst.sort()
lstt.sort()
cn=0
pos1=0
pos2=0
for i in lst:
    if(lst[pos1]==lstt[pos2]):
        print(lst[pos1])
        pos1+=1
        pos2+=1
        cn+=1
    elif(lst[pos1]>lstt[pos2]):
        pos2+=1
    else:
        pos1+=1
print("count:",cn)

#time complexity is more
# for i in lst:
#     for j in lstt:
#         cn+=1
#         if(i==j):
#             print(i)
# print("count:",cn)