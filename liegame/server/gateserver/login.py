# -*- coding: utf-8 -*-

"""
    handle the login logic
    created by Adam Sun
"""

from common.controller import BaseController
import gateevents

class LoginController(BaseController):

    def init_event(self):
        self.event_manager.add_event(gateevents.LOGIN_REQUEST, self.login_request)
        self.event_manager.add_event(gateevents.REGISTER_REQUEST, self.register_request)

    def remove_event(self):
        self.event_manager.remove_event(gateevents.LOGIN_REQUEST, self.login_request)
        self.event_manager.remove_event(gateevents.REGISTER_REQUEST, self.register_request)

    def login_request(self):
        pass

    def register_request(self):
        pass