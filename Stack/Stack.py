from .Node import Node


class Stack(object):
    """
        class make by @dot1mav ------> twitter : dot1mav
        Stack class
        Attribute ----> Private Node class object -----> items = []
        methods ------> 1:- push = add to first
                        2:- pop = remove from  last
                        3:- peek = show last one
                        4:- show = show all item
                        5:- isEmpty = check the list is empty (return bool)
    """

    def __init__(self):
        self.__stacknode = Node()

    def push(self, data):
        """
        method for add data to stack
        :param data:
        :return:
        """
        self.__stacknode.items.append(data)

    def pop(self):
        """
        method for remove last data
        :return: last data
        """
        if self.__stacknode.items:
            return self.__stacknode.items.pop()

    def peek(self):
        """
        show last data
        :return data:
        """
        if self.__stacknode.items:
            return self.__stacknode.items[-1]

    def show(self):
        """
        show list
        :return list:
        """
        return self.__stacknode.items

    def isEmpty(self):
        """
        show stack is empty or not
        :return bool:
        """
        return bool(not self.__stacknode.items)

