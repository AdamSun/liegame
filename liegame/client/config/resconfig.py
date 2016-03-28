# -*- coding: utf-8 -*-

'''
    created by Adam Sun
'''

bg_res_path = 'res/bg/%d%s'

def get_bg_res(index = 0, suffix = '.jpg'):
    return bg_res_path % (index, suffix)