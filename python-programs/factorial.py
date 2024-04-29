#without using recursion
def factorial(n):
    
    if n==1 or n==1: #checking the base condition
        return 1
    else:
        result = 1      
        while n > 0:  
            result *= n
            n -= 1
        
    return result    
        
    

n = int(input("enter a number: "))
print("factorial of "+ str(n) + " is:", factorial(n))