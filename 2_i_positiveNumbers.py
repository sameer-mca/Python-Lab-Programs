n=int(input("Enter the limt:"))
num=[]
for x in range(n):
    element=int(input("Enter the elements:"))
    num.append(element)
print("List:",num)
print("Positive numbers:")
for x in num:
    if(x>0):
        print(x)
