num=[]
n=int(input("Enter the numbers of elements:"))
print("ENTER THE LIST OF INTEGERS:")
for i in range(1,n+1):
    e=int(input())
    if(e>100):
        num.append("OVER")
    else:
        num.append(e)
print("Enter list:",num)
