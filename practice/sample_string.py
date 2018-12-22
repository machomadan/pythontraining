"""5. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class String(object):

    def __init__(self):
        self.mystr=""

    def getString(self):
        self.mystr=input("enter any string:")

    def printString(self):
        print(self.mystr)
        
    def upper(self):
        print("string upper value is :" + self.mystr.upper())

myString=String()

myString.getString()
myString.printString()
myString.upper()
        
        
        
