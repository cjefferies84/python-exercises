

# must define mph_input to accept raw_input string to avoid ValueError
mph_input = raw_input("Please enter speed in miles per hour: ")
# if user input is not a number or user input is a #number  and it's value is <= 0
# then we #continues to the if statement conditions
while mph_input.isalpha() or (not mph_input.isalpha() and float(mph_input) <= 0):
    if mph_input.isdigit() and float(mph_input) <= 0:
        print "You cannot enter 0, please enter a number"
        mph_input = raw_input("Please enter speed in miles per hour: ")
    elif not mph_input.isdigit():
        print "You must enter a number please"
        mph_input = raw_input("Please enter speed in miles per hour: ")
# after while loop must redefine gall_input from raw_input string to convert to a float
mph_input = float(mph_input)
print "The original speed in mph is: " + str(mph_input)
b_corn = " Converted to barleycorn is: " + str(mph_input * (189334.02298 * 24))
furlong = " Converted to furlongs is:  " + str(mph_input * float(192 * 14))
mach = " Converted to Mach number is: " + str(mph_input/768.6)
sp_of_light = " Converted to the percentage of the speed of light is: " + str(mph_input/670616629*100)

print str(mph_input) + b_corn
print str(mph_input) + furlong
print str(mph_input) + mach
print str(mph_input) + sp_of_light
