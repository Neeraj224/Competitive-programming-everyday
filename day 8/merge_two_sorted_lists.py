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
    
    def solver(self, list1, list2):
        # pass
        # we need two new ListNodes
        # one for our resulting merged list
        newListHead = ListNode()
        # another for traversing!
        current = ListNode()
        newListHead = current
        
        # so while we reach the end of either of the lists,
        # we keep traversing and updating pointers
        while list1 and list2:
            # if the list1 node's value is less than the other list's
            # make our current's next pointer point to it
            if list1.val < list2.val:
                current.next = list1
                # and then move the list1 pointer ahead
                list1 = list1.next
            else:
                # else, make the current's next point to the other list's
                # node
                current.next = list2
                # and the update it's pointer
                list2 = list2.next
            
            # and then update our current pointer so that we can slowly build up our 
            # merged list!
            current = current.next
        
        # we will always traverse through one list first all the time,
        # so if any nodes are remaining from the other list
        # make sure our current (that will be the end of the previously 
        # merged and sorted list) node's next pointer points to the
        # remainder of that list - remember, we were using list1 and list2
        # as pointers and updating them likewise so the remnant of that
        # list be appended to our resultant list!
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        newListHead = newListHead.next

        return newListHead

####################################################################

def main():
    arr1 = [1, 2, 4]
    arr2 = [1, 3, 4]
   
    listOne = LinkedList()
    listOne.buildList(elements = arr1)
   
    listTwo = LinkedList()
    listTwo.buildList(elements = arr2)
    
    listOne.printList()
    listTwo.printList()
    
    arbitraryListNode = ListNode()
    solver = Solution()
    arbitraryListNode = solver.solver(listOne.head, listTwo.head)
    arbitraryListNode.printListFromNode(arbitraryListNode)
   
    # listOne.printList()
    # print(listOne.findNext(2))
    # print(listOne.findNext(5))
    # print(listOne.findNext(8))
    # print(listOne.getListLength())

if __name__ == "__main__":
    main()