first_num = raw_input("Please enter the first integer: ")
second_num = raw_input("Please enter the second integer: ")
if first_num.is_digit() or second_num.is_digit():
        print "Both integers should be numbers, not something else!"
        quit()

num1 = int(first_num)
num2 = int(second_num)
if num2 == 0:  # second number input cannot equal zero
        print "The second number would cause a divide by zero exception!"
        quit()

print "The sum of %d and %d is: %d" %(num1, num2, num1 + num2)
print "The difference of %d and %d is: %d" %(num1, num2, num1 - num2)
print "The product of %d and %d is: %d" %(num1, num2, num1 * num2)
print "The quotient of %d and %d is: %d with remainder %d" %(num1, num2, num1 / num2, num1 % num2)