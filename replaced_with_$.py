n = input("enter a string for modification : ")
length = len(n)
first = str(n[0])
replace = "$"
length = length - 1
last = replace * length 
print(first + str(last))
