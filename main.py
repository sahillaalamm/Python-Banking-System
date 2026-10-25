# string slicing
# a = str(input("Enter your name "))
# print(a[0:5])

# Q1. accept numbers from a user
# num = int(input("Enter a number "))
# print(f"Number is {num}")

# Q2. accept age from a user
# age = int(input("Enter your age "))
# print(f"Age is {age}")


# conditional statements questions

# 1 accept two numbers and print greatest between them

# n1 = int(input("Enter number 1- "))
# n2 = int(input("Enter number 2- "))

# if n1>n2:
#     print(f"{n1} is greater than {n2}")

# elif n2 > n1:
#     print(f"{n2} is greater than {n1}")

# else:
#     print("Both numbers are same")



# 2 accept the gender from the user as char and print the respective greeting message Ex- Good Morning Sir (on the basis of gender)

# gender = str(input("Enter your Gender as Char (M or F)- "))

# if gender == "M" or gender == "m":
#     print("Good Morning Sir")

# elif gender == "F" or gender == "f":
#     print("Good Morning Ma'am")

# else:
#     print("Enter correct value")



# 3 accept an integer and check whether it is even number or odd number

# num = int(input("Enter a number- "))

# if num%2 == 0:
#     print(f"{num} is an even number")

# else:
#     print(f"{num} is an odd number")



# 4 accept name and age from the user and check whether the user is valid user or not

# name = str(input("Enter your name- "))
# age = int(input("Enter your age- "))

# if age >= 18:
#     print(f"{name} you can vote")

# elif age >= 0 and age <=17:
#     print(f"{name} you cannot vote")
    
# else:
#     print("Enter correct details")



# 5 accept a year and check if it is a leap year or not

# year = int(input("Enter any year- "))

# if year%100 == 0 and year % 400 ==0:
#     print(f"{year} is a leap year")

# elif year%100 != 0 and year%4 == 0:
#     print(f"{year} is a leap year")

# else:
#     print("It's not a leap year")



# 6 

# temp = int(input("Enter Temperature in Celcius- "))
# if temp < 0:
#     print("Freezing Cold")

# elif temp >= 0 and temp <= 10:
#     print("Very Cold")

# elif temp >= 11 and temp <= 20:
#     print("Cold")

# elif temp >= 21 and temp <= 30:
#     print("Pleasent")

# elif temp >= 31 and temp <= 40:
#     print("Hot")

# else:
#     print("Very Hot")



# For Loop

# 1 take an input from user and print its table

# n = int(input("Which table you want"))

# for i in range(n,(n*10)+1,n):
#     print(i)



# 2 accept an integer and print hello world n times

# num = int(input("Enter a number- "))

# for i in range(0,num,1):
#     print("Hello world")



# 3 print natural number upto n

# n = int(input("Enter a number- "))
# for i in range(1,n+1,1):
#     print(i)



# 4 reverse for loop print n to 1

# num = int(input("Enter a number- "))

# for i in range(num, 0, -1):
#     print(i)



# 5 take a number as input and print its table

# n = int(input("Enter number for table- "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")



# 6 sum upto n terms

# n = int(input("Enter a number- "))

# sum =0

# for i in range(1, sum+1):
#     sum = sum + i

# print(f"Your sum is {sum}")



# 7 print factorial of a number

# n = int(input("Enter a number- "))

# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print(f"Your factorial is {fact}")



# 8 print the sum of all even & odd numbers in a range separately

# n = int(input("Enter a number- "))

# even = 0
# odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"Even and Odd sums are {even}, {odd}")



# 9 print all the factors of a number

# n = int(input("Which number factors do you want- "))

# for i in range(1, n+1):
#     if n%1 == 0:
#         print(i)



# 10 accept a number and check whether it is a perfect number or not

# n= int(input("Check whether number is perfect or not- "))
# sum = 0

# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print(f"{n} is a Perfect Number")
# else:
#     print(f"{n} is not a Perfect Number")



# 11 Check whether the number is prime or not

# n = int(input("Check whether the number is prime or not- "))
# count_fact = 0

# for i in range(1,n+1):
#     if n%i==0:
#         count_fact +=1

# print(count_fact)

# if count_fact == 2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is a composite number")



# 12 reverse a string without using inbuilt functions


# a = "SHERYIANS"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)



# 13 check if a number is pallindrom or not


# a = "SHERYIANS"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if b == a:
#     print(f"{a} is a pallindrome")
# else:
#     print(f"{a} is not a pallindrome")



