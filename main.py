__author__ = "Mr Bancroft"

import math

# str function
age = 37
print("My age is " + str(age) + " years.\n")
# if you tried "print("my age is " + 37 + " years.")", Python will crash as it tries to add an int to a string
# the str() function attempts to cast the variable in the brackets to a string.

# replacement field
print("My age is {0} years.\n".format(age))
# the replacement field is the number in the curly braces. This is especially useful for multiple fields
months31 = ["31", "January", "March", "May", "July", "August", "October", "December"]
months30 = ["30", "April", "June", "September", "November"]
months2S = ["28", "29", "February"]
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(months31[0], months31[1],
months31[2], months31[3], months31[4], months31[5], months31[6], months31[7]))
print("There are {0} days in {1}, {2}, {3} and {4}".format(months30[0], months30[1], months30[2],
months30[3], months30[4]))
print("There are {0} or {1} days in {2}, depending on whether it is a leap year".format(months2S[0], months2S[1],
months2S[2]) + "\n")
# as you can see, very helpful

# replacement fields can mix and match variable types
print("Pi == {0}, so said {1} around {2} B.C.".format(3.141592654, "Archimedes of Syracuse", 210) + "\n")
# here we have a double, a string and an integer

# triple quotes can also be useful when formatting groups of string data
print("""Days in the months -->\n
January:    {2}
February:   {0}
March:      {2}
April:      {1}
May:        {2}
June:       {1}
July:       {2}
August:     {2}
September:  {1}
October:    {2}
November:   {1}
December:   {2}""".format(28, 30, 31) + "\n")
# the triple quotes, of course, maintain the formatting from the code, note the same variable can be used multiple times

# string formatting operator (deprecated - you can use it but it is not recommended in Python 3)
print("My age is %d years." % age)
print("My age is %d %s, %d %s." % (age, "years", 7, "months"))
# the letter following the % must relate to the data type you wish to put there, the list of type is:
# %d    signed integer decimal
# %i    signed integer decimal
# %o    signed octal
# %u    unsigned decimal
# %x    unsigned hexadecimal (lowercase e.g. 3de3d)
# %X    unsigned hexadeicmal (uppercase e.g. 3DE3D)
# %e    floating point exponential format (lowercase e.g. 1.00e+02)
# %E    floating point exponential format (uppercase e.g. 1.00E+02)
# %f    floating point decimal format
# %F    floating point decimal format
# %g    same as "e" if exponent is greater than -4 or less than precision (otherwise f)
# %G    same as "E" if exponent is greater than -4 or less than precision (otherwise E)
# %c    Single character (char)
# %r    string (python object converted with %repr())
# %s    string (python object converted with %str())
# %     No argument just give a % character in the result
# now you can see why this method is deprecated (talk about confusing!!)
# this old method could also be used to allocate space for the outputs
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d." % (i, i ** 2, i ** 3))
# specify precision by:
print("\nPi is approximately (5 decimal places) %.5f" % math.pi)
print("\nPi is approximately (10 decimal places) %.10f" % math.pi)
# now you know these string formatters DO NOT USE THEM. Just be aware of them because Python 2 code may use them


