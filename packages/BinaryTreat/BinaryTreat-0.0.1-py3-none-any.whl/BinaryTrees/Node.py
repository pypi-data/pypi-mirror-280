import collections
from BinaryTrees.graphical import drawtree , Banching
NodesBeenMade = 0  

class Node : 
    def __init__(self , data )  :
        self.left = None  
        self.right = None  
        self.value = data 
        
    def addLeftChild(self, value: int):
        self.left = Node(value)
        return self.left
    
    def addRightChild(self, value: int):
        self.right = Node(value)
        return self.right
    
    
  

    def __repr__(self):
        return "Node data : " + str(self.value)
    
    
class BinaryTree : 
    def __init__(self , data : list or Node) -> None: 
        
        self.data = data
        self.root = None
        
        if type(data) == list:
            for number in data:
                self._branching(self.root, number)
        elif type(data) == Node:
            self.root = data
        else:
            print("wrong input type -> allowed types (list[numbers], TreeNode), entered type -> {}".format(type(data)))
            exit(-1)
    
    
    
    def _branching(self, node: Node, data: int) :

        if self.root == None:
            self.root = Node(data)
        else:
            if node.value > data:
                if node.left != None:
                    self._branching(node.left, data)
                else:
                    node.addLeftChild(data)
            elif node.value < data:
                if node.right != None:
                    self._branching(node.right, data)
                else:
                    node.addRightChild(data)
            elif node.value == data:
                print("you can't insert duplicate value")
                return -1
    
    
    def PrintTree(self , trav_type) :
        
        """ Print tree using your desired traversal 

        Returns:
            desired traversal 
        """
        
        if trav_type == "1"  : 
            return self.preorder_tree(self.root , "")
        elif trav_type == "2" :
            return self.inorder_tree(self.root , "")
        elif trav_type == "3" : 
            return self.postorder_tree(self.root , "")
        elif trav_type == "4" : 
            return self.levelorder_tree(self.root)
        else : 
            print("Invalid input !")
    
    def preorder_tree(self , start : Node , trav) : 

        """ Preorder from root to left then right 

        Returns:
            preorder traversal 
        """
        
        if start : 
            global NodesBeenMade 
            NodesBeenMade +=1 
            trav += (str(start.value) + "," )
            trav = self.preorder_tree(start.left , trav) 
            trav = self.preorder_tree(start.right , trav)
        return trav 
        
    def inorder_tree(self , start : Node  , trav) : 
        
        """ Inorder from left to root then right 

        Returns:
            inorder traversal 
        """
        
        if start : 
            global NodesBeenMade 
            NodesBeenMade +=1 
            trav = self.inorder_tree(start.left , trav) 
            trav += (str(start.value) + ",")
            trav = self.inorder_tree(start.right , trav)
        return trav 
    
    def postorder_tree(self , start : Node , trav)  :

        """ Postorder from left to right then root 

        Returns:
            postorder traversal 
        """
        
        if start : 
            global NodesBeenMade 
            NodesBeenMade +=1 
            trav = self.postorder_tree(start.left , trav) 
            trav = self.postorder_tree(start.right , trav)
            trav += (str(start.value) + ",")
        return trav 
    
    def levelorder_tree(self , start) :
        
        """ Levelorder itrating over tree in the levels 
        
        Returns:
            levelorder traversal 
        """
        
        ans = []
        if start is None : 
            return ans 
        
        queue = collections.deque()
        queue.append(start)
        
        while queue :
            currSize = len(queue)
            currList = []
            
            while currSize > 0 :
                currNode = queue.popleft()
                currList.append(currNode.value)
                currSize -= 1
                
                if currNode.left is not None : 
                    queue.append(currNode.left)
                    
                if currNode.right is not None : 
                    queue.append(currNode.right) 
            ans.append(currList) 
        return ans
    
    def floors_number(self , node) : 
        if node is None:
            return 0
        left = self.floors_number(node.left)
        right = self.floors_number(node.right)
        return max(left, right) + 1
    
    def delete_tree(self) : 
        
        """ Delete the tree 
        
        Returns : 
            for deleting 
        """
        self.root = None 
        
    def MAX(self) : 
        
        """ Max and Min in the tree : 
        used a traversal so we can itrate 

        Returns:
            _type_: _description_
        """
        result = self.PrintTree("1")
        result = result.split(",")
        result.pop()
        result = [int(x) for x in result ]
        
        return max(result)
    
    def MIN(self) :
         
        """ Max and Min in the tree : 
        used a traversal so we can itrate 

        Returns:
            _type_: _description_
        """
        
        result = self.PrintTree("1")
        result = result.split(",")
        result.pop()
        result = [int(x) for x in result ]
        
        return min(result)
        
    
    def compare(self) : 
        """ been made in the main function
        """
        pass 
        
    def draw(self) :
        
        """ Draw tree 
        
        drawing tree using personal module 
        first we branch our data and then we draw our tree 
        
        Returns : 
            Graphical tree using python's turtle 

        """
        Banching(self.data)
        drawtree()
    
    def numberOfLeafs(self, node: Node) :        
        if node is None:
            return 0
        if (node.left is None and node.right is None):
            return 1
        else:
            return self.numberOfLeafs(node.left) + self.numberOfLeafs(node.right)
        
    def search(self, node: Node , Arg: int) :
        """ Binary search 
            implanting binary search on the tree and compare two nodes with each other 
            search will go to right node if arg is bigger and go to left if arg is smaller 
       
        Returns:
            Node 
        """
        if node is None or node.value == Arg:
            return node

        if node.value > Arg:
            return self.search(node.left, Arg)
        elif node.value < Arg:
            return self.search(node.right, Arg)
        
    
    def FullTree(self , node ) :
        queue = list()
        queue.append(node)

        while queue != []:
            temp = queue.pop()

            if temp.left == None and temp.right == None:
                continue
            elif temp.right != None and temp.left != None:
                queue.append(temp.right)
                queue.append(temp.left)
            else:
                return False
        return True
    

    def isComplete(self):
        def RisComplete(node: Node, index: int, nodeCount: int) :
            if node == None:
                return True
            if index >= nodeCount:
                return False
            return RisComplete(node.left, 2 * index + 1, nodeCount) and RisComplete(node.right, 2 * index + 2, nodeCount)
        
    def get_count_of_children(self) :
        def count_of_children(node: Node) : # recursive call
            if (node == None):
                return 0;
            return (1 + count_of_children(node.left) + count_of_children(node.right))
        return count_of_children(self.root) - 1 
    
    def number_of_nodes(self) : 
        def count_nodes(node, counter=0) :
            if node:
                counter += 1
                counter = count_nodes(node.right, counter)
                counter = count_nodes(node.left, counter)
            return counter

        return count_nodes(self.root)
    
    def depth(self , node ) : 
        if node is None:
            return 0
        left = self.floors_number(node.left)
        right = self.floors_number(node.right)
        return max(left, right) 