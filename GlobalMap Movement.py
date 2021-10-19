# import pygame
import  linecache
import ast
import re
import pandas as pd


# class Ship(pygame.sprite.Sprite):
#
#     def __init__(self, speed, color):
#         super().__init__()
#         self.image = pygame.Surface((10, 10))
#         self.image.set_colorkey((12,34,56))
#         self.image.fill((12,34,56))
#         pygame.draw.circle(self.image, color, (5, 5), 3)
#         self.rect = self.image.get_rect()
#
#         self.pos = pygame.Vector2(0, 0)
#         self.set_target((0, 0))
#         self.speed = speed
#
#     def set_target(self, pos):
#         self.target = pygame.Vector2(pos)
#
#     def update(self):
#         move = self.target - self.pos
#         move_length = move.length()
#
#         if move_length < self.speed:
#             self.pos = self.target
#         elif move_length != 0:
#             move.normalize_ip()
#             move = move * self.speed
#             self.pos += move
#
#         self.rect.topleft = list(int(v) for v in self.pos)
#
# def main():
#     pygame.init()
#     quit = False
#     screen = pygame.display.set_mode((300, 300))
#     clock = pygame.time.Clock()
#
#     group = pygame.sprite.Group(
#         Ship(1.5, pygame.Color('white')),
#         Ship(3.0, pygame.Color('orange')),
#         Ship(4.5, pygame.Color('dodgerblue')))
#
#     while not quit:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 for ship in group.sprites():
#                     ship.set_target(pygame.mouse.get_pos())
#
#         group.update()
#         screen.fill((20, 20, 20))
#         group.draw(screen)
#         pygame.display.flip()
#         clock.tick(60)
#
# if __name__ == '__main__':
#     main()












#
# # import
# import pygame
#
# # initialize pygame
# pygame.init()
#
# # frame rate variables
# FPS = 120
# clock = pygame.time.Clock()
#
# # game variables
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 800
#
# # colors
# BLUE = (0, 0, 255)
#
# # activate screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Bonker')
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         # init the sprite class
#         pygame.sprite.Sprite.__init__(self)
#         self.rect = pygame.Rect(0, 0, 40, 40)
#         self.rect.x = x
#         self.rect.y = y
#         self.radius = 20
#         self.destination = None
#         self.moving = False
#         self.dx = 0
#         self.dy = 0
#
#     def set_destination(self, pos):
#         self.destination = pos
#         # delta x and delta y
#         self.dx = self.destination[0] - self.rect.centerx
#         self.dy = self.destination[1] - self.rect.centery
#
#         self.moving = True
#
#     def move(self):
#         if self.rect.centerx != self.destination[0]:
#             if self.dx > 0:
#                 self.rect.centerx += 1
#             elif self.dx < 0:
#                 self.rect.centerx -= 1
#
#         if self.rect.centery != self.destination[1]:
#             if self.dy > 0:
#                 self.rect.centery += 1
#             elif self.dy < 0:
#                 self.rect.centery -= 1
#         elif self.rect.center == self.destination:
#             self.moving = False
#
#     def draw(self):
#         # draw the circle
#         pygame.draw.circle(screen, BLUE, self.rect.center, self.radius)
#
#
# # create instances
# # player instance
# player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
# player.draw()
#
# # main loop
# run = True
# movetime = 100
# move = False
#
# while run:
#     # run frame rate
#     dt = clock.tick(FPS)
#     movetime -= dt
#     if movetime <= 0:
#         move = True
#         movetime = 400
#
#     # events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             player.set_destination(mouse_pos)
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 run = False
#
#     if player.moving:
#         player.move()
#
#     screen.fill((0, 0, 0))
# #     player.draw()
# #     pygame.display.update()
# #
# pygame.quit()

# with open('BattleScreen/units/RandomUnits.txt') as f:
#     h_unit =  [ast.literal_eval(s) for s in next(f)[:-1].split()]
#         #linecache.getline('BattleScreen/units/RandomUnits.txt',1)
#     #h_unit_healthbar =
#     #linecache.getline('BattleScreen/units/RandomUnits.txt',2)
#     #h_unit_armorbar = linecache.getline('BattleScreen/units/RandomUnits.txt',3)
#     print(h_unit)
#     #print(h_unit_healthbar)
#     #print(h_unit_armorbar)

# h_unit_healthbar = ()
# h_unit_armorbar = ()
# Fighter = ()
#with open('BattleScreen/units/RandomUnits.txt', 'r') as f:
    # for line in f.readlines():
    #     l = line.strip().split(',')
    #     Fighter = l[0]
    #     h_unit_healthbar = l[1]
    #     h_unit_armorbar = l[2]
# for i in open('BattleScreen/units/RandomUnits.txt'):
#     parse(i)
#     print(i)
# with open("file.txt") as f:
#     a, b, c, d = [[s[0], float(s[1]), int(s[2]), bool(s[3])] \
#                   for s in [next(f)[:-1].split()]][0]
# Based on Niclas Nilsson's comment I could do the following:
#
# a,b,c,d= [ast.literal_eval(s) for s in next(f)[:-1].split()]
##h_unit =  [ast.literal_eval(s) for s in next(f)[:-1].split()]
# # with open('BattleScreen/units/RandomUnits.txt') as f:
# #     Fighter = Fighter
# h_unit = tuple(linecache.getline('BattleScreen/units/RandomUnits.txt',1).split(','))
# #     print(h_unit)
#
#
# #h_unit = tuple(pd.read_csv('BattleScreen/units/RandomUnits.txt', nrows=0))
# print(h_unit)