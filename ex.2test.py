
# must define gall_input to accept raw_input string to avoid ValueError
gall_input = raw_input("Please enter number of gallons: ")
# if user input is not a number or user input is a #number  and it's value is <= 0
# then we #continues to the if statement conditions
while gall_input.isalpha() or (not gall_input.isalpha() and float(gall_input) <= 0):
    if gall_input.isdigit() and float(gall_input) <= 0:
        print "You cannot enter 0, please enter a number"
        gall_input = raw_input("Please enter number of gallons: ")
    elif not gall_input.isdigit():
        print "You must enter a number please"
        gall_input = raw_input("Please enter number of gallons: ")
# after while loop must redefine gall_input from raw_input string to convert to a float
gall_input = float(gall_input)

print "The original number of gallons is: " + str(gall_input)
# conversions of each parameter of exercise
liters_conversion = " gallons is the equivalent of " + str(gall_input * 3.07854117847) + " liters of gas"
barrels_conversion = " gallons of gasoline requires " + str(gall_input * 19.5) + " barrels of oil"
carbon_d_conversion = " gallons of gasoline produces " + str(gall_input * 20) + " pounds of CO2"
ethanol_conversion = " gallons of gasoline produces " + str(gall_input * 75700) + " British Thermal Units"
cost_per_gall = " gallons of gasoline requires $" + str(gall_input * 4) + " US dollars"
print str(gall_input) + liters_conversion
print str(gall_input) + barrels_conversion
print str(gall_input) + carbon_d_conversion
print str(gall_input) + ethanol_conversion
print str(gall_input) + cost_per_gall
