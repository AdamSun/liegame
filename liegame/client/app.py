# -*- coding: utf-8 -*-

'''
    the main app of game
    created by Adam Sun
'''

import pygame
from pygame.locals import *
from config import resconfig, serverconfig
from sys import exit
from network.network import LieGameFactory
from twisted.internet import reactor
from model import globaldata

pygame.init()
screen = pygame.display.set_mode((1024, 731), 0, 32)
pygame.display.set_caption("lie game client")

bg = pygame.image.load(resconfig.get_bg_res()).convert()

# print pygame.font.get_fonts()
font = pygame.font.SysFont("fangsong", 16)
text_surface = font.render(globaldata.test_data, True, (0, 0, 255))

# connect the server
reactor.connectTCP(serverconfig.IP, serverconfig.PORT, LieGameFactory())
reactor.run()

# game event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(bg, (0, 0))
    if globaldata.test_data_change:
        text_surface = font.render(globaldata.test_data, True, (0, 0, 255))
        globaldata.test_data_change = False
    screen.blit(text_surface, (200, 200))
    pygame.display.update()