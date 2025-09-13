items=[2,4,3,1,2,3,4,5,7,7]
f={}
for item in items:
    if item in f:
        f[item]+=1
    else:
        f[item]=1
print("Element frequencies:")
for key, value in f.items():
    print(f"{key}: {value}")
