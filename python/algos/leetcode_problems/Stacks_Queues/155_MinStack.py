"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""

class MyStack(object):
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.full_stack = MyStack()
        self.min_stack = MyStack()
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.full_stack.push(x)
        if self.min_stack.isEmpty():
            self.min_stack.push(x)
        elif x <= self.min_stack.peek():
            self.min_stack.push(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.full_stack.isEmpty():
            data = self.full_stack.pop()
            if data == self.min_stack.peek():
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.full_stack.isEmpty():
            return None
        else:
            return self.full_stack.peek()

    def getMin(self):
        """
        :rtype: int
        """
        if self.full_stack.isEmpty():
            return None
        else:
            return self.min_stack.peek()
        


# 25.57% 
