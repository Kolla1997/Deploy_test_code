import requests
import json
import os
import time
import random
import string


def testCall():
    print("testCall()")

def getRandomString(length):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    print(''.join(random.choice(letters) for i in range(length)))

def getRandomInt(min, max):
    """Generate a random integer between min and max"""
    print(random.randint(min, max))


def getSquare(num):
    """Return the square of a number"""
    print(num ** 2)

def printProgressbar(iteration, total, prefix='', length=40, fill='█', printEnd='\r'):
    """Prints a progress bar in the console"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% Complete', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

if __name__ == "__main__":
    testCall()
    getRandomString(10)
    getRandomInt(1, 10)
    getSquare(5)
    printProgressbar(5, 10, prefix='Progress', length=50)