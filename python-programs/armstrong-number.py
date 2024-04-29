#153 armstrong number cause 1^3 + 5^3 + 3^3 = 153

# num = (input("enter a number "))
# sum = 0

# for i in num:
#     digit = int(i
#     power = digit**len(num)
#     sum+=power


# if sum == int(num):
#     print(num + " is an armstrong number")
# else:
#     print(num + " is not an armstrong number") 


def armstrong(num):
    sum_of_digits = 0
    for i in num:
        digit = int(i)
        sum_of_digits += digit ** len(num)
    
    if sum_of_digits == int(num):
        return " is an Armstrong number"
    else:
        return " is not an Armstrong number"

# Input the number of test cases
num_test_cases = int(input("Enter the number of test cases: "))

# Process each test case
for _ in range(num_test_cases):
    number = input("Enter a number: ")
    result = armstrong(number)
    print(number + result)

