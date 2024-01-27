#program to check if the number is prime or not

def prime(number):
    for i in len(number):
        if i % 2 !=0:
            print("it is prime")
        else:
            print("it is not prime")

    

number = (input("enter a number: "))
print(prime(number))