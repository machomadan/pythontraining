"""4. Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

class List_tuple(object):

    def __init__(self):
        self.tup=()
        self.list=[]

    def data_update(self):
        temp=input("enter the numbers:")
        
        self.list.extend(temp.split(','))
        list1=list(self.tup)
        list1.extend(temp.split(','))
        tup1=tuple(list1)
        print(self.list, tup1)

my_list_tuple= List_tuple()

my_list_tuple.data_update()
