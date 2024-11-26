class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.inorderTraversal = []
        self.preorderTraversal = []
        self.postorderTraversal = []
        self.levelorderTraversal = []
        
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
    
    def levelOrder(self, root):
        if root is None:
            return self.levelorderTraversal
        
        # we set a queue first
        queue = []
        # next we push the root to the queue:
        queue.append(root)
        
        while queue:
            # this (sub)array is used to store the nodes
            # on the current level of the tree
            current_level = []
            
            # now we go through each and every node in the queue:
            for _ in range(len(queue)):
                # we get the node at the front of the queue:
                current = queue[0]
                
                # next we check if this node has a left child:
                if current.left:
                    # if it does, we append it to the queue
                    # so that we check it later on (and also its' children)
                    queue.append(current.left)
                
                # next we do the same for the right child (if it has one):
                if current.right:
                    queue.append(current.right)
                    
                # next we pop the node from queue:
                current_node = queue.pop(0)
                # we take it's value
                current_node_val = current_node.val
                # and append it to the current_level subarray:
                current_level.append(current_node_val)
            
            # then we append that current_level subarray to out traversal array:
            self.levelorderTraversal.append(current_level)
    
    def printTraversal(self, root = None, preorder = False, inorder = False, postorder = False, levelorder = False):
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
        if levelorder:
            self.levelOrder(root = root)
            print("levelorder: ", end = "")
            print(self.levelorderTraversal)
    
######################################################################

class Solution:
    def __init__(self):
        self.levelOrderTraversal = []

    def levelOrder(self, root):
        if root is None:
            return self.levelOrderTraversal
        
        # we set a queue first
        queue = []
        # next we push the root to the queue:
        queue.append(root)
        
        while queue:
            # this (sub)array is used to store the nodes
            # on the current level of the tree
            current_level = []
            
            # now we go through each and every node in the queue:
            for _ in range(len(queue)):
                # we get the node at the front of the queue:
                current = queue[0]
                
                # next we check if this node has a left child:
                if current.left:
                    # if it does, we append it to the queue
                    # so that we check it later on (and also its' children)
                    queue.append(current.left)
                
                # next we do the same for the right child (if it has one):
                if current.right:
                    queue.append(current.right)
                    
                # next we pop the node from queue:
                current_node = queue.pop(0)
                # we take it's value
                current_node_val = current_node.val
                # and append it to the current_level subarray:
                current_level.append(current_node_val)
            
            # then we append that current_level subarray to out traversal array:
            self.levelOrderTraversal.append(current_level)
        
        return self.levelOrderTraversal

    def solver(self, root):
        # pass
        return (len(self.levelOrder(root = root)))

    def maxDepth(self, root):
        # if there's no root
        if not root:
            # we return 0 to add
            return 0

        # now first get the left subtree's depth:
        left_depth = self.maxDepth(root.left)
        # then next get the right subtree's depth:
        right_depth = self.maxDepth(root.right)
        # now, from whatever the depth of the subtrees
        # take the maximum one, and add 1 to it, so that we account
        # for the currently being explored subtree's root's height:
        root_depth = max(left_depth, right_depth) + 1
        
        # and then return this root's depth:
        return root_depth
    
        """
            So, this will keep on going depth-wise and return both left
            and right subtrees' depths and take max of that.
            this is the DFS way.
        """

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
    tree1.printTraversal(root = tree1, levelorder = True)   
    
    solver = Solution()
    print(solver.solver(root = tree1))
    print(solver.maxDepth(root = tree1))

if __name__ == "__main__":
    main()