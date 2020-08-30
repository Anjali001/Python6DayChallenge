# Euclid's theorem:  the largest number that divides them both without a remainder

def gcd(num1,num2):
    max_num= max(num1,num2)
    for i in range(1,max_num+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd=i

    print(f'GCD is {gcd}')

gcd(63,36) 