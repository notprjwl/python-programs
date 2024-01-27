from ast import If


def reverse(num):
    rev = 0
    for _ in range(len(str(num))):
        digit = num % 10            #mod wil return the remainder
        rev = rev * 10 + digit      #will make it reverse
        num = num // 10        #extract next_number by floor div rounds down the result to the nearest integer

    return rev  


num = int(input("enter a number: "))
print("reversed number is: ",reverse(num))
