clst1 = set()
clst2 = set()
n1 = int(input("Enter the number of colors in List1: "))
print("Enter the colors LIST1: ")
for x in range(n1):
    color = input()
    clst1.add(color)
n2 = int(input("Enter the number of colors in List2: "))
print("Enter the colors to LIST2: ")
for x in range(n2):
    color = input()
    clst2.add(color)
diff = clst1.difference(clst2)
print("COLORS IN LIST1 IS NOT LIST2: ",diff)
