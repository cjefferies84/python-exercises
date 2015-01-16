# # must define gall_input to accept raw_input string to avoid ValueError
# gall_input = raw_input("Please enter number of gallons: ")
# # if user input is not a number or user input is a #number  and it's value is <= 0
# # then we #continues to the if statement conditions
# while gall_input.isalpha() or (not gall_input.isalpha() and float(gall_input) <= 0):
#     if gall_input.isdigit() and float(gall_input) <= 0:
#         print "You cannot enter 0, please enter a number"
#         gall_input = raw_input("Please enter number of gallons: ")
#     elif not gall_input.isdigit():
#         print "You must enter a number please"
#         gall_input = raw_input("Please enter number of gallons: ")
# # after while loop must redefine gall_input from raw_input string to convert to a float
# gall_input = float(gall_input)
#
# print "The original number of gallons is: " + str(gall_input)
# # conversions of each parameter of exercise
# liters_conversion = " gallons is the equivalent of " + str(gall_input * 3.07854117847) + " liters of gas"
# barrels_conversion = " gallons of gasoline requires " + str(gall_input * 19.5) + " barrels of oil"
# carbon_d_conversion = " gallons of gasoline produces " + str(gall_input * 20) + " pounds of CO2"
# ethanol_conversion = " gallons of gasoline produces " + str(gall_input * 75700) + " British Thermal Units"
# cost_per_gall = " gallons of gasoline requires $" + str(gall_input * 4) + " US dollars"
# print str(gall_input) + liters_conversion
# print str(gall_input) + barrels_conversion
# print str(gall_input) + carbon_d_conversion
# print str(gall_input) + ethanol_conversion
# print str(gall_input)

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
mach = " Converted to Mach number is: " + str(float(mph_input/768.6))
sp_of_light = " Converted to the percentage of the speed of light is: " + str(float(mph_input/670616629*100))


print str(mph_input) + b_corn
print str(mph_input) + furlong
print str(mph_input) + mach
print str(mph_input) + sp_of_light
print "Thanks of playing the conversion game"




