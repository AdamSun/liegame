# -*- coding: utf-8 -*-

"""
   the implement of queue
    created by Adam Sun
"""

class Queue(object):

    def __init__(self):
        self.__queue = []

    def push(self, func, argv):
        self.__queue.append([func, argv])

    def pop(self):
        """
        only can pop the first element
        :return:
        """
        len = len(self.__queue)
        if len > 0:
            element = self.__queue[0]
            self.__queue.remove(element)
            return element
        return None

    def len(self):
        return len(self.__queue)