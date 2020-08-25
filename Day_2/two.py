user=[]
a=True
while (a):
    add=input("Enter line")
    user.append(add)
    a= input("Wanna enter more(True/False)")
    if a == str(False):
        break
user='\n'.join(user)
print(user.upper())

