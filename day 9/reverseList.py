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
        # pass
        self.store = []
    
    def extractElements(self, head):
        current = head
        
        while current:
            self.store.append(current.val)
            current = current.next
        
    def reverseElements(self):
        left = 0
        right = len(self.store) - 1

        while left <= right:
            self.store[left], self.store[right] = self.store[right], self.store[left]
            left += 1
            right -= 1
        
        return

    def buildList(self):
        current = ListNode(self.store[0])
        head = current
        
        for i in range(1, len(self.store)):
            current.next = ListNode(val = self.store[i])
            current = current.next
        
        return head
        
    def solver(self, listHead):
        # pass
        if listHead is None:
            return None
        
        self.extractElements(listHead)
        self.reverseElements()
        reverseListHead = self.buildList()
        
        return reverseListHead
    
    def solver2(self, head):
        if head is None:
            return None
        
        # 'previousNode': to keep track of the previous node in the reversed list
        # 'currentNode': to traverse the original list, starting from the head
        previousNode = None
        currentNode = head
        
        while currentNode:
            # we first temporarily store the next node to preserve the link
            # i mean we need to go to that node next, so that we can reverse its pointer too
            tempNodeNext = currentNode.next
            # reverse the 'next' pointer of the current node; make it point
            # to the previous node so that we have reversed it
            currentNode.next = previousNode
            # now we just move 'previousNode' and 'currentNode' one step forward
            # so previousNode now will point to the currentNode whose pointer we just reversed
            previousNode = currentNode
            # and the currentNode will move on to the next node in the original list
            # since that node was preserved by pointing a temporary pointer to it
            # we just move currentNode to the temp pointer!
            currentNode = tempNodeNext
        
        # after the end, the last node will be our head, and the list will be completely
        # reversed, so just return it!
        return previousNode
                

####################################################################

def main():
    arr = [1, 2]
   
    listOne = LinkedList()
    listOne.buildList(elements = arr)
   
    solver = Solution()
    reverseListHead = solver.solver2(listOne.head)
    reverseListHead.printListFromNode(reverseListHead)
    
    # listOne.printList()
    # print(listOne.findNext(2))
    # print(listOne.findNext(5))
    # print(listOne.findNext(8))
    # print(listOne.getListLength())

if __name__ == "__main__":
    main()