# 14 count all letters, digits, special symbols from a given string

# a = "lugilby451!@#$%"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         spchr+= 1
        
# print(f"Your Digits are {dig}\nyour Alphabets are {char}\nyour Special Characters are {spchr}")



# while loop questions

# 1 separate each digit of a number and print it on a new line

# a = 256
# while a>0:
#     print(a%10)
#     a = a//10


# 2 accept a number and print its reverse

# a = int(input("Tell a Number- "))
# rev = 0

# while a>0:
#     rev = rev*10 + a%10
#     a = a//10



# 2 accept a number and print its reverse

# a = int(input("Tell a Number- "))
# copy = a
# rev = 0

# while a>0:
#     rev = rev*10 + a%10
#     a = a//10

# if copy == rev:
#     print("Its a Pallindromic Number")
# else:
#     print("Its not a Pallindromic Number")


# mini game - Random number guessing game

# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("Guess your Number between 1 to 10- "))

#     if num == guess:
#         tries += 1
#         print(f"You are right you guessed the number in {tries} try")
#         break

#     elif num < guess:
#         print("Try a little lower number")
#         tries += 1

#     elif num > guess:
#         print("Try a little higher number")
#         tries += 1
    
#     else:
#         print("Sorry You are Wrong")




# Function - positional argument, default argument, keyword argument

# positional argument
# def add(a, b):
#     return a+b

# print(add(10,12))     # 10 is assigned to 'a', 12 is assigned to 'b'



# default argument
# def introduce(name, age):
#     print(f"Hello my name is {name} and ny age is {age}")

# introduce(age = 23, name = "Sahil")



# keyword argument
# def greet(name = "Guest"):
#     print(f"Hello {name}")

# greet()         # it uses default value "Guest"
# greet("Friends")    #uses "Friends"



# Q. check whether a string is a pallindrome or not by using function

# def pallindrome(str):
#     rev = ""
#     for i in range(len(str)-1,-1,-1):
#         rev = rev + str[i]

#     if rev == str:
#         print(f"{str} is a pallindromic string")
#     else:
#         print(f"{str} is not a pallindromic string")

# pallindrome("naman")
# pallindrome("amma")


# a = [10,20,30,40]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])




# Q.1 Print Positive and Negative Elements of an List

# l = [-45, 67, 12, -68, -23, 8]

# print("Positive Elements are-")
# for i in l:
#     if i >= 0:
#         print(i)

# print("\nNegative Elements are-")
# for i in l:
#     if i < 0:
#         print(i)


# Q2.Print mean of list element

# a = [12, 435, 67, 89, 23, 25, 69]

# sum = 0

# for i in a:
#     sum = sum + i

# print(f"Sum is- {sum}")
# print(f"Mean is- {sum/len(a)}")



# Q.3 Find the greatest element and print it's index too


# a = [142, 264, 375, 489, 458]

# largest = a[0]
# index = 0

# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i

# print(f"Largest Element is {largest} at index {index}")



# Q. 4 Find the second greatest element

# a = [12, 16, 13, 19]

# largest = a[0]
# sec_largest = a[0]

# for i in a:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest, largest)



# Q.5 Check if list is sorted or not


# a = [12, 13, 14, 15, 16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("Your List is not sorted")
#         break
# else:
#     print("Your List is sorted")



# Q1. Write a Python script to merge two python dictionaries

# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)



# Q2. Write a python program to sum all the values in a dictionary

# d1 = {1:100, 2:200, 3:300, 4:400}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)



# Q.3 count the frequency of each elements in a list

# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8,]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)


# Q.4 Write a python prgoram to combine two dictionary by adding values for common keys


# d1 = {1:100, 2:200, 4:300}
# d2 = {4:400, 5:500, 6:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)



# exception handling

# age = int(input("Enter your age- "))

# try:
#     if age<10 or age>18:
#         raise ValueError("Your age must be between 10 and 18")
#     else:
#         print("Welcome to the Team")

# except Exception as err:
#     print(f"an error occured as {err}")

# print("Matches will start soon")



# --------- Object Oriented Programming --------


# imperative approach
# a = 8
# b = 10
# print(a+b)


# functional approach
# def add(c,d):
#     print(c+d)

# add(20, 30)


# object oriented programming approach
# class Addition:
#     def __init__(self, a,b):
#         print(a+b)

# obj = Addition(7,5)


# what are attributes?
# variables defined inside class are attributes


# what are methods?
# functions defined inside a class are methods


