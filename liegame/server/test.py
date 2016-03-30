# -*- coding: utf-8 -*-

'''
    created by Adam Sun
'''

from common import event

class A(object):
    def abc(self, data):
        if data:
            print data
        else:
            print "abc"

arr = []

def test_func(func):
    arr.append(func)
    if callable(func):
        func()

a = A()
b = A()
# test_func(a.abc)
# test_func(a.abc)

# if arr[0] == arr[1]:
#     print "the same func"

event_manager = event.EventManager()
event_manager.add_event("abc", a.abc)
event_manager.add_event("abc", b.abc)
event_manager.dispatch_event("abc", "bac")