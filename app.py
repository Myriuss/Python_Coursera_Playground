import re

filename = input("Enter the name of the file: ")
handle = open(filename)
contents = handle.read()
numbers = re.findall(r'\d+', contents)
numbers = list(map(int, numbers))
total = sum(numbers)
print("The sum of the numbers in the file is:", total)
handle.close()
