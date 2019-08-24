import hashlib
import base64
"""Assignment 11 Created"""

def hash(workingkey):
    key=bytes(workingkey,'utf-8')
    result = hashlib.md5(key).hexdigest()
    print("The Hash Value is : ", result)
    print("To Check and verify the result, please go to the following url --> http://www.md5.cz/ online md5 genertor Tool")

try:
    Input=input("Enter Key to Hash : ")
    if Input!="":
        hash(Input)
except Exception as e:
    print(e)
