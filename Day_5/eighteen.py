'''
Sorting a list of lists according to length of sublists
    We suppose that a list (inlist) contains elements that are lists themselves.
    The objective is to sort the elements of inlist according to their length.
    Example: def sort_list([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L)--> [[o], [d, e], [d, e], [m, n], [a, b, c], [f, g, h], [i, j, k, l]]
    '''
list1 = [['a','b','c'],['d','e'],['f','g','h'],['d','e'],['i','j','k','l'],['m','n'],['o']]
list1.sort(key = len)
print(list1)
