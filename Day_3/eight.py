dict1={
    "Name": "Carmel",
    "Series":"High Seas"
}
def check_key(dict1,key):
    count=0
    for i in dict1.keys():
        if i == key:
            count+=1
    if count==0:
        return False
    else:
        return True

print(check_key(dict1,"Series"))

    
