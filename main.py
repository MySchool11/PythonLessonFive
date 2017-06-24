__author__ = "Mr Bancroft"

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
# the triple quotes, of course, maintain the formatting from the code

