print("Enter 3 numbers: ")
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

if(n1>n2 and n1>n3):
    print(n1," is the biggest!")
elif(n2>n3):
    print(n2," is the biggest!")
else:
    print(n3," is the biggest!")
