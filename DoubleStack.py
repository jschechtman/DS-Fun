"""
DoubleStack.py
A simple implementation of a space-efficient double stack in Python. Elements of first stack
are pushed and popped at the beginning of the list, elements of second are pushed and popped
from the end. 
John Schechtman-Marko
"""

class DoubleStack:
    #Creates underlying list, size tracking variable, 
    #and variable tracking index of final element of 
    #first stack.
    def __init__(self):
        self.data = []
        self.size = 0
        self.last1 = None 
    
   #Adds element of stack 1
   #to beginning of list
    def push1(self, element):
        self.data.insert(0, element)
        self.size += 1
        #If stack 1 was empty, set last1
        #to first element of list. Otherwise 
        #increment it.
        if self.last1 == None:
            self.last1 = 0
        else:
            self.last1 += 1
    
    #Add element to Stack 2 at end of list
    #and increment size
    def push2(self, element):
        self.data.append(element)
        self.size += 1
    
    #Remove element of stack 1 from start of list
    def pop1(self):
        #If stack 1 is empty return none
        if self.last1 == None:
            return None
        #Pop first element of list
        else:
            oldVal = self.data[0]
            self.data.pop(0)
            self.size -= 1
            self.last1 -= 1
            #Set last1 to none if
            #stack 1 is empty
            if self.last1 < 0:
                self.last1 = None
            return oldVal
                
    def pop2(self):
        #Empty stack 2: return none
        if self.size == 0 or self.last1 == self.size-1:
            return None
        #Non-empty stack,empty stack1: remove last 
        #value, de-increment size
        else:
            oldVal = self.data[len(self.data)-1]
            self.data.pop()
            self.size -= 1
    
    def peek1():
        if self.last1 == None: #If stack 1 is empty
            return None
        else:
            return self.data[self.last1]
        
    def peek2():
        if self.size == 0 or self.last1 == self.size-1: #Empty stack 2
            return None
        else: 
            return self.data[self.size-1]
