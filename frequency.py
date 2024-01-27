# program to count the frequency of each element in a list

def find_frequency(numbers):
    
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
         
    return frequency
    

numbers = [1, 2, 3, 4, 4, 1, 2, 3, 5, 3]
print(find_frequency(numbers))
