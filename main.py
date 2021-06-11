#Syntax
if 5 > 2:
  print("Five is greater than two!")


#Variables 
x = 5
y = "John"
print(x)
print(y)
#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))
#Variable names are case-sensitive
a = 4
A = "Sally"
#A will not overwrite a
#Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#And you can assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)
#If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#The Python print statement is often used to output variables .To combine both text and a variable, Python uses the + character
x = "awesome"
print("Python is " + x)
#You can also use the + character to add a variable to another variable
x = "Python is "
y = "awesome"
z =  x + y
print(z)
#For numbers, the + character works as a mathematical operator
x = 5
y = 10
print(x + y)
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.Global variables can be used by everyone, both inside of functions and outside.
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()

print("Python is " + x)
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#datatypes 
#built in data types 
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
x = 5
print(type(x))
x = "hello world"
#int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
#here may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

#Casting in python is therefore done using constructor  functionsint() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)     float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings
a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)
  #To get the length of a string, use the len() function.
  #The len() function returns the length of a string:
  a = "Hello, World!"
print(len(a))
#To check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)
#Print only if "free" is present:
txt = "The best things in life are a glee!"
if "free" in txt:
  print("Yes, 'free' is present.")
else:
   print("No , 'free' is not present" )
    #To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
txt = "The best things in life are free!"
print("expensive" not in txt)
#print only if "expensive" is NOT present:
txt = "The best things in life are expensive!"
if "expensive" not in txt:
 print("Yes, 'expensive' is NOT present.")
else:
  print("you are dumb")
#You can return a range of characters by using the slice syntax.Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])
#By leaving out the start index, the range will start at the first character
b = "Hello, World!"
print(b[:5])
#By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])
#Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])
#the upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#the split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#But we can combine strings and numbers by using the format() method!The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#To insert characters that are illegal in a string, use an escape character.An escape character is a backslash \ followed by the character you want to insert.An example of an illegal character is a double quote inside a string that is surrounded by double quotes
txt = "We are the so-called \"Vikings\" from the north."
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value


#Python has a set of built-in methods that you can use on strings

#Method	Description
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning


#Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)
#
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
#The following will return true 
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#The following will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())
#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))



#Operators are used to perform operations on variables and values.
print(10 + 5)

#+=	x += 3	x = x + 3	
#-=	x -= 3	x = x - 3	
#*=	x *= 3	x = x * 3	
#/=	x /= 3	x = x / 3	
#%=	x %= 3	x = x % 3	
#//=	x //= 3	x = x // 3	
#**=	x **= 3	x = x ** 3	
#&=	x &= 3	x = x & 3	
#|=	x |= 3	x = x | 3	
#^=	x ^= 3	x = x ^ 3	
#>>=	x >>= 3	x = x >> 3	
#<<=	x <<= 3	x = x << 3

#==	Equal	x == y	
#!=	Not equal	x != y	
#>	Greater than	x > y	
#<	Less than	x < y	
#>=	Greater than or equal to	x >= y	
#<=	Less than or equal to	x <= y

#and 	Returns True if both statements are true	
x < 5 and  x < 10	
#or	Returns True if one of the statements is true	
x < 5 or x < 4	
#not	Reverse the result, returns False if the result is true	not
(x < 5 and x < 10)	

#is 	Returns True if both variables are the same object	
x is y	
#is not	Returns True if both variables are not the same object	
x is not y