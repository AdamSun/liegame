# -*- coding: utf-8 -*-

'''
    the center of event dispatch
    event is used for notification of the message
    created by Adam Sun
'''

class EventManager(object):

    def __init__(self):
        self.__event_list = {}

    def add_event(self, type, call_back):
        """
        register some event to get the related message
        :param type:
        :param call_back:
        :return:
        """
        if not self.__event_list.has_key(type):
            self.__event_list[type] = []
        if not call_back in self.__event_list[type]:
            self.__event_list[type].append(call_back)


    def remove_event(self, type, call_back):
        """
        remove some event in order not to care the event
        :param type:
        :param call_back:
        :return:
        """
        if self.__event_list.has_key(type) and (call_back in self.__event_list[type]):
            self.__event_list[type].remove(call_back)

    def dispatch_event(self, type, data):
        """
        dispatch the event, the event listener will get the message
        :param type:
        :return:
        """
        if self.__event_list.has_key(type):
            [call_back(data) for call_back in self.__event_list[type]]

    def remove_all_event(self, type):
        """
        remove all the event for some type
        :param type:
        :return:
        """
        if self.__event_list.has_key(type):
            for call_back in self.__event_list[type]:
                self.remove_event(type, call_back)