from itertools import groupby
l = [1, 1, 1, 2, 2, 3, 3, 4,4,6,7,8,5,5,5,5]
def pack(l):
    list1=[]
    for key , group in groupby(l):
        list1.append(list(group))
    print(list1)

pack(l)