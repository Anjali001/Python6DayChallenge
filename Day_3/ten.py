def combine_duplicates(d1,d2):
    d3={}
    d3.update(d1)
    d3.update(d2)
    for i,j in d1.items():
        for k,l in d2.items():
            if i==k:
                d3[i] = j+l
    print(d3)

D1 = {'a': 100, 'b': 200, 'c':300,'e':700}
D2 = {'a': 300, 'b': 200, 'd':400}
combine_duplicates(D1,D2)

