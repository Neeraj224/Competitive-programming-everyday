"""
    141. Linked List Cycle
    
    Given head, the head of a linked list, determine if 
    the linked list has a cycle in it. There is a cycle in a 
    linked list if there is some node in the list that can be
    reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that
    tail's next pointer is connected to. Note that pos is not 
    passed as a parameter.
    Return true if there is a cycle in the linked list. 
    Otherwise, return false.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
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
    
    #################################################################
    
    def stitch(self, source, destination):
        """
            This method is used to stich one node to another
            so that we can create a loop/cycle in our linked list!
            We will use this to test out our solution for 
            LC 141 (Linked List Cycle).
        """
        if self.head == None:
            return
        
        # first we find the source node
        current = self.head
        while current and current.val != source:
            current = current.next
        # store the source node!
        fromNode = current
        
        # reset the current the node so that we can search
        # for the destination node:
        current = self.head
        while current and current.val != destination:
            current = current.next
        # save it too!
        toNode = current
        
        # now, stitch fromNode to toNode:
        fromNode.next = toNode
        return 
        
#####################################################################

class Solution():
    def __init__(self):
        pass

    def solver(self, head):
        """
            This method uses the fast and slow pointer
            approach. fast travels double the speed of the slow
            pointer.
            we check if fast and slow pointers collide - if they do,
            that means we'd seen that node before, so yes, there's
            a cycle.
            if they do not collide then no, there was no cycle.
        """
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        
        return False

    def solver2(self, head):
        """
            This method uses a hashmap.
            We hash the node's address in the memory and
            store it in the hashmap.
            and while traversing we check if we already have
            the current node in our map or not; if we do, then 
            we had already encountered this node before and that means theres
            a cycle.
            if we do not, and we also reach the end of the list, then that means
            theres no cycle.
            Fun!
        """
        nodeMap = {}
        current = head
        
        while current:
            if current in nodeMap:
                return True
            
            nodeMap[current] = current.val
            current = current.next
        
        return False

def main():
    arr = [3, 2, 0, -4]
    listOne = LinkedList()
    listOne.buildList(elements = arr)
    listOne.stitch(-4, 2)
    # listOne.printList()
    solver = Solution()
    print(solver.solver(listOne.head))
    
    arr = [1, 2]
    listTwo = LinkedList()
    listTwo.buildList(elements = arr)
    # first we check normally - the list does not have a cycle:
    solver = Solution()
    print(solver.solver2(listTwo.head))
    # next, we stitch two nodes together, thus creating a cycle:
    listTwo.stitch(2, 1)
    # and then we check again:
    print(solver.solver2(listTwo.head))

if __name__ == "__main__":
    main()