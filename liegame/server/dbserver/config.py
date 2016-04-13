# -*- coding: utf-8 -*-

"""
    config of db
    created by Adam Sun
"""

# is debug mode
DEBUG_MODE = True

# the time of waiting the client, after this time
# the server will disconnect with the client
# if the value is set -1, it means permanent connection
CONNECTION_WAITING_TIME = -1

PORT = 10004

# the max connection number of the client
MAX_CONNECTION_NUMBER = 1000

MYSQL_IP = u'127.0.0.1'

MYSQL_PORT = 0

MYSQL_USER = u"root"

MYSQL_PASSWORD = u"123456"


DB_TYPE_MYSQL = 0
DB_TYPE_REDIS = 1
DB_TYPE_MONGODB = 2

# the type of db, the default db type is mysql
db_type = 0

DB_NAME = "lie_game"

# ############################db type define####################
MODULE_USER = 0

MODULE_USER_CREATE = 0
MODULE_USER_SEARCH_BY_USERNAME = 1
MODULE_USER_CREATE_RESULT = 2
MODULE_USER_SEARCH_BY_USERNAME_RESULT = 3