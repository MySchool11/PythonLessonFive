__author__ = "Mr Bancroft"

# str function
age = 37
print("My age is " + str(age) + " years.")
# if you tried "print("my age is " + 37 + " years.")", Python will crash as it tries to add an int to a string
# the str() function attempts to cast the variable in the brackets to a string.

# replacement field
print("My age is {0} years.".format(age))
# the replacement field is the number in the curly braces. This is especially useful for multiple fields
months31 = ["31", "January", "March", "May", "July", "August", "October", "December"]
months30 = ["30", "April", "June", "September", "November"]
months2S = ["28", "29", "February"]
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(months31[0], months31[1],
months31[2], months31[3], months31[4], months31[5], months31[6], months31[7]))
print("There are {0} days in {1}, {2}, {3} and {4}".format(months30[0], months30[1], months30[2],
months30[3], months30[4]))
print("There are {0} or {1} days in {2}, depending on whether it is a leap year".format(months2S[0], months2S[1],
months2S[2]))
# as you can see, very helpful

