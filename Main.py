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

if __name__ == "__main__":
    testCall()
    getRandomString(10)
    getRandomInt(1, 10)
    getSquare(5)