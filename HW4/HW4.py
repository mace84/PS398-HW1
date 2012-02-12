## PS398 Homework 4
## Matthias Orlowski
## 02/12/2012
## Script implementing a singly linked list with nodes class

class Exceptions(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Node(object):
    def __init__(self,_value=None, _next=None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)

    def appendChild(self,new_value):
        if self.next == None:
            self.next = Node(new_value)
        else:
            self.next.appendChild(new_value)
    
    def concatChildValues(self):
        if self.next == None:
            return str(self.value)
        else:
            return str(self.value) + ", " + self.next.concatChildValues()

    def height(self):
        if self.next == None:
            return 1
        else:
            return self.next.height() + 1

    def pointer(self,position):
        if position != 0 and self.next == None:
            raise Exceptions, "Index out of range!"
        elif position == 0:
            return self
        else:
            temp = position - 1
            return self.next.pointer(temp)

    def preValues(self,position):
        if position == 0:
            return Node(None)
        elif self.next == self.pointer(position):
            return self
        else:
            temp = position - 1
            return self.next.preValues(temp)
        
    def checkValues(self,check):
        if self.value == check:
            return True
        elif self.next == None:
            return False
        else:
            return self.next.checkValues(check)

    
class LinkedList(object):
    def __init__(self,_node=None):
        self.head=_node

    def __str__(self):
        return self.head.concatChildValues()

    def length(self):
        return self.head.hight()
    
    def appendNode(self,new_value):
        if self.head == None:
            self.head = Node(new_value)
        else:
            self.head.appendChild(new_value)

    def addNodeAfter(self, new_value, after_node):
        endValues = self.head.pointer(after_node+1)
        startValues = self.head.preValues(after_node)
        startValues.next = Node(new_value,endValues)

    def addNodeBefore(self, new_value, before_node):
        endValues = self.head.pointer(before_node)
        startValues = self.head.preValues(before_node-1)    
        startValues.next = Node(new_value,endValues)

    def removeNode(self, node_to_remove):
        remNode = self.head.pointer(node_to_remove)
        startValues = self.head.preValues(node_to_remove)
        endValues = remNode.next
        startValues.next = endValues

    # def removeNodesByValue(self, value):
    #     removeNode()

    # def reverse(self):

    # def hasCycle(self):
