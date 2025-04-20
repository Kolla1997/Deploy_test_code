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
    random_string = ''.join(random.choice(letters) for i in range(length))
    print(f"Random String of length {length}: {random_string}")

def getRandomInt(min, max):
    """Generate a random integer between min and max"""
    random_int = random.randint(min, max)
    print(f"Random Integer: {random_int}")
    return random_int

def printProgressbar(iteration, total, prefix='', length=40, fill='█', printEnd='\r'):
    """Prints a progress bar in the console"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% Complete', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def getSquareOfNumber(num):
    """Return the square of a number"""
    print(f"Get Square: {num ** 2}")

if __name__ == "__main__":
    testCall()
    random_length = getRandomInt(1, 10)  # Generate random integer
    getRandomString(random_length)
    printProgressbar(5, 10, prefix='Progress', length=50)
    getSquareOfNumber(5)