f=open("demo","r")
names=[]
dict={}
for lines in f:
    names.append(lines.rstrip("\n").split(" "))

for i in names:
    print(i)
for word in names:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)