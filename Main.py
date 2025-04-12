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
    return random.randint(min, max)

if __name__ == "__main__":
    testCall()
    print(getRandomString(10))
    print(getRandomInt(1, 10))