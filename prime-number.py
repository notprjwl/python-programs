# program to check if the number is prime or not
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

def prime(number):
    for i in range(2, number):
        if number % i == 0:  #checking every number is divisible from 2
            return False
    else:
        return True          



number = int(input("enter a number: "))
if prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
    