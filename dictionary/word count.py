text="hello hai how hello hai hai"
words=text.split(" ")
dict={}
for word in words:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)

#find highest recursing word

print("largest recursive word:",min(dict))