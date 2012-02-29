## PS398 Homework 4
## Matthias Orlowski
## 02/12/2012
## Script implementing a singly linked list with nodes class

# !/usr/bin/python
    
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
    
    def concatChildValues(self, head):
        if self.next == None:
            return str(self.value)
        elif self.next == head:
            return str(self.value) + ",...(cyclical)"
        else:
            return str(self.value) + ", " + self.next.concatChildValues(head)

    def height(self, head):
        if self.next == None or self.next == head:
            return 1
        else:
            return self.next.height(head) + 1

    def index(self,position):
        if position != 0 and self.next == None:
            raise Exceptions, "Index out of range!"
        elif position == 0:
            return self
        else:
            temp = position - 1
            return self.next.index(temp)
        
    def checkValues(self,check):
        if self.value == check:
            return True
        else:
            return False

    
class LinkedList(object):
    def __init__(self,_node=None):
        if _node != None:
            self.head = Node(_node)
        else:
            self.head=_node

    def __str__(self):
        try:
            return self.head.concatChildValues(self.head)
        except:
            if self.head == None:
                raise Exceptions, "This list is empty!"
        
    def length(self):
        return self.head.height(self.head)
            #best case: O(n), worst: O(n)
    
    def appendNode(self,new_value):
        if self.head == None:
            self.head = Node(new_value)
        else:
            self.head.appendChild(new_value)
            #best case: O(n), worst: O(n)
            
    def addNodeAfter(self, new_value, after_node):
        if after_node == 0:
            insertPoint = self.head
        else:
            insertPoint = self.head.index(after_node)
        addedNode = Node(new_value,insertPoint.next)
        insertPoint.next = addedNode
            #best case: O(1), worst: O(n), depends on after_node chosen
        
    def addNodeBefore(self, new_value, before_node):
        if before_node == 0:
            oldhead = self.head
            self.head = Node(new_value,oldhead)
        else:
            insertPoint = self.head.index(before_node - 1)
            addedNode = Node(new_value,insertPoint.next)
            insertPoint.next = addedNode
            #best case: O(1), worst: O(n), depends on before_node chosen
            
    def removeNode(self, node_to_remove):
        if node_to_remove == 0:
            newhead = self.head.next
            self.head = newhead
            return
        preRemNode = self.head.index(node_to_remove - 1)
        if node_to_remove == self.length() -1:
            preRemNode.next = None
        else:
            postRemNode = self.head.index(node_to_remove + 1)
            preRemNode.next = postRemNode
            #best case: O(1), worst: O(2n), depends on node_to_remove chosen, if thats not 0, then time is at least n+1 due to checking the if condition
            
    def removeNodesByValue(self, value):
        if self.length() == 1:
            if self.head.checkValues(value) == True:
                self.removeNode(0)
                return
            return
        for i in range(1,self.length()):
            checkelement = self.head.index(i)
            if checkelement.checkValues(value) == True:
                self.removeNode(i)
                self.removeNodesByValue(value)
                # This raises an index out of bound error but generates the right result. Why?
            #best case: O(n), worst: O(3n^2)
                
    def reverse(self):
        try:
            for i in range(1,self.length()):
                newhead = self.head.index(i).value
                self.addNodeBefore(newhead,0)
                self.removeNode(i+1)
                return self
        except:
            if self.hasCycle() == T:
                raise Exceptions, "Reverse does not yet work for circular lists. Sorry, but we are working on it!"
            # best: O(n^2), worst: O(n^2)
            
    def addCycle(self):
        self.head.index(self.length()-1).next = self.head
            # best = worst: O(n)
        
    def hasCycle(self):
        for i in range(0,self.length()):
            if self.head.index(i).next == None:
                return False
            elif i == self.length()-1:
                return True
            # best:O(n) worst: O(n^2)
            
        # add checks for bad inputs (check index values for being integers)
