# 3.Write a program that:
# Asks the user for a number N.
# Prints numbers from 1 to N:
# Print "Fizz" for numbers divisible by 3.
# Print "Buzz" for numbers divisible by 5.
# Print "FizzBuzz" for numbers divisible by both 3 and 5.

a=int(input())
for i in range(1,a+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)