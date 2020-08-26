dict1={
    "Name": "Carmel",
    "Series":"High Seas"
}
dict2={}

def is_empty(diction):
    result = not bool(diction) # bool value of diction would be false if dictionary is empty and not will give opposite 
    #So true that dictionary is empty
    return result

print(is_empty(dict1))
print(is_empty(dict2))
