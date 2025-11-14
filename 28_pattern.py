# 28.Pyramid Pattern
step = 5
# print upper part
for i in range(1,step+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# print lower part
for i in range(step-1,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()