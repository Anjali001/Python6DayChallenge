
list1=['a','b','c','d','e','f','g','h']
by=3
list2= list1[by:]+list1[:by] # Left Rotate
#list2= list1[-by:]+list1[:-by] #Right rotate

print(list2)

