'''
	Determine whether a given integer number is prime. Example:
    is_prime(7)-->True
    is_prime(10)-->False
'''
def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1
    
    if count==2:
        print(True)
    else:
        print(False)

is_prime(7)
is_prime(10)
