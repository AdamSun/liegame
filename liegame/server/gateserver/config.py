# -*- coding: utf-8 -*-

'''
    created by Adam Sun
'''

DEBUG = True
IP = '127.0.0.1'
PORT = 10001

##login server info
LOGIC_SERVER_IP = '127.0.0.1'
LOGIC_SERVER_PORT = 10002

##log server info
LOG_SERVER_IP = '127.0.0.1'
LOG_SERVER_PORT = 10003

##db server info
DB_SERVER_IP = '127.0.0.1'
DB_SERVER_PORT = 10004

################################ db connection status ##########################
# disconnect status
DB_CONNECTION_STATUS_DISCONNECT = 0
# connect status
DB_CONNECTION_STATUS_CONNECT = 0


# ############################db type define####################
MODULE_USER = 0

# cmd to create user
MODULE_USER_CREATE = 0
# cmd to search by username
MODULE_USER_SEARCH_BY_USERNAME = 1
# result of create user
MODULE_USER_CREATE_RESULT = 2
# result of search by username
MODULE_USER_SEARCH_BY_USERNAME_RESULT = 3