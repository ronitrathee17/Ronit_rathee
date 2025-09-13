a=[2,4,3,1,2,3,4,5,7,7]
b=[]
for item in a:
    if item not in b:
        b.append(item)
print("original list ",a)
print("list after remove duplicate ",b)