import string
from random import choice
from random import randint
import random
import csv


FILE_NAME = "strings.txt"


def generate_random_string():
    """Generate 10 random strings and write them to a file called 'strings.txt'."""

    with open(FILE_NAME, "w") as f:
        for i in range(0, 11):
            random_integer = randint(0, 101)
            s = ''.join(random.sample(string.letters*10, random_integer))

            f.write(s + "\n")


def pretty_print_counts(counts):
    for key, value in counts.items():
        print "%s -> %s" % (key, value)


def letter_counter():
    with open(FILE_NAME, "r") as f:
        for random_string in f:
            counts = {}
            for character in random_string:
                if character in counts:
                    counts[character] += 1
                else:
                    counts[character] = 1

            print random_string + "contains: "
            pretty_print_counts(counts)


def read_book():
    bible = dict()
    f = open("bible 2.txt", "r")
    reader = csv.reader(open('bible 2.txt', 'rb'), delimiter="|")

    word_list = []
    f = open("bible 2.txt", "r")
    reader = csv.reader(open('bible 2.txt', 'rb'), delimiter="|")

    f.close()

def clean_list(word_list):
        clean_word_list = []
        for word in word_list:
            symbols = "!@#$%^&*()=-""; "
            for i in range(0, len(symbols)):
                word = word.replace(symbols[i], "")
                if len(word) > 0:
                    print(word)
                    clean_word_list.append(word)


generate_random_string()
letter_counter()
# print clean_list(word_list)
# letter_counter("upper")
#
# letter_counter("lower")


wordCount = {}

# for word in string.split(s):
#     if word not in wordCount:
#             wordCount[word] = 1
#     else:  # in word count
#             wordCount[word] += 1
# wordCount
# # getting keys and values
# wordCountList = [(v, k) for k, v in wordCount.items()]
# wordCountList
# # sort most common word to least common word, must use reverse of default
# wordCountList.sort(reverse=True)
# for word in wordCountList:
#     # the word is the second and count is the first
#     print "10%s : %d" % (word[1], word[0])





