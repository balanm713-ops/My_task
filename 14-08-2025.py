# qns 1 : Create a calculator that handles invalid input and division by zero

a = int(input())
b = int(input())
c = input()
match c:
    case 'add':
        print(a+b)
    case 'sub' :
        print(a-b)
    case 'div':
        if (b!=0):
            print(a/b)
        else:
             print("Invalid input")
    case 'mult':
        print(a*b)

# ---------------------------------------------------------------------

# question 2

from datetime import *

date1 = input("Give date :")
date2 = input("Give date :")

madhu = "%Y-%B-%d"

starting_date = datetime.strptime(date1,madhu)
ending_date  = datetime.strptime(date2, madhu)

calculating_days = ending_date-starting_date
remaining_days = calculating_days.days
print(f"Starting day: {date1}")
print(f"End date: {date2}")
print(f"Number of days between them: {remaining_days}")

# -----------------------------------------------------------------
# quns 3 : Find the sum of all numbers below 1000 that are multiples of 3 or 5. 

a = 0 
for i in range (1001):
    if (i%3==0 or i%5==0):
        a = a+i
        print(a)
        # print(i)

# --------------------------------------------------

 # qns 5 : Write a loop that finds the sum of even numbers between 1 and 100.

a = 0
for i in range (101):
    if (i%2==0):
        a = a+i
        print(a)