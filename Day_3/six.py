dict1={
    "Name": "Carmel",
    "Series":"High Seas"
}
def add_keyvalue(dict1,key,value):
    dict1.update({key:value})
    print(dict1)

add_keyvalue(dict1,"Channel","Netflix")
