#recursive factorial

def recusive_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        while n > 0:
            return n * recusive_factorial(n-1)
        


n = int(input("enter a number: "))
print("factorial of "+ str(n) + " using recursion is:", recusive_factorial(n))