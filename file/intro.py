f=open("demo","r")
names=set()
for lines in f:
    names.add(lines.rstrip("\n"))
print(names)