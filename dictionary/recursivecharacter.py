text="ABCBACB"
dict={}
for word in text:
    if word in dict:
        dict[word]+=1
        print("First recursive character is:",word)
        break
    else:
        dict[word]=1
