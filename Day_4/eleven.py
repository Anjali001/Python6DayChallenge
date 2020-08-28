l = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a', 'd', 'd', 'd', 'x', 'x']
def compress(l):
    compressed_list=[]
    for i,j in enumerate(l) :
        if j != l[i-1]:
            compressed_list.append(j)
    print(compressed_list)

compress(l)