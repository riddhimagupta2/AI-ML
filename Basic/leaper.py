year = int(input("Enter First Number :"))

if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print (f"{year} is leap year")
elif year % 2 != 0:
    print (f"{year} is not leap year")

else:
    print ("Enter valid numbers")       