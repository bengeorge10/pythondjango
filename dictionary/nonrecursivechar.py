text="AABBCD"
dict={}
for word in text:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
for k,v in dict.items():      #gives key and values at a time
    if(v==1):
        print(k)
        break