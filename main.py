text = "hello world!"
print(len(text))
# Slicing
print(text[6])
print(text[0:12])
print(text[0:5])

# Slice From the Start
print(text[:6])
print(text[:9])
# print(text[:9:2])
# Slice To the End
print(text[6:])
# Negative Indexing
# it starts from -1 to -n from the end of the string
print(text[-1])
print(text[-6:-1])

# String Methods
print(text.upper())
print(text.lower()) 
print(text.capitalize())
print(text.title())
# Remove Whitespace
text2 = "   hello world!   "
print(text2)
print(text2.strip())
# Replace
print(text.replace("h", "H"))
print(text.replace("h", "B").replace("o", "a").replace("l", "🤪").replace("!", "😂"))
# Split
print(text.split(","))

# f-strings
age = 39
name = "Amin"
occupation = "Developer"
print(f"My name is {name} and I am {age} years old and I am a {occupation}.")

# placeholder
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {price * 1.1:.3f} dollars"
print(txt)
# escape characters
print("We are the so-called \"Vikings\" from the north.")
print('It\'s alright.')
print("This is a backslash: \\")
print("First line.\nSecond line.")
print("Name\tAge\tCity") # tab
print("Hello\bWorld!") # backspace
print("Hello\rWorld!") # carriage return
print("Hello\vWorld!")  # vertical tab
# print("Hello\fWorld!") # form feed
print("Hello\aWorld!") # alert (bell)
print("Hello\0World!") # null character
print("Hello\U0001F600World!")  # Unicode character (grinning face)
print("Hello\N{GRINNING FACE}World!")  # Named Unicode character (
print("Salam\033[1;32;40m Amin!\033[0m")  # ANSI escape code for colored text

# hexadecimal value 
print("\x48\x65\x6c\x6c\x6f")  # prints "Hello"

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
print(text.zfill(20))
print("42".zfill(5))
print("hello".capitalize())
print("hello".upper())
