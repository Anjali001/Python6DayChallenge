def remove_element(l,k):
    list1=[]
    for i in range(k):
        list1.append(l[i])
    for j in range(k+1,len(l)):
        list1.append(l[j])
    return list1

print(remove_element(['a','b','c','d'],3))