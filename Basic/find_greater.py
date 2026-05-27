num_1 = int(input("Enter First Number :"))
num_2 = int(input("Enter Second Number :"))

if num_1 > num_2:
    print (f"{num_1} is greater than {num_2}") 

elif num_1 < num_2:
    print (f"{num_2} is greater than {num_1}")

elif num_1 == num_2:
    print (f"{num_1} is equal to {num_2}") 

else:
    print ("Enter valid numbers")       