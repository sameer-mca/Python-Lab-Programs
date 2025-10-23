string = input("ENTER STRING: ")
length_of_str = len(string)
first = string[0]
last = string[length_of_str - 1]
mod_str = last +string[1:length_of_str - 1]+first
print("Modified string: ",mod_str)
