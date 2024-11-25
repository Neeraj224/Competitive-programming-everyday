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
        # lets make a dummy node first so that we can use it to start
        # bulding our resultingList
        dummy = ListNode()
        resultingList = dummy
        
        total = 0
        carry = 0
        
        # we go on until there's either list's elements remaining
        # or if there's a carry over from the previous sum!
        while list1 or list2 or carry:
            # get the previous carry first as our current total:
            total = carry
            
            if list1:
                total += list1.val
                list1 = list1.next
            
            if list2:
                total += list2.val
                list2 = list2.next
            
            # we mod it by 10 because we want the units digit, 
            # for example we have total up till now, 18
            # so, currentNodeVal would be 18 % 10 = 8
            # later we will make a node of this for our new list!
            currentNodeVal = total % 10
            # then we divide it by 10 because we want the carry over
            # the carry will never go over 1 because the max single digits
            # added together will give us 9 + 9 = 18
            # AND if there was previous carry over, it would be 9 + 9 + 1 (for carry over)
            # which is still 19.
            # ex: the previous total was 18, so now, 18 // 10 = 1
            # which is our carryover now!
            carry = total // 10
            # dummy pointer is used for traversal, so we are making a node
            # next to dummy, so that we can later on update dummy for other upcoming
            # nodes (if any!). so we make a node out of currentNodeVal that we took previously!
            dummy.next = ListNode(currentNodeVal)
            # so yeah, update dummy now:
            dummy = dummy.next
        
        return resultingList.next

####################################################################

def main():
    arr1 = [2, 4, 3]
    arr2 = [5, 6, 4]
    
    listOne = LinkedList()
    listOne.buildList(elements = arr1)
    
    listTwo = LinkedList()
    listTwo.buildList(elements = arr2)
    
    listOne.printList()
    listTwo.printList()
    
    solver = Solution()
    listNode = ListNode()
    listNode = solver.solver(listOne.head, listTwo.head)
    listNode.printListFromNode(listNode)
    
    # listOne.printList()
    # print(listOne.findNext(2))
    # print(listOne.findNext(5))
    # print(listOne.findNext(8))
    # print(listOne.getListLength())

if __name__ == "__main__":
    main()