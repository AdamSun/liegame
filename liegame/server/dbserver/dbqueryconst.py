# -*- coding: utf-8 -*-

"""
    created by Adam Sun
"""

CREATE_USER = u"INSERT INTO lg_user (username, nickname, email, password, avatar, is_admin) VALUES('%s', '%s', '%s', '%s', '%s', '%s')"
SEARCH_USER_BY_USERNAME = u"SELECT * FROM lg_user WHERE username = '%s'"