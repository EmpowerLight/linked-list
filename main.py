#linked list

class Node:
    """Node"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def printList(self):
        """Print list"""
        current_node = self.head
        while current_node:
            print(f" {current_node.value} ", end="")
            current_node = current_node.next
        

    def prepend(self, value):
        """At a node at the begining of the list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            return
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """At node at the end of the list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def _traverse(self, index):
        """return the previous node from the given index"""
        current_node = self.head
        count = 0
        while count < index-1:
            current_node = current_node.next
            count += 1
        return current_node

    def insert(self, value, index):
        """At a node at a given index"""
        new_node = Node(value)
        if index == 0:
            self.append(value)
            return
        leader_node = self._traverse(index)
        holding_node = leader_node.next
        leader_node.next = new_node
        new_node.next = holding_node

    def reverse_list(self):
        """Reverse the linked list"""
        prevNode = self.head
        nextNode = prevNode.next
        prevNode.next = None
        currentNode = nextNode
        while currentNode:
            next = currentNode.next
            nextNode.next = prevNode 
            prevNode = nextNode
            nextNode = next 
            currentNode = next
        self.head = prevNode
    
    def delATBeg(self):
        """Delete a node from the begining of the list"""
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
    
    def delAtEnd(self):
        """Delete a node from the end of the list"""
        currentNode = self.head
        while currentNode.next.next:
            currentNode = currentNode.next
        self.tail = currentNode
        self.tail.next = None
    
    def remove(self, index):
        """Delete the node at the given index"""
        if index == 0:
            self.delATBeg()
            return
        leaderNode = self._traverse(index)
        holdingNode = leaderNode.next
        leaderNode.next = holdingNode.next

   
list = LinkedList()
list.prepend("Google")
list.prepend("Facebook")
list.prepend("Twitter")
list.append("Facebook")
list.insert("Instagram", 1)
list.reverse_list()
list.printList()
# list.delATBeg()
# print()
# list.printList()
# print()
# list.delAtEnd()
# list.printList()
# print()
# print(list.tail.value)
# list.printList()
# list.remove(1)
# print()
# list.printList()