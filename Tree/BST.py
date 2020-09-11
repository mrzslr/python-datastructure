from .Tree import Tree
from .Node import BSTNode


class BST(Tree):
    def __init__(self):
        self.__root = None

    def insert(self, data):
        newnode = BSTNode(data)
        if self.__root is None:
            self.__root = newnode
            return
        temp = self.__root
        while temp:
            print(temp.val)
            if data >= temp.val:
                if temp.right is None:
                    temp.right = newnode
                    return
                temp = temp.right
            elif data < temp.val:
                if temp.left is None:
                    temp.left = newnode
                    return
                temp = temp.left

    def search(self, data):
        if self.__root is None:
            return False
        temp = self.__root
        while temp:
            if data >= temp.val:
                temp = temp.right
            elif data < temp.val:
                temp = temp.left
            elif data == temp.val:
                return True
        return False

    def remove(self, data):
        pass

    def travers(self, kind):
        pass
