dict1={}
print("Enter the elements of first dictionary:")
while True:
    key = input("Enter a key(or 'q' to quit):")
    if key == 'q':
        break
    value=int(input("Enter a values:"))
    dict1[key]=value
dict2={}
print("Enter the elements of second dictionary:")
while True:
    key = input("Enter a key(or 'q' to quit):")
    if key == 'q':
        break
    value=int(input("Enter a values:"))
    dict2[key]=value
print(dict1|dict2)
