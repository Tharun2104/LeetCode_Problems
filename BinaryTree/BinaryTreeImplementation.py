class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

    def __repr__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.rootNode = None


    def __search__(self, searchValue, node):
        # Two base cases
        # 1) Child node does not exist 
        # 2) Child node is the value we are looking for
        if node is None or node.value == searchValue:
            return node

        elif searchValue < node.value:
            return self.__search__(searchValue, node.leftChild)

        else:
            return self.__search__(searchValue, node.rightChild)

    def search(self, searchValue):
        return self.__search__(searchValue, self.rootNode)


    def __insert__(self, value, node):
        if node is None:
            self.rootNode = TreeNode(value)
            return

        if value < node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)          
                return
            else:
                self.__insert__(value, node.leftChild)
        elif value > node.value:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
                return
            else:
                self.__insert__(value, node.rightChild)

    def insert(self, value):


        return self.__insert__(value, self.rootNode)


    def lift(self, node, nodeToDelete):
        if node.leftChild:
            print(f'node: {node}; Put on Lift stack: leftChild: {node.leftChild}; nodeToDelete: {nodeToDelete}')
            liftReturnValue = self.lift(node.leftChild, nodeToDelete)
            node.leftChild = liftReturnValue
            print(f'node: {node}; Pop from Lift stack: liftReturnValue: {liftReturnValue}; leftChild --> {liftReturnValue}')
            return node
        else:
            print('Deleting node via lift')
            print(f'node: {node}; nodeToDelete: {nodeToDelete}; nodeToDelete.value = node.value')
            nodeToDelete.value = node.value
            print(f'Lift value after deleting: {node.rightChild}')
            return node.rightChild

    def __delete__(self, valueToDelete, node):
        # Base case happens when:
        # 1) rootNode is empty
        # 2) when a recursive call to this function tries to access a child node that does not exist, 
        # meaning the value you are looking for is not in the tree
        if node is None:
            return None

        elif valueToDelete < node.value:
            print(f'node: {node}; Put on Stack: valueToDelete: {valueToDelete}; leftChild: {node.leftChild}')
            returnedNode = self.__delete__(valueToDelete, node.leftChild)
            print(f'node: {node}; Pop from Stack: returnedNode: {returnedNode}; leftChild --> {returnedNode}')
            node.leftChild = returnedNode # often, this "overwrite" does not change the left child
            return node 

        elif valueToDelete > node.value:
            print(f'node: {node}; Put on Stack: valueToDelete: {valueToDelete}; rightChild: {node.rightChild}')
            returnedNode = self.__delete__(valueToDelete, node.rightChild)
            print(f'node: {node}; Pop from Stack: returnedNode: {returnedNode}; rightChild --> {returnedNode}')
            node.rightChild = returnedNode # often, this "overwrite" does not change the left child; change only happens
            # when the next recursive call involves an actual deletion
            return node


        elif valueToDelete == node.value:
            if node.leftChild is None:
                return_value =  node.rightChild
            elif node.rightChild is None:
                return_value = node.leftChild
            else:
                print(f'node: {node}; Put on Lift stack: rightChild: {node.rightChild}; nodeToDelete: {node}')
                liftReturnValue = self.lift(node.rightChild, node)
                print(f'node: {node}; Pop from Lift stack: liftReturnValue: {liftReturnValue}; rightChild --> {liftReturnValue}')
                node.rightChild = liftReturnValue
                return_value = node
            return return_value


    def delete(self, valueToDelete):
        return self.__delete__(valueToDelete, self.rootNode)

    def __inorder__(self, node):
        if node is None:
            return   
        self.__inorder__(node.leftChild)
        print(node.value)
        self.__inorder__(node.rightChild)

    def inorder(self):
        self.__inorder__(self.rootNode)


    def __preorder__(self, node):
        if node is None:
            return  
        print(node.value)
        self.__preorder__(node.leftChild)
        self.__preorder__(node.rightChild)

    def preorder(self):
        self.__preorder__(self.rootNode)

    def __postorder__(self, node):
        if node is None:
            return   
        self.__postorder__(node.leftChild)   
        self.__postorder__(node.rightChild)
        print(node.value)

    def postorder(self):
        self.__postorder__(self.rootNode)

    def __max__(self, node):
        if node.rightChild:
            return self.__max__(node.rightChild)
        else:
            return node.value

    def max(self):
        return self.__max__(self.rootNode)


    def __min__(self, node):
        if node.leftChild:
            return self.__min__(node.leftChild)
        else:
            return node.value

    def min(self):
        return self.__min__(self.rootNode)