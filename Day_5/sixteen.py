def is_palindrome(list1):
    count=0
    for i,j in enumerate(list1):
        i=i+1
        if j != list1[-i]:
            count+=1

    if count==0:
        return True
    else:
        return False


print(f'is_palindrome([1, 2, 1])->{is_palindrome([1,2,1])}')
print(f'is_palindrome([1, 2, 3, 2, 1])->{is_palindrome([1, 2, 3, 2, 1])}')
print(f'is_palindrome([1, 2, 3, 1])->{is_palindrome([1, 2, 3, 1])}')





