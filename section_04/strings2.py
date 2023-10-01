number = "9,223;372,036 854,775;807"
separators = ""

#    This loop extracts the characters that don't belong in the number group to a string
for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

#    These lines extract the numbers contained in the number variable, and stores them into an array
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
