def even_odd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
    

print(even_odd(3))


def armstrong_number(n):
    length = len(str(n))
    sum = 0
    temp = n
    for i in range(length):
        digit = n % 10  # 3 5 1
        power = digit ** length # 27 125 1
        sum += power    # 27 152 
        n = n // 10 # 15 1
    print(sum)
    if sum == temp:
        return 'ARMSTRONG NUMBER'
    else:
        return 'NOT AN ARMSTRONG NUMBER'


print(armstrong_number(153))


def prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        else: i += 1
    
    if count <= 2:
        return 'PRIME'
    else:
        return 'NOT PRIME'
           
print(prime(89))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        # return n * factorial(n-1)
        result = n
        for i in range(1, n):
            result *= i
        return result
        
print(factorial(10))

def palindrome(s):
    # if s == s[::-1]:
    #     return 'PALINDROME'
    # else:
    #     return 'NOT A PALINDROME'
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    print(result)
    if result == s:
        return 'PALINDROME'
    else:
        return 'NOT A PALINDROME'

print(palindrome('noon'))

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
def fibonacci(n):
    result = [0, 1]
    for i in range(0, n-2):
        sum = result[i] + result [i+1]
        result.append(sum)
    return result
        
print(fibonacci(10))

def bubble_sort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
            else:
                j+=1
    return list1

print(bubble_sort(list1=[3, 1, 8, 45, 56, 9]))

CLASSES AND OBJECTS




