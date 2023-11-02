"""
The following are practice examples on strings
"""
my_string = "The big, brown Fox"
# print the first 10 characters of the string in a single line

print(my_string[:10])

# Check if a certain word is in the string
print("brown" in my_string)
print("Blue" in my_string)

# Check if my string is if title form (i.e. follows the rules of a title
print(my_string.istitle())

new_string = "The Big Brown Fox"
print(new_string.istitle())
# Reverse the string
print(my_string[::-1])

# Modifying the strings
a = " Hello, World "
print(a.upper())  # prints the string in uppercase
print(a.lower())  # prints the string in lowercase
print(a.capitalize())  # Makes the first character a capital letter
print(len(a))  # Returns the length of the string
print(a.strip())  # Removes whitespaces before and after the string
print(len(a.strip()))  # To check the effect of the .strip() method
print(a.split(','))  # Returns a list based on the separator provided. In this case(,)

# Using the format() method
age = 36
my_text = "This is Agnes, she is {} years old"
print(my_text.format(age))

# We can also specify the placement of items in the format() method using indexing
Name = "Alice"
Age = "28"
Location = "Sweden"

txt = "This is {2}. She is {0} years old and lives in {1}"

print(txt.format(28, "Sweden", "Alice"))
print(a.encode())
