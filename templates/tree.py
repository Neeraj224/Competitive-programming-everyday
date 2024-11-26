class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.inorderTraversal = []
        self.preorderTraversal = []
        self.postorderTraversal = []
        
    def buildBST(self, elements, index, n):
        """
            we'll use a recursive method to build our tree.
            we'll pass the array of elements, the current index and the length of
            the elements array to this method. 
            NOTE:   a node at ith position will have its
                    left-child at (2 * i) + 1 position
                    and its right-child at (2 * i) + 2 position.
        """
        # initialise a temporary root value
        root = None
        
        # if it is a valid not out-of-bounds index
        # AND if the elements[index] is not Null/None i.e.
        # there's no node present at that position in the
        # tree, then:
        if index < n and elements[index] is not None:
            # create a TreeNode with that value
            root = TreeNode(val = elements[index])
            
            # and recursively build its left subtree first:
            root.left = self.buildBST(elements, (2 * index) + 1, n)
            # and then recursively build its right subtree next:
            root.right = self.buildBST(elements, (2 * index) + 2, n)
        
        # and after recursively bulding everything, return the root!
        # even if nothing was built, it will return a Null/None.
        # that will make the absence of a node there, even if there
        # are further nodes elsewhere next.
        return root

    def preorder(self, root):
        if not root:
            return
        
        self.preorderTraversal.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        self.inorderTraversal.append(root.val)
        self.inorder(root.right)
    
    def postorder(self, root):
        if not root:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        self.postorderTraversal.append(root.val)
    
    def printTraversal(self, root = None, preorder = False, inorder = False, postorder = False):
        if preorder:
            self.preorder(root = root)
            print("preorder: ", end = "")
            print(self.preorderTraversal)
        if inorder:
            self.inorder(root = root)
            print("inorder: ", end = "")
            print(self.inorderTraversal)
        if postorder:
            self.postorder(root = root)
            print("postorder: ", end = "")
            print(self.postorderTraversal)
    
######################################################################

class Solution:
    def __init__(self):
        pass

    def solver(self):
        pass

######################################################################

def main():
    null = None
    elements = [3,9,20,null,null,15,7]
    
    tree1 = TreeNode()
    n = len(elements)
    tree1 = tree1.buildBST(elements = elements, index = 0, n = n)
    
    tree1.printTraversal(root = tree1, inorder = True)
    tree1.printTraversal(root = tree1, preorder = True)
    tree1.printTraversal(root = tree1, postorder = True)    
    
    solver = Solution()

if __name__ == "__main__":
    main()