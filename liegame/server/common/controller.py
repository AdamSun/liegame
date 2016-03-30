# -*- coding: utf-8 -*-

'''
    the super class of controller
    created by Adam Sun
'''

class BaseController(object):

    def __init__(self, event_manager):
        self.event_manager = event_manager

    def init_event(self):
        pass

    def remove_event(self):
        pass