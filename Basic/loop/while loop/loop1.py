# pallidromic

num2 = int(input("Enter a Number : "))
rev = 0
while num2 > 0 :
    rev = rev * 10 + num2 % 10
    num2 = num2 //10

if rev == num2:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")



num1 = int(input("Enter a Number : "))
rev = 0
while num1 > 0 :
    rev = rev * 10 + num1 % 10
    num1 = num1 //10
print(rev)


num = int(input("Enter a Number : "))

while num > 0 :
    print (num%10)
    num = num //10
   