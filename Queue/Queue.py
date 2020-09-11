from .Node import Node


class Queue(object):
    """
        class make by @dot1mav ------> twitter : dot1mav
        Queue class
        Attribute ----> Private Node class object -----> items = []
        methods ------> 1:- enqueue = add to last
                        2:- dequeue = remove from  last
                        4:- show = show all item
                        5:- isEmpty = check the list is empty (return bool)
    """

    def __init__(self):
        self.__queuenode = Node()

    def enqueue(self, data):
        """
        method to add data in queue
        :param data:
        :return nothing:
        """
        self.__queuenode.items.insert(0, data)

    def dequeue(self):
        """
        remove data and return that
        :return data:
        """
        if self.__queuenode.items:
            return self.__queuenode.items.pop()

    def show(self):
        """
        show list
        :return list:
        """
        return self.__queuenode.items

    def isEmpty(self):
        """
        show queue is empty or not
        :return bool:
        """
        return bool(not (self.__queuenode.items))
