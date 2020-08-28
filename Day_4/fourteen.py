l = [1, 3, 9, 8, 7]
def insert_element(l,elem,i):
    list1=[]
    j=0
    for j in range(i):
        list1.append(l[j])
    list1.append(elem)
    for k in range(i,len(l)):
        list1.append(l[k])
    return list1

print(insert_element(l, 1, 3))
