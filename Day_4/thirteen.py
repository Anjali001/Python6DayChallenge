l = [1, 3, 9, 8, 7]
def slice(l,i,k):
    list1=[]
    for i in range(i,k):
        list1.append(l[i])
    print(list1)

slice(l,1,3)