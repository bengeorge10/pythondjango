emplo=[
    [100,"ben","developer",8000,1989,1995],
    [102,"joju","manager",6000,1970,1990],
    [103,"roshan","accountant",3000,1989,1991],
    [104,"basil","hr",4000,1990,1999]
]
#print third column
# for emp in emplo:
#     print(emp[3])

#print developer row full
# for emp in emplo:
#     if(emp[2]=="developer"):
#         print(emp)

#print total fund raise by the company
# tot=0
# for emp in emplo:
#     tot+=emp[3]
# print("total fund:",tot)

#print the maximun salary
# sallist=[]
# for emp in emplo:
#     sallist.append(emp[3])
# print(max(sallist)) #//to get maximun salary

#the above method in a much more less code is as:
# maxsal=max(list(map(lambda emp:int(emp[3]),emplo)))
# print(maxsal)

#print employee worked in 90`s
#print experience of each employee
#print details of developers


exp=[]
for emp in emplo:
    exp.append(emp[5]-emp[4])
print(exp)
high=max(exp)
for emp in emplo:
    exp=emp[5]-emp[4]
    if(exp==high):
        print("maximum experienced employee is :",emp)
