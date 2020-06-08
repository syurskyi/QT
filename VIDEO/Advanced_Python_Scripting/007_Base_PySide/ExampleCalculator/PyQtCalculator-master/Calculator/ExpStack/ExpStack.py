__author__ = 'Joel'


# the calculator stack, in fact is a list
class ExpStack():
    #init method
    def __init__(self):
        self.top = -1
        self.data = []

    #whether Stack is empty
    def is_empty(self):
        return -1 == self.top

    #pop an element from stack
    def pop(self):
        if self.is_empty():
            print "Stack is Empty..."
        else:
            self.data.pop(self.top)
            self.top -= 1

    #push an element into stack
    def push(self, e):
        self.data.append(e)
        self.top += 1

    #get an element in the top of the stack
    def get_top(self):
        if self.is_empty():
            print "Stack is Empty"
            return None
        else:
            return self.data[self.top]

    #get the size of the stack
    def size(self):
        return self.top + 1

    #clear stack
    def clear(self):
        self.top = -1
        self.data = []

    #get data of stack
    def get_data(self):
        return self.data
