text="hello hai how hello hai hai"
words=text.split(" ")
dict={}
for word in words:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)
data=sorted(dict,key=dict.get,reverse=True)
print("Sorted data:",data)
print("Highest occuring value:",data[0])
print("Least occuring value:",max(data))