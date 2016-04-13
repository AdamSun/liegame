# -*- coding: utf-8 -*-

"""
    the handle of str
    created by Adam Sun
"""

import commonconst
import re

email_re = "([^@|\s]+@[^@]+\.[^@|\s]+)"

def is_username_legal(username):
    """
    to judge if the username is legal
    :param username:
    :return:
    """
    if not(isinstance(username, str)):
        return commonconst.ERROR_USERNAME_ILLEGAL_TYPE
    if is_str_none(username):
        return commonconst.ERROR_USERNAME_NONE


def is_email_legal(email):
    """
    to judge if the email is legal
    :param email:
    :return:
    """
    if not(isinstance(email, str)):
        return commonconst.ERROR_USERNAME_ILLEGAL_TYPE
    if re.match(email_re, email) == None:
        return commonconst.ERROR_EMAIL_ILLEGAL_FORMAT
    return commonconst.SUCCESS_EMAIL_LEGAL_FORMAT

def is_str_none(s):
    """
    if the str is None
    :param s:
    :return:
    """
    if s != "" and s != None:
        return False
    return True