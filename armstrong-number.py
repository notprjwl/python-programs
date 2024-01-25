#153 armstrong number cause 1^3 + 5^3 + 3^3 = 153

num = (input("enter a number "))
sum = 0

for i in num:
    digit = int(i)
    power = digit**len(num)
    sum+=power


if sum == int(num):
    print(num + " is an armstrong number")
else:
    print(num + " is not an armstrong number") 


