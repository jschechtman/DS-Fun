class DoubleStack:
    def __init__(self):
        self.data = []
        self.size = 0
        self.last1 = None
        
    def push1(self, element):
        self.data.insert(0, element)
        self.size += 1
        if self.last1 == None:
            self.last1 = 0
        else:
            self.last1 += 1
            
    def push2(self, element):
        self.data.append(element)
        self.size += 1
        
    def pop1(self):
        if self.last1 == None:
            return None
        else:
            oldVal = self.data[0]
            self.data.pop(0)
            self.size -= 1
            self.last1 -= 1
            if self.last1 <= 0:
                self.last1 = None
            return oldVal
                
    def pop2(self):
        #Empty stack: return none
        if self.size == 0 or self.last1 == self.size-1:
            return None
        #Non-empty stack,empty stack1: remove last 
        #value, de-increment size
        else:
            oldVal = self.data[len(self.data)-1]
            self.data.pop()
            self.size -= 1
    
    def peek1():
        if self.last1 == None:
            return None
        else:
            return self.data[self.last1]
        
    def peek2():
        if self.size == 0 or self.last1 == self.size-1:
            return None
        else:
            return self.data[self.size-1]
