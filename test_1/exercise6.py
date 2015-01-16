
def f_open(f):
    try:
        f = open('sleepyPuppies.txt', 'w')
        f.write("This is test file for exception handling!!")
    finally:
        print "Uh noooooooo!!!!!!!!, cannot find the file or read data"


def file_open(f):
    try:
        f = open('sleepyPuppies.txt', 'w')
        f.write("This is test file for exception handling!!")
    except IOError:
        print "Uh Oh, cannot find the file or read data"
    else:
        print "Written content in the file was successful"

f = open('sleepyPuppies.txt', 'w')
f.write("This is test file for exception handling!!")
with open('sleepyPuppies.txt', 'w') as f:
    f_open(f)
    file_open(f)
print "This block of code called the functions to handle the exception"




