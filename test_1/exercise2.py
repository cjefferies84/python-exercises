

While True:
    my_float = float(raw_input("Enter a float: "))

    try:
    my_float = float(my_float)
    except Exception as e:
        print e
        print "That is not a float!"

    print type(my_float)



x = None
# used to hold a value of later use

File I/O # lecture notes


# always use the with statement with opening files
with open("text.txt", 'r') as f: #opening a txt file and retrieving context of file with automatically
    for line in f:               #closes the file for you when you leave the with scope
        print line
print f

# refer to modes of opening a file on lecture notes
#
#tuples are immutable - tuples are faster because they acutually hold the value itself, hence it does not have to go into memeory to find the value like lists
#lists in python are mutable - convenient but slower because they point to the address in memory that hold a value and have to retrieve the value

dictionary

d = {
    1: "one",
    2: "two",
    3: "three"
}

print d

#this will print {1: 'one', 2: 'two', 3: 'three'} for output

# dictionaries do not use an index, they use a key, in the example above the key's are 1:, 2:, and 3:

lists in python are very similar to stacks in other languages

slicing
- unique to python, this can be used with any collection (strings or lists) slicing is very useful when trying to pull out a subset of data
stride - how many items are we traversing
