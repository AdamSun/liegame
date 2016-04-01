# -*- coding: utf-8 -*-

"""
    connection to the db, the specific db connection will inherit
    from the BaseDBConnection.We use adbapi because we want no blocking
    during the query of db
    created by Adam Sun
"""

import config
import dbqueryconst

class BaseDBConnection(object):

    def __init__(self, session):
        self.session = session

    def connect(self):
        pass

    def disconnect(self):
        pass

    def query(self, type, sub_type):
        pass


class MYSQLConnnection(BaseDBConnection):
    """
    mysql connection
    """
    def __init__(self, session, dbpool):
        super(MYSQLConnnection, self).__init__(session)
        self.dbpool = dbpool

    def disconnect(self):
        if self.dbpool:
            self.dbpool.close()
            self.dbpool = None

    def query(self, type, sub_type):
        if not self.dbpool:
            return
        if type == config.MODULE_TYPE_USER:
            self.query_user(sub_type)

    def query_user(self, sub_type):
        if sub_type == config.MODULE_SUBTYPE_CREATE:
            user_name = self.session.user.user_name
            nick_name = self.session.user.nick_name
            email = self.session.user.email
            pwd = self.session.user.password
            avatar = self.session.user.avatar
            is_admin = self.session.user.is_admin
            sql = dbqueryconst.CREATE_USER % (user_name, nick_name, email, pwd, avatar, is_admin)
            d = self.dbpool.runQuery(sql)
            d.addCallback(self.user_create_success)
            print "start query"
        elif sub_type == config.MODULE_SUBTYPE_SEARCH_BY_USERNAME:
            user_name = self.session.user.user_name
            sql = dbqueryconst.SEARCH_USER_BY_USERNAME % user_name
            d = self.dbpool.runQuery(sql)
            # d = self.dbpool.runQuery(dbqueryconst.SEARCH_USER_BY_USERNAME, (user_name,))
            d.addCallback(self.search_user_by_username_success)
        else:
            print "invalid cmd"


    def user_create_success(self, results):
        print results
        print "user_create_success"

    def search_user_by_username_success(self, results):
        print results
        print "search_user_by_username_success"

    def search_user_by_username_fail(self, results):
        print results
        print "search_user_by_username_fail"