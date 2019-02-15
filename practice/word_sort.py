"""8. Write a program that accepts a comma separated sequence of words as
input and prints the words in a comma-separated sequence after sorting them
alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

class Sort(object):

    def __init__(self):
        self.l=[]


    def word_sort(self,word):

        for i in word.split(','):
            self.l.append(i)

        self.l.sort()
        
        print(*self.l, sep=',')

my_sort=Sort()

word=input("enter the words to be sorted :")
my_sort.word_sort(word)
