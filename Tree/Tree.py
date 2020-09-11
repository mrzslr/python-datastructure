import abc


class Tree(abc.ABC, object):

    @abc.abstractmethod
    def insert(self, data):
        pass

    @abc.abstractmethod
    def search(self, data):
        pass

    @abc.abstractmethod
    def remove(self, data):
        pass

    @abc.abstractmethod
    def travers(self, kind):
        pass
