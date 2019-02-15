"""9. Write a program that accepts sequence of lines as input and
prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""

class Capital(object):

    def __init__(self):
        self.l=[]

    def make_caps(self,my_list):
        print(my_list)
        for i in range(len(my_list)):
            print(my_list[i].upper())


my_capital=Capital()

my_list=[]
for i in range(3):
    sentence=input("enter the sentence :")
    my_list.append(sentence)
    

my_capital.make_caps(my_list)


        
