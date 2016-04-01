# -*- coding: utf-8 -*-

'''
    the model of user
    created by Adam Sun
'''

class User(object):
    def __init__(self):
        self.user_id = 0
        self.user_name = ""
        self.nick_name = ""
        self.email = ""
        self.avatar = ""
        self.password = ""
        self.is_admin = 0
        self.session = None