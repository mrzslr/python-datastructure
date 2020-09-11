from .SLLNode import SLLNode


class SLL(object):
    __all__ = ["SLL"]
    """
        write class doc here
    """

    def __init__(self):
        """

        """
        self.__start = None

    def add_last(self, data):
        """

        :param data:
        :return:
        """
        new_node = SLLNode(data=data)
        if self.__start is None:
            self.__start = new_node
            return
        last = self.__start
        while last.next:
            last = last.next
        last.next = new_node

    def add(self, data):
        """

        :param data:
        :return:
        """
        new_node = SLLNode(data=data)
        if self.__start is None:
            self.__start = new_node
            return
        new_node.next = self.__start
        self.__start = new_node

    def add_after(self, data, after):
        """

        :param data:
        :param after:
        :return:
        """
        new_node = SLLNode(data=data)
        if self.__start is None:
            self.__start.next = new_node
            return
        check = self.__start
        while check:
            print(f'{check}')
            if check.data == after:
                temp = check.next
                new_node.next = temp
                check.next = new_node
            check = check.next

    def remove(self, data):
        """

        :param data:
        :return:
        """
        temp = self.__start
        while temp:
            if temp.next.data == data:
                temp2 = temp.next.next
                temp.next = temp2
                return True
            temp = temp.next
        return False

    def remove_last(self):
        """

        :return:
        """
        temp = self.__start
        while temp:
            if temp.next.next is None:
                temp.next = None
            temp = temp.next

    def remove_first(self):
        """

        :return:
        """
        temp = self.__start.next
        self.__start = temp

    def remove_after(self, after):
        temp = self.__start
        while temp:
            if temp.data == after:
                temp.next = temp.next.next
            temp.next

    def show(self):
        """

        :return:
        """
        temp = self.__start
        print('--->')
        while temp:
            if temp.next is None:
                print(f'{temp.data}')
                return
            print(f'{temp.data} --->')
            temp = temp.next

    def revers(self):
        """

        :return:
        """
        temp = self.__start
        temp2 = None
        while temp:
            next = temp.next
            temp.next = temp2
            temp2 = temp
            temp = next
        self.__start = temp2

    def search(self, data):
        """

        :param data:
        :return:
        """
        temp = self.__start
        while temp:
            if data == temp.data:
                return True
            temp = temp.next
        return False

    def convert_to_stack(self):
        """

        :return:
        """
        from Stack import Stack
        stack = Stack()
        temp = self.__start
        while temp:
            stack.push(temp.data)
            temp = temp.next
        return stack

    def convert_to_queue(self):
        """

        :return:
        """
        from Queue import Queue
        temp = self.__start
        queue = Queue()
        while temp:
            queue.enqueue(temp.data)
            temp = temp.next
        return queue
