# 
c = "nkdsfknKNJCVKJ@###%%%%4467568764873"

char = 0
dig = 0
special  = 0

for i in c :
    if i.isalpha():
        char+=1
    elif i.isdigit():
        dig+=1
    else:
        special+=1
print(f"Characters : {char},Digits : {dig} , Special Characters :{special}")                

#pallindrome
a = input("Enter a word: ")
b = ""
for i in range (len(a)-1,-1,-1):
    b += a[i]

if (b == a):
    print(f"{a} is a pallindrome string")
else:
    print(f"{a} is not a pallindrome string")    


# reverse string 
a = "Riddhima"
b = ""
for i in range (len(a)-1,-1,-1):
    b += a[i]
print(b)

# check whether number is prime or not 
num = int(input("Enter a Number : "))
count = 0
for i in range (1, num+1):
    if num % i == 0:
        count +=1

if count == 2 :
    print(f"{num} is a prime number")
else:    
    print(f"{num} is not a prime number")

#check whether number is prefect or not 
num = int(input("Enter a Number : "))
sum = 0
for i in range (1, num):
    if num % i == 0:
        print(i)

        sum +=i
if (sum == num):
    print (f"{num} is a prefect number")
else:
     print (f"{num} is not a prefect number")    

# print hello world 
num = int(input("Enter a Number : "))

for i in range (num):
    print ("Hello World")

#Factors
num = int(input("Enter a Number : "))

for i in range (1 , num+1):
    if num % i == 0:
        print (i)

#factorial
num = int(input("Enter a Number : "))
fact = 1
if ( num < 0):
    print("Factorial is not defined for negative numbers")
else:
    for i in range (1 , num +1 ):
        fact *= i
        print (fact)

# sum of n numbers
num = int(input("Enter a Number : "))
sum = 0
evn_sum = 0 
odd_sum = 0
for i in range (1 , num +1 ):
    if i % 2 == 0: evn_sum += i
    else : odd_sum += i 

    sum += i
    
print (sum)
print (f"Sum of Even Number  is {evn_sum} and Sum of Odd Number is {odd_sum}")

num = int(input("Enter a Number : "))

for i in range (num, 0 , -1):
    print (i)


# print number
num = int(input("Enter a Number : "))

for i in range (num +1):
    print (i)    

#multiplication
num = int(input("Enter a Number : "))

for i in range (10):
    print (f"{num} * {i +1 } = {num * (i+1)}")