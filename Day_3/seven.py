dic1={1:10, 2:20} 
dic2={3:30, 4:40}
dic3={5:50,6:60}

def dict_concatenate(dict1,dict2,dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    print(dict1)

dict_concatenate(dic1,dic2,dic3)
