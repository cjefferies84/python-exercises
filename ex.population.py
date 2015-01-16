
# must define mph_input to accept raw_input string to avoid ValueError
count = 0
x = 0
y = 0
year_input = (raw_input("How many years into the future would you like to predict?:  "))
pop_current = x
x == float(307357870)
yearly_pop_change = y
y == float(2980325.2747252)
val_1 = float(year_input * yearly_pop_change) - float(pop_current)
val_2 = float(val_1 - pop_current)

# if user input is not a number or user input is a #number  and it's value is <= 0
# then we continue to the if statement conditions
while year_input.isalpha() or (year_input.isalpha() and (year_input()) <= 0):
    if year_input.isdigit() and str(year_input) <= 0:
        print "You cannot enter 0, please enter a number"
        year_input = raw_input("How many years into the future would you like to predict?:  ")
    elif not year_input.isdigit():
        print "You must enter a number please"
        year_input = raw_input("How many years into the future would you like to predict?:  ")
while yearly_pop_change == 2980325.2747252:
    yearly_pop_change = x + 1
# after while loop must redefine gall_input from raw_input string to convert to a float
year_input = int(year_input)
val_1 = str(val_1)
val_2 = str(val_2)

new_pop1 = " The new population in  " + (year_input + 1) + " years will change by " + val_1 + " to be " + val_2
new_pop2 = " The new population in  " + year_input + " years will change by " + val_1 + " to be " + val_2
new_pop3 = " The new population in  " + str(year_input) + " years will change by " + str(val_1) + " to be " + str(val_2)
new_pop4 = " The new population in  " + str(year_input) + " years will change by " + str(val_1) + " to be " + str(val_2)

print year_input + new_pop1
print str(year_input) + str(new_pop2)
print str(year_input) + str(new_pop3)
print str(year_input) + str(new_pop4)