word=input("enter the string:")
word=list(word)
count={}
for char in word:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count) 
