#Write a Python program to find the largest element in a list.

def find_largest(numbers):
    
    if not numbers:
        return "empty list"
    
    largest = numbers[0]   #choosing a number to compare
    
    for num in numbers:
        if(num > largest):
            largest = num
            
    return largest

numbers = [5, 12, 8, 3, 21, 17 ,91 ,82, 70000]
print("The largest number is:", find_largest(numbers))       