
def isHappy(n):

    if n ** 2 == 1:
        return True

    squares = 0
    while n != 1:
        n = str(n) 
        squares = 0    
        for i in n:  
            squares += int(i) ** 2  
            # print(squares)
        n = squares  
        # print(squares)
        if n == 4:  # if n is 4 then it is a unhappy number
            return False
    return True
    


print(isHappy(10000000))