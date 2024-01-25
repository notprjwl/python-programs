# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....
def fibonacci(length):
    sum = 0
    result = [0, 1]

    for i in range(length - 2):
        next_num = result[-1] + result[-2]
        result.append(next_num)
    
    return result

length = int(input("enter the length: "))
result = fibonacci(length)
print("fibonacci series: ",result)


#other way

# length = int(input("enter the length: "))
# sum = 0
# result = [0, 1]

# while len(result)<length:
#     next_num = result[-1] + result[-2]
#     result.append(next_num)
    
# print(result)
