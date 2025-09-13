sen=input("enter any sentence ")
wd=sen.split()
long=""
for word in wd:
    if len(word)>len(long):
        long=word
print(long)