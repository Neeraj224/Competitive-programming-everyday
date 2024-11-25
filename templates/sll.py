"""
    Template for the Linked List questions on Leetcode.
    I have added basic methods like:
        - building the list from an array
        - getting the length of the list
        - printing the list
        - getting the next node of a node
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None
    
    def printListFromNode(self, head):
        """
            This method is for lists we need to print directly
            from the node. Because we cannot use another list's
            object to randomly pass a node for some other list
            just to print it.
        """
        if head == None:
            return []
        
        current = head
        
        print("[", end = "")
        while current:
            print(current.val, end = " -> ")
            current = current.next
        print("None]")
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def buildList(self, elements):
        if len(elements) == 0:
            return self.head
        
        current = ListNode(elements[0])
        self.head = current
        
        for i in range(1, len(elements)):
            current.next = ListNode(elements[i])
            current = current.next
        
        return self.head

    def getListLength(self):
        if self.head == None:
            return 0
        
        current = self.head
        numElements = 0
        
        while current:
            numElements += 1
            current = current.next
        
        return numElements
    
    def printList(self):
        if self.head == None:
            return []
        
        current = self.head
        
        print("[", end = "")
        while current:
            print(current.val, end = " -> ")
            current = current.next
        print("None]")
    
    def findNext(self, val):
        current = self.head
        
        while current and current.val != val:
            current = current.next
        
        if not current:
            return "Node not found!"
        
        if current.next:
            return current.next.val
        else:
            print("There's nothing at the end of this node!")
            return None

####################################################################

class Solution:
    def __init__(self):
        pass
    
    def solver(self):
        pass

####################################################################

def main():
    arr = [1, 2, 3, 4, 5]
   
    listOne = LinkedList()
    listOne.buildList(elements = arr)
   
   
    # listOne.printList()
    # print(listOne.findNext(2))
    # print(listOne.findNext(5))
    # print(listOne.findNext(8))
    # print(listOne.getListLength())

if __name__ == "__main__":
    main()
