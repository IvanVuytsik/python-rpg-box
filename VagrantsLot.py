import inspect
import pyautogui
from button import *
import pygame, sys, random,time,os
import collections
from collections import Counter
from pygame.locals import *
import pygame as py
import itertools
vec = pygame.math.Vector2
from abc import ABC, abstractmethod
import threading
from tkinter import *
from pygame.locals import *
import numpy as np
import re
import pandas as pd
import button
import linecache
import json
from itertools import cycle
from random import shuffle
from PIL import Image
from scipy.ndimage import zoom
import scipy

# srcImage = Image.open("WorldMap/BWMap.png")
# grayImage = srcImage.convert('L')
# array = np.array(grayImage)
# array = zoom(array, 310/174)
# np.savetxt("WorldMap/mapbinarized.txt", array<128, fmt="%d")

mainClock = pygame.time.Clock()

pygame.init()
pygame.mixer.set_num_channels(32)
pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.display.set_caption("Vagrant's Lot")  # screen window name
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode((1280, 720), 0, 32)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

bg_main_menu = pygame.image.load("MainMenuRes/MainMenu.png").convert_alpha()
bg_main_menu = pygame.transform.scale(bg_main_menu, (int(WINDOW_SIZE[0]), (int(WINDOW_SIZE[1]))))

normal_icon = pygame.image.load("WorldMap/cursor_final.png").convert_alpha()
normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

bg_infosheet = pygame.image.load("MainMenuRes/scroll.png").convert_alpha()
bg_infosheet = pygame.transform.scale(bg_infosheet, (int(WINDOW_SIZE[0] * 0.6), (int(WINDOW_SIZE[1] * 0.6))))

# display = pygame.Surface((800,600))
# mouse_position = pygame.mouse.get_pos()
select_sound = pygame.mixer.Sound('MainMenuRes/selection.wav')
scroll_sound = pygame.mixer.Sound('WorldMap/scroll_sound.wav')
inv_click_sound = pygame.mixer.Sound('MainMenuRes/inventory/inv_click.wav')
inv_click_sound.set_volume(0.5)

def play_music(type):
    global play_music
    if type == 'Adventure':
        pygame.mixer.music.load('ExplorationMaps/sounds/forest.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
    elif type == 'Battle':
        pygame.mixer.music.load('BattleScreen/resources/sounds/battlemusic.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
    elif type == 'Battle1':
        pygame.mixer.music.load('BattleScreen/resources/sounds/battlemusic1.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif type == 'Battle2':
        pygame.mixer.music.load('BattleScreen/resources/sounds/battlemusic2.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif type == 'Battle3':
        pygame.mixer.music.load('BattleScreen/resources/sounds/battlemusic3.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif type == 'Battle4':
        pygame.mixer.music.load('BattleScreen/resources/sounds/battlemusic1.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif type == 'Map':
        pygame.mixer.music.load('WorldMap/WorldMapOst.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.02)
    elif type == 'MainTheme':
        pygame.mixer.music.load('MainTheme.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif type == 'Outro':
        pygame.mixer.music.load('OutroSong.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif type == 'BattleVictory':
        pygame.mixer.music.load('BattleScreen/resources/sounds/victory.mp3')
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.1)
    elif type == 'BattleDefeat':
        pygame.mixer.music.load('BattleScreen/resources/sounds/defeat.mp3')
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.1)
    else:
        pygame.mixer.music.fadeout(2500)

if __name__ == '__main__':
    play_music('MainTheme')
    font = pygame.font.SysFont('Times New Roman', 18)
    fontMenu = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
    fontStats = pygame.font.Font('WorldMap/ESKARGOT.ttf', 20)
    fontDescription = pygame.font.SysFont('Times New Roman', 22)
    fontMenuLarge = pygame.font.Font('WorldMap/ESKARGOT.ttf', 48)
    fontMenuCharSheet = pygame.font.Font('WorldMap/ESKARGOT.ttf', 100)
    # pygame.font.Font('WorldMap/ESKARGOT.ttf', 20)
    player_rect = pygame.Rect((screen.get_width() / 2), (screen.get_height() / 2), 50, 50)

def draw_bg_main_menu():
    screen.blit(bg_main_menu, (0, 0))

def draw_infosheet(screen, xcor, ycor):
    screen.blit(bg_infosheet, (xcor, ycor))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# def draw_tips(tips, xcor,ycor):
#     tips_list = []
#     line_spacing_count = 0
#     for line in tips.split('\n'):
#         tips = fontDescription.render(line,True,'#2c2d47')
#         tips_list.append(tips)
#         line_spacing_count += 25
#         screen.blit(tips,(xcor, ycor + (line_spacing_count*1)))

# tips_path = open('MainMenuRes/Tips.txt','r')
# tips_path_lore = tips_path.read()
# tips_path.close()

def mouse_map_position_align(x, y):
    pyautogui.moveTo(x, y)

menuClick = False

def main_menu():
    global menuClick
    clicked = False
    clicking = False
    mouse_position = pygame.mouse.get_pos()
    main_menu_running = True
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

    screen = pygame.display.set_mode((1280, 720), 0, 32)

    fullscreen = button.fullscreen
    #     not bool(linecache.getline('genericmap.txt',1))
    # with open('genericmap.txt', 'w') as file:
    #     file.write(str(fullscreen))

    if fullscreen:
        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

    button_2 = pygame.Rect(520, 320, 200, 50)
    # button_1 = pygame.Rect(520,320,200,50)
    #     #ToggleButton (screen,520,320, bg_infosheet, 200,50, 0, True, "Tips" )
    button_3 = pygame.Rect(520, 420, 200, 50)

    # -----------------------------Particles-------------------------------
    particles = []

    def circle_surf(radius, color):
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey((0, 0, 0))
        return surf

    while main_menu_running:
        screen.fill((0, 0, 0))
        draw_bg_main_menu()
        draw_text('Vagrant\'s Lot', fontMenu, (255, 225, 100), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        if button_2.collidepoint((mx, my)):
            if menuClick:
                pygame.mixer.Sound(select_sound).play()
                stats()
        if button_3.collidepoint((mx, my)):  # quit button
            if menuClick:
                pygame.mixer.Sound(select_sound).play()
                main_menu_running = False

        # pygame.draw.rect(screen, (255,0,0), button_1)
        # pygame.draw.rect(screen, (0,255,0), button_2)
        # pygame.draw.rect(screen, (0,0,255), button_3)

        # if button_1.collidepoint(mouse_position):
        #     draw_text('Tips', fontMenu, (255,255,150),screen, 590,320)
        # else:
        #     draw_text('Tips', fontMenu, (255,225,100),screen, 590,320)

        if button_2.collidepoint(mouse_position):
            draw_text('New Campaign', fontMenu, (255, 255, 150), screen, 530, 320)
        else:
            draw_text('New Campaign', fontMenu, (255, 225, 100), screen, 530, 320)

        if button_3.collidepoint(mouse_position):
            draw_text('Quit', fontMenu, (255, 255, 150), screen, 600, 420)
        else:
            draw_text('Quit', fontMenu, (255, 225, 100), screen, 600, 420)

            # if button_1.collidepoint((mx,my)) and clicked:
            #     draw_infosheet(screen,button_1.x-260,button_1.y-200)
            #     draw_tips(tips_path_lore, button_1.x-210,button_1.y-180)
            #     if menuClick:
            #         pygame.mixer.Sound(scroll_sound).play()
            # elif not button_1.collidepoint((mx,my)):
            #     clicked = False

        # -------------------------Partiles--------------------------
        # location / velocity / timer

        # particles.append([[mouse_position[0] ,mouse_position[1]],[random.randint(0,20)/10 - 1, -2],random.randint(4,6)])
        if clicking:
            for i in range(10):
                particles.append([[mx, my], [random.randint(0, 40) / 6 - 3.5, random.randint(0, 40) / 6 - 3.5],
                                  random.randint(2, 4)])

        particles.append([[480, 660], [random.randint(9, 10) / 10 - 1, -2], random.randint(4, 6)])
        for particle in particles:
            particle[0][0] += particle[1][0]  # x velocity
            particle[0][1] += particle[1][1]  # y velocity
            particle[1][1] -= 0.001
            particle[2] -= 0.35
            pygame.draw.circle(screen, (255, 225, 100), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 1.5
        screen.blit(circle_surf(radius, (220, 20, 20)),
                    (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                    special_flags=BLEND_RGB_ADD)

        if particle[2] <= 0:
            particles.remove(particle)
        # -----------------------------------------------------------------------------

        menuClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), 0, 32)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_o:
                    button.fullscreen = not button.fullscreen
                    fullscreen = button.fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    menuClick = True
                    clicking = True
                if event.button == 1 and clicked == False:
                    clicked = True
                elif event.button == 1 and clicked == True:
                    clicked = False

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False

        screen.blit(normal_icon, player_rect)
        pygame.mouse.set_visible(False)
        mouse_position = pygame.mouse.get_pos()
        player_rect.x, player_rect.y = mouse_position

        pygame.display.update()
        mainClock.tick(60)

































































































































































def stats():
    stats_running = True
    menuClick = False
    clicked = False
    roll_dice = False
    mouse_position = pygame.mouse.get_pos()
    mx, my = pygame.mouse.get_pos()
    inventory_active = False
    skills_active = False
    WINDOW_SIZE = (1280, 720)
    screen = pygame.display.set_mode((1280, 720))
    display = pygame.Surface((1280, 720))
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    # surface = pygame.Surface((1280, 720))
    # screen.blit(surface, (1280, 720))

    fullscreen = button.fullscreen
    # not bool(linecache.getline('genericmap.txt',1))
    if fullscreen:
        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

    bg_char_sheet = pygame.image.load("MainMenuRes/charsheet.png").convert_alpha()
    bg_char_sheet = pygame.transform.scale(bg_char_sheet, (int(WINDOW_SIZE[0] * 1), (int(WINDOW_SIZE[1] * 1))))

    bg_char_sheet_lid = pygame.image.load("MainMenuRes/charsheetlid.png").convert_alpha()
    bg_char_sheet_lid = pygame.transform.scale(bg_char_sheet_lid, (int(WINDOW_SIZE[0] * 1), (int(WINDOW_SIZE[1] * 1))))

    dice_icon = pygame.image.load("MainMenuRes/dice.png").convert_alpha()
    dice_icon = pygame.transform.scale(dice_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    plus_icon = pygame.image.load("MainMenuRes/plus.png").convert_alpha()
    plus_icon = pygame.transform.scale(plus_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    minus_icon = pygame.image.load("MainMenuRes/minus.png").convert_alpha()
    minus_icon = pygame.transform.scale(minus_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    plus_green_icon = pygame.image.load("MainMenuRes/plus_green.png").convert_alpha()
    plus_green_icon = pygame.transform.scale(plus_green_icon, (int(WINDOW_SIZE[0] * 0.015), (int(WINDOW_SIZE[1] * 0.025))))

    bg_pointer = pygame.image.load("MainMenuRes/pointerDark.png").convert_alpha()
    bg_pointer = pygame.transform.scale(bg_pointer, (int(WINDOW_SIZE[0] * 0.05), (int(WINDOW_SIZE[1] * 0.06))))

    inventory_icon = pygame.image.load("MainMenuRes/inventorybag.png").convert_alpha()
    inventory_icon = pygame.transform.scale(inventory_icon,(int(WINDOW_SIZE[0] * 0.015), (int(WINDOW_SIZE[1] * 0.025))))

    skills_icon = pygame.image.load("MainMenuRes/skills_icon.png").convert_alpha()
    skills_icon = pygame.transform.scale(skills_icon, (int(WINDOW_SIZE[0] * 0.03), (int(WINDOW_SIZE[1] * 0.06))))

    troops_icon = pygame.image.load("MainMenuRes/troops_icon.png").convert_alpha()
    troops_icon = pygame.transform.scale(troops_icon, (int(WINDOW_SIZE[0] * 0.03), (int(WINDOW_SIZE[1] * 0.06))))

    inv_arrow_up = pygame.image.load("MainMenuRes/inventory/inv_arrow_dark.png").convert_alpha()
    inv_arrow_up = pygame.transform.scale(inv_arrow_up, (int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.020))))
    inv_arrow_down = pygame.image.load("MainMenuRes/inventory/inv_arrow_dark.png").convert_alpha()
    inv_arrow_down = pygame.transform.scale(inv_arrow_down,(int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.020))))
    inv_arrow_down = pygame.transform.flip(inv_arrow_down, False, True)
    inv_return = pygame.image.load("MainMenuRes/inventory/inv_return_button.png").convert_alpha()
    inv_return = pygame.transform.scale(inv_return,(int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.20))))

    skill_scroll = pygame.image.load("MainMenuRes/techniques/skill_scroll.png").convert_alpha()
    skill_scroll = pygame.transform.scale(skill_scroll, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))
    gm_check = pygame.image.load("WorldMap/check.png").convert_alpha()
    gm_check = pygame.transform.scale(gm_check, (int(WINDOW_SIZE[0] * 0.06), (int(WINDOW_SIZE[1] * 0.06))))
    gm_cross = pygame.image.load("WorldMap/cross.png").convert_alpha()
    gm_cross = pygame.transform.scale(gm_cross, (int(WINDOW_SIZE[0] * 0.06), (int(WINDOW_SIZE[1] * 0.06))))
    gm_greencheck = pygame.image.load("WorldMap/greencheck.png").convert_alpha()
    gm_greencheck = pygame.transform.scale(gm_greencheck, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.03))))
    gm_greencross = pygame.image.load("WorldMap/greencrosses.png").convert_alpha()
    gm_greencross = pygame.transform.scale(gm_greencross, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.03))))

    font = pygame.font.SysFont('Times New Roman', 18)
    fontMenu = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
    fontStats = pygame.font.Font('WorldMap/ESKARGOT.ttf', 20)
    fontDescription = pygame.font.SysFont('Times New Roman', 22)
    fontMenuLarge = pygame.font.Font('WorldMap/ESKARGOT.ttf', 48)
    fontMenuCharSheet = pygame.font.Font('WorldMap/ESKARGOT.ttf', 100)

    select_sound = pygame.mixer.Sound('MainMenuRes/selection.wav')

    randomlist = []
    for i in range(0, 10):
        n = random.randint(1, 10)
        randomlist.append(n)

    # ----------------------------------Animations------------------------------------
    global animation_frames
    animation_frames = {}

    def animation_load(path, frame_durations):
        global animation_frames
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            animation_image = pygame.image.load(img_loc).convert()
            animation_image.set_colorkey((0, 0, 0))
            animation_image = pygame.transform.scale(animation_image, (160, 160))
            animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    animation_database = {}
    animation_database['apple'] = animation_load('MainMenuRes/rowan/apple', [100, 200, 50, 50, 50, 50])
    animation_database['idle'] = animation_load('MainMenuRes/rowan/idle', [50, 50])
    rowan_action = random.choice(['idle', 'apple'])
    rowan_frame = 0
    rowan_rect = pygame.Rect(80, 100, 80, 120)

    # ------------------------------------------------------------------------------------
    def draw_bg_char_sheet(x, y):
        display.blit(bg_char_sheet, (x, y))

    def draw_bg_char_sheet_lid(x, y):
        display.blit(bg_char_sheet_lid, (x, y))

    def stats_draw_text(number, font, color, surface, x, y):
        textobj = font.render(number, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    # def draw_rowan_portrait():
    #     screen.blit(bg_rowan,(85,100))
    # ----------------------------RollButton--------------------------------
    roll_button = button.Button(display, 140, 655, dice_icon, 40, 40, 0, True, 'Roll Dice')
    # plus_button = button.Button(display, 200, 200, plus_icon, 15,20,0, True,'Increase')
    # minus_button = button.Button(display, 180, 200, minus_icon, 15,20,0, True,'Decrease')

    # ----------------------------FreeStatsSButton--------------------------------
    bottom_text = (780, 690)

    # char_level = 1
    # char_experience = 0
    stat_distributable = 0 + button.learning_points

    bonus_ranged_damage = 0
    bonus_melee_damage = 0
    bonus_critical_strike = 0
    bonus_parry = 0
    bonus_block = 0
    bonus_leadership = 0

    bonus_tricks = 0
    bonus_supply = 0
    bonus_health_points = 0
    bonus_armor_points = 0

    bonus_threshold = 0
    bonus_defence = 0
    bonus_arcana_res = 0
    bonus_energy_res = 0
    bonus_frost_res = 0
    bonus_fire_res = 0
    bonus_poison_res = 0

    # with open('MainMenuRes/char_statistic/charbonussecondary.txt', 'w') as out:
    #     out.writelines(
    #         [str(bonus_ranged_damage) + "\n", str(bonus_melee_damage) + "\n", str(bonus_critical_strike) + "\n",
    #          str(bonus_tricks) + "\n",
    #          str(bonus_supply) + "\n", str(bonus_health_points) + "\n", str(bonus_armor_points) + "\n",
    #          str(bonus_threshold) + "\n",
    #          str(bonus_defence) + "\n", str(bonus_arcana_res) + "\n", str(bonus_energy_res) + "\n",
    #          str(bonus_frost_res) + "\n",
    #          str(bonus_fire_res) + "\n", str(bonus_poison_res)])

    class Stat():
        def __init__(self, value):
            self.value = value

        def draw(self, plus_X, plus_Y, minus_X, minus_Y):
            plus_button = button.Button(display, plus_X, plus_Y, plus_icon, 15, 20, 0, True, 'Increase')
            minus_button = button.Button(display, minus_X, minus_Y, minus_icon, 15, 20, 0, True, 'Decrease')
            if plus_button.draw() and button.learning_points != 0:
                self.value += 1
                button.learning_points -= 1
                time.sleep(0.1)
            elif minus_button.draw() and self.value > 0:  # and button.learning_points <= button.learning_points - 1:
                self.value -= 1
                time.sleep(0.1)
                button.learning_points += 1
            if self.value > 0:
                display.blit(plus_green_icon, (plus_button.rect.x - 2, plus_button.rect.y))
            # return self.value

    bonus_melee = Stat(0)
    bonus_ranged = Stat(0)
    bonus_parrying = Stat(0)
    bonus_athletics = Stat(0)
    bonus_intimidation = Stat(0)
    bonus_tactics = Stat(0)
    bonus_arming = Stat(0)
    bonus_siege = Stat(0)

    bonus_skirmish = []
    bonus_skirmish.extend((bonus_melee, bonus_ranged, bonus_parrying,
                           bonus_athletics, bonus_intimidation, bonus_tactics,
                           bonus_arming, bonus_siege))

    bonus_acrobatics = Stat(0)
    bonus_stealth = Stat(0)
    bonus_thievery = Stat(0)
    bonus_lockpicking = Stat(0)
    bonus_deception = Stat(0)
    bonus_traps = Stat(0)
    bonus_stupefy = Stat(0)
    bonus_nature = Stat(0)

    bonus_survival = []
    bonus_survival.extend((bonus_acrobatics, bonus_stealth, bonus_thievery,
                           bonus_lockpicking, bonus_deception, bonus_traps,
                           bonus_stupefy, bonus_nature))

    bonus_investigation = Stat(0)
    bonus_medicine = Stat(0)
    bonus_lore = Stat(0)
    bonus_persuasion = Stat(0)
    bonus_arcane = Stat(0)
    bonus_divine = Stat(0)
    bonus_alchemy = Stat(0)
    bonus_engineering = Stat(0)

    bonus_savviness = []
    bonus_savviness.extend((bonus_investigation, bonus_medicine, bonus_lore,
                            bonus_persuasion, bonus_arcane, bonus_divine,
                            bonus_alchemy, bonus_engineering))

    def draw_bonus_stats(xPl, yPl, xMn, yMn, bonus_tree, plXmod, plYmod, mnXmod, mnYmod):
        Plx = 0
        Ply = 0
        Mnx = 0
        Mny = 0
        for i in bonus_tree:
            Plx += plXmod
            Ply += plYmod
            Mnx += mnXmod
            Mny += mnYmod
            i.draw(xPl + Plx, yPl + Ply, xMn + Mnx, yMn + Mny)
    # ------------------------------------------------------------------
    def show_skills(surface, skill_tree, x, y, Yspacing, Xspacing):
        spacing_ver = 0
        spacing_hor = 0
        for i in skill_tree:
            j = fontStats.render(str(i), True, (0, 0, 0))
            spacing_ver += Yspacing
            spacing_hor += Xspacing
            surface.blit(j, (x + (spacing_hor * 1), y + (spacing_ver * 1)))

    attributes_open = open('MainMenuRes/attributes.txt', 'r')
    attributes_read = attributes_open.read()
    attributes_open.close()
    attributes_path = open('MainMenuRes/attributes_description.txt', 'r')
    attributes_txt = 'MainMenuRes/attributes_description.txt'
    attributes_lore = attributes_path.read()
    attributes_path.close()

    skills_open = open('MainMenuRes/skills_list.txt', 'r')
    skills_read = skills_open.read()
    skills_open.close()
    skirmish_path = open('MainMenuRes/skirmish_tree_description.txt', 'r')
    skirmish_txt = 'MainMenuRes/skirmish_tree_description.txt'
    skirmish_lore = skirmish_path.read()
    skirmish_path.close()
    survival_path = open('MainMenuRes/survival_tree_description.txt', 'r')
    survival_txt = 'MainMenuRes/survival_tree_description.txt'
    survival_lore = survival_path.read()
    survival_path.close()
    savviness_path = open('MainMenuRes/savviness_tree_description.txt', 'r')
    savviness_txt = 'MainMenuRes/savviness_tree_description.txt'
    savviness_lore = savviness_path.read()
    savviness_path.close()
    resistanes_path = open('MainMenuRes/resistances.txt', 'r')
    resistanes_txt = 'MainMenuRes/resistances.txt'
    resistanes_lore = resistanes_path.read()
    resistanes_path.close()

    attack_path = open('MainMenuRes/attacks.txt', 'r')
    attack_txt = 'MainMenuRes/attacks.txt'
    attack_lore = attack_path.read()
    attack_path.close()

    def show_attributes_skills(text, txt, Xspacing, Yspacing, rectX, rectY):
        lines_list = []
        rect_list = []
        spacingX = 0
        spacingY = 0
        count_lines = 0
        counter = 0
        for i in text.split('\n'):
            line = fontDescription.render(i, True, (0, 0, 0,))
            lines_list.append(line)
            count_lines += 1
        for rect in range(count_lines):
            spacingX += Xspacing
            spacingY += Yspacing
            rect = pygame.Rect(rectX + (spacingX * 1), rectY + (spacingY * 1), 70, 10)
            rect_list.append(rect)
            # pygame.draw.rect(screen, (255,0,0), rect)
            counter += 1
            if rect.collidepoint(mouse_position):
                descr = linecache.getline(txt, counter).rstrip('\n')
                stats_draw_text(descr, fontDescription, (0, 0, 0,), display, 490, 690)
    # ----------------------------------------------------------------------
    def show_names(surface, text, x, y, modX, ModY, deli0, deli1, deli2):
        spacingX = 0
        spacingY = 0
        for i in text.split('\n')[deli0:deli1:deli2]:
            j = fontStats.render(str(i), True, (0, 0, 0))
            k = fontStats.render(str(i)[:1], True, (255, 255, 150))
            spacingX += modX
            spacingY += ModY
            surface.blit(j, (x + (spacingX * 1), y + (spacingY * 1)))
            surface.blit(k, (x + (spacingX * 1), y + (spacingY * 1)))

    # ---------------------------------------Inventory----------------------------------
    path, dirs, bow = next(os.walk("MainMenuRes/inventory/items/bow"))
    bow_count = len(bow)
    BOW_TYPES = bow_count
    path, dirs, armor = next(os.walk("MainMenuRes/inventory/items/armor"))
    armor_count = len(armor)
    ARMOR_TYPES = armor_count
    path, dirs, cloak = next(os.walk("MainMenuRes/inventory/items/cloak"))
    cloak_count = len(cloak)
    CLOAK_TYPES = cloak_count
    path, dirs, dagger = next(os.walk("MainMenuRes/inventory/items/dagger"))
    dagger_count = len(dagger)
    DAGGER_TYPES = dagger_count
    path, dirs, gloves = next(os.walk("MainMenuRes/inventory/items/gloves"))
    gloves_count = len(gloves)
    GLOVES_TYPES = gloves_count
    path, dirs, helm = next(os.walk("MainMenuRes/inventory/items/helm"))
    helm_count = len(helm)
    HELM_TYPES = helm_count
    path, dirs, necklace = next(os.walk("MainMenuRes/inventory/items/necklace"))
    necklace_count = len(necklace)
    NECKLACE_TYPES = necklace_count
    path, dirs, pants = next(os.walk("MainMenuRes/inventory/items/pants"))
    pants_count = len(pants)
    PANTS_TYPES = pants_count
    path, dirs, ring = next(os.walk("MainMenuRes/inventory/items/ring"))
    ring_count = len(ring)
    RING_TYPES = ring_count
    path, dirs, shoes = next(os.walk("MainMenuRes/inventory/items/shoes"))
    shoes_count = len(shoes)
    SHOES_TYPES = shoes_count
    path, dirs, sword = next(os.walk("MainMenuRes/inventory/items/sword"))
    sword_count = len(sword)
    SWORD_TYPES = sword_count
    path, dirs, belt = next(os.walk("MainMenuRes/inventory/items/belt"))
    belt_count = len(belt)
    BELT_TYPES = belt_count
    path, dirs, trinkets = next(os.walk("MainMenuRes/inventory/items/trinkets"))
    trinkets_count = len(trinkets)
    TRINKETS_TYPES = trinkets_count

    path, dirs, slots = next(os.walk("MainMenuRes/inventory/slots"))
    slots_count = len(slots)
    SLOT_TYPES = slots_count
    #-------------------------------------------------------------------------------------


    #------------------------------------Troops---------------------------------------
    class Troops():
        def __init__(self, image,scale,descr,bonus,status,id,value):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.toggled = False
            self.bonus = bonus
            self.descr = descr
            self.status = status
            self.id = id
            self.value = value

        def item_text(self,text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            if skills_active == True:
                surface.blit(textobj, textrect)

        def draw(self, surface, x, y):
            self.x = x
            self.y = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            action = False
            self.clicked = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
            if troops_active == True:
                surface.blit(self.image, (self.rect.x, self.rect.y))
            return action

    #-------------------------------------TroopsButtons--------------------------------
    TILE_SIZE = 64
    path, dirs, types = next(os.walk("MainMenuRes/troops/types"))
    types_count = len(types)
    TROOPS_TYPES = types_count
    types_img = []
    for x in range(TROOPS_TYPES):
        img = pygame.image.load(f'MainMenuRes/troops/types/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        types_img.append(img)

    def draw_empty_troops_slots():
        if troops_active == True:
            for y in range(4):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[11], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[0], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    novice = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE,ranks_img[0].get_width(), ranks_img[0].get_height())
                    if novice.collidepoint(mouse_position):
                        stats_draw_text('Close combat units', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[1], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))
                    adept = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE,ranks_img[1].get_width(), ranks_img[1].get_height())
                    if adept.collidepoint(mouse_position):
                        stats_draw_text('Range combat units', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[2], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE))
                    expert = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE,ranks_img[2].get_width(), ranks_img[2].get_height())
                    if expert.collidepoint(mouse_position):
                        stats_draw_text('Cavalry and beasts', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[3], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE))
                    master = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE,ranks_img[3].get_width(), ranks_img[3].get_height())
                    if master.collidepoint(mouse_position):
                        stats_draw_text('War machines and support units', fontDescription, (0, 0, 0,), display, 490, 690)

    #----------------------------------------Techniques/Skills--------------------------------
    #global skill_counter
    class Technique():
        def __init__(self,x,y,image,scale,descr,skillcheck,status,id,skillvalue,effect,tier,value):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.image_rect = self.image.get_rect()
            self.rect = self.image.get_rect()
            self.rect.x = x*TILE_SIZE
            self.rect.y = y*TILE_SIZE
            self.toggled = False
            self.skillcheck = skillcheck
            self.descr = descr
            self.status = status
            self.id = id
            self.effect = effect
            self.skillvalue = skillvalue
            self.tier = tier
            self.value = value

        def item_text(self,text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            if skills_active == True:
                surface.blit(textobj, textrect)

        def skill_scroll(self, surface):
            surface.blit(skill_scroll, (surface.get_width() * 0.28, surface.get_height() * 0.26))

        def skill_text(self, surface, text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            surface.blit(img, (x, y))

        def draw(self, surface, x, y):
            self.x = x
            self.y = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            selection_rect = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
            action = False
            self.clicked = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and \
                skills_active == True and self.status == 0 and self.value <= button.learning_points:
                    action = True
                    self.clicked = True
                    self.status = 1
                    button.learning_points -= self.value
                    #button.start_learning_points = button.learning_points

            # if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
            #     self.clicked = False
            if skills_active == True:
                if self.toggled == True:
                    pygame.draw.rect(surface, (225, 225, 225), selection_rect)
                surface.blit(self.image, (self.rect.x, self.rect.y))
            return action

        def event_handler (self,event):
            action = False
            pos = pygame.mouse.get_pos()
            #for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if skills_active == True:
                    if event.button == 1 and self.toggled == False and \
                            skills_active == True and self.value <= button.learning_points:
                        if self.rect.collidepoint(event.pos):
                            self.toggled = True
                            self.status = 1
                            pygame.mixer.Sound(select_sound).play()
                            button.learning_points -= self.value
                    # elif event.button == 1 and self.toggled == True:
                    #     if self.rect.collidepoint(event.pos):
                    #         self.toggled = False

    #-------------------------------------SkillButtons--------------------------------
    path, dirs, ranks = next(os.walk("MainMenuRes/techniques/ranks"))
    ranks_count = len(ranks)
    RANK_TYPES = ranks_count
    ranks_img = []
    path, dirs, techniques = next(os.walk("MainMenuRes/techniques/all"))
    techniques_count = len(techniques)
    TECHNIQUE_TYPES = techniques_count
    techniques_img = []
    path, dirs, inactive = next(os.walk("MainMenuRes/techniques/inactive"))
    inactive_count = len(inactive)
    INACTIVE_TYPES = inactive_count
    inactive_img = []
    for x in range(RANK_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/ranks/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        ranks_img.append(img)
    for x in range(TECHNIQUE_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/all/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        techniques_img.append(img)
    for x in range(INACTIVE_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/inactive/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        inactive_img.append(img)

    skill_counter = 0       # counts availability of new tiers
    def draw_empty_skill_slots():
        if skills_active == True:
            for y in range(4):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[10], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[0], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE))
                    novice = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE,ranks_img[0].get_width(), ranks_img[0].get_height())
                    if novice.collidepoint(mouse_position):
                        stats_draw_text('Novice Tier', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[1], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE))
                    adept = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE,ranks_img[1].get_width(), ranks_img[1].get_height())
                    if adept.collidepoint(mouse_position):
                        stats_draw_text('Adept Tier || Requires 6 Learned Techniques', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[2], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))
                    expert = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE,ranks_img[2].get_width(), ranks_img[2].get_height())
                    if expert.collidepoint(mouse_position):
                        stats_draw_text('Expert Tier || Requires 12 Learned Techniques', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[3], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    master = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE,ranks_img[3].get_width(), ranks_img[3].get_height())
                    if master.collidepoint(mouse_position):
                        stats_draw_text('Master Tier || Requires 18 Learned Techniques', fontDescription, (0, 0, 0,), display, 490, 690)
            #-------------------------------------------------------------------------
            if skill_counter >= 0:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE))
            if skill_counter >= 6:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE))
            if skill_counter >= 12:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))
            if skill_counter >= 18:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))

    #---------------------------------------------------Techniques----------------------------------
    skill_novice = []
    Cartographer = Technique(7.1, 9.1,techniques_img[0], 0.8, 'Increases speed on the global map by 50%',button.nature,0,'Cartographer',0,50,1, 10)
    Combo = Technique(8.1, 9.1,techniques_img[66], 0.8,'Attack target twice in melee',button.melee,0,'Combo',0,2,1, 10)
    Educated = Technique(9.1, 9.1,techniques_img[29], 0.8,'Increases experience gain by 25%',button.lore,0,'Educated',0,25,1,10)
    Quick_Shot = Technique(10.1, 9.1,techniques_img[56], 0.8,'Gives 25% chance of a free ranged attack',button.ranged,0,'Quick Shot',0,15,1, 10)
    Camp_Doctor = Technique(11.1, 9.1,techniques_img[42], 0.8, 'Increases healing rate on the map by 25%',button.medicine,0,'Camp Doctor',0,25,1, 10)
    Thief = Technique(12.1, 9.1,techniques_img[30], 0.8,'Allows to steal from traders',button.thievery,0,'Thief',0,15,1, 10)
    Quartermaster = Technique(13.1, 9.1,techniques_img[46], 0.8,'Doubles efficiency of resting in battle',button.arming,0,'Quartermaster',0,100,1, 10)
    Scout = Technique(14.1, 9.1,techniques_img[71], 0.8,'Chance to avoid encounters is increased by 25%',button.deception,0,'Scout',0,25,1, 10)
    Haggler = Technique(15.1, 9.1,techniques_img[73], 0.8,'Allows to sell items',button.intimidation,0,'Haggler',0,15,1, 10)
    Estates = Technique(16.1, 9.1,techniques_img[6], 0.8,'Increases gold income from enterprises by 25%',button.persuasion,0,'Estates',0,25,1, 10)
    Curse = Technique(17.1, 9.1,techniques_img[7], 0.8,'Decreases target resistances or defence',button.arcane,0,'Curse',0,20,1, 10)
    Healing = Technique(18.1, 9.1,techniques_img[35], 0.8,'Restores 20% of target health',button.divine,0,'Healing',0,35,1, 10)
    #---------------------------------------------------------------------------------------------------------------------
    skill_novice.extend([Cartographer,Combo,Educated,Quick_Shot, Camp_Doctor, Thief, Quartermaster,Scout, Haggler,Estates, Curse, Healing])
    #-----------------------------------------------------------------------------------------------------------------------
    skill_adept = []
    Snake_Eater = Technique(7.1, 8.1,techniques_img[18], 0.8, 'Immunity to poisons',button.medicine,0,'Snake Eater',0,50,2, 15)
    Power_Blow = Technique(8.1, 8.1,techniques_img[44], 0.8,'Killing in melee grants a free action',button.melee,0,'Power Blow',0,2,2, 15)
    Scholar = Technique(9.1, 8.1,techniques_img[4], 0.8,'Gives 5 extra learning points with every level',button.lore,0,'Scholar',0,5,2,15)
    Multiple_Shot = Technique(10.1, 8.1,techniques_img[13], 0.8,'Attack target twice with a ranged weapon',button.ranged,0,'Multiple Shot',0,2,2, 15)
    Duelist = Technique(11.1, 8.1,techniques_img[45], 0.8,'Can retaliate to ranged attacks',button.parrying,0,'Duelist',0,15,2, 15)
    Bear_Trap = Technique(12.1, 8.1,techniques_img[27], 0.8, 'Hits target every turn for 5% health',button.traps,0,'Bear Trap',0,5,2, 15)
    Potion_Master = Technique(13.1, 8.1,techniques_img[17], 0.8,'Using potions in battle is a free action',button.alchemy,0,'Potion Master',0,1,2, 15)
    Knock_Down = Technique(14.1, 8.1,techniques_img[74], 0.8,'Target has 10% chance of missing its turn',button.stupefy,0,'Knock Down',0,10,2, 15)
    Battle_Reflex = Technique(15.1, 8.1,techniques_img[38], 0.8,'Gives 20% chance to ignore ranged attacks',button.acrobatics,0,'Battle Reflex',0,20,2, 15)
    Persevere = Technique(16.1, 8.1,techniques_img[49], 0.8,'Gives 10% chance to survive a deadly strike',button.athletics,0,'Persevere',0,10,2, 15)
    Moon_Shield = Technique(17.1, 8.1,techniques_img[34], 0.8,'Creates a shield of 10% of armor every turn',button.arcane,0,'Moon Shield',0,10,2, 15)
    Purifier = Technique(18.1, 8.1,techniques_img[55], 0.8,'Removes all negative statuses from all troops',button.divine,0,'Purifier',0,25,2, 15)
    #-----------------------------------------------------------------------------------------------------------------------
    skill_adept.extend([Snake_Eater,Power_Blow,Scholar,Multiple_Shot, Duelist, Bear_Trap, Potion_Master,Knock_Down, Battle_Reflex,Persevere, Moon_Shield, Purifier])
    #-----------------------------------------------------------------------------------------------------------------------
    skill_expert = []
    Readiness = Technique(7.1, 7.1,techniques_img[33], 0.8,'Increases armor efficiency by 25%',button.arming,0,'Readiness',0,25,3, 20)
    Slice = Technique(8.1, 7.1,techniques_img[28], 0.8,'Hits multiple targets in melee',button.melee,0,'Slice',0,4,3, 20)
    War_Engineer = Technique(9.1, 7.1,techniques_img[1], 0.8,'Increases efficiency of support war machines',button.engineering,0,'War Engineer',0,2,3, 20)
    Deadeye = Technique(10.1, 7.1,techniques_img[65], 0.8,'Ranged attack critical damage is quadrupled',button.ranged,0,'Deadeye',0,50,3, 20)
    Barrage = Technique(11.1, 7.1,techniques_img[39], 0.8,'Hit multiple targets with a ranged weapon',button.ranged,0,'Barrage',0,4,3, 20)
    Shields_Up = Technique(12.1, 7.1,techniques_img[16], 0.8,'Restores 25% armor of all troops',button.tactics,0,'Shields Up',0,25,3, 20)
    Field_Engineer = Technique(13.1, 7.1,techniques_img[60], 0.8,'Doubles armor of war machines',button.engineering,0,'Field Engineer',0,20,3, 20)
    Charge = Technique(14.1, 7.1,techniques_img[62], 0.8,'Increases all troops damage by 10%',button.tactics,0,'Charge',0,10,3, 20)
    Reaper = Technique(15.1, 7.1,techniques_img[75], 0.8,'Increases critical hit chance by 10%',button.stupefy,0,'Reaper',0,10,3, 20)
    Troll_Skin = Technique(16.1, 7.1,techniques_img[32], 0.8,'Restores 3% health each turn',button.athletics,0,'Troll Skin',0,3,3, 20)
    Dream_Cloud = Technique(17.1, 7.1,techniques_img[11], 0.8,'Several targets have a chance to loose action',button.arcane,0,'Dream Cloud',0,4,3, 20)
    Second_Wind = Technique(18.1, 7.1,techniques_img[9], 0.8,'10% chance to restore full health each turn',button.divine,0,'Second Wind',0,10,3, 20)
    #-----------------------------------------------------------------------------------------------------------------------
    skill_expert.extend([Readiness,Slice,Field_Engineer,Deadeye,Barrage,Shields_Up,War_Engineer,Charge,Reaper,Troll_Skin,Dream_Cloud,Second_Wind])
    #-----------------------------------------------------------------------------------------------------------------------
    skill_master = []
    Backstab = Technique(7.1, 6.1,techniques_img[54], 0.8,'Tries to kill a human target instantly',button.stupefy,0,'Backstab',0,50,4, 25)
    Weak_Spot = Technique(8.1, 6.1,techniques_img[19], 0.8,'Melee attack critical damage is quadrupled',button.melee,0,'Weak Spot',0,4,4, 25)
    Siege_Master = Technique(9.1, 6.1,techniques_img[12], 0.8,'Increases efficiency of war machines',button.siege,0,'Siege Master',0,2,4, 25)
    Piercing_Arrows = Technique(10.1, 6.1,techniques_img[2], 0.8,'Ranged attacks ignore armor',button.ranged,0,'Piercing Arrows',0,1,4, 25)
    Planewalker = Technique(11.1, 6.1,techniques_img[22], 0.8,'15% chance of getting aid from another worlds',button.investigation,0,'Planewalker',0,10,4, 25)
    Commander = Technique(12.1, 6.1,techniques_img[63], 0.8,'Deploying troops is 20% cheaper',button.tactics,0,'Commander',0,20,4, 25)
    Master_Mechanist = Technique(13.1, 6.1,techniques_img[64], 0.8,'Fortifies war machines with 20 resistances',button.engineering,0,'Master Mechanist',0,20,4, 25)
    Battle_Prudence = Technique(14.1, 6.1,techniques_img[43], 0.8,'Poisons all enemy troops for 3% health',button.traps,0,'Battle Prudence',0,3,4, 25)
    Channelling = Technique(15.1, 6.1,techniques_img[24], 0.8,'Restores two tricks every turn',button.arcane,0,'Channelling',0,2,4, 25)
    Divine_Intervention = Technique(16.1, 6.1,techniques_img[67], 0.8,'Restores 25% health of all troops',button.divine,0,'Divine Intervention',0,25,4, 25)
    Shadows = Technique(17.1, 6.1,techniques_img[20], 0.8,'Creates two shadow copies',button.arcane,0,'Shadows',0,2,4, 25)
    Blessing = Technique(18.1, 6.1,techniques_img[41], 0.8,'Gives 20 elemental resistances to all troops',button.divine,0,'Blessing',0,20,4, 25)
    #-----------------------------------------------------------------------------------------------------------------------
    skill_master.extend([Backstab,Weak_Spot,Siege_Master,Piercing_Arrows,Planewalker,Commander,Master_Mechanist,Battle_Prudence,Channelling,Divine_Intervention,Shadows,Blessing])
    #-----------------------------------------------------------------------------------------------------------------------
    list_of_skills = []
    list_of_skills.extend([skill_novice, skill_adept, skill_expert, skill_master])

    def draw_skills_in_inventory(surface, item_list, Xmod, Ymod):
        item_list = item_list
        Xmod = Xmod
        Ymod = Ymod
        item_col = 0
        item_row = 0
        for i, j in enumerate(item_list):
            j.draw(surface, TILE_SIZE * Xmod + TILE_SIZE * item_col, TILE_SIZE * Ymod + TILE_SIZE * item_row)
            item_col += 1
            if item_col == 12:
                item_row += 1
                item_col = 0

    #draw_skills_in_inventory(display, skill_novice, 7.1, 9.1)

    #------------------------------------------Inventory------------------------------------
    TILE_SIZE = 64
    MAX_ROWS = 4
    MAX_COLS = 3
    current_item = 0
    current_bow = 0
    current_helm = 0
    current_armor = 0
    current_cloak = 0
    current_dagger = 0
    current_gloves = 0
    current_necklace = 0
    current_pants = 0
    current_ring = 0
    current_shoes = 0
    current_sword = 0
    current_belt = 0

    bows_list_img = []
    for x in range(BOW_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/bow/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        bows_list_img.append(img)

    dagger_list_img = []
    for x in range(DAGGER_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/dagger/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        dagger_list_img.append(img)

    armor_list_img = []
    for x in range(ARMOR_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/armor/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        armor_list_img.append(img)

    cloak_list_img = []
    for x in range(CLOAK_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/cloak/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        cloak_list_img.append(img)

    gloves_list_img = []
    for x in range(GLOVES_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/gloves/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        gloves_list_img.append(img)

    helm_list_img = []
    for x in range(HELM_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/helm/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        helm_list_img.append(img)

    necklace_list_img = []
    for x in range(NECKLACE_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/necklace/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        necklace_list_img.append(img)

    pants_list_img = []
    for x in range(PANTS_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/pants/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        pants_list_img.append(img)

    ring_list_img = []
    for x in range(RING_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/ring/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        ring_list_img.append(img)

    shoes_list_img = []
    for x in range(SHOES_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/shoes/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        shoes_list_img.append(img)

    sword_list_img = []
    for x in range(SWORD_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/sword/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        sword_list_img.append(img)

    belt_list_img = []
    for x in range(BELT_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/belt/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        belt_list_img.append(img)

    trinkets_list_img = []
    for x in range(TRINKETS_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/trinkets/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        trinkets_list_img.append(img)

    slot_list_img = []
    for x in range(SLOT_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/slots/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        slot_list_img.append(img)

    # ---------------------------------SlotIDs----------------------------------------
    #   for col in range(MAX_COLS):
    #     for row in range(MAX_ROWS):
    equipable_slots = []
    nek = [-1]
    hel = [-2]
    clk = [-3]
    bow = [-4]
    arm = [-5]
    glv = [-6]
    pnt = [-9]
    dgr = [-7]
    srd = [-8]
    bts = [-12]
    rng = [-10]
    blt = [-13]
    inv = [-11]
    equipable_slots.extend([nek,hel,clk,bow,arm,glv,pnt,dgr,srd,bts,rng,blt,inv])

    # for col in range(2):
    # #     for row in range(MAX_ROWS):
    #     inv = [-11]
    #     equipable_slots.append(inv)
    # ----------------------------------------------------------------------------------
    # def draw_grid():
    #     for i in range(MAX_COLS + 1):
    #         pygame.draw.line(screen, (255,255,255), (TILE_SIZE*6+i * TILE_SIZE, TILE_SIZE*6),(TILE_SIZE*6+i * TILE_SIZE, TILE_SIZE*10))
    #     for i in range(MAX_ROWS + 1):
    #         pygame.draw.line(screen, (255,255,255), (TILE_SIZE*6, TILE_SIZE*6+i * TILE_SIZE),(TILE_SIZE*9, TILE_SIZE*6+i * TILE_SIZE))
    # ----------------------------------------------------------------------------------
    class Item():
        def __init__(self, image,scale,descr,bonus,status,id,value):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.toggled = False
            self.bonus = bonus
            self.descr = descr
            self.status = status
            self.id = id
            self.value = value

        def item_text(self,text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            if inventory_active == True:
                surface.blit(textobj, textrect)

        def draw(self, surface, x, y):
            self.x = x
            self.y = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            action = False
            self.clicked = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
            if inventory_active == True:
                surface.blit(self.image, (self.rect.x, self.rect.y))
            return action

        def event_handler (self,event):
            action = False
            pos = pygame.mouse.get_pos()
            #for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inventory_active == True:
                    if event.button == 1 and self.toggled == False:
                        if self.rect.collidepoint(event.pos):
                            self.toggled = True
                    elif event.button == 1 and self.toggled == True:
                        if self.rect.collidepoint(event.pos):
                            self.toggled = False

        def sell_item(self, list,item):
            self.list = list
            self.item = item
            list.remove([item])
            button.wealth += self.value
            button.start_wealth = button.wealth

        def get_item(self, list,item):
            self.list = list
            self.item = item
            list.extend([item])

        def buy_item(self, list,item):
            self.list = list
            self.item = item
            list.extend([item])
            if button.start_wealth >= self.value*10:
                button.wealth -= self.value*10
                button.start_wealth = button.wealth

        # def equip_item (self,id, stat, bonus):
        #    self.stat = stat
        #    self.id = id
        #    self.bonus = bonus
        #
        # def unequip_item(self,id, stat, bonus):
        #     self.stat = stat
        #     self.id = id
        #     self.bonus = bonus

    def draw_empty_slots():
        if inventory_active == True:
            for y in range(1):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[10], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
            for y in range(3):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[11], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))

    def draw_inventory_slots():
        for x, row in enumerate(equipable_slots):
            for y, slot in enumerate(row):
                if inventory_active == True:
                    if slot == -1:
                        display.blit(slot_list_img[5], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -2:
                        display.blit(slot_list_img[4], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -3:
                        display.blit(slot_list_img[2], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -4:
                        display.blit(slot_list_img[7], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -5:
                        display.blit(slot_list_img[1], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -6:
                        display.blit(slot_list_img[3], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -7:
                        display.blit(slot_list_img[0], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -8:
                        display.blit(slot_list_img[12], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -9:
                        display.blit(slot_list_img[6], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -10:
                        display.blit(slot_list_img[8], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -11:
                        display.blit(slot_list_img[13], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -12:
                        display.blit(slot_list_img[9], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -13:
                        display.blit(slot_list_img[14], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))

    # def draw_items():
    #     for y, row in enumerate(item_slots):
    #         for x, item in enumerate(row):
    #             if item >= 0:
    #                 screen.blit(items_list_img[item], (x * TILE_SIZE, y * TILE_SIZE))

    belt_list = []
    travel_belt = Item(belt_list_img[0], 0.8,'Travel belt',1,0,'travel_belt',50)
    belt_list.extend([])
    #travel_belt
    necklace_list = []
    traders_luck = Item(necklace_list_img[0], 0.8,'Trader\'s luck',1,0,'traders_luck',50)
    necklace_list.extend([])
    #traders_luck
    helm_list = []
    travel_hat = Item(helm_list_img[0], 0.8,'Travel hat',2,0,'travel_hat',50)
    helm_list.extend([])
    #travel_hat
    cloak_list = []
    travel_cloak = Item(cloak_list_img[0], 0.8,'Travel cloak',2,0,'travel_cloak',50)
    cloak_list.extend([])
    #travel_cloak
    armor_list = []
    travel_clothes = Item(armor_list_img[0], 0.8,"Simple clothes",4,0,'travel_clothes',100)
    armor_list.extend([])
    #travel_clothes
    gloves_list = []
    travel_gloves = Item(gloves_list_img[0], 0.8,'Leather gloves',2,0,'travel_gloves',50)
    gloves_list.extend([])
    #travel_gloves
    pants_list = []
    cloth_pants = Item(pants_list_img[0], 0.8,'Cloth pants',4,0,'cloth_pants',50)
    pants_list.extend([])
    #cloth_pants
    dagger_list = []
    steel_dagger = Item(dagger_list_img[0], 0.8,'Steel dagger',6,0,'steel_dagger',100)
    dagger_list.extend([])
    #steel_dagger
    sword_list = []
    steel_sword = Item(sword_list_img[0], 0.8,'Steel sword',10,0,'steel_sword',150)
    sword_list.extend([])
    #steel_sword
    shoes_list = []
    simple_shoes = Item(shoes_list_img[0], 0.8,'Slippers',2,0,'simple_shoes',50)
    shoes_list.extend([])
    #simple_shoes
    ring_list = []
    silver_ring = Item(ring_list_img[0], 0.8,"Silver ring",6,0,'silver_ring',100)
    moon_ring = Item(ring_list_img[1], 0.8,'Moon ring',20,0,'moon_ring',200)
    holy_ring = Item(ring_list_img[2], 0.8,"Holy ring",12,0,'holy_ring',350)
    ring_list.extend([])
    #silver_ring, moon_ring, holy_ring

    inv_list = []
    letter_1 = Item(trinkets_list_img[0], 0.8, 'A signed royal document that grants you freedom',0,0,'royal_pardon',0)
    apple = Item(trinkets_list_img[1], 0.8, 'Apple',5,0, 'red_apple',10)
    inv_list.extend([letter_1, apple])

    bow_list = []
    simple_bow = Item(bows_list_img[0], 0.8,'Makeshift bow',8,0,'simple_bow',150)
    bow_list.extend([])
    #simple_bow

    list_of_items = []
    list_of_items.extend([belt_list, necklace_list, helm_list, cloak_list,
                          armor_list, gloves_list, pants_list, dagger_list,
                          sword_list, shoes_list, ring_list, inv_list, bow_list])

    def draw_items_in_inventory(surface, item_list, Xmod, Ymod):
        item_list = item_list
        Xmod = Xmod
        Ymod = Ymod
        item_col = 0
        item_row = 0
        for i, j in enumerate(item_list):
            j.draw(surface, TILE_SIZE * Xmod + TILE_SIZE * item_col, TILE_SIZE * Ymod + TILE_SIZE * item_row)
            item_col += 1
            if item_col == 1:
                item_row += 1
                item_col = 0

    draw_items_in_inventory(display, necklace_list, 6.1, 7.1)
    draw_items_in_inventory(display, helm_list, 7.1, 7.1)
    draw_items_in_inventory(display, cloak_list, 8.1, 7.1)
    draw_items_in_inventory(display, bow_list, 9.1, 7.1)
    draw_items_in_inventory(display, armor_list, 10.1, 7.1)
    draw_items_in_inventory(display, gloves_list, 11.1, 7.1)
    draw_items_in_inventory(display, pants_list, 12.1, 7.1)
    draw_items_in_inventory(display, dagger_list, 13.1, 7.1)
    draw_items_in_inventory(display, sword_list, 14.1, 7.1)
    draw_items_in_inventory(display, shoes_list, 15.1, 7.1)
    draw_items_in_inventory(display, ring_list, 16.1, 7.1)
    draw_items_in_inventory(display, belt_list, 17.1, 7.1)
    draw_items_in_inventory(display, inv_list, 18.1, 7.1)
    # --------------------------------------------------------------------------------------
    def active_inactive_skill(surface,value,check,checkname,skill,x,y,inactive_value):
        inactive_rect = inactive_img[inactive_value].get_rect()
        inactive_rect.x,inactive_rect.y = x*TILE_SIZE,y*TILE_SIZE
        if check >= value:
            skill.draw(surface,x*TILE_SIZE,y*TILE_SIZE)
            if skill.rect.collidepoint(mouse_position):
                skill.item_text(f'{skill.id}. {skill.descr} || LP: {skill.value}', fontDescription, (0, 0, 0,), display, 490, 690)
        elif check < value and skills_active == True:
            #img_rect = inactive_img[inactive_value].get_rect()
            display.blit(inactive_img[inactive_value],(x*TILE_SIZE-5,y*TILE_SIZE-5))
        if inactive_rect.collidepoint(mouse_position) and check < value and skills_active == True:
                skill.item_text(f'{skill.id} || Required: {value} {checkname}', fontDescription, (0, 0, 0,), display, 490, 690)

    # -----------------------------------Inventory/Skills-----------------------------------
    inventory_button = button.ToggleButton(display, 360, 330, inventory_icon, 40, 40, 0, True, 'Inventory and Techniques')
    troops_button = button.ToggleButton(display, 1190, 330, troops_icon, 50, 50, 0, True, 'Troops')
    inv_up = button.ScrollButton(1220, 450, inv_arrow_up, 30, 40, 0, True, 'Up')
    inv_down = button.ScrollButton(1220, 530, inv_arrow_down, 30, 40, 0, True, 'Down')
    inv_return = button.ScrollButton(1224, 490, inv_return, 22, 40, 0, True, 'Return')
    # --------------------------------------------------------------------------------------
    scroll_up = False
    scroll_down = False
    click_counter = 0
    scroll = [0, 0]
    inventory_active = True
    skills_active = False
    troops_active = False

    #-------------------------------------------------------------------------------------
    while stats_running:
        display.fill("#d5bc79")
        # screen.fill((0,0,0))
        draw_bg_char_sheet_lid(0, 0)
        draw_empty_slots()
        # draw_grid()
        #--------------------------------InvSideButtons----------------------------------------
        if inv_up.clicked:
            click_counter += 1
            time.sleep(0.1)
            pygame.mixer.Sound(inv_click_sound).play()
            for i in list_of_items:
                for j in i:
                    j.y -= TILE_SIZE
        elif inv_down.clicked and click_counter > 0:
            click_counter -= 1
            time.sleep(0.1)
            pygame.mixer.Sound(inv_click_sound).play()
            for i in list_of_items:
                for j in i:
                    j.y += TILE_SIZE
        elif inv_return.clicked and click_counter > 0:
            pygame.mixer.Sound(inv_click_sound).play()
            for i in list_of_items:
                for j in i:
                    j.y += TILE_SIZE*click_counter
            click_counter = 0

        # -------------------------------------DrawingSELECTION--------------------------------
        item_count = 0
        for item_count, i in enumerate(inv_list):
            if i.draw(display, i.x, i.y):
                current_item = item_count
                if current_item == item_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_item == item_count:
                        i.status = 1
                        if i.id == 'red_apple':
                            bonus_health_points += i.bonus
                    elif i.toggled == False and i.status == 1 and current_item == item_count:
                        i.status = 0
                        if i.id == 'red_apple':
                            bonus_health_points -= i.bonus
            if current_item != item_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'red_apple':
                    bonus_health_points -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), inv_list[current_item].rect, 3)
        #-------------------------------------------------------------------------------------------
        bow_count = 0
        for bow_count, i in enumerate(bow_list):
            if i.draw(display, i.x, i.y):
                current_bow = bow_count
                if current_bow == bow_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_bow == bow_count:
                        i.status = 1
                        if i.id == 'simple_bow':
                            bonus_ranged_damage += i.bonus
                    elif i.toggled == False and i.status == 1 and current_bow == bow_count:
                        i.status = 0
                        if i.id == 'simple_bow':
                            bonus_ranged_damage -= i.bonus
            if current_bow != bow_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'simple_bow':
                    bonus_ranged_damage -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), bow_list[current_bow].rect, 3)
        #-------------------------------------------------------------------------------------------
        ring_count = 0
        for ring_count, i in enumerate(ring_list):
            if i.draw(display, i.x, i.y):
                current_ring = ring_count
                if current_ring == ring_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_ring == ring_count:
                        i.status = 1
                        if i.id == 'silver_ring':
                            bonus_frost_res += i.bonus
                            bonus_fire_res += i.bonus
                            bonus_energy_res += i.bonus
                        elif i.id == 'moon_ring':
                            bonus_arcana_res += i.bonus
                            bonus_tricks += i.bonus//i.bonus
                        elif i.id == 'holy_ring':
                            bonus_frost_res += i.bonus
                            bonus_fire_res += i.bonus
                            bonus_energy_res += i.bonus
                            bonus_armor_points += i.bonus//2
                    elif i.toggled == False and i.status == 1 and current_ring == ring_count:
                        i.status = 0
                        if i.id == 'silver_ring':
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                        elif i.id == 'moon_ring':
                            bonus_arcana_res -= i.bonus
                            bonus_tricks -= i.bonus//i.bonus
                        elif i.id == 'holy_ring':
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                            bonus_armor_points -= i.bonus//2
            if current_ring != ring_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'silver_ring':
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                elif i.id == 'moon_ring':
                    bonus_arcana_res -= i.bonus
                    bonus_tricks -= i.bonus//i.bonus
                elif i.id == 'holy_ring':
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                    bonus_armor_points -= i.bonus//2
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), ring_list[current_ring].rect, 3)
        #-------------------------------------------------------------------------------------------
        necklace_count = 0
        for necklace_count, i in enumerate(necklace_list):
            if i.draw(display, i.x, i.y):
                current_necklace = necklace_count
                if current_necklace == necklace_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_necklace == necklace_count:
                        i.status = 1
                        if i.id == 'traders_luck':
                            bonus_tricks += i.bonus
                    elif i.toggled == False and i.status == 1 and current_necklace == necklace_count:
                        i.status = 0
                        if i.id == 'traders_luck':
                            bonus_tricks -= i.bonus
            if current_necklace != necklace_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'traders_luck':
                    bonus_tricks -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), necklace_list[current_necklace].rect, 3)
        #-------------------------------------------------------------------------------------------
        helm_count = 0
        for helm_count, i in enumerate(helm_list):
            if i.draw(display, i.x, i.y):
                current_helm = helm_count
                if current_helm == helm_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_helm == helm_count:
                        i.status = 1
                        if i.id == 'travel_hat':
                            bonus_defence += i.bonus
                    elif i.toggled == False and i.status == 1 and current_helm == helm_count:
                        i.status = 0
                        if i.id == 'travel_hat':
                            bonus_defence -= i.bonus
            if current_helm != helm_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'travel_hat':
                    bonus_defence -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), helm_list[current_helm].rect, 3)
        #-------------------------------------------------------------------------------------------
        cloak_count = 0
        for cloak_count, i in enumerate(cloak_list):
            if i.draw(display, i.x, i.y):
                current_cloak = cloak_count
                if current_cloak == cloak_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_cloak == cloak_count:
                        i.status = 1
                        if i.id == 'travel_cloak':
                            bonus_defence += i.bonus
                    elif i.toggled == False and i.status == 1 and current_cloak == cloak_count:
                        i.status = 0
                        if i.id == 'travel_cloak':
                            bonus_defence -= i.bonus
            if current_cloak != cloak_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'travel_cloak':
                    bonus_defence -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), cloak_list[current_cloak].rect, 3)
        #-------------------------------------------------------------------------------------------
        armor_count = 0
        for armor_count, i in enumerate(armor_list):
            if i.draw(display, i.x, i.y):
                current_armor = armor_count
                if current_armor == armor_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_armor == armor_count:
                        i.status = 1
                        if i.id == 'travel_clothes':
                            bonus_defence += i.bonus//2
                            bonus_armor_points += i.bonus
                    elif i.toggled == False and i.status == 1 and current_armor == armor_count:
                        i.status = 0
                        if i.id == 'travel_clothes':
                            bonus_defence -= i.bonus//2
                            bonus_armor_points -= i.bonus
            if current_armor != armor_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'travel_clothes':
                    bonus_defence -= i.bonus //2
                    bonus_armor_points -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), armor_list[current_armor].rect, 3)
        #-------------------------------------------------------------------------------------------
        gloves_count = 0
        for gloves_count, i in enumerate(gloves_list):
            if i.draw(display, i.x, i.y):
                current_gloves = gloves_count
                if current_gloves == gloves_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_gloves == gloves_count:
                        i.status = 1
                        if i.id == 'travel_gloves':
                            bonus_defence += i.bonus
                    elif i.toggled == False and i.status == 1 and current_gloves == gloves_count:
                        i.status = 0
                        if i.id == 'travel_gloves':
                            bonus_defence -= i.bonus
            if current_gloves != gloves_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'travel_gloves':
                    bonus_defence -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), gloves_list[current_gloves].rect, 3)
        #-------------------------------------------------------------------------------------------
        pants_count = 0
        for pants_count, i in enumerate(pants_list):
            if i.draw(display, i.x, i.y):
                current_pants = pants_count
                if current_pants == pants_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_pants == pants_count:
                        i.status = 1
                        if i.id == 'cloth_pants':
                            bonus_defence += i.bonus//2
                            bonus_armor_points += i.bonus
                    elif i.toggled == False and i.status == 1 and current_pants == pants_count:
                        i.status = 0
                        if i.id == 'cloth_pants':
                            bonus_defence -= i.bonus//2
                            bonus_armor_points -= i.bonus
            if current_pants != pants_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'cloth_pants':
                    bonus_defence -= i.bonus //2
                    bonus_armor_points -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), pants_list[current_pants].rect, 3)
        #-------------------------------------------------------------------------------------------
        dagger_count = 0
        for dagger_count, i in enumerate(dagger_list):
            if i.draw(display, i.x, i.y):
                current_dagger = dagger_count
                if current_dagger == dagger_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_dagger == dagger_count:
                        i.status = 1
                        if i.id == 'steel_dagger':
                            bonus_melee_damage += i.bonus
                            bonus_critical_strike += i.bonus //2
                    elif i.toggled == False and i.status == 1 and current_dagger == dagger_count:
                        i.status = 0
                        if i.id == 'steel_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= i.bonus //2
            if current_dagger != dagger_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'steel_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= i.bonus //2
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), dagger_list[current_dagger].rect, 3)

        #-------------------------------------------------------------------------------------------
        sword_count = 0
        for sword_count, i in enumerate(sword_list):
            if i.draw(display, i.x, i.y):
                current_sword = sword_count
                if current_sword == sword_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_sword == sword_count:
                        i.status = 1
                        if i.id == 'steel_sword':
                            bonus_melee_damage += i.bonus
                    elif i.toggled == False and i.status == 1 and current_sword == sword_count:
                        i.status = 0
                        if i.id == 'steel_sword':
                            bonus_melee_damage -= i.bonus
            if current_sword != sword_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'steel_sword':
                    bonus_melee_damage -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), sword_list[current_sword].rect, 3)

        #-------------------------------------------------------------------------------------------
        shoes_count = 0
        for shoes_count, i in enumerate(shoes_list):
            if i.draw(display, i.x, i.y):
                current_shoes = shoes_count
                if current_shoes == shoes_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_shoes == shoes_count:
                        i.status = 1
                        if i.id == 'simple_shoes':
                            bonus_defence += i.bonus
                    elif i.toggled == False and i.status == 1 and current_shoes == shoes_count:
                        i.status = 0
                        if i.id == 'simple_shoes':
                            bonus_defence -= i.bonus
            if current_shoes != shoes_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'simple_shoes':
                    bonus_defence -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), shoes_list[current_shoes].rect, 3)
        #-------------------------------------------------------------------------------------------
        belt_count = 0
        for belt_count, i in enumerate(belt_list):
            if i.draw(display, i.x, i.y):
                current_belt = belt_count
                if current_belt == belt_count and i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_belt == belt_count:
                        i.status = 1
                        if i.id == 'travel_belt':
                            bonus_supply += i.bonus
                    elif i.toggled == False and i.status == 1 and current_belt == belt_count:
                        i.status = 0
                        if i.id == 'travel_belt':
                            bonus_supply -= i.bonus
            if current_belt != belt_count and i.status == 1 and i.y > 7*TILE_SIZE:
                if i.id == 'travel_belt':
                    bonus_supply -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), belt_list[current_belt].rect, 3)

        # ----------------------------------------------------------------------------------------------
        draw_bg_char_sheet(0, 0)
        draw_inventory_slots()
        draw_empty_skill_slots()
        draw_empty_troops_slots()
  #------------------------------------InventoryButtons-----------------------------------
        if inventory_active == True:
            inv_up.draw(display)
            inv_return.draw(display)
            inv_down.draw(display)
        #--------------------------------DescriptionOfItems----------------------------
        for i in list_of_items:
            for j in i:
                if j.rect.collidepoint(mouse_position) and j.y > 7*TILE_SIZE:
                    j.item_text(f'{j.descr}', fontDescription, (0, 0, 0,), display, 490, 690)

        # for i in list_of_skills:
        #     for j in i:
        #         if j.classrect.collidepoint(mouse_position):
        #             j.item_text(f'{j.id}. {j.descr} || LP: {j.value}', fontDescription, (0, 0, 0,), display, 490, 690)

        #list_of_skills.extend([skill_novice, skill_adept, skill_expert, skill_master])

        #----------------------------------------Inventory/Skills_Toggle---------------------------
        pygame.draw.circle(display, "#F4E8B9", (inventory_button.rect.centerx, inventory_button.rect.centery), 30)
        pygame.draw.circle(display, "#F4E8B9", (troops_button.rect.centerx, troops_button.rect.centery), 30)

        troops_button.draw(display)

        if troops_button.rect.collidepoint(mouse_position):
            stats_draw_text(f'{troops_button.description}', fontDescription, (0, 0, 0,), display, 490, 690)
        if inventory_button.rect.collidepoint(mouse_position):
            stats_draw_text(f'{inventory_button.description}', fontDescription, (0, 0, 0,), display, 490, 690)

        # ----------------------------------Inventory/SkillsActivation-----------------------------
        if inventory_button.toggled == True:
            inventory_active = True
            skills_active = False
            troops_active = False
            inventory_button.draw(display)
        elif inventory_button.toggled == False:
            inventory_active = False
            skills_active = True
            troops_active = False
            display.blit(skills_icon, (inventory_button.rect.x, inventory_button.rect.y))
        if troops_button.toggled == True:
            inventory_active = False
            skills_active = False
            troops_active = True

        #print(troops_active)
        # print(inventory_active)
        # print(skills_active)

        #---------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        # draw_text('ESC to return', fontMenu, (0,225,0),screen, 10,0)  #Yvan\'s
        # draw_text('SPACE to continue', fontMenu, (0,225,0),screen, 1060,0)  #Yvan\'s
        # draw_rowan_portrait()
        stats_draw_text('Rowan', fontMenu, "#f4e8b9", display, 120, 280)
        # stats_draw_text('Attributes',fontStats, (0,0,0),screen, 120,368)
        stats_draw_text('Skirmish', fontStats, (0, 0, 0), display, 450, 10)
        stats_draw_text('Survival', fontStats, (0, 0, 0), display, 760, 10)
        stats_draw_text('Savviness', fontStats, (0, 0, 0), display, 1060, 10)

        # ----------------------------------ShowDescriptions------------------------------
        show_attributes_skills(attributes_lore, attributes_txt, 0, 26, 65, 382)
        show_attributes_skills(skirmish_lore, skirmish_txt, 0, 26, 405, 25)
        show_attributes_skills(survival_lore, survival_txt, 0, 26, 710, 25)
        show_attributes_skills(savviness_lore, savviness_txt, 0, 26, 1015, 25)
        show_attributes_skills(resistanes_lore, resistanes_txt, 110, 0, 340, 305)
        show_attributes_skills(attack_lore, attack_txt, 110, 0, 440, 335)
        # -----------------------------------DrawStatBonuses------------------------------
        draw_bonus_stats(582, 18, 512, 18, bonus_skirmish, 0, 27, 0, 27)
        draw_bonus_stats(900, 18, 830, 18, bonus_survival, 0, 27, 0, 27)
        draw_bonus_stats(1208, 18, 1140, 18, bonus_savviness, 0, 27, 0, 27)

        show_names(display, attributes_read, 80, 366, 0, 26.2, None, 10, None)
        show_names(display, skills_read, 390, 15, 0, 26.2, None, 8, None)
        show_names(display, skills_read, 710, 15, 0, 26.2, 8, 16, None)
        show_names(display, skills_read, 1010, 15, 0, 26.2, 16, 24, None)

        # ----------------------------Stats-------------------------------------
        strength = int(randomlist[0])
        constitution = int(randomlist[1])
        dexterity = int(randomlist[2])
        agility = int(randomlist[3])
        awareness = int(randomlist[4])
        personality = int(randomlist[5])
        intelligence = int(randomlist[6])
        wisdom = int(randomlist[7])
        willpower = int(randomlist[8])
        luck = int(randomlist[9])

        stat_spacing = 0
        stat_list = []
        for i in randomlist:
            stat = fontStats.render(str(i), True, (0, 0, 0))
            stat_list.append(stat)
            stat_spacing += 27
            display.blit(stat, (220, 364 + (stat_spacing * 1)))

        # ----------------------------RollDiceButton-----------------------------------
        if roll_button.available == True:
            if roll_button.draw():
                randomlist = []
                for i in range(0, 10):
                    n = random.randint(1, 10)
                    randomlist.append(n)
                    # need to run a func to update txt with attributes in button
            if roll_button.rect.collidepoint(mouse_position):
                stats_draw_text(f'{roll_button.description}', fontMenu, (0, 225, 0), display, roll_button.rect.x + 50,
                                roll_button.rect.y)

        with open('MainMenuRes/char_statistic/charattributes.txt', 'w') as out:
            out.writelines([str(strength) + "\n", str(constitution) + "\n", str(dexterity) + "\n", str(agility) + "\n",
                            str(awareness) + "\n", str(personality) + "\n", str(intelligence) + "\n",
                            str(wisdom) + "\n", str(willpower) + "\n", str(luck) + "\n"])

    # if button.learning_points < 20:
        #     roll_button.available = False
        # else:
        #     roll_button.available = True
    # ---------------------------------------------techniques-------------------------------------
        skirmish_tree = []
        melee = int((agility + dexterity) / 2 + strength + luck / 4 + bonus_melee.value)
        ranged = int((willpower + dexterity) / 2 + awareness + luck / 4 + bonus_ranged.value)
        parrying = int((willpower + dexterity) / 2 + agility + int(luck) / 4 + bonus_parrying.value)
        athletics = int((agility + willpower) / 2 + constitution + bonus_athletics.value)
        intimidation = int((personality + intelligence) / 2 + strength + bonus_intimidation.value)
        tactics = int((wisdom + willpower) / 2 + personality + bonus_tactics.value)
        arming = int((strength + willpower) / 2 + constitution + bonus_arming.value)
        siege = int((wisdom + intelligence) / 2 + willpower + bonus_siege.value)
        skirmish_tree.append(melee)
        skirmish_tree.extend((ranged, parrying, athletics, intimidation, tactics, arming, siege))
        # with open('MainMenuRes/char_statistic/charskirmish.txt', 'w') as out:
        #     out.writelines([str(melee) + "\n", str(ranged) + "\n", str(parrying) + "\n", str(athletics) + "\n",
        #                     str(intimidation) + "\n", str(tactics) + "\n", str(arming) + "\n", str(siege)])

        survival_tree = []
        acrobatics = int((strength + dexterity) / 2 + agility + bonus_acrobatics.value)
        stealth = int((agility + dexterity) / 2 + awareness + luck / 4 + bonus_stealth.value)
        thievery = int((willpower + awareness) / 2 + dexterity + luck / 4 + bonus_thievery.value)
        lockpicking = int((intelligence + awareness) / 2 + dexterity + luck / 4 + bonus_lockpicking.value)
        deception = int((wisdom + personality) / 2 + intelligence + bonus_deception.value)
        traps = int((willpower + awareness) / 2 + dexterity + luck / 4 + bonus_traps.value)
        stupefy = int((willpower + dexterity) / 2 + strength + luck / 4 + bonus_stupefy.value)
        nature = int((willpower + wisdom) / 2 + awareness + bonus_nature.value)
        survival_tree.append(acrobatics)
        survival_tree.extend((stealth, thievery, lockpicking, deception, traps, stupefy, nature))
        # with open('MainMenuRes/char_statistic/charsurvive.txt', 'w') as out:
        #     out.writelines([str(acrobatics) + "\n", str(stealth) + "\n", str(thievery) + "\n", str(lockpicking) + "\n",
        #                     str(deception) + "\n", str(traps) + "\n", str(stupefy) + "\n", str(nature)])

        savviness_tree = []
        investigation = int((wisdom + awareness) / 2 + intelligence + bonus_investigation.value)
        medicine = int((wisdom + dexterity) / 2 + intelligence + bonus_medicine.value)
        lore = int((intelligence + awareness) / 2 + wisdom + bonus_lore.value)
        persuasion = int((wisdom + intelligence) / 2 + personality + bonus_persuasion.value)
        arcane = int((intelligence + willpower) / 2 + wisdom + bonus_arcane.value)
        divine = int((intelligence + wisdom) / 2 + willpower + bonus_divine.value)
        alchemy = int((intelligence + dexterity) / 2 + wisdom + bonus_alchemy.value)
        engineering = int((dexterity + awareness) / 2 + intelligence + bonus_engineering.value)
        savviness_tree.append(investigation)
        savviness_tree.extend((medicine, lore, persuasion, arcane, divine, alchemy, engineering))
        # with open('MainMenuRes/char_statistic/charsavviness.txt', 'w') as out:
        #     out.writelines([str(investigation) + "\n", str(medicine) + "\n", str(lore) + "\n", str(persuasion) + "\n",
        #                     str(arcane) + "\n", str(divine) + "\n", str(alchemy) + "\n", str(engineering)])

        resistance_box = []
        threshold = int((constitution + willpower) / 4 + athletics / 10 + bonus_threshold)
        defence = int((parrying + acrobatics) / 2 + bonus_defence)
        arcana_res = int((intelligence + luck) / 2 + arcane / 4 + bonus_arcana_res)
        energy_res = int((willpower + luck) / 2 + nature / 4 + bonus_energy_res)
        frost_res = int((willpower + luck) / 2 + nature / 4 + bonus_frost_res)
        fire_res = int((willpower + luck) / 2 + nature / 4 + bonus_fire_res)
        poison_res = int((constitution + luck) / 2 + medicine / 4 + bonus_poison_res)
        resistance_box.append(threshold)
        resistance_box.extend((defence, arcana_res, energy_res, frost_res, fire_res, poison_res))
        # with open('MainMenuRes/char_statistic/charres.txt', 'w') as out:
        #     out.writelines([str(threshold) + "\n", str(defence) + "\n", str(arcana_res) + "\n", str(energy_res) + "\n",
        #                     str(frost_res) + "\n", str(fire_res) + "\n", str(poison_res) + "\n"])

        attack_box = []
        melee_damage = int((melee / 2 + arming /4) + bonus_melee_damage)
        ranged_damage = int((ranged / 2 + arming/4) / 2 + bonus_ranged_damage)
        critical_strike = int(luck / 2 + medicine / 4 + bonus_critical_strike)
        block = int((arming + athletics) // 4 + luck//4 + bonus_block)
        parry = int((parrying + acrobatics) //4 + luck//4 + bonus_parry)
        attack_box.append(melee_damage)
        attack_box.extend((block,ranged_damage,parry,critical_strike))
        # with open('MainMenuRes/char_statistic/charattack.txt', 'w') as out:
        #     out.writelines([str(melee_damage) + "\n", str(ranged_damage) + "\n", str(critical_strike)])

        # stat_distributable = int((intelligence+luck)/4 + wisdom/2)
        tricks = int(button.new_level / 2 + luck / 4 + bonus_tricks)
        supply = int(button.new_level / 2 + luck / 4 + bonus_supply)
        health_points = int(10 + (strength + willpower) / 2 + constitution * 2 + athletics / 2 + button.new_level * 5 + bonus_health_points)
        armor_points = int(10 + (arming + acrobatics + tactics) / 2 + bonus_armor_points)
        leadership = int((tactics+persuasion+intimidation+deception)//2 + button.new_level*10 + bonus_leadership)

        # with open('MainMenuRes/char_statistic/charsecondary.txt', 'w') as out:
        #     out.writelines([str(tricks) + "\n", str(supply) + "\n", str(health_points) + "\n", str(armor_points) + "\n"])
        #--------------------------------------------Techniques---------------------------------------
        active_inactive_skill(display, 20,nature,'Nature',Cartographer,7.1, 9.1, 0)
        active_inactive_skill(display, 20,melee,'Melee',Combo,8.1, 9.1, 66)
        active_inactive_skill(display, 20,lore,'Lore',Educated,9.1, 9.1, 29)
        active_inactive_skill(display, 20,ranged,'Ranged',Quick_Shot,10.1, 9.1, 56)
        active_inactive_skill(display, 20,medicine,'Medicine',Camp_Doctor,11.1, 9.1, 42)
        active_inactive_skill(display, 20,thievery,'Thievery',Thief,12.1, 9.1, 30)
        active_inactive_skill(display, 20,arming,'Arming',Quartermaster,13.1, 9.1, 46)
        active_inactive_skill(display, 20,deception,'Deception',Scout,14.1, 9.1, 71)
        active_inactive_skill(display, 20,intimidation,'Intimidation',Haggler,15.1, 9.1, 73)
        active_inactive_skill(display, 20,persuasion,'Persuasion',Estates,16.1, 9.1, 6)
        active_inactive_skill(display, 20,arcane,'Arcane',Curse,17.1, 9.1, 7)
        active_inactive_skill(display, 20,divine,'Divine',Healing,18.1, 9.1, 35)
        #-------------------------------------------------------------------------------------
        if skill_counter >=6:
            active_inactive_skill(display, 40,medicine,'Medicine',Snake_Eater,7.1, 8.1, 18)
            active_inactive_skill(display, 40,melee,'Melee',Power_Blow,8.1, 8.1, 44)
            active_inactive_skill(display, 40,lore,'Lore',Scholar,9.1, 8.1, 4)
            active_inactive_skill(display, 40,ranged,'Ranged',Multiple_Shot,10.1, 8.1, 13)
            active_inactive_skill(display, 40,parrying,'Parrying',Duelist,11.1, 8.1, 45)
            active_inactive_skill(display, 40,traps,'Traps',Bear_Trap,12.1, 8.1, 27)
            active_inactive_skill(display, 40,alchemy,'Alchemy',Potion_Master,13.1, 8.1, 17)
            active_inactive_skill(display, 40,stupefy,'Stupefy',Knock_Down,14.1, 8.1, 74)
            active_inactive_skill(display, 40,acrobatics,'Acrobatics',Battle_Reflex,15.1, 8.1, 38)
            active_inactive_skill(display, 40,athletics,'Athletics',Persevere,16.1, 8.1, 49)
            active_inactive_skill(display, 40,arcane,'Arcane',Moon_Shield,17.1, 8.1, 34)
            active_inactive_skill(display, 40,divine,'Divine',Purifier,18.1, 8.1, 55)
        #-------------------------------------------------------------------------------------
        if skill_counter >=12:
            active_inactive_skill(display, 60,arming,'Arming',Readiness,7.1, 7.1, 33)
            active_inactive_skill(display, 60,melee,'Melee',Slice,8.1, 7.1, 28)
            active_inactive_skill(display, 60,engineering,'Engineering',War_Engineer,9.1, 7.1, 1)
            active_inactive_skill(display, 60,ranged,'Ranged',Deadeye,10.1, 7.1, 65)
            active_inactive_skill(display, 60,ranged,'Ranged',Barrage,11.1, 7.1, 39)
            active_inactive_skill(display, 60,tactics,'Tactics',Shields_Up,12.1, 7.1, 16)
            active_inactive_skill(display, 60,engineering,'Engineering',Field_Engineer,13.1, 7.1, 60)
            active_inactive_skill(display, 60,tactics,'Tactics',Charge,14.1, 7.1, 62)
            active_inactive_skill(display, 60,stupefy,'Stupefy',Reaper,15.1, 7.1, 75)
            active_inactive_skill(display, 60,athletics,'Athletics',Troll_Skin,16.1, 7.1, 32)
            active_inactive_skill(display, 60,arcane,'Arcane',Dream_Cloud,17.1, 7.1, 11)
            active_inactive_skill(display, 60,divine,'Divine',Second_Wind,18.1, 7.1, 9)
        #-------------------------------------------------------------------------------------
        if skill_counter >=18:
            active_inactive_skill(display, 80,stupefy,'Stupefy',Backstab,7.1, 6.1, 54)
            active_inactive_skill(display, 80,melee,'Melee',Weak_Spot,8.1, 6.1, 19)
            active_inactive_skill(display, 80,siege,'Siege',Siege_Master,9.1, 6.1, 12)
            active_inactive_skill(display, 80,ranged,'Ranged',Piercing_Arrows,10.1, 6.1, 2)
            active_inactive_skill(display, 80,investigation,'Investigation',Planewalker,11.1, 6.1, 22)
            active_inactive_skill(display, 80,tactics,'Tactics',Commander,12.1, 6.1, 63)
            active_inactive_skill(display, 80,engineering,'Engineering',Master_Mechanist,13.1, 6.1, 64)
            active_inactive_skill(display, 80,traps,'Traps',Battle_Prudence,14.1, 6.1, 43)
            active_inactive_skill(display, 80,arcane,'Arcane',Channelling,15.1, 6.1, 24)
            active_inactive_skill(display, 80,divine,'Divine',Divine_Intervention,16.1, 6.1, 67)
            active_inactive_skill(display, 80,arcane,'Arcane',Shadows,17.1, 6.1, 20)
            active_inactive_skill(display, 80,divine,'Divine',Blessing,18.1, 6.1, 41)
        #---------------------------------------------------------------------------------------------
        skill_counter = len([i for k in list_of_skills for i in k if i.status == 1])

        # -------------------------------------------
        # stat_list = []
        show_skills(display, skirmish_tree, 540, 14, 27, 0)
        show_skills(display, survival_tree, 856, 14, 27, 0)
        show_skills(display, savviness_tree, 1165, 14, 27, 0)
        show_skills(display, resistance_box, 365, 298, 0, 109)
        show_skills(display, attack_box, 475, 324, 0, 109)

        # with open('MainMenuRes/char_statistic/charbonusstats.txt', 'w') as out:
        #     out.writelines(
        #         [str(bonus_melee.value) + "\n", str(bonus_ranged.value) + "\n", str(bonus_parrying.value) + "\n",
        #          str(bonus_athletics.value) + "\n",
        #          str(bonus_intimidation.value) + "\n", str(bonus_tactics.value) + "\n", str(bonus_arming.value) + "\n",
        #          str(bonus_siege.value) + "\n",
        #          str(bonus_acrobatics.value) + "\n", str(bonus_stealth.value) + "\n", str(bonus_thievery.value) + "\n",
        #          str(bonus_lockpicking.value) + "\n",
        #          str(bonus_deception.value) + "\n", str(bonus_traps.value) + "\n", str(bonus_stupefy.value) + "\n",
        #          str(bonus_nature.value) + "\n",
        #          str(bonus_investigation.value) + "\n", str(bonus_medicine.value) + "\n", str(bonus_lore.value) + "\n",
        #          str(bonus_persuasion.value) + "\n",
        #          str(bonus_arcane.value) + "\n", str(bonus_divine.value) + "\n", str(bonus_alchemy.value) + "\n",
        #          str(bonus_engineering.value) + "\n"])

        # -----------------------------------ExperienceManagement------------------------------
        stats_draw_text(f'{button.learning_points}', fontStats, (0, 0, 0,), display, 1070, 652)
        exp_points_rect = pygame.Rect(1100, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), exp_points)
        if exp_points_rect.collidepoint(mouse_position):
            stats_draw_text('Learning points', fontDescription, (0, 0, 0,), display, 490, 690)

        stats_draw_text(f'{button.new_level}', fontStats, (0, 0, 0,), display, 538, 652)
        chat_level_rect = pygame.Rect(490, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), chat_level_rect)
        if chat_level_rect.collidepoint(mouse_position):
            stats_draw_text('Character level', fontDescription, (0, 0, 0,), display, 490, 690)

        stats_draw_text(f'{button.start_experience}', fontStats, (0, 0, 0,), display, 822, 652)
        char_experience_rect = pygame.Rect(760, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), char_experience_rect)
        if char_experience_rect.collidepoint(mouse_position):
            stats_draw_text('Experience', fontDescription, (0, 0, 0,), display, 490, 690)

        # -----------------------------------Tricks/Supply------------------------------
        stats_draw_text(str(tricks), fontStats, (0, 0, 0,), display, 410, 655)
        tricks_rect = pygame.Rect(360, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), tricks_rect)
        if tricks_rect.collidepoint(mouse_position):
            stats_draw_text('Tricks are required to use abilities in battle',
                            fontDescription, (0, 0, 0,), display, 490, 690)

        stats_draw_text(str(supply), fontStats, (0, 0, 0,), display, 410, 688)
        supply_rect = pygame.Rect(360, 690, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), supply_rect)
        if supply_rect.collidepoint(mouse_position):
            stats_draw_text('Supply is required to use consumables in battle',
                            fontDescription, (0, 0, 0,), display, 490, 690)

        # -----------------------------------HP/ARM-----------------------------
        button_hero_hp = pygame.Rect(1160, 652, 35, 35)
        # pygame.draw.rect(screen, (255,0,0), button_hero_hp)
        if button_hero_hp.collidepoint(mouse_position):
            stats_draw_text('Health points', fontDescription, (0, 0, 0,), display, 490, 690)
        stats_draw_text(f'{health_points}', fontStats, (0, 0, 0,), display, 1205, 654)

        button_hero_armor = pygame.Rect(1160, 690, 35, 35)
        # pygame.draw.rect(screen, (255,0,0), button_hero_armor)
        if button_hero_armor.collidepoint(mouse_position):
            stats_draw_text('Armor points', fontDescription, (0, 0, 0,), display, 490, 690)
        stats_draw_text(f'{armor_points}', fontStats, (0, 0, 0,), display, 1205, 685)

        # ---------------adventureSubDef----------------------------
        button_adventure = pygame.Rect(1220, 5, 200, 50)
        pygame.draw.circle(display, "#F4E8B9", (button_adventure.x+30, button_adventure.y+25), 30)
        display.blit(bg_pointer, (1220, 5))
        if button_adventure.collidepoint((mouse_position)):  # and stat_distributable == 0:
            if menuClick:
                pygame.mixer.Sound(select_sound).play()
                global_map()
                stats_running = False
            #elif button.learning_points != 0:
            #   stats_draw_text('Distribute your learning points!', fontDescription, (0, 0, 0), display, 490, 690)
        if button_adventure.collidepoint(mouse_position):
            stats_draw_text('Begin Campaign', fontDescription, (0, 0, 0),display,  490, 690)

        #if  stat_distributable >0:
        #    stats_draw_text('Distribute your points!', fontMenu, (0,225,0),screen, 1000,40)

        # -----------------------------------rowan-----------------------------------------------
        rowan_frame += 1
        try:
            if rowan_frame >= len(animation_database[rowan_action]):  # 2300
                rowan_frame = 0
            rowan_img_id = animation_database[rowan_action][rowan_frame]  # animation_database[timewheel][0]
            rowan_img = animation_frames[rowan_img_id]  # [frame_0] for frame_0.png
        except:
            pass
        display.blit(rowan_img, (rowan_rect.x, rowan_rect.y))
        # ---------------backToMainMenu--------------------------------------------
        button_back_to_main_menu = pygame.Rect(-5, 10, 200, 50)
        pygame.draw.circle(display, "#F4E8B9", (button_back_to_main_menu.x+35, button_adventure.y+25), 30)
        img = pygame.transform.flip(bg_pointer, True, False)
        display.blit(img, (-5, 5))

        if button_back_to_main_menu.collidepoint((mouse_position)):
            if menuClick:
                pygame.mixer.Sound(select_sound).play()
                stats_running = False
        if button_back_to_main_menu.collidepoint(mouse_position):
            stats_draw_text('Back to Main Menu', fontDescription, (0, 0, 0), display, 490, 690)
        # -------------------------------------------------------------------------
        menuClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), 0, 32)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    stats_running = False
                if event.key == K_o:
                    button.fullscreen = not button.fullscreen
                    fullscreen = button.fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

                # if event.key == K_p:
                #    button.experience +=100
                #    button.start_experience = button.experience
                #    print(button.new_level)
                #    print(button.experience)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    menuClick = True

            #----------------------------------EventHandlers---------------------------------
            for i in list_of_items:
                for j in i:
                    j.event_handler(event)
            for i in list_of_skills:
                for j in i:
                    j.event_handler(event)

            inventory_button.event_handler(event)
            troops_button.event_handler(event)

        #--------------------------------------------------------------------------------

        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.mouse.set_visible(False)
        mouse_position = pygame.mouse.get_pos()
        player_rect.x, player_rect.y = mouse_position
        screen.blit(normal_icon, player_rect)

        pygame.display.update()
        mainClock.tick(60)

































































































































































































































def global_map():
    menuClick = False
    clicked = False
    roll_dice = False
    mouse_position = pygame.mouse.get_pos()
    mx, my = pygame.mouse.get_pos()
    inventory_active = False
    skills_active = False
    WINDOW_SIZE = (1280, 720)
    screen = pygame.display.set_mode((1280, 720))
    display = pygame.Surface((1280, 720))
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    # surface = pygame.Surface((1280, 720))
    # screen.blit(surface, (1280, 720))
    TILE_SIZE = 64

    fullscreen = button.fullscreen
    # not bool(linecache.getline('genericmap.txt',1))
    if fullscreen:
        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

    bg_char_sheet = pygame.image.load("MainMenuRes/charsheet.png").convert_alpha()
    bg_char_sheet = pygame.transform.scale(bg_char_sheet, (int(WINDOW_SIZE[0]*1), (int(WINDOW_SIZE[1]*1))))

    bg_char_sheet_lid = pygame.image.load("MainMenuRes/charsheetlid.png").convert_alpha()
    bg_char_sheet_lid = pygame.transform.scale(bg_char_sheet_lid, (int(WINDOW_SIZE[0] * 1), (int(WINDOW_SIZE[1] * 1))))

    dice_icon = pygame.image.load("MainMenuRes/dice.png").convert_alpha()
    dice_icon = pygame.transform.scale(dice_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    plus_icon = pygame.image.load("MainMenuRes/plus.png").convert_alpha()
    plus_icon = pygame.transform.scale(plus_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    minus_icon = pygame.image.load("MainMenuRes/minus.png").convert_alpha()
    minus_icon = pygame.transform.scale(minus_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    plus_green_icon = pygame.image.load("MainMenuRes/plus_green.png").convert_alpha()
    plus_green_icon = pygame.transform.scale(plus_green_icon,(int(WINDOW_SIZE[0] * 0.015), (int(WINDOW_SIZE[1] * 0.025))))

    inventory_icon = pygame.image.load("MainMenuRes/inventorybag.png").convert_alpha()
    inventory_icon = pygame.transform.scale(inventory_icon,(int(WINDOW_SIZE[0] * 0.015), (int(WINDOW_SIZE[1] * 0.025))))

    skills_icon = pygame.image.load("MainMenuRes/skills_icon.png").convert_alpha()
    skills_icon = pygame.transform.scale(skills_icon, (int(WINDOW_SIZE[0] * 0.03), (int(WINDOW_SIZE[1] * 0.06))))

    troops_icon = pygame.image.load("MainMenuRes/troops_icon.png").convert_alpha()
    troops_icon = pygame.transform.scale(troops_icon, (int(WINDOW_SIZE[0] * 0.03), (int(WINDOW_SIZE[1] * 0.06))))

    inv_arrow_up = pygame.image.load("MainMenuRes/inventory/inv_arrow_dark.png").convert_alpha()
    inv_arrow_up = pygame.transform.scale(inv_arrow_up, (int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.020))))
    inv_arrow_down = pygame.image.load("MainMenuRes/inventory/inv_arrow_dark.png").convert_alpha()
    inv_arrow_down = pygame.transform.scale(inv_arrow_down,(int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.020))))
    inv_arrow_down = pygame.transform.flip(inv_arrow_down, False, True)
    inv_return = pygame.image.load("MainMenuRes/inventory/inv_return_button.png").convert_alpha()
    inv_return = pygame.transform.scale(inv_return,(int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.20))))

    sell_icon = pygame.image.load("MainMenuRes/inventory/selling_icon.png").convert_alpha()
    sell_icon = pygame.transform.scale(sell_icon,(int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.20))))
    steal_icon = pygame.image.load("MainMenuRes/inventory/steal.png").convert_alpha()
    steal_icon = pygame.transform.scale(steal_icon,(int(WINDOW_SIZE[0] * 0.020), (int(WINDOW_SIZE[1] * 0.20))))

    skill_scroll = pygame.image.load("MainMenuRes/techniques/skill_scroll.png").convert_alpha()
    skill_scroll = pygame.transform.scale(skill_scroll, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))
    gm_check = pygame.image.load("WorldMap/check.png").convert_alpha()
    gm_check = pygame.transform.scale(gm_check, (int(WINDOW_SIZE[0] * 0.06), (int(WINDOW_SIZE[1] * 0.06))))
    gm_cross = pygame.image.load("WorldMap/cross.png").convert_alpha()
    gm_cross = pygame.transform.scale(gm_cross, (int(WINDOW_SIZE[0] * 0.06), (int(WINDOW_SIZE[1] * 0.06))))
    gm_greencheck = pygame.image.load("WorldMap/greencheck.png").convert_alpha()
    gm_greencheck = pygame.transform.scale(gm_greencheck, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.03))))
    gm_greencross = pygame.image.load("WorldMap/greencrosses.png").convert_alpha()
    gm_greencross = pygame.transform.scale(gm_greencross, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.03))))

    font = pygame.font.SysFont('Times New Roman', 18)
    font10 = pygame.font.Font('WorldMap/ESKARGOT.ttf', 10)
    font12 = pygame.font.Font('WorldMap/ESKARGOT.ttf', 12)
    font14 = pygame.font.Font('WorldMap/ESKARGOT.ttf', 14)
    font18 = pygame.font.Font('WorldMap/ESKARGOT.ttf', 18)
    fontMenu = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
    fontStats = pygame.font.Font('WorldMap/ESKARGOT.ttf', 20)
    fontDescription = pygame.font.SysFont('Times New Roman', 22)
    fontMenuLarge = pygame.font.Font('WorldMap/ESKARGOT.ttf', 28)
    fontMenuCharSheet = pygame.font.Font('WorldMap/ESKARGOT.ttf', 100)

    select_sound = pygame.mixer.Sound('MainMenuRes/selection.wav')
    page_sound = pygame.mixer.Sound('WorldMap/page.wav')
    level_up_sound = pygame.mixer.Sound('MainMenuRes/level_up.mp3')
    coins_sound = pygame.mixer.Sound('WorldMap/coins.wav')
    chest_open_sound = pygame.mixer.Sound('WorldMap/settlement/open_chest.wav')
    chest_open_sound.set_volume(0.5)
    take_item_sound = pygame.mixer.Sound('WorldMap/settlement/take_sound.wav')
    locked_sound = pygame.mixer.Sound('WorldMap/settlement/locked.wav')
    snap_trap_sound = pygame.mixer.Sound('WorldMap/settlement/snap_trap.wav')
    town_enter_sound = pygame.mixer.Sound('WorldMap/settlement/town_enter.wav')
    heal_sound = pygame.mixer.Sound('WorldMap/settlement/healing.wav')
    trader_sound = pygame.mixer.Sound('WorldMap/settlement/trader.wav')
    port_sound = pygame.mixer.Sound('WorldMap/settlement/port.wav')
    smith_sound = pygame.mixer.Sound('WorldMap/settlement/smith.wav')
    tavern_sound = pygame.mixer.Sound('WorldMap/settlement/tavern.wav')
    alchemy_sound = pygame.mixer.Sound('WorldMap/settlement/alchemy.mp3')
    chorus_sound = pygame.mixer.Sound('WorldMap/settlement/chorus.wav')
    city_board_sound = pygame.mixer.Sound('WorldMap/settlement/city_board.mp3')
    caravan_sound = pygame.mixer.Sound('WorldMap/settlement/caravan_sound.wav')
    # randomlist = []
    # for i in range(0, 10):
    #     n = random.randint(1, 10)
    #     randomlist.append(n)

    # ----------------------------------Animations------------------------------------
    global animation_frames
    animation_frames = {}

    def animation_load(path, frame_durations):
        global animation_frames
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            animation_image = pygame.image.load(img_loc).convert()
            animation_image.set_colorkey((0, 0, 0))
            animation_image = pygame.transform.scale(animation_image, (160, 160))
            animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    animation_database = {}
    # animation_database['apple'] = animation_load('MainMenuRes/rowan/apple', [100, 200, 50, 50, 50, 50])
    # animation_database['idle'] = animation_load('MainMenuRes/rowan/idle', [50, 50])
    # rowan_action = 'idle'
    # rowan_frame = 0
    # rowan_rect = pygame.Rect(80, 100, 80, 120)

    # ------------------------------------------------------------------------------------
    def draw_bg_char_sheet(surface):
        surface.blit(bg_char_sheet, (0, 0))

    def draw_bg_char_sheet_lid(surface):
        surface.blit(bg_char_sheet_lid, (0, 0))

    def stats_draw_text(number, font, color, surface, x, y):
        textobj = font.render(number, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    # def draw_rowan_portrait():
    #     screen.blit(bg_rowan,(85,100))
    # ----------------------------RollButton--------------------------------

    # plus_button = button.Button(display, 200, 200, plus_icon, 15,20,0, True,'Increase')
    # minus_button = button.Button(display, 180, 200, minus_icon, 15,20,0, True,'Decrease')

    # ----------------------------FreeStatsSButton--------------------------------
    bottom_text = (780, 690)
    global char_level
    char_level = 0
    global learning_points
    learning_points = 0
    # global stat_distributable
    # stat_distributable = 0

    def level_up ():
        global char_level
        global learning_points
        if button.start_experience >= 1000:
            char_level +=1
            if Scholar.status == 1:
                learning_points += 25
            else:
                learning_points += 20
            button.experience -= 1000
            button.start_experience = button.experience
            pygame.mixer.Sound(level_up_sound).play()

    bonus_ranged_damage = 0
    bonus_melee_damage = 0
    bonus_critical_strike = 0
    bonus_parry = 0
    bonus_block = 0
    bonus_leadership = 0

    bonus_tricks = 0
    bonus_supply = 0
    bonus_health_points = 0
    bonus_armor_points = 0

    bonus_threshold = 0
    bonus_defence = 0
    bonus_arcana_res = 0
    bonus_energy_res = 0
    bonus_frost_res = 0
    bonus_fire_res = 0
    bonus_poison_res = 0

    with open('MainMenuRes/char_statistic/charbonussecondary.txt', 'w') as out:
        out.writelines(
            [str(bonus_ranged_damage) + "\n", str(bonus_melee_damage) + "\n", str(bonus_critical_strike) + "\n",
             str(bonus_tricks) + "\n",str(bonus_supply) + "\n", str(bonus_health_points) + "\n",
             str(bonus_armor_points) + "\n",str(bonus_threshold) + "\n",str(bonus_defence) + "\n",
             str(bonus_arcana_res) + "\n", str(bonus_energy_res) + "\n",str(bonus_frost_res) + "\n",
             str(bonus_fire_res) + "\n", str(bonus_poison_res) + "\n",str(bonus_parry) + "\n",
             str(bonus_block) + "\n",str(bonus_leadership) + "\n" ])

    class Stat():
        def __init__(self, value):
            self.value = value

        def draw(self, plus_X, plus_Y, minus_X, minus_Y):
            global learning_points
            plus_button = button.Button(display, plus_X, plus_Y, plus_icon, 15, 20, 0, True, 'Increase')
            minus_button = button.Button(display, minus_X, minus_Y, minus_icon, 15, 20, 0, True, 'Decrease')
            if plus_button.draw() and learning_points != 0:
                self.value += 1
                learning_points -= 1
                time.sleep(0.1)
            # elif minus_button.draw() and self.value > 0:  # and button.learning_points <= button.learning_points - 1:
            #     self.value -= 1
            #     time.sleep(0.1)
            #     button.learning_points += 1
            if self.value > 0:
                display.blit(plus_green_icon, (plus_button.rect.x - 2, plus_button.rect.y))

    bonus_melee = Stat(0)
    bonus_ranged = Stat(0)
    bonus_parrying = Stat(0)
    bonus_athletics = Stat(0)
    bonus_intimidation = Stat(0)
    bonus_tactics = Stat(0)
    bonus_arming = Stat(0)
    bonus_siege = Stat(0)

    bonus_skirmish = []
    bonus_skirmish.extend((bonus_melee, bonus_ranged, bonus_parrying,
                           bonus_athletics, bonus_intimidation, bonus_tactics,
                           bonus_arming, bonus_siege))

    bonus_acrobatics = Stat(0)
    bonus_stealth = Stat(0)
    bonus_thievery = Stat(0)
    bonus_lockpicking = Stat(0)
    bonus_deception = Stat(0)
    bonus_traps = Stat(0)
    bonus_stupefy = Stat(0)
    bonus_nature = Stat(0)

    bonus_survival = []
    bonus_survival.extend((bonus_acrobatics, bonus_stealth, bonus_thievery,
                           bonus_lockpicking, bonus_deception, bonus_traps,
                           bonus_stupefy, bonus_nature))

    bonus_investigation = Stat(0)
    bonus_medicine = Stat(0)
    bonus_lore = Stat(0)
    bonus_persuasion = Stat(0)
    bonus_arcane = Stat(0)
    bonus_divine = Stat(0)
    bonus_alchemy = Stat(0)
    bonus_engineering = Stat(0)

    bonus_savviness = []
    bonus_savviness.extend((bonus_investigation, bonus_medicine, bonus_lore,
                            bonus_persuasion, bonus_arcane, bonus_divine,
                            bonus_alchemy, bonus_engineering))

    def draw_bonus_stats(xPl, yPl, xMn, yMn, bonus_tree, plXmod, plYmod, mnXmod, mnYmod):
        Plx = 0
        Ply = 0
        Mnx = 0
        Mny = 0
        for i in bonus_tree:
            Plx += plXmod
            Ply += plYmod
            Mnx += mnXmod
            Mny += mnYmod
            i.draw(xPl + Plx, yPl + Ply, xMn + Mnx, yMn + Mny)
    # ------------------------------------------------------------------
    def show_skills(surface, skill_tree, x, y, Yspacing, Xspacing):
        spacing_ver = 0
        spacing_hor = 0
        for i in skill_tree:
            j = fontStats.render(str(i), True, (0, 0, 0))
            spacing_ver += Yspacing
            spacing_hor += Xspacing
            surface.blit(j, (x + (spacing_hor * 1), y + (spacing_ver * 1)))

    attributes_open = open('MainMenuRes/attributes.txt', 'r')
    attributes_read = attributes_open.read()
    attributes_open.close()
    attributes_path = open('MainMenuRes/attributes_description.txt', 'r')
    attributes_txt = 'MainMenuRes/attributes_description.txt'
    attributes_lore = attributes_path.read()
    attributes_path.close()

    skills_open = open('MainMenuRes/skills_list.txt', 'r')
    skills_read = skills_open.read()
    skills_open.close()
    skirmish_path = open('MainMenuRes/skirmish_tree_description.txt', 'r')
    skirmish_txt = 'MainMenuRes/skirmish_tree_description.txt'
    skirmish_lore = skirmish_path.read()
    skirmish_path.close()
    survival_path = open('MainMenuRes/survival_tree_description.txt', 'r')
    survival_txt = 'MainMenuRes/survival_tree_description.txt'
    survival_lore = survival_path.read()
    survival_path.close()
    savviness_path = open('MainMenuRes/savviness_tree_description.txt', 'r')
    savviness_txt = 'MainMenuRes/savviness_tree_description.txt'
    savviness_lore = savviness_path.read()
    savviness_path.close()
    resistances_path = open('MainMenuRes/resistances.txt', 'r')
    resistances_txt = 'MainMenuRes/resistances.txt'
    resistances_lore = resistances_path.read()
    resistances_path.close()

    attack_path = open('MainMenuRes/attacks.txt', 'r')
    attack_txt = 'MainMenuRes/attacks.txt'
    attack_lore = attack_path.read()
    attack_path.close()

    def show_attributes_skills(text, txt, Xspacing, Yspacing, rectX, rectY):
        lines_list = []
        rect_list = []
        spacingX = 0
        spacingY = 0
        count_lines = 0
        counter = 0
        for i in text.split('\n'):
            line = fontDescription.render(i, True, (0, 0, 0,))
            lines_list.append(line)
            count_lines += 1
        for rect in range(count_lines):
            spacingX += Xspacing
            spacingY += Yspacing
            rect = pygame.Rect(rectX + (spacingX * 1), rectY + (spacingY * 1), 70, 10)
            rect_list.append(rect)
            # pygame.draw.rect(screen, (255,0,0), rect)
            counter += 1
            if rect.collidepoint(mouse_position):
                descr = linecache.getline(txt, counter).rstrip('\n')
                stats_draw_text(descr, fontDescription, (0, 0, 0,), display, 490, 690)
    # ----------------------------------------------------------------------
    def show_names(surface, text, x, y, modX, ModY, deli0, deli1, deli2):
        spacingX = 0
        spacingY = 0
        for i in text.split('\n')[deli0:deli1:deli2]:
            j = fontStats.render(str(i), True, (0, 0, 0))
            k = fontStats.render(str(i)[:1], True, (255, 255, 150))
            spacingX += modX
            spacingY += ModY
            surface.blit(j, (x + (spacingX * 1), y + (spacingY * 1)))
            surface.blit(k, (x + (spacingX * 1), y + (spacingY * 1)))



    path, dirs, slots = next(os.walk("MainMenuRes/inventory/slots"))
    slots_count = len(slots)
    SLOT_TYPES = slots_count

    #------------------------------------Troops---------------------------------------
    path, dirs, units = next(os.walk("MainMenuRes/troops/unit_img"))
    units_count = len(units)
    UNITS_TYPES = units_count
    units_img = []
    for x in range(UNITS_TYPES):
        img = pygame.image.load(f'MainMenuRes/troops/unit_img/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        units_img.append(img)

    #----------------------------------------------------------------------------------
    current_melee = 0
    current_ranged = 0
    current_cavalry = 0
    current_support = 0
    #----------------------------------------------------------------------------------

    class Troops():
        def __init__(self, image,scale,descr,bonus,status,id,value):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.toggled = False
            self.taken = False
            self.bonus = bonus
            self.descr = descr
            self.status = status
            self.id = id
            self.value = value

        def item_text(self,text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            if troops_active == True:
                surface.blit(textobj, textrect)

        def draw(self, surface, x, y):
            self.x = x
            self.y = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            action = False
            self.clicked = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
            if troops_active == True:
                surface.blit(self.image, (self.rect.x, self.rect.y))
            return action

    #-------------------------------------TroopsButtons--------------------------------
    path, dirs, types = next(os.walk("MainMenuRes/troops/types"))
    types_count = len(types)
    TROOPS_TYPES = types_count
    types_img = []
    for x in range(TROOPS_TYPES):
        img = pygame.image.load(f'MainMenuRes/troops/types/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        types_img.append(img)

    def draw_empty_troops_slots():
        if troops_active == True:
            for y in range(4):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[11], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[0], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    novice = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE,ranks_img[0].get_width(), ranks_img[0].get_height())
                    if novice.collidepoint(mouse_position):
                        stats_draw_text('Close combat units', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[1], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))
                    adept = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE,ranks_img[1].get_width(), ranks_img[1].get_height())
                    if adept.collidepoint(mouse_position):
                        stats_draw_text('Range combat units', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[2], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE))
                    expert = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE,ranks_img[2].get_width(), ranks_img[2].get_height())
                    if expert.collidepoint(mouse_position):
                        stats_draw_text('Cavalry and beasts', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(types_img[3], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE))
                    master = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE,ranks_img[3].get_width(), ranks_img[3].get_height())
                    if master.collidepoint(mouse_position):
                        stats_draw_text('War machines and support units', fontDescription, (0, 0, 0,), display, 490, 690)

    #------------------------------------------------TroopsTypes----------------------------
    troops_melee = []
    Dunstan = Troops(units_img[0], 0.8, 'Your younger brother and skilled swordsman Dunstan',0,0,'dunstan',0)
    Light_Infantry = Troops(units_img[1], 0.8, 'A regiment of militia and spearmen led by a captain ',0,0,'light_infantry',0)
    Bartelago = Troops(units_img[5], 0.8, 'Bartelago is a mighty warrior and your old friend',0,0,'bartelago',0)
    Anselm = Troops(units_img[6], 0.8, 'Brother Anselm is a former grey cloak agent',0,0,'anselm',0)


    troops_melee.extend([])

    #Dunstan
    #_------------------------------------------------------------------------------------
    troops_ranged = []
    Light_Archers = Troops(units_img[2], 0.8, 'A regiment of light archers',0,0,'light_archers',0)
    Regina = Troops(units_img[7], 0.8, 'Regina a former grey cloak ranger and a skilled hunter',0,0,'regina',0)
    Alba = Troops(units_img[9], 0.8, 'Alba is a coven witch sent to find an ancient artifact',0,0,'alba',0)
    Severin = Troops(units_img[8], 0.8, 'Severin is a battle mage and scholar',0,0,'severin',0)


    troops_ranged.extend([])
    #-------------------------------------------------------------------------------------
    troops_cavalry = []
    Chevaliers = Troops(units_img[3], 0.8, 'Armored assault cavalry',0,0,'chevaliers',0)


    troops_cavalry.extend([])
    #-------------------------------------------------------------------------------------
    troops_support = []
    Scouts = Troops(units_img[4], 0.8, 'A group of trained scouts',0,0,'scouts',0)



    troops_support.extend([])
    #-------------------------------------------------------------------------------------

    list_of_troops = []
    list_of_troops.extend([troops_melee,troops_ranged,troops_cavalry,troops_support])


    #-------------------------------------------------------------------------------------
    def draw_troops_in_inventory(surface, item_list, Xmod, Ymod):
        item_list = item_list
        Xmod = Xmod
        Ymod = Ymod
        troop_col = 0
        troop_row = 0
        for i, j in enumerate(item_list):
            j.draw(surface, TILE_SIZE * Xmod + TILE_SIZE * troop_col, TILE_SIZE * Ymod + TILE_SIZE * troop_row)
            troop_col += 1
            if troop_col == 12:
                troop_row += 1
                troop_col = 0












    #----------------------------------------Techniques/Skills--------------------------------
    class Technique():
        def __init__(self,x,y, image,scale,descr,skillcheck,status,id,skillvalue,effect,tier,value):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.image_rect = self.image.get_rect()
            self.rect = self.image.get_rect()
            self.rect.x = x*TILE_SIZE
            self.rect.y = y*TILE_SIZE
            self.toggled = False
            self.clicked = False
            self.active = False
            self.skillcheck = skillcheck
            self.descr = descr
            self.status = status
            self.id = id
            self.effect = effect
            self.skillvalue = skillvalue
            self.tier = tier
            self.value = value

        def item_text(self,text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            if skills_active == True:
                surface.blit(textobj, textrect)

        def skill_scroll(self, surface):
            surface.blit(skill_scroll, (surface.get_width() * 0.28, surface.get_height() * 0.26))

        def skill_text(self, surface, text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            surface.blit(img, (x, y))

        def selected(self, surface):
            selection_rect = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
            pygame.draw.rect(surface, (82, 82, 82), selection_rect)
            #surface.blit(slot_list_img[10], (self.rect.x, self.rect.y))

        def draw(self, surface, x, y):
            global learning_points
            action = True
            self.x = x
            self.y = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and skills_active == True \
                        and self.status == 0 and self.value <= learning_points and self.tier*6 <= skill_counter:
                    pygame.mixer.Sound(select_sound).play()
                    self.clicked = True
                    self.active = True
                    self.status = 1
                    learning_points -= self.value
                    time.sleep(0.1)
            if skills_active == True:
                if self.status == 1:
                   self.selected(display)
                surface.blit(self.image, (self.rect.x, self.rect.y))
            return action

        def event_handler (self,event):
            global learning_points
            action = False
            pos = pygame.mouse.get_pos()
            #for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pos):
                    if event.button == 1 and self.toggled == False and skills_active == True \
                       and self.status == 0 and self.value <= learning_points and self.tier*6 <= skill_counter \
                       and self.active == True:
                           self.toggled = True
                           self.status = 1
                           learning_points -= self.value
                           time.sleep(0.1)
                    # elif event.button == 1 and self.toggled == True:
                    #     if self.rect.collidepoint(event.pos):
                    #         self.toggled = False


    #-------------------------------------SkillButtons--------------------------------
    TILE_SIZE = 64
    path, dirs, ranks = next(os.walk("MainMenuRes/techniques/ranks"))
    ranks_count = len(ranks)
    RANK_TYPES = ranks_count
    ranks_img = []
    path, dirs, techniques = next(os.walk("MainMenuRes/techniques/all"))
    techniques_count = len(techniques)
    TECHNIQUE_TYPES = techniques_count
    techniques_img = []
    path, dirs, inactive = next(os.walk("MainMenuRes/techniques/inactive"))
    inactive_count = len(inactive)
    INACTIVE_TYPES = inactive_count
    inactive_img = []
    for x in range(RANK_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/ranks/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        ranks_img.append(img)
    for x in range(TECHNIQUE_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/all/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        techniques_img.append(img)
    for x in range(INACTIVE_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/inactive/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        inactive_img.append(img)

    skill_counter = 0       # counts availability of new tiers
    def draw_empty_skill_slots():
        if skills_active == True:
            for y in range(4):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[10], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[0], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE))
                    novice = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE,ranks_img[0].get_width(), ranks_img[0].get_height())
                    if novice.collidepoint(mouse_position):
                        stats_draw_text('Novice Tier', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[1], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE))
                    adept = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE,ranks_img[1].get_width(), ranks_img[1].get_height())
                    if adept.collidepoint(mouse_position):
                        stats_draw_text('Adept Tier || Requires 6 Learned Techniques', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[2], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))
                    expert = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE,ranks_img[2].get_width(), ranks_img[2].get_height())
                    if expert.collidepoint(mouse_position):
                        stats_draw_text('Expert Tier || Requires 12 Learned Techniques', fontDescription, (0, 0, 0,), display, 490, 690)
            for y in range(1):
                for x in range(1):
                    display.blit(ranks_img[3], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    master = pygame.Rect(TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE,ranks_img[3].get_width(), ranks_img[3].get_height())
                    if master.collidepoint(mouse_position):
                        stats_draw_text('Master Tier || Requires 18 Learned Techniques', fontDescription, (0, 0, 0,), display, 490, 690)
            #-------------------------------------------------------------------------
            if skill_counter >= 0:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 9 + y * TILE_SIZE))
            if skill_counter >= 6:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 8 + y * TILE_SIZE))
            if skill_counter >= 12:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))
            if skill_counter >= 18:
                for y in range(1):
                    for x in range(MAX_COLS * 4):
                        display.blit(slot_list_img[11], (TILE_SIZE * 7 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))

    #---------------------------------------------------Techniques----------------------------------
    skill_novice = []
    Cartographer = Technique(7.1, 9.1,techniques_img[0], 0.8, 'Increases speed on the global map by 50%',button.nature,0,'Cartographer',20,50,0, 10)
    Combo = Technique(8.1, 9.1,techniques_img[66], 0.8,'Attack target twice in melee',button.melee,0,'Combo',20,2,0, 10)
    Educated = Technique(9.1, 9.1,techniques_img[29], 0.8,'Increases experience gain by 25%',button.lore,0,'Educated',20,25,0,10)
    Quick_Shot = Technique(10.1, 9.1,techniques_img[56], 0.8,'Gives 25% chance of a free ranged attack',button.ranged,0,'Quick Shot',20,15,0, 10)
    Camp_Doctor = Technique(11.1, 9.1,techniques_img[42], 0.8, 'Increases healing rate on the map by 25%',button.medicine,0,'Camp Doctor',20,25,0, 10)
    Thief = Technique(12.1, 9.1,techniques_img[30], 0.8,'Allows to steal from traders',button.thievery,0,'Thief',20,15,0, 10)
    Quartermaster = Technique(13.1, 9.1,techniques_img[46], 0.8,'Doubles efficiency of resting in battle',button.arming,0,'Quartermaster',20,100,0, 10)
    Scout = Technique(14.1, 9.1,techniques_img[71], 0.8,'Chance to avoid encounters is increased by 25%',button.deception,0,'Scout',20,25,0, 10)
    Haggler = Technique(15.1, 9.1,techniques_img[73], 0.8,'Allows to sell items',button.intimidation,0,'Haggler',20,15,0, 10)
    Estates = Technique(16.1, 9.1,techniques_img[6], 0.8,'Increases gold income from ventures by 25%',button.persuasion,0,'Estates',20,25,0, 10)
    Curse = Technique(17.1, 9.1,techniques_img[7], 0.8,'Decreases enemy resistances and defence',button.arcane,0,'Curse',20,10,0, 10)
    Healing = Technique(18.1, 9.1,techniques_img[35], 0.8,'Restores 25% of health',button.divine,0,'Healing',20,35,0, 10)
    #---------------------------------------------------------------------------------------------------------------------
    skill_novice.extend([Cartographer,Combo,Educated,Quick_Shot, Camp_Doctor, Thief, Quartermaster,Scout, Haggler,Estates, Curse, Healing])
    #-----------------------------------------------------------------------------------------------------------------------
    skill_adept = []
    Snake_Eater = Technique(7.1, 8.1,techniques_img[18], 0.8, 'Immunity to poisons',button.medicine,0,'Snake Eater',40,50,1, 15)
    Power_Blow = Technique(8.1, 8.1,techniques_img[44], 0.8,'Killing in melee grants a free action',button.melee,0,'Power Blow',40,2,1, 15)
    Scholar = Technique(9.1, 8.1,techniques_img[4], 0.8,'Gives 5 extra learning points with every level',button.lore,0,'Scholar',40,5,1,15)
    Multiple_Shot = Technique(10.1, 8.1,techniques_img[13], 0.8,'Attack target twice with a ranged weapon',button.ranged,0,'Multiple Shot',40,2,1, 15)
    Duelist = Technique(11.1, 8.1,techniques_img[45], 0.8,'Always retaliates at te cost of tricks',button.parrying,0,'Duelist',40,15,1, 15)
    Bear_Trap = Technique(12.1, 8.1,techniques_img[27], 0.8, 'Applies bleeding to multiple targets',button.traps,0,'Bear Trap',40,5,1, 15)
    Potion_Master = Technique(13.1, 8.1,techniques_img[17], 0.8,'Decreases supply cost to use potions',button.alchemy,0,'Potion Master',40,1,1, 15)
    Knock_Down = Technique(14.1, 8.1,techniques_img[74], 0.8,'Attack target and make it skip its turn',button.stupefy,0,'Knock Down',40,10,1, 15)
    Battle_Reflex = Technique(15.1, 8.1,techniques_img[38], 0.8,'Gives 20% chance to avoid ranged attacks',button.acrobatics,0,'Battle Reflex',40,20,1, 15)
    Persevere = Technique(16.1, 8.1,techniques_img[49], 0.8,'Gives 10% chance to survive a deadly strike',button.athletics,0,'Persevere',40,10,1, 15)
    Moon_Shield = Technique(17.1, 8.1,techniques_img[34], 0.8,'Creates a shield of 10% of armor every turn',button.arcane,0,'Moon Shield',40,10,1, 15)
    Purifier = Technique(18.1, 8.1,techniques_img[55], 0.8,'Removes all negative statuses from all troops',button.divine,0,'Purifier',40,1,1, 15)
    #-----------------------------------------------------------------------------------------------------------------------
    skill_adept.extend([Snake_Eater,Power_Blow,Scholar,Multiple_Shot, Duelist, Bear_Trap, Potion_Master,Knock_Down, Battle_Reflex,Persevere, Moon_Shield, Purifier])
    #-----------------------------------------------------------------------------------------------------------------------
    skill_expert = []
    Readiness = Technique(7.1, 7.1,techniques_img[33], 0.8,'Increases armor efficiency by 25%',button.arming,0,'Readiness',60,25,2, 20)
    Slice = Technique(8.1, 7.1,techniques_img[28], 0.8,'Hits multiple targets in melee',button.melee,0,'Slice',60,4,2, 20)
    War_Engineer = Technique(9.1, 7.1,techniques_img[1], 0.8,'Increases efficiency of support war machines',button.engineering,0,'War Engineer',60,2,2, 20)
    Deadeye = Technique(10.1, 7.1,techniques_img[65], 0.8,'Ranged attack critical damage is quadrupled',button.ranged,0,'Deadeye',60,50,2, 20)
    Barrage = Technique(11.1, 7.1,techniques_img[39], 0.8,'Hit multiple targets with a ranged weapon',button.ranged,0,'Barrage',60,4,2, 20)
    Shields_Up = Technique(12.1, 7.1,techniques_img[16], 0.8,'Restores 25% armor of all troops',button.tactics,0,'Shields Up',60,25,2, 20)
    Field_Engineer = Technique(13.1, 7.1,techniques_img[60], 0.8,'Doubles armor of war machines',button.engineering,0,'Field Engineer',60,20,2, 20)
    Charge = Technique(14.1, 7.1,techniques_img[62], 0.8,'Increases damage of all troops by 10%',button.tactics,0,'Charge',60,10,2, 20)
    Reaper = Technique(15.1, 7.1,techniques_img[75], 0.8,'Increases critical hit chance by 10%',button.stupefy,0,'Reaper',60,10,2, 20)
    Troll_Skin = Technique(16.1, 7.1,techniques_img[32], 0.8,'Applies regeneration. Restores 5% health each turn',button.athletics,0,'Troll Skin',60,3,2, 20)
    Dream_Cloud = Technique(17.1, 7.1,techniques_img[11], 0.8,'Several targets have a chance to skip turn',button.arcane,0,'Dream Cloud',60,4,2, 20)
    Second_Wind = Technique(18.1, 7.1,techniques_img[9], 0.8,'Restores full health',button.divine,0,'Second Wind',60,10,2, 20)
    #-----------------------------------------------------------------------------------------------------------------------
    skill_expert.extend([Readiness,Slice,Field_Engineer,Deadeye,Barrage,Shields_Up,War_Engineer,Charge,Reaper,Troll_Skin,Dream_Cloud,Second_Wind])
    #-----------------------------------------------------------------------------------------------------------------------
    skill_master = []
    Backstab = Technique(7.1, 6.1,techniques_img[54], 0.8,'Tries to kill a human target instantly',button.stupefy,0,'Backstab',80,50,3, 25)
    Weak_Spot = Technique(8.1, 6.1,techniques_img[19], 0.8,'Melee attack critical damage is quadrupled',button.melee,0,'Weak Spot',80,4,3, 25)
    Siege_Master = Technique(9.1, 6.1,techniques_img[12], 0.8,'Increases efficiency of war machines',button.siege,0,'Siege Master',80,2,3, 25)
    Piercing_Arrows = Technique(10.1, 6.1,techniques_img[2], 0.8,'Ranged attack that ignores armor',button.ranged,0,'Piercing Arrows',80,1,3, 25)
    Planewalker = Technique(11.1, 6.1,techniques_img[22], 0.8,'15% chance of getting aid from another planes',button.investigation,0,'Planewalker',80,10,3, 25)
    Commander = Technique(12.1, 6.1,techniques_img[63], 0.8,'Deploying troops is 20% cheaper',button.tactics,0,'Commander',80,20,3, 25)
    Master_Mechanist = Technique(13.1, 6.1,techniques_img[64], 0.8,'Fortifies war machines with 25 threshold',button.engineering,0,'Master Mechanist',80,20,3, 25)
    Battle_Prudence = Technique(14.1, 6.1,techniques_img[43], 0.8,'Poisons or applies bleeding to all enemy troops',button.traps,0,'Battle Prudence',80,3,3, 25)
    Channelling = Technique(15.1, 6.1,techniques_img[24], 0.8,'Restores two tricks every turn',button.arcane,0,'Channelling',80,2,3, 25)
    Divine_Intervention = Technique(16.1, 6.1,techniques_img[67], 0.8,'Restores 25% health of all troops',button.divine,0,'Divine Intervention',80,25,3, 25)
    Shadows = Technique(17.1, 6.1,techniques_img[20], 0.8,'Creates two shadow copies',button.arcane,0,'Shadows',80,2,3, 25)
    Blessing = Technique(18.1, 6.1,techniques_img[41], 0.8,'All troops are hastened',button.divine,0,'Blessing',80,20,3, 25)
    #-----------------------------------------------------------------------------------------------------------------------
    skill_master.extend([Backstab,Weak_Spot,Siege_Master,Piercing_Arrows,Planewalker,Commander,Master_Mechanist,Battle_Prudence,Channelling,Divine_Intervention,Shadows,Blessing])
    #-----------------------------------------------------------------------------------------------------------------------
    list_of_skills = []
    list_of_skills.extend([skill_novice, skill_adept, skill_expert, skill_master])

    def draw_skills_in_inventory(surface, item_list, Xmod, Ymod):
        item_list = item_list
        Xmod = Xmod
        Ymod = Ymod
        item_col = 0
        item_row = 0
        for i, j in enumerate(item_list):
            j.draw(surface, TILE_SIZE * Xmod + TILE_SIZE * item_col, TILE_SIZE * Ymod + TILE_SIZE * item_row)
            item_col += 1
            if item_col == 12:
                item_row += 1
                item_col = 0

    #draw_skills_in_inventory(display, skill_novice, 7.1, 9.1)
    #------------------------------------------Inventory------------------------------------
    path, dirs, bow = next(os.walk("MainMenuRes/inventory/items/bow"))
    bow_count = len(bow)
    BOW_TYPES = bow_count
    path, dirs, armor = next(os.walk("MainMenuRes/inventory/items/armor"))
    armor_count = len(armor)
    ARMOR_TYPES = armor_count
    path, dirs, cloak = next(os.walk("MainMenuRes/inventory/items/cloak"))
    cloak_count = len(cloak)
    CLOAK_TYPES = cloak_count
    path, dirs, dagger = next(os.walk("MainMenuRes/inventory/items/dagger"))
    dagger_count = len(dagger)
    DAGGER_TYPES = dagger_count
    path, dirs, gloves = next(os.walk("MainMenuRes/inventory/items/gloves"))
    gloves_count = len(gloves)
    GLOVES_TYPES = gloves_count
    path, dirs, helm = next(os.walk("MainMenuRes/inventory/items/helm"))
    helm_count = len(helm)
    HELM_TYPES = helm_count
    path, dirs, necklace = next(os.walk("MainMenuRes/inventory/items/necklace"))
    necklace_count = len(necklace)
    NECKLACE_TYPES = necklace_count
    path, dirs, pants = next(os.walk("MainMenuRes/inventory/items/pants"))
    pants_count = len(pants)
    PANTS_TYPES = pants_count
    path, dirs, ring = next(os.walk("MainMenuRes/inventory/items/ring"))
    ring_count = len(ring)
    RING_TYPES = ring_count
    path, dirs, shoes = next(os.walk("MainMenuRes/inventory/items/shoes"))
    shoes_count = len(shoes)
    SHOES_TYPES = shoes_count
    path, dirs, sword = next(os.walk("MainMenuRes/inventory/items/sword"))
    sword_count = len(sword)
    SWORD_TYPES = sword_count
    path, dirs, belt = next(os.walk("MainMenuRes/inventory/items/belt"))
    belt_count = len(belt)
    BELT_TYPES = belt_count
    path, dirs, trinkets = next(os.walk("MainMenuRes/inventory/items/trinkets"))
    trinkets_count = len(trinkets)
    TRINKETS_TYPES = trinkets_count


    TILE_SIZE = 64
    MAX_ROWS = 4
    MAX_COLS = 3
    current_item = 0
    current_bow = 0
    current_helm = 0
    current_armor = 0
    current_cloak = 0
    current_dagger = 0
    current_gloves = 0
    current_necklace = 0
    current_pants = 0
    current_ring = 0
    current_shoes = 0
    current_sword = 0
    current_belt = 0

    bows_list_img = []
    for x in range(BOW_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/bow/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        bows_list_img.append(img)

    dagger_list_img = []
    for x in range(DAGGER_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/dagger/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        dagger_list_img.append(img)

    armor_list_img = []
    for x in range(ARMOR_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/armor/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        armor_list_img.append(img)

    cloak_list_img = []
    for x in range(CLOAK_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/cloak/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        cloak_list_img.append(img)

    gloves_list_img = []
    for x in range(GLOVES_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/gloves/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        gloves_list_img.append(img)

    helm_list_img = []
    for x in range(HELM_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/helm/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        helm_list_img.append(img)

    necklace_list_img = []
    for x in range(NECKLACE_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/necklace/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        necklace_list_img.append(img)

    pants_list_img = []
    for x in range(PANTS_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/pants/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        pants_list_img.append(img)

    ring_list_img = []
    for x in range(RING_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/ring/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        ring_list_img.append(img)

    shoes_list_img = []
    for x in range(SHOES_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/shoes/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        shoes_list_img.append(img)

    sword_list_img = []
    for x in range(SWORD_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/sword/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        sword_list_img.append(img)

    belt_list_img = []
    for x in range(BELT_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/belt/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        belt_list_img.append(img)

    trinkets_list_img = []
    for x in range(TRINKETS_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/items/trinkets/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        trinkets_list_img.append(img)

    slot_list_img = []
    for x in range(SLOT_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/slots/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        slot_list_img.append(img)

    # ---------------------------------SlotIDs----------------------------------------
    #   for col in range(MAX_COLS):
    #     for row in range(MAX_ROWS):
    equipable_slots = []
    nek = [-1]
    hel = [-2]
    clk = [-3]
    bow = [-4]
    arm = [-5]
    glv = [-6]
    pnt = [-9]
    dgr = [-7]
    srd = [-8]
    bts = [-12]
    rng = [-10]
    blt = [-13]
    inv = [-11]
    equipable_slots.extend([nek,hel,clk,bow,arm,glv,pnt,dgr,srd,bts,rng,blt,inv])

    # for col in range(2):
    # #     for row in range(MAX_ROWS):
    #     inv = [-11]
    #     equipable_slots.append(inv)
    # ----------------------------------------------------------------------------------
    # def draw_grid():
    #     for i in range(MAX_COLS + 1):
    #         pygame.draw.line(screen, (255,255,255), (TILE_SIZE*6+i * TILE_SIZE, TILE_SIZE*6),(TILE_SIZE*6+i * TILE_SIZE, TILE_SIZE*10))
    #     for i in range(MAX_ROWS + 1):
    #         pygame.draw.line(screen, (255,255,255), (TILE_SIZE*6, TILE_SIZE*6+i * TILE_SIZE),(TILE_SIZE*9, TILE_SIZE*6+i * TILE_SIZE))
    # ----------------------------------------------------------------------------------
    class Item():
        def __init__(self, image,scale,descr,bonus,status,id,value):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.toggled = False
            self.taken = False
            self.bonus = bonus
            self.descr = descr
            self.status = status
            self.id = id
            self.value = value

        def item_text(self,text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            if inventory_active == True:
                surface.blit(textobj, textrect)

        def draw(self, surface, x, y):
            self.x = x
            self.y = y
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            action = False
            self.clicked = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
            if inventory_active == True and 10*TILE_SIZE > self.y > 7*TILE_SIZE:
                surface.blit(self.image, (self.rect.x, self.rect.y))
            return action

        def event_handler (self,event):
            action = False
            pos = pygame.mouse.get_pos()
            #for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inventory_active == True:
                    if event.button == 1 and self.toggled == False:
                        if self.rect.collidepoint(event.pos):
                            self.toggled = True
                    elif event.button == 1 and self.toggled == True:
                        if self.rect.collidepoint(event.pos):
                            self.toggled = False

        def sell_item(self, list,item):
            self.list = list
            self.item = item
            if self.value > 0:
                list.remove(item)
                button.wealth += self.value
                button.start_wealth = button.wealth
                coins_sound.play()

        def get_item(self, list,item):
            self.list = list
            self.item = item
            list.extend([item])

        def buy_item(self, list,item):
            self.list = list
            self.item = item
            list.extend([item])
            if button.start_wealth >= self.value:
                button.wealth -= self.value
                button.start_wealth = button.wealth
                coins_sound.play()

#-------------------------------------------------------------------------------------
    def draw_empty_slots():
        if inventory_active == True:
            for y in range(1):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[10], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
            for y in range(3):
                for x in range(MAX_COLS * 4 + 1):
                    display.blit(slot_list_img[11], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 7 + y * TILE_SIZE))

    def draw_inventory_slots():
        for x, row in enumerate(equipable_slots):
            for y, slot in enumerate(row):
                if inventory_active == True:
                    if slot == -1:
                        display.blit(slot_list_img[5], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -2:
                        display.blit(slot_list_img[4], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -3:
                        display.blit(slot_list_img[2], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -4:
                        display.blit(slot_list_img[7], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -5:
                        display.blit(slot_list_img[1], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -6:
                        display.blit(slot_list_img[3], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -7:
                        display.blit(slot_list_img[0], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -8:
                        display.blit(slot_list_img[12], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -9:
                        display.blit(slot_list_img[6], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -10:
                        display.blit(slot_list_img[8], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -11:
                        display.blit(slot_list_img[13], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -12:
                        display.blit(slot_list_img[9], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))
                    if slot == -13:
                        display.blit(slot_list_img[14], (TILE_SIZE * 6 + x * TILE_SIZE, TILE_SIZE * 6 + y * TILE_SIZE))

    # def draw_items():
    #     for y, row in enumerate(item_slots):
    #         for x, item in enumerate(row):
    #             if item >= 0:
    #                 screen.blit(items_list_img[item], (x * TILE_SIZE, y * TILE_SIZE))

    belt_list = []
    travel_belt = Item(belt_list_img[0], 0.8,f'Travel leather belt. Supply+{1}',1,0,'travel_belt',100)
    hunter_belt = Item(belt_list_img[1], 0.8,f'Hunter\'s belt. Supply+{3}',3,0,'hunter_belt',350)
    war_belt = Item(belt_list_img[2], 0.8,f'War belt. Supply+{4} | ARM+{20} | DEF+{5}',20,0,'war_belt',900)
    double_belt = Item(belt_list_img[3], 0.8,f'Double belt. Supply+{6}',6,0,'double_belt',1200)
    noble_belt = Item(belt_list_img[4], 0.8,f'Noble belt. Supply+{2} | Retaliate+{6} | Block +{6}',6,0,'noble_belt',2500)
    night_belt = Item(belt_list_img[5], 0.8,f'Night belt. Supply+{3} | Crit+{5}',5,0,'night_belt',2000)
    day_belt = Item(belt_list_img[6], 0.8,f'Day belt. Supply+{3} | Health+{50}',50,0,'day_belt',2000)
    warlock_belt = Item(belt_list_img[7], 0.8,f'Warlock belt. Supply+{2} | Resistances+{10}',10,0,'warlock_belt',3000)
    duel_belt = Item(belt_list_img[8], 0.8,f'Duel belt. Supply+{4} | Retaliate+{12} | Block+{12}',12,0,'duel_belt',4500)
    druid_belt = Item(belt_list_img[9], 0.8,f'Druid belt. Supply+{2} | THR+{4}',4,0,'druid_belt',3000)
    belt_list.extend([])

    necklace_list = []
    traders_luck = Item(necklace_list_img[0], 0.8,f'Trader\'s luck. Tricks+{1}',1,0,'traders_luck',100)
    moon_crest = Item(necklace_list_img[1], 0.8,f'Moon crest. Tricks+{2} | Arcana res.+{10}',10,0,'moon_crest',800)
    brothers_mark = Item(necklace_list_img[2], 0.8,f'Brother\'s mark. Tricks+{3} | Crit+{3}',3,0,'brothers_mark',1200)
    the_eye = Item(necklace_list_img[3], 0.8,f'The Eye. Tricks+{6}',6,0,'the_eye',2500)
    war_amulet = Item(necklace_list_img[4], 0.8,f'War amulet. Tricks+{2} | DEF+{2} | ARM+{10}',10,0,'war_amulet',1500)
    deep_endless = Item(necklace_list_img[5], 0.8,f'Deep Endless. Tricks+{12}',12,0,'deep_endless',2700)
    warlock_amulet = Item(necklace_list_img[6], 0.8,f'Warlock amulet. Tricks+{4} | Resistances+{10}',10,0,'warlock_amulet',2600)
    spider_amulet = Item(necklace_list_img[7], 0.8,f'Spider amulet. Tricks+{4} | Retaliate+{8}',8,0,'spider_amulet',2100)
    defilers_amulet = Item(necklace_list_img[8], 0.8,f'Defiler\'s amulet. Tricks+{6} | Poison/Fire Res.+{20}',20,0,'defilers_amulet',1600)
    grimshard_amulet = Item(necklace_list_img[9], 0.8,f'Grimshard amulet. Tricks+{4} | Crit+{8}',8,0,'grimshard_amulet',2300)
    the_shining = Item(necklace_list_img[10], 0.8,f'The Shining. Health+{12} | BLK+{6}',12,0,'the_shining',1100)
    sailors_luck = Item(necklace_list_img[11], 0.8,f'Sailor\'s luck. Tricks+{4} | Energy/Frost Res.+{20}',20,0,'sailors_luck',1300)
    crystal_amulet = Item(necklace_list_img[12], 0.8,f'Crystal amulet. Tricks+{10} | DEF+{20}',20,0,'crystal_amulet',2800)
    necklace_list.extend([])

    helm_list = []
    travel_hat = Item(helm_list_img[0], 0.8,f'Travel hat. DEF+{4}',4,0,'travel_hat',200)
    steel_helm = Item(helm_list_img[1], 0.8,f'Steel helmet. ARM+{18} | DEF+{6}',18,0,'steel_helm',1200)
    tournament_helm = Item(helm_list_img[2], 0.8,f'Tournament helmet. ARM+{40} | DEF+{10} THR+{6}',40,0,'tournament_helm',3600)
    monk_hood = Item(helm_list_img[3], 0.8,f'Monk hood. DEF+{8}',8,0,'monk_hood',400)
    leather_hood = Item(helm_list_img[4], 0.8,f'Leather hood. ARM+{8} | DEF+{4}',8,0,'leather_hood',500)
    light_chain_helm = Item(helm_list_img[5], 0.8,f'Light chain helmet. ARM+{28} | DEF+{6} | THR+{2}',28,0,'light_chain_helm',2200)
    protector_helm = Item(helm_list_img[6], 0.8,f'Protector\'s helmet. ARM+{36} | DEF+{14} | THR+{4}',36,0,'protector_helm',2800)
    legion_helm = Item(helm_list_img[7], 0.8,f'Legion helmet. ARM+{32} | DEF+{9} | THR+{2}',32,0,'legion_helm',1200)
    leather_helm = Item(helm_list_img[8], 0.8,f'Leather helmet. ARM+{12} | DEF+{2}',12,0,'leather_helm',700)
    pretorian_helm = Item(helm_list_img[9], 0.8,f'Pretorian helmet.  ARM+{38} | DEF+{14} | THR+{4}',38,0,'pretorian_helm',2200)
    inquisitor_hat = Item(helm_list_img[10], 0.8,f'Inquisitor hat. DEF+{6} | Melee Attack+{12} | Crit+{3}',12,0,'inquisitor_hat',1900)
    brigade_helm = Item(helm_list_img[11], 0.8,f'Brigade helmet. ARM+{26} | DEF+{8}',26,0,'brigade_helm',1400)
    mage_hat = Item(helm_list_img[12], 0.8,f'Mage hat. DEF+{6} | Resistances+{12}',12,0,'mage_hat',1400)
    mercenary_helm = Item(helm_list_img[13], 0.8,f'Mercenary helmet. ARM+{32} | DEF+{6} | THR+{3}',32,0,'mercenary_helm',1250)
    turtle_helm = Item(helm_list_img[14], 0.8,f'Turtle helmet. ARM+{56} | DEF+{14} | THR+{7}',56,0,'turtle_helm',3200)
    pigface_helm = Item(helm_list_img[15], 0.8,f'Pigface helmet. ARM+{40} | DEF+{20} | THR+{5}',40,0,'pigface_helm',3000)
    full_helm = Item(helm_list_img[16], 0.8,f'Full helmet. ARM+{36} | DEF+{10} | THR+{5}',36,0,'full_helm',2600)
    ranger_hat = Item(helm_list_img[17], 0.8,f'Ranger hat. DEF+{6} | Ranged Attack+{12} | Crit+{4}',12,0,'ranger_hat',1500)
    hoplite_helm = Item(helm_list_img[18], 0.8,f'Hoplite helmet. ARM+{36} | DEF+{12} | THR+{3}',36,0,'hoplite_helm',1650)


    helm_list.extend([])

    cloak_list = []
    travel_cloak = Item(cloak_list_img[0], 0.8,f'Travel cloak. DEF+{2}',2,0,'travel_cloak',150)
    night_cloak = Item(cloak_list_img[1], 0.8,f'Night cloak. DEF+{4} | Crit+{4}',4,0,'night_cloak',300)
    full_cloak = Item(cloak_list_img[2], 0.8,f'Full cloak. DEF+{4} | ARM+{8}',8,0,'full_cloak',500)
    ranger_cloak = Item(cloak_list_img[3], 0.8,f'Ranger cloak. DEF+{6} | BLK+{6} | Ranged attack+{10}',10,0,'ranger_cloak',900)
    jester_cloak = Item(cloak_list_img[4], 0.8,f'Jester cloak. DEF+{8} | Retaliate+{8} | Health+{20}',20,0,'jester_cloak',750)
    war_cloak = Item(cloak_list_img[5], 0.8,f'War cloak. DEF+{8} | ARM+{20} | THR+{2}',20,0,'war_cloak',1400)
    noble_cloak = Item(cloak_list_img[6], 0.8,f'Noble cloak. DEF+{6} | Block+{6} | Retaliate+{6}',6,0,'noble_cloak',1800)
    warlock_cloak = Item(cloak_list_img[7], 0.8,f'Warlock cloak. DEF+{4} | Tricks+{4} | Resistances+{10}',10,0,'warlock_cloak',2600)
    royal_cloak = Item(cloak_list_img[8], 0.8,f'Royal cloak. DEF+{10} | Tricks+{2} | Health +{20}',20,0,'royal_cloak',3200)
    thief_cloak = Item(cloak_list_img[9], 0.8,f'Thief cloak. DEF+{4} | Tricks+{4} | Stealth+{20}',20,0,'thief_cloak',1600)
    cloak_list.extend([])

    armor_list = []
    travel_clothes = Item(armor_list_img[0], 0.8,f"Travel clothes. ARM+{4} | DEF+{2}",4,0,'travel_clothes',150)
    robes = Item(armor_list_img[1], 0.8,f"Robes. DEF+{6}",6,0,'robes',200)
    light_leather = Item(armor_list_img[2], 0.8,f"Light leather armor. ARM+{12} | DEF+{6}",12,0,'light_leather',700)
    light_chain_mail = Item(armor_list_img[3], 0.8,f"Light chain mail. ARM+{40} | DEF+{10} | THR +{4}",40,0,'light_chain_mail',1600)
    light_plate_armor = Item(armor_list_img[4], 0.8,f"Light plate armor. ARM+{60} | DEF+{12} | BLK+{6} | THR+{6}",60,0,'light_plate_armor',2600)
    leather_armor = Item(armor_list_img[5], 0.8,f"Leather armor. ARM+{20} | DEF+{8}",20,0,'leather_armor',1200)
    reinforced_armor = Item(armor_list_img[6], 0.8,f"Reinforced leather armor. ARM+{30} | DEF+{8} | THR+{2}",30,0,'reinforced_armor',1600)
    nomad_armor = Item(armor_list_img[7], 0.8,f"Nomad armor. ARM+{24} | DEF+{16}",24,0,'nomad_armor',900)
    legion_armor = Item(armor_list_img[8], 0.8,f"Legion armor. ARM+{32} | DEF+{16} | THR+{4}",32,0,'legion_armor',1400)
    cuirasse = Item(armor_list_img[9], 0.8,f"Cuirasse. ARM+{28} | DEF+{8} | THR+{3}",28,0,'cuirasse',1150)
    tournament_armor = Item(armor_list_img[10], 0.8,f"Tournament armor. ARM+{120} | DEF+{30} | THR+{12}",120,0,'tournament_armor',9000)
    heavy_plate = Item(armor_list_img[11], 0.8,f"Heavy plate armor. ARM+{100} | DEF+{26} | THR+{10}",100,0,'heavy_plate',7500)
    reinforced_chain = Item(armor_list_img[12], 0.8,f"Reinforced chain mail. ARM+{48} | DEF+{14} | THR+{5}",48,0,'reinforced_chain',2200)
    lamellar_armor = Item(armor_list_img[13], 0.8,f"Lamellar armor. ARM+{44} | DEF+{20} | THR+{6}",44,0,'lamellar_armor',1800)
    plate_armor = Item(armor_list_img[14], 0.8,f"Plate armor. ARM+{80} | DEF+{22} | THR+{8}",80,0,'plate_armor',6000)
    armor_list.extend([])

    gloves_list = []
    travel_gloves = Item(gloves_list_img[0], 0.8,f'Travel gloves. DEF+{4} | ARM+{4}',4,0,'travel_gloves',150)
    hand_wraps = Item(gloves_list_img[1], 0.8,f'Hand wraps. DEF+{6}',6,0,'hand_wraps',100)
    light_leather_gloves = Item(gloves_list_img[2], 0.8,f'Light leather gloves. DEF+{6} | ARM+{8}',8,0,'light_leather_gloves',300)
    light_chain_gloves = Item(gloves_list_img[3], 0.8,f'Light chain gloves. DEF+{10} | ARM+{16} | THR+{1}',16,0,'light_chain_gloves',1200)
    light_plate_gloves = Item(gloves_list_img[4], 0.8,f'Light plate gloves. DEF+{12} | ARM+{24} | THR+{2}',24,0,'light_plate_gloves',1800)
    leather_gloves = Item(gloves_list_img[5], 0.8,f'Leather gloves. DEF+{6} | ARM+{12}',12,0,'leather_gloves',450)
    reinforced_gloves = Item(gloves_list_img[6], 0.8,f'Reinforced gloves. DEF +{8} | ARM+{18}',18,0,'reinforced_gloves',600)
    ranger_gloves = Item(gloves_list_img[7], 0.8,f'Ranger gloves. DEF+{10} | ARM+{20} | Ranged Attack+{8}',20,0,'ranger_gloves',1200)
    thieves_gloves = Item(gloves_list_img[8], 0.8,f'Thief\'s gloves. DEF+{8} | ARM+{10} | Thievery+{20}',20,0,'thieves_gloves',1100)
    plate_gloves = Item(gloves_list_img[9], 0.8,f'Plate gloves. DEF+{16} | ARM+{32} | THR+{4}',32,0,'plate_gloves',2400)
    tournament_gloves = Item(gloves_list_img[10], 0.8,f'Tournament gloves. DEF+{20} | ARM+{40} | THR+{6}',40,0,'tournament_gloves',3000)
    war_gloves = Item(gloves_list_img[11], 0.8,f'War gloves. DEF+{14} | ARM+{28} | THR+{3}',28,0,'war_gloves',2000)
    basilisk_gloves = Item(gloves_list_img[12], 0.8,f'Basilisk gloves. DEF+{10} | ARM+{20} | Tricks+{4} | Fire/Poison Res.+{60}',20,0,'basilisk_gloves',4000)
    gloves_list.extend([])

    pants_list = []
    cloth_pants = Item(pants_list_img[0], 0.8,f'Cloth pants. DEF+{4} | ARM+{4}',4,0,'cloth_pants',200)
    monk_pants = Item(pants_list_img[1], 0.8,f'Monk pants. DEF+{8} | BLK+{4}',8,0,'monk_pants',100)
    leather_pants = Item(pants_list_img[2], 0.8,f'Leather pants. DEF+{8} | ARM+{20}',20,0,'leather_pants',300)
    light_chain_pants = Item(pants_list_img[3], 0.8,f'Light chain pants. DEF+{12} | ARM+{24} | THR+{2}',24,0,'light_chain_pants',900)
    reinforced_pants = Item(pants_list_img[4], 0.8,f'Reinforced pants. DEF+{10} | ARM+{22}',22,0,'reinforced_pants',1200)
    light_plate_pants = Item(pants_list_img[5], 0.8,f'Light plate pants. DEF+{10} | ARM+{28} | THR+{4}',28,0,'light_plate_pants',1400)
    plate_pants = Item(pants_list_img[6], 0.8,f'Plate pants. DEF+{12} | ARM+{32} | THR+{6}',32,0,'plate_pants',2200)
    heavy_plate_pants = Item(pants_list_img[7], 0.8,f'Heavy plate pants. DEF+{14} | ARM+{36} | THR+{8}',36,0,'heavy_plate_pants',2600)
    tournament_pants = Item(pants_list_img[8], 0.8,f'Tournment pants. DEF+{16} | ARM+{42} | THR+{10}',42,0,'tournament_pants',3400)
    pants_list.extend([])

    dagger_list = []
    steel_dagger = Item(dagger_list_img[0], 0.8,f'Steel dagger. Melee Attack+{6} | Crit+{3} | BLK+{6}',6,0,'steel_dagger',900)
    thief_dagger = Item(dagger_list_img[1], 0.8,f'Thief\'s dagger. Melee Attack+{4} | Crit+{6}',6,0,'thief_dagger',400)
    ranger_dagger = Item(dagger_list_img[2], 0.8,f'Ranger dagger. Melee Attack+{12} | Crit+{8} | BLK+{8}',12,0,'ranger_dagger',1200)
    butcher_dagger = Item(dagger_list_img[3], 0.8,f'Butcher\'s dagger. Melee Attack+{10} | Crit+{4}',10,0,'butcher_dagger',600)
    common_dagger = Item(dagger_list_img[4], 0.8,f'Common dagger. Melee Attack+{2} | BLK+{6}',6,0,'common_dagger',300)
    broad_dagger = Item(dagger_list_img[5], 0.8,f'Broad dagger. Melee Attack+{6} | BLK+{8}',8,0,'broad_dagger',450)
    hunt_knife = Item(dagger_list_img[6], 0.8,f'Hunt knife. Melee Attack+{5}',5,0,'hunt_knife',200)
    war_dagger = Item(dagger_list_img[7], 0.8,f'War dagger. Melee Attack+{16} | Crit+{3} | BLK+{12}',16,0,'war_dagger',1600)
    storm_dagger = Item(dagger_list_img[8], 0.8,f'Storm dagger. Melee Attack+{20} | BLK+{10} | Energy Res.+{20}',20,0,'storm_dagger',1400)
    sting_dagger = Item(dagger_list_img[9], 0.8,f'Sting dagger. Melee Attack+{24} | Crit+{8}',24,0,'sting_dagger',2200)
    bone_dagger = Item(dagger_list_img[10], 0.8,f'Bone dagger. Melee Attack+{6} | BLK+{12} | DEF+{6}',12,0,'bone_dagger',1150)
    druid_dagger = Item(dagger_list_img[11], 0.8,f'Druid dagger. Melee Attack+{24} | Retaliate+{12} | Health+{24}',24,0,'druid_dagger',1700)
    sun_dagger = Item(dagger_list_img[12], 0.8,f'Sun dagger. Melee Attack+{20} | BLK+{10} | Fire Res.+{20}',20,0,'sun_dagger',1400)
    redsteel_dagger = Item(dagger_list_img[13], 0.8,f'Redsteel dagger. Melee Attack+{24} |  BLK+{8}',24,0,'redsteel_dagger',1600)
    royal_dagger = Item(dagger_list_img[14], 0.8,f'Royal dagger. Melee Attack+{10} | Retaliate+{10}',10,0,'royal_dagger',1900)
    mercenary_dagger = Item(dagger_list_img[15], 0.8,f'Mercenary dagger. Melee Attack+{8} | Crit+{2} | BLK+{4}',8,0,'mercenary_dagger',800)
    quality_dagger = Item(dagger_list_img[16], 0.8,f'Quality dagger. Melee Attack+{10} | Crit+{1} | BLK+{6}',10,0,'quality_dagger',900)
    knight_dagger = Item(dagger_list_img[17], 0.8,f'Knight dagger. Melee Attack+{20} | Crit+{4} | BLK+{8}',20,0,'knight_dagger',2000)
    duel_dagger = Item(dagger_list_img[18], 0.8,f'Duel dagger. Melee Attack+{12} | Retaliate+{6} | BLK+{6}',12,0,'duel_dagger',1800)

    dagger_list.extend([])

    sword_list = []
    steel_sword = Item(sword_list_img[0], 0.8,f'Steel sword. Melee Attack+{16}',16,0,'steel_sword',900)
    simple_sword = Item(sword_list_img[1], 0.8,f'Simple sword. Melee Attack+{8}',8,0,'simple_sword',200)
    short_sword = Item(sword_list_img[2], 0.8,f'Short sword. Melee Attack+{12}',12,0,'short_sword',700)
    long_sword = Item(sword_list_img[3], 0.8,f'Long sword. Melee Attack+{20}',20,0,'long_sword',1200)
    the_sunrise = Item(sword_list_img[4], 0.8,f'The Sunrise. Melee Attack+{60} | Crit+{6}',60,0,'the_sunrise',4000)
    spider_sword = Item(sword_list_img[5], 0.8,f'Spider sword. Melee Attack+{30} | Crit+{3}',30,0,'spider_sword',2600)
    soldier_sword = Item(sword_list_img[6], 0.8,f'Soldier\'s sword. Melee Attack+{24}',24,0,'soldier_sword',1600)
    mercenary_sword = Item(sword_list_img[7], 0.8,f'Mercenary sword. Melee Attack+{28}',28,0,'mercenary_sword',1900)
    broad_sword = Item(sword_list_img[8], 0.8,f'Broad sword sword. Melee Attack+{22}',22,0,'broad_sword',1400)
    snake_sword = Item(sword_list_img[9], 0.8,f'Snake sword. Melee Attack+{40} | Crit+{6}',40,0,'snake_sword',2650)
    great_sword = Item(sword_list_img[10], 0.8,f'Great sword. Melee Attack+{38} | BLK+{4}',38,0,'great_sword',1750)
    paladin_sword = Item(sword_list_img[11], 0.8,f'Paladin sword. Melee Attack+{48} | BLK+{12}',48,0,'paladin_sword',2700)
    pirate_sword = Item(sword_list_img[12], 0.8,f'Pirate sword. Melee Attack+{18}',18,0,'pirate_sword',950)
    aircutter = Item(sword_list_img[13], 0.8,f'Aircutter. Melee Attack+{32} | Crit+{8} | Retaliate+{12}',32,0,'aircutter',3400)
    captain_sword = Item(sword_list_img[14], 0.8,f'Captain sword. Melee Attack+{26} | BLK+{8}',26,0,'captain_sword',1800)
    sabre = Item(sword_list_img[15], 0.8,f'Sabre. Melee Attack+{24} | Retaliate+{4} | BLK+{4}',24,0,'sabre',1600)
    temple_sword = Item(sword_list_img[16], 0.8,f'Temple sword. Melee Attack+{36} | Crit+{6}',36,0,'temple_sword',3400)
    nomad_sword = Item(sword_list_img[17], 0.8,f'Nomad sword. Melee Attack+{26}',28,0,'nomad_sword',1250)
    curved_sword = Item(sword_list_img[18], 0.8,f'Curved sword. Melee Attack+{32}',32,0,'curved_sword',1550)
    legion_sword = Item(sword_list_img[19], 0.8,f'Legion sword. Melee Attack+{24} | BLK+{6}',24,0,'legion_sword',1450)
    pretorian_sword = Item(sword_list_img[20], 0.8,f'Pretorian sword. Melee Attack+{32}| BLK+{12}',32,0,'pretorian_sword',1900)
    the_sorrow = Item(sword_list_img[21], 0.8,f'The Sorrow. Melee Attack+{72} | Crit+{10}',72,0,'the_sorrow',4400)
    sword_list.extend([])

    shoes_list = []
    simple_shoes = Item(shoes_list_img[0], 0.8,f'Slippers. DEF+{2}',2,0,'simple_shoes',50)
    travel_shoes = Item(shoes_list_img[1], 0.8,f'Travel shoes. DEF+{4} | ARM+{8}',8,0,'travel_shoes',300)
    light_plate_shoes = Item(shoes_list_img[2], 0.8,f'Light plate shoes. DEF+{8} | ARM+{24} | THR+{2}',24,0,'light_plate_shoes',2000)
    light_chain_shoes = Item(shoes_list_img[3], 0.8,f'Light chain shoes. DEF+{6} | ARM+{16} | THR+{1}',16,0,'light_chain_shoes',1400)
    plate_shoes = Item(shoes_list_img[4], 0.8,f'Plate shoes. DEF+{10} | ARM+{30} | THR+{3}',30,0,'plate_shoes',2400)
    common_shoes = Item(shoes_list_img[5], 0.8,f'Common shoes. DEF+{2} | ARM+{4}',4,0,'common_shoes',200)
    hunter_shoes = Item(shoes_list_img[6], 0.8,f'Hunter shoes. DEF+{6} | ARM+{6}',6,0,'hunter_shoes',500)
    ranger_shoes = Item(shoes_list_img[7], 0.8,f'Ranger shoes. DEF+{10} | ARM+{6}',10,0,'ranger_shoes',900)
    heavy_plate_shoes = Item(shoes_list_img[8], 0.8,f'Heavy plate shoes. DEF+{12} | ARM+{36} | THR+{4}',36,0,'heavy_plate_shoes',2800)
    shadow_shoes = Item(shoes_list_img[9], 0.8,f'Shadow shoes. DEF+{14} | ARM+{10} | Crit+{4}',14,0,'shadow_shoes',1600)
    arcane_shoes = Item(shoes_list_img[10], 0.8,f'Arcane shoes. DEF+{6} | ARM+{6} | Elemental Res.+{10}',10,0,'arcane_shoes',2300)
    trader_shoes = Item(shoes_list_img[11], 0.8,f'Trader shoes. ARM+{20} | Health+{20} | Block+{8}',20,0,'trader_shoes',1300)
    leather_shoes = Item(shoes_list_img[12], 0.8,f'Leather shoes. DEF+{6} | ARM+{12}',12,0,'leather_shoes',800)
    tournament_shoes = Item(shoes_list_img[13], 0.8,f'Tournament shoes. DEF+{12} | ARM+{48} | THR+{6}',48,0,'tournament_shoes',3600)
    snakeskin_shoes = Item(shoes_list_img[14], 0.8,f'Snakeskin shoes. DEF+{10} | ARM+{10} | Retaliate+{8}',10,0,'snakeskin_shoes',1450)
    shoes_list.extend([])

    ring_list = []
    silver_ring = Item(ring_list_img[0], 0.8,f"Silver ring. Elemental Res.+{6}",6,0,'silver_ring',150)
    moon_ring = Item(ring_list_img[1], 0.8,f'Moon ring. Arcana Res.+{20} | Tricks+{2} ',20,0,'moon_ring',300)
    holy_ring = Item(ring_list_img[2], 0.8,f"Holy ring. Elemental Res+{12} | ARM+{6}",12,0,'holy_ring',400)
    trinity_ring = Item(ring_list_img[3], 0.8,f"Trinity ring. DEF+{5} | Block +{5} | THR+{5}",5,0,'trinity_ring',3000)
    minor_protection_ring = Item(ring_list_img[4], 0.8,f"Minor protection ring. ARM+{20} | THR+{2}",20,0,'minor_protection_ring',1600)
    minor_health_ring = Item(ring_list_img[5], 0.8,f"Minor health ring. Health+{20}",20,0,'minor_health_ring',1200)
    emerald_ring = Item(ring_list_img[6], 0.8,f"Emerald ring. Poison res.+{20}",20,0,'emerald_ring',900)
    unity_ring = Item(ring_list_img[7], 0.8,f"Unity ring. Melee Attack+{6} | Ranged Attack+{6}",6,0,'unity_ring',1300)
    protection_ring = Item(ring_list_img[9], 0.8,f"Protection ring. ARM+{30} | THR+{3}",30,0,'protection_ring',2100)
    health_ring = Item(ring_list_img[8], 0.8,f"Health ring. Health+{40}",40,0,'health_ring',1900)
    medusa_ring = Item(ring_list_img[10], 0.8,f"Medusa ring. Health+{10} | THR+{2}",10,0,'medusa_ring',1250)
    bloodoath_ring = Item(ring_list_img[11], 0.8,f"Bloodoath ring. Crit+{7}",7,0,'bloodoath_ring',2200)
    duel_ring = Item(ring_list_img[12], 0.8,f"Duel ring. BLK+{8} | Melee Attack+{4}",8,0,'duel_ring',1700)
    snake_ring = Item(ring_list_img[13], 0.8,f"Snake ring. Retaliation+{8} | DEF+{4}",8,0,'snake_ring',1450)
    obscurity_ring = Item(ring_list_img[14], 0.8,f"Obscurity ring. Stealth+{20} | Crit+{2}",20,0,'obscurity_ring',1300)
    ocean_ring = Item(ring_list_img[15], 0.8,f"Ocean ring. Energy/Frost Res.+{40} | Tricks+{2}",40,0,'ocean_ring',2300)
    war_ring = Item(ring_list_img[16], 0.8,f"War ring. DEF+{12} | Block +{6} | THR+{3}",12,0,'war_ring',2650)
    bone_ring = Item(ring_list_img[17], 0.8,f"Bone ring. Armor+{20} | Poison Res.+{40}",40,0,'bone_ring',2250)
    sun_ring = Item(ring_list_img[18], 0.8,f"Sun ring. Fire/Arcane Res.+{40} | Tricks+{2}",40,0,'sun_ring',2300)
    ring_list.extend([])

    inv_list = []
    letter_1 = Item(trinkets_list_img[0], 0.8, f'A signed royal document that grants you freedom',0,0,'royal_pardon',0)
    apple = Item(trinkets_list_img[1], 0.8, f'Red apple. Health+{5}',5,0, 'red_apple',10)
    seafarer_charm = Item(trinkets_list_img[7], 0.8, f'Charm used by seafarers for good luck.',0,0, 'seafarer_charm',0)
    crowbar = Item(trinkets_list_img[45], 0.8, f'Crowbar for opening chests',10,0, 'crowbar',200)
    lockmaster_tools = Item(trinkets_list_img[47], 0.8, f'Tools used by thieves and burglars',20,0, 'lockmaster_tools',750)
    alchemist_kit = Item(trinkets_list_img[46], 0.8, f'A set of tools for preparing potions',20,0, 'alchemist_kit',750)

    inv_list.extend([letter_1, apple])

    bow_list = []
    simple_bow = Item(bows_list_img[0], 0.8,f'Makeshift bow. Ranged Attack+{8}',8,0,'simple_bow',100)
    hunter_bow = Item(bows_list_img[1], 0.8,f'Hunter bow. Ranged Attack+{14}',14,0,'hunter_bow',400)
    war_bow = Item(bows_list_img[2], 0.8,f'War bow. Ranged Attack+{36} | Crit+{5}',36,0,'war_bow',2400)
    peasant_bow = Item(bows_list_img[3], 0.8,f'Peasant bow. Ranged Attack+{12}',12,0,'peasant_bow',300)
    metal_bow = Item(bows_list_img[4], 0.8,f'Metal bow. Ranged Attack+{28}',28,0,'metal_bow',1600)
    militia_bow = Item(bows_list_img[5], 0.8,f'Militia bow. Ranged Attack+{16}',16,0,'militia_bow',550)
    redwood_bow = Item(bows_list_img[6], 0.8,f'Redwood bow. Ranged Attack+{20}',20,0,'redwood_bow',800)
    curved_bow = Item(bows_list_img[7], 0.8,f'Curved bow. Ranged Attack+{24} | Crit+{3}',24,0,'curved_bow',1100)
    nomad_bow = Item(bows_list_img[8], 0.8,f'Nomad bow. Ranged Attack+{26} | Crit+{4}',26,0,'nomad_bow',1200)
    bone_bow = Item(bows_list_img[9], 0.8,f'Bone bow. Ranged Attack+{24} | Crit+{2} | Arcana Res.+{20}',24,0,'bone_bow',1300)
    marksman_bow = Item(bows_list_img[10], 0.8,f'Marksman bow. Ranged Attack+{36} | Crit+{9}',36,0,'marksman_bow',2300)
    forest_bow = Item(bows_list_img[11], 0.8,f'Forest bow. Ranged Attack+{24} | Crit+{12} | Poison/Frost Res.+{20}',24,0,'forest_bow',1800)
    blackwood_bow = Item(bows_list_img[12], 0.8,f'Blackwood bow. Ranged Attack+{32} | Crit+{7}',32,0,'blackwood_bow',2100)
    flameguard = Item(bows_list_img[13], 0.8,f'Flameguard. Ranged Attack+{40} | Crit+{10} | Fire Res.+{20}',40,0,'flameguard',3600)
    mechanized_bow = Item(bows_list_img[14], 0.8,f'Mechanized bow. Ranged Attack+{48} | Crit+{6}',48,0,'mechanized_bow',4000)
    soldier_bow = Item(bows_list_img[15], 0.8,f'Soldier bow. Ranged Attack+{30} | Crit+{4} | Tricks+{2}',30,0,'soldier_bow',1700)
    long_bow = Item(bows_list_img[16], 0.8,f'Long bow. Ranged Attack+{42}',42,0,'long_bow',2600)
    valley_bow = Item(bows_list_img[17], 0.8,f'Valley bow. Ranged Attack+{18} | Crit+{1}',20,0,'valley_bow',650)
    bow_list.extend([])

    list_of_items = []
    list_of_items.extend([belt_list, necklace_list, helm_list, cloak_list,
                          armor_list, gloves_list, pants_list, dagger_list,
                          sword_list, shoes_list, ring_list, inv_list, bow_list])

    def draw_items_in_inventory(surface, item_list, Xmod, Ymod):
        item_list = item_list
        Xmod = Xmod
        Ymod = Ymod
        item_col = 0
        item_row = 0
        for i, j in enumerate(item_list):
            j.draw(surface, TILE_SIZE * Xmod + TILE_SIZE * item_col, TILE_SIZE * Ymod + TILE_SIZE * item_row)
            item_col += 1
            if item_col == 1:
                item_row += 1
                item_col = 0

    # -----------------------------------Inventory/Skills-----------------------------------
    inventory_button = button.ToggleButton(display, 360, 330, inventory_icon, 40, 40, 0, True,'Inventory and Techniques')
    troops_button = button.ToggleButton(display, 1190, 330, troops_icon, 50, 50, 0, True,'Troops')
    inv_up = button.ScrollButton(1220, 450, inv_arrow_up, 30, 40, 0, True, 'Up')
    inv_down = button.ScrollButton(1220, 530, inv_arrow_down, 30, 40, 0, True, 'Down')
    inv_return = button.ScrollButton(1224, 490, inv_return, 22, 40, 0, True, 'Return')
    sell_item = button.ToggleButton(display,1223, 594, sell_icon, 30, 40, 0, False, 'Sell')

    # --------------------------------------------------------------------------------------
    click_counter = 0
    inventory_active = True
    skills_active = False
    troops_active = False

    # -----------------------------------WorldMap---------------------------------------
    clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.set_num_channels(32)
    pygame.mixer.pre_init(44100, -16, 2, 512)

    play_music('Map')
    global global_map_running
    global_map_running = True

    WINDOW_SIZE = (1280, 720)
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

    display = pygame.Surface((800, 600))

    fullscreen = button.fullscreen
    # not bool(linecache.getline('genericmap.txt',1))

    if fullscreen:
        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

    # pygame.display.set_caption("Vagrant's Lot: World Map") #screen window name

    player_rect = pygame.Rect((screen.get_width() / 2), (screen.get_height() / 2), 50, 50)
    mouse_position = pygame.mouse.get_pos()
    mx, my = pygame.mouse.get_pos()
    player_rect.x, player_rect.y = mouse_position

    GM_normal_icon = pygame.image.load("WorldMap/cursor_final.png").convert_alpha()
    GM_normal_icon = pygame.transform.scale(GM_normal_icon, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.03))))

    GM_select_icon = pygame.image.load("WorldMap/icon_select.png").convert_alpha()
    GM_select_icon = pygame.transform.scale(GM_select_icon, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.03))))

    bag_of_coins = pygame.image.load("WorldMap/bag.png").convert_alpha()
    bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0] * 0.08), (int(WINDOW_SIZE[1] * 0.15))))

    gm_injury = pygame.image.load("WorldMap/healthbar.png").convert_alpha()
    gm_injury = pygame.transform.scale(gm_injury, (int(WINDOW_SIZE[0] * 0.08), (int(WINDOW_SIZE[1] * 0.10))))
    gm_injury = pygame.transform.flip(gm_injury, True, False)

    gm_quest_icon = pygame.image.load("WorldMap/quest_icon.png").convert_alpha()
    gm_quest_icon = pygame.transform.scale(gm_quest_icon, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.04))))
    gm_quest_icon_inactive = pygame.image.load("WorldMap/quest_icon_inactive.png").convert_alpha()
    gm_quest_icon_inactive = pygame.transform.scale(gm_quest_icon_inactive,(int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.04))))

    gm_talk_icon = pygame.image.load("WorldMap/talk_icon.png").convert_alpha()
    gm_talk_icon = pygame.transform.scale(gm_talk_icon, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.04))))

    gm_infosheet = pygame.image.load("WorldMap/gm_scroll.png").convert_alpha()
    gm_infosheet = pygame.transform.scale(gm_infosheet, (int(WINDOW_SIZE[0] * 0.3), (int(WINDOW_SIZE[1] * 0.3))))
    menu_sheet = pygame.image.load("MainMenuRes/scroll.png").convert_alpha()
    menu_sheet = pygame.transform.scale(menu_sheet, (int(WINDOW_SIZE[0] * 0.3), (int(WINDOW_SIZE[1] * 0.3))))

    GM_font_TNR = pygame.font.SysFont('Times New Roman', 18)
    GM_font_ESK = pygame.font.Font('WorldMap/ESKARGOT.ttf', 36)
    GM_font_Lore = pygame.font.SysFont('Times New Roman', 16)
    font = pygame.font.SysFont('Times New Roman', 18)
    fontMenu = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
    fontStats = pygame.font.Font('WorldMap/ESKARGOT.ttf', 20)
    fontDescription = pygame.font.SysFont('Times New Roman', 22)
    fontMenuLarge = pygame.font.Font('WorldMap/ESKARGOT.ttf', 48)
    fontMenuCharSheet = pygame.font.Font('WorldMap/ESKARGOT.ttf', 100)

    dice_icon = pygame.image.load("MainMenuRes/dice.png").convert_alpha()
    dice_icon = pygame.transform.scale(dice_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    plus_icon = pygame.image.load("MainMenuRes/plus.png").convert_alpha()
    plus_icon = pygame.transform.scale(plus_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    minus_icon = pygame.image.load("MainMenuRes/minus.png").convert_alpha()
    minus_icon = pygame.transform.scale(minus_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.06))))

    plus_green_icon = pygame.image.load("MainMenuRes/plus_green.png").convert_alpha()
    plus_green_icon = pygame.transform.scale(plus_green_icon, (int(WINDOW_SIZE[0] * 0.015), (int(WINDOW_SIZE[1] * 0.025))))

    chest_icon = pygame.image.load("WorldMap/settlement/chest_icon.png").convert_alpha()
    chest_icon = pygame.transform.scale(chest_icon, (int(WINDOW_SIZE[0] * 0.015), (int(WINDOW_SIZE[1] * 0.025))))

    city_icon = pygame.image.load("WorldMap/settlement/city_icon.png").convert_alpha()
    city_icon = pygame.transform.scale(city_icon, (int(WINDOW_SIZE[0] * 0.01), (int(WINDOW_SIZE[1] * 0.02))))

    town_icon = pygame.image.load("WorldMap/settlement/town_icon.png").convert_alpha()
    town_icon = pygame.transform.scale(town_icon, (int(WINDOW_SIZE[0] * 0.01), (int(WINDOW_SIZE[1] * 0.02))))

    gm_open_chest = pygame.image.load("WorldMap/settlement/chest_open.png").convert_alpha()
    gm_open_chest = pygame.transform.scale(gm_open_chest, (int(WINDOW_SIZE[0] * 0.2), (int(WINDOW_SIZE[1] * 0.3))))

# -------------------------------------QuestList------------------------------------------
    toggle_char_sheet = False
    toggle_journal = False
    global toggle_game_menu
    toggle_game_menu = False
    pyautogui.moveTo(750, 400)
    global block_movement
    block_movement = False
    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False
    movement_modifier = 0
    inv_modifier = 0
    scroll = [0, 0]
    GM_player_rect = pygame.Rect((display.get_width() / 2), (display.get_height() / 2), 50, 50)
    encounter_timer = 0
    encounter = False
    throw_dice = False
    escape_dice = True

    healing_timer = 0
    income_timer = 0

    map_borders = True
    westrad_borders = map_borders
    kharfajian_borders = False
    charlatan_borders = False
    free_islands_borders = False
    nomad_valley_borders = False
    solomir_borders = False
    eastgard_borders = False

    #----------------------------------------playsound-------------------------------------
    global playSoundScroll
    playSoundScroll = True
    global playSoundScroll_counter
    playSoundScroll_counter = 0

    global whileSound
    whileSound = True
    global whileSound_counter
    whileSound_counter = 0

    global trapSound
    trapSound = True
    global trapCounter
    trapCounter = 0

#------------------------------------------------------------------------------
    quest_box = []
    mines_box = []
    chest_box = []
    town_box = []
#------------------------------------------------------------------------------
    def gm_draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        display.blit(img, (x, y))

    def gm_draw_bag():
        display.blit(bag_of_coins, (-20, display.get_height() * 0.84))
        gm_draw_text(f'{button.wealth}', GM_font_ESK, (255, 225, 100), bag_of_coins.get_width() - 30,
                     display.get_height() * 0.92)

#---------------------------------------CollisionMask -----------------------------------
    world_map = pygame.image.load("WorldMap/Map.png").convert_alpha()
    world_map = pygame.transform.scale(world_map, (int(WINDOW_SIZE[0]), (int(WINDOW_SIZE[1]))))
    #map_border = pygame.image.load("WorldMap/map_mask.png").convert_alpha()
    #map_border = pygame.transform.scale(map_border, (int(WINDOW_SIZE[0]), (int(WINDOW_SIZE[1]))))
    gm_party_icon = pygame.image.load("WorldMap/party_icon.png").convert_alpha()
    gm_party_icon = pygame.transform.scale(gm_party_icon, (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.04))))
#------------------------------------------------------------------------------------------
    party_movement = [0, 0]
    class PlayerParty:
        def __init__(self, posX, posY):
            self.img = gm_party_icon
            self.rect = self.img.get_rect()
            self.rect.w,self.rect.h = 1,1
            self.rect.x = posX
            self.rect.y = posY
            self.speed = 0.25

        def draw(self):
            self.view = pygame.draw.circle(display, (255,255,255), (self.rect.centerx, self.rect.centery),30,1)
            display.blit(self.img, (self.rect.x-12, self.rect.y-14))

        def collision_test(self,tiles):
            hit_list = []
            for tile in tiles:
                if self.rect.colliderect(tile):
                    hit_list.append(tile)
            return hit_list

        def move(self, tiles):
            collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
            self.rect.x += party_movement[0]
            hit_list = self.collision_test(tiles)
            for tile in hit_list:
                if moving_right and self.rect.colliderect(tile):
                    party_movement[0] -= 5
                    self.speed = 0
                    collision_types['right'] = True
                elif moving_left and self.rect.colliderect(tile):
                    party_movement[0] += 5
                    self.speed = 0
                    collision_types['left'] = True
            # ---------------------------YCollision-----------------------------
            self.rect.y += party_movement[1]
            hit_list = self.collision_test(tiles)
            for tile in hit_list:
                if moving_up and self.rect.colliderect(tile):
                    party_movement[1] += 5
                    self.speed = 0
                    collision_types['bottom'] = True
                elif moving_down and self.rect.colliderect(tile):
                    party_movement[1] -= 5
                    self.speed = 0
                    collision_types['top'] = True
            return self.rect, collision_types

#----------------------------------------------------------------------------------
    def gm_draw_map():
        display.blit(world_map, (-100 - scroll[0], 0 - scroll[1]))
#-------------------------------------WhileSounds-----------------------------------
    def play_while_sound (sound):
        global whileSound
        global whileSound_counter
        if whileSound == True:
            sound.play()
            whileSound = False
        elif whileSound_counter == 10:
            whileSound_counter = 0

#------------------------------------Traps----------------------------------------
    def activate_trap(trapsound, count, minDamage, maxDamage):
        global trapSound
        global trapCounter
        if trapSound == True:
            trapsound.play()
            button.PartyHealth -= random.randint(minDamage, maxDamage)
            button.PartyStartHealth = button.PartyHealth
            trapSound = False
        elif trapCounter == count:
            trapCounter = 0

    def initiate_encounter (encounter, mapsize):
        with open('BattleScreen/encounter_conditions.txt', 'w') as out:
            out.writelines([str(encounter) + "\n", str(mapsize) + "\n"])
        battle_module()

 #----------------------------------------WorldMapMessage------------------------------------
    class MessageText(pygame.sprite.Sprite):
        def __init__(self, x, y, damage, color):
            pygame.sprite.Sprite.__init__(self)
            self.image = fontDescription.render(damage, True, color)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.counter = 0

        def update(self):
            #self.rect.y -= 1
            self.counter += 1
            if self.counter > 1:
                self.kill()

    message_text_group = pygame.sprite.Group()

    # ---------------------------------------Encounters--------------------------------------
    def show_message(message, font, col, Xtext, Ytext):
        display.blit(gm_infosheet, (display.get_width() * 0.28, display.get_height() * 0.26))
        img = font.render(message, True, col)
        display.blit(img, (Xtext, Ytext))

    class Encounter():
        def __init__(self, type, probability, x, y, difficulty):
            self.type = type
            self.probability = probability
            self.difficulty = difficulty
            self.x = x
            self.y = y

        def encounter_scroll(self):
            display.blit(gm_infosheet, (display.get_width() * 0.28, display.get_height() * 0.26))

        def encounter_text(self, text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            display.blit(img, (x, y))

    road_ambush = Encounter('Highwaymen', 0, 365, 290, 10)
    wolves_encounter = Encounter('Wolves', 1, 390, 290, 5)

    encounter_box = []
    encounter_box.extend((road_ambush, wolves_encounter))

    # -----------------------------------QuestTexts-----------------------------------
    old_ways_path = open('WorldMap/quest/old_ways.txt', 'r')
    old_ways_lore = old_ways_path.read()
    old_ways_path.close()
    # -----------------------------------QuestImg-----------------------------------
    path, dirs, quest= next(os.walk("MainMenuRes/inventory/gold"))
    quest_count = len(quest)
    QUEST_TYPES = quest_count
    quest_img = []
    for x in range(QUEST_TYPES):
        img = pygame.image.load(f'WorldMap/quest/quest_img/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * 0.2), (int(WINDOW_SIZE[1] * 0.44))))
        quest_img.append(img)
    #-----------------------------------QuestJournal-------------------------------
    gm_quest_book = pygame.image.load("WorldMap/quest_book.png").convert_alpha()
    gm_quest_book = pygame.transform.scale(gm_quest_book, (int(WINDOW_SIZE[0] * 0.3), (int(WINDOW_SIZE[1] * 0.4))))

    log_entries = []
    class Journal():
        def __init__(self, x, y, chapter):
            self.x = x
            self.y = y
            self.max_chapter = 0
            self.cur_chapter = chapter

        def log_scroll(self):
            display.blit(gm_quest_book, (display.get_width() * 0.3, display.get_height() * 0.3))
            img = fontStats.render(f'Chapter {self.cur_chapter}', True, (61, 38, 34))
            display.blit(img, (WINDOW_SIZE[0]//4.2, WINDOW_SIZE[1]//3.8))

        # def log_entry(self, text, font, text_col, x, y):
        #     img = font.render(text, True, text_col)
        #     display.blit(img, (x, y))
        #
        # def log_text(self, text, font, text_col, x, y):
        #     img = font.render(text, True, text_col)
        #     display.blit(img, (x, y))

        def initiate(self):
            self.log_scroll()
            # self.log_entry()
            # self.log_text()

    journal = Journal(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2, 1)
    # -----------------------------------Quest-------------------------------------
    class Quest(pygame.sprite.Sprite):
        def __init__(self, x, y, img, story_image, story_text, status):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.clicked = False
            self.story_text = story_text
            self.story_image = story_image
            self.status = status

        def draw_story(self, lore, xmodifier, ymodifier):
            msg_list = []
            line_spacing_count = 0
            if self.rect.collidepoint(mouse_position) and encounter == False and self.rect.colliderect(player_party.rect):
                display.blit(self.story_image, (self.rect.x - 120, self.rect.y + 10))
                gm_draw_text(self.story_text, GM_font_TNR, (255, 225, 100), self.rect.x - 100, self.rect.y + 20)
                for line in lore.split('\n'):
                    msg = GM_font_Lore.render(line, True, '#2c2d47')
                    msg_list.append(msg)
                    line_spacing_count += 20
                    display.blit(msg, (self.rect.x - xmodifier, self.rect.y + ymodifier + (line_spacing_count * 1)))
                play_while_sound(scroll_sound)

        def hide_quest(self):
            if self.rect.collidepoint(mouse_position) and self.status == 'unlocked' and self.rect.colliderect(player_party.rect):
                for count, i in enumerate(quest_box):
                    if all(i.status) != 'invisible':
                        i.status = 'invisible'
                self.status = 'unlocked'
                for count, k in enumerate(mines_box):
                    if all(k.status) != 'invisible':
                      k.status = 'invisible'
                for count, j in enumerate(chest_box):
                    if all(j.status) != 'invisible':
                        j.status = 'invisible'
                for count, l in enumerate(town_box):
                    if all(l.status) != 'invisible':
                        l.status = 'invisible'

        def quest_unavailable(self):
            # if self.rect.collidepoint(mouse_position):
            self.image = gm_quest_icon_inactive
            display.blit(self.image, (self.rect.x, self.rect.y))
            # self.status = 'locked'
            # display.blit(gm_quest_icon_inactive, self.rect.center)
            # gm_draw_text(self.story_text, fontDescription, '#2c2d47', self.rect.x, self.rect.y)

        def initiate(self):
            activate = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_position) and self.rect.colliderect(player_party.rect) and encounter == False:
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        activate = True
                        self.clicked = True
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                    return activate
#------------------------------------------------------------------------------------------
    path, dirs, scr_mines = next(os.walk("WorldMap/mines/scroll_img"))
    scr_mines_count = len(scr_mines)
    SCR_MINES_TYPES = scr_mines_count
    scr_mines_img = []
    for x in range(SCR_MINES_TYPES):
        img = pygame.image.load(f'WorldMap/mines/scroll_img/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * 0.1), (int(WINDOW_SIZE[1] * 0.2))))
        scr_mines_img.append(img)

    path, dirs, mines = next(os.walk("WorldMap/mines/small_img"))
    mines_count = len(mines)
    MINES_TYPES = mines_count
    mines_img = []
    for x in range(MINES_TYPES):
        img = pygame.image.load(f'WorldMap/mines/small_img/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * 0.02), (int(WINDOW_SIZE[1] * 0.04))))
        mines_img.append(img)

    white_flag = pygame.image.load("WorldMap/mines/neutral_flag.png").convert_alpha()
    white_flag = pygame.transform.scale(white_flag, (int(WINDOW_SIZE[0] * 0.01), (int(WINDOW_SIZE[1] * 0.04))))
    red_flag = pygame.image.load("WorldMap/mines/red_flag.png").convert_alpha()
    red_flag = pygame.transform.scale(red_flag, (int(WINDOW_SIZE[0] * 0.01), (int(WINDOW_SIZE[1] * 0.04))))

    #--------------------------------------Mines-------------------------------------------------
    class Mine(pygame.sprite.Sprite):
        def __init__(self, surface,x, y, img, status,value,owner):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.clicked = False
            self.status = status
            self.value = value
            self.surface = surface
            self.owner = owner
            if toggle_char_sheet == False:
                if self.status != 'invisible':
                    if self.owner != 'player':
                        surface.blit(white_flag, (self.rect.x-10, self.rect.y-10))
                    else:
                        surface.blit(red_flag, (self.rect.x-10, self.rect.y-10))

        def mine_text(self, surface, scroll, text, font, text_col, x, y):
            if self.status != 'invisible':
                if self.owner != 'player':
                    surface.blit(scroll,  (self.rect.x-55, self.rect.y - 130))
                    img = font.render(text, True, text_col)
                    surface.blit(img, (x, y))

        def hide_mine(self):
            if self.rect.collidepoint(mouse_position) and self.status != 'invisible' and self.rect.colliderect(player_party.rect):
                for count, i in enumerate(mines_box):
                    if all(i.status) != 'invisible':
                        i.status = 'invisible'
                self.status = 'visible'
                for count, k in enumerate(quest_box):
                    if all(k.status) != 'invisible':
                        k.status = 'invisible'
                for count, j in enumerate(chest_box):
                    if all(j.status) != 'invisible':
                        j.status = 'invisible'
                for count, l in enumerate(town_box):
                    if all(l.status) != 'invisible':
                        l.status = 'invisible'

        def initiate(self):
            activate = False
            if self.rect.collidepoint(mouse_position) and self.rect.colliderect(player_party.rect) \
                    and encounter == False and self.owner != 'player' and self.status != 'invisible' and toggle_char_sheet == False:
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        activate = True
                        self.clicked = True
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                    return activate

#-----------------------------------------------------------------------------------
    def mine_encounter (surface, mine, mine_img, mine_text, textX, textY):
        if mine.rect.collidepoint(mouse_position) and mine.rect.colliderect(player_party.rect):
            if mine.owner != 'player' and mine.status != 'invisible' and toggle_char_sheet == False:
                mine.mine_text(surface, mine_img,mine_text, fontDescription, (0, 0, 0), (mine.rect.x - textX), (mine.rect.y-textY))
                play_while_sound(scroll_sound)

#------------------------------------------------------------------------------------------
    path, dirs, gold= next(os.walk("MainMenuRes/inventory/gold"))
    gold_count = len(gold)
    GOLD_TYPES = gold_count
    gold_img = []
    for x in range(GOLD_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/gold/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(TILE_SIZE), int(TILE_SIZE)))
        gold_img.append(img)

    #--------------------------------------Chest------------------------------------------
    items_in_chest = []
    class Chest(pygame.sprite.Sprite):
        def __init__(self, surface,x, y, img, investigation,difficulty, trap, status):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.clicked = False
            self.difficulty = difficulty
            self.investigation = investigation
            self.surface = surface
            self.status = status
            self.trap = trap
            self.toggled = False
            self.trap_active = False
            self.trap_counter = 0

        def chest_text(self, surface, text, font, text_col, x, y):
            if self.status != 'invisible':
                    img = font.render(text, True, text_col)
                    surface.blit(img, (x, y))

        def open_chest(self, surface, scroll, x,y):
            if self.status != 'invisible' and investigation >= self.investigation:
                surface.blit(scroll,(x, y))

        def hide_chest(self):
            if self.rect.colliderect(player_party.rect) and encounter == False \
               and self.status != 'invisible' and toggle_char_sheet == False:
                for count, i in enumerate(chest_box):
                   if all(i.status) != 'invisible':
                       i.status = 'invisible'
                self.status = 'visible'
                for count, j in enumerate(mines_box):
                    if all(j.status) != 'invisible':
                        j.status = 'invisible'
                for count, k in enumerate(quest_box):
                    if all(k.status) != 'invisible':
                        k.status = 'invisible'
                for count, l in enumerate(town_box):
                    if all(l.status) != 'invisible':
                        l.status = 'invisible'

        def initiate(self, item0,item1, item2,item3,item4,item5,item6,item7):
            if self.rect.colliderect(player_party.rect) and encounter == False \
                and self.status != 'invisible' and toggle_char_sheet == False \
                and investigation >= self.investigation:
                items_in_chest.extend([item0,item1,item2,item3,item4,item5,item6,item7])
                if lockpicking >= self.difficulty:
                    if self.trap_active == False and traps < self.trap:
                        self.trap_active = True
                        activate_trap(snap_trap_sound,100,5,10)
                        message_text = MessageText(player_party.rect.centerx, player_party.rect.centery-20,
                                                   f'Trap! {self.trap}',(255,255,255))
                        message_text_group.add(message_text) #"#fdc253"
                        message_text_group.update()
                        message_text_group.draw(display)
                    self.toggled = True
                    if self.toggled == True:
                       self.open_chest(display, gm_open_chest,TILE_SIZE*4.5, TILE_SIZE*2)
                       self.status = 'invisible'
                       for count, j in enumerate(mines_box):
                           if all(j.status) != 'invisible':
                               j.status = 'invisible'
                       for count, k in enumerate(quest_box):
                            if all(k.status) != 'invisible':
                                k.status = 'invisible'
                       for count, l in enumerate(town_box):
                            if all(l.status) != 'invisible':
                                l.status = 'invisible'
                       play_while_sound(chest_open_sound)
                elif lockpicking < self.difficulty:
                      play_while_sound(locked_sound)
                      message_text = MessageText(player_party.rect.centerx, player_party.rect.centery-20,
                                                 f'The chest is locked! Difficulty: {self.difficulty} || Trap: {self.trap}',(255,255,255))
                      message_text_group.add(message_text)
                      message_text_group.update()
                      message_text_group.draw(display)
    #----------------------------------------StoredItems--------------------------------------
    steal_item = button.ToggleButton(display,500, 370, steal_icon, 20, 30, 0, False, 'Steal')
    #-----------------------------------------------------------------------------------------
    npc_talk = pygame.image.load("WorldMap/talk_icon.png").convert_alpha()
    npc_talk = pygame.transform.scale(npc_talk, (int(WINDOW_SIZE[0] * 0.01), (int(WINDOW_SIZE[1] * 0.02))))

    path, dirs, trader_potions = next(os.walk("MainMenuRes/inventory/trader_potions"))
    trader_potions_count = len(trader_potions)
    TRADER_POTION_TYPES = trader_potions_count
    trader_potions_img = []
    for x in range(TRADER_POTION_TYPES):
        img = pygame.image.load(f'MainMenuRes/inventory/trader_potions/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(TILE_SIZE), (int(TILE_SIZE))))
        trader_potions_img.append(img)
#-------------------------------------------------Unlocked---------------------------------
    potions_dict = {}
    potions_dict.update({"0":False,"1":False,"2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8.png":False,
                         "9":False,"10":False,"11":False,"12":False,"13":False,"14":False,"15":False,"16":False,"17":False,
                         "18":False,"19":False,"20":False,"21":False,"22":False,"23":False,"24":False,"25":False,"26":False})

    troops_dict = {}
    troops_dict.update({"0":False,"1":False,"2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8.png":False,"9":False,
                        "10":False,"11":False,"12":False,"13":False,"14":False,"15":False,"16":False,"17":False,"18":False,
                        "19":False,"20":False,"21":False,"22":False,"23":False,"24":False,"25":False,"26":False,"27":False,
                        "28":False,"29":False,"30":False,"31":False,"32":False,"33":False,"34":False,"35":False,"36":False})

    #-----------------------------------------------------------------------------------------
    class StoredItem():
        def __init__(self, surface, list_image, n,list, item, in_chest, available,info,value,type):
            self.list = list #which inventory lists its added
            self.item = item #what is the item (Item)
            self.type = type
            self.info = info
            self.costmod = round(random.uniform(1,3), 2)
            self.value = int(value*self.costmod)
            #self.x = x
            #self.y = y
            self.scale = 0.75
            self.n = n
            self.list_image = list_image[n] #item list image (gloves_list_img[0])
            self.width = list_image[n].get_width()
            self.height = list_image[n].get_height()
            self.rect = list_image[n].get_rect()
            self.rect.x = int(TILE_SIZE*0.8)
            self.rect.y = int(TILE_SIZE*0.8)
            self.rect.width = int(TILE_SIZE*0.8)
            self.rect.height = int(TILE_SIZE*0.8)
            self.list_image = pygame.transform.scale(list_image[n], (int(self.width * self.scale), int(self.height * self.scale)))
            #self.rect.topleft = ()
            self.surface = surface
            self.taken = False
            self.clicked = False
            self.in_chest = in_chest
            self.available = available
            self.caught = False
            self.countdown = 0

        def get_item(self, list,item):
            self.list = list
            self.item = item
            if self.item != None :
               list.extend([item])
            if self.item != None and self.type != 'item' and self.type != 'potion':
                    troops_dict.update({self.n:self.type})
            take_item_sound.play()

        def buy_item(self, list,item):
            self.list = list
            self.item = item
            if self.item != None:
               list.extend([item])
            if self.item != None and self.type != 'item' and self.type != 'potion':
                   troops_dict.update({self.n:self.type})
                   coins_sound.play()
            if button.start_wealth >= self.value:
                button.wealth -= self.value
                button.start_wealth = button.wealth

        def get_potion(self, list,item):
            self.item = item
            self.list = list
            if self.item != None:
                list.update({self.n:item})
            take_item_sound.play()

        def buy_potion(self, list,item):
            self.item = item
            self.list = list
            if self.item != None:
               list.update({self.n:item})
            coins_sound.play()
            if button.start_wealth >= self.value:
                button.wealth -= self.value
                button.start_wealth = button.wealth

        def start_quest(self):
            if self.type == 'caravan':
                caravan_sound.play()
                initiate_encounter(1,1)
                party_movement[0],party_movement[1] = (self.list, self.item)

        def draw_chest_item (self,surface,x,y,Xmod,Ymod):
            self.Xmod = Xmod
            self.Ymod =Ymod
            list_image = self.list_image
            if self.taken == False and self.available == True:
                surface.blit(list_image,(x + Xmod,y + Ymod))
                self.rect.topleft = (x + Xmod,y + Ymod)
                if self.item == 'npc':
                   surface.blit(npc_talk,(x+5 + Xmod,y+5 + Ymod))

        def stored_item_info(self,surface,font,text,value,col,x,y):
            if self.rect.collidepoint(mouse_position):
                if self.taken == False and self.in_chest == True:
                    img = font.render(text, True, col)
                    surface.blit(img,(x,y))
                    price = font.render(f'Cost: {value}', True, col)
                    surface.blit(price,(x,y+20))
                    if steal_item.toggled == True:
                        if self.type == 'potion' or self.type == 'item':
                            steal_chance = int(thievery//2+(stealth+deception)//4 + luck) - self.value//50
                            steal_try = font.render(f'Chance: {steal_chance}%', True, col)
                            surface.blit(steal_try,(x+200,y+20))

        def chest_event_handler(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.taken == False and self.available == True:
                    if event.button == 1:
                        if self.rect.collidepoint(event.pos):
                            self.taken = True
                            self.in_chest = False
                            if self.type == 'gold':
                                button.wealth += self.value
                                button.start_wealth = button.wealth
                                coins_sound.play()
                            else:
                                self.get_item(self.list,self.item)

        def quest_npc_event_handler(self):
            action = False
            pos = pygame.mouse.get_pos()
            if self.available == True:
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        time.sleep(0.1)
                        action = True
                        self.clicked = True
                        self.start_quest()
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                return action

        def store_event_handler(self, event):
            if steal_item.toggled==False and self.caught == False:
                if self.taken == False and self.available == True:
                    if button.start_wealth >= self.value:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if self.rect.collidepoint(event.pos):
                                    self.taken = True
                                    self.in_chest = False
                                    self.clicked = True
                                    if self.type == 'potion':
                                        self.buy_potion(self.list,self.item)
                                    elif self.type != 'potion' and self.item != 'npc':
                                        self.buy_item(self.list,self.item)

            if steal_item.toggled==True:
                if self.taken == False and self.available == True:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            steal_dice= random.randint(0,100)
                            steal_chance = int(thievery//2+(stealth+deception)//4 + luck) - self.value//100
                            if self.rect.collidepoint(event.pos) and self.type != 1:
                                if steal_chance >= steal_dice:
                                    self.taken = True
                                    self.in_chest = False
                                    if self.type == 'potion':
                                        self.get_potion(self.list,self.item)
                                    elif self.type == 'item':
                                        self.get_item(self.list,self.item)
                                    self.caught = False
                                    steal_item.toggled = False
                                    print(steal_dice)
                                    print(steal_chance)
                                else:
                                    self.caught = True
                                    if self.caught == True and self.type != 1 and self.value != 0:
                                        initiate_encounter(0,0)
                                    steal_item.toggled = False
                                    self.countdown +=1
                                    if self.countdown >= 100:
                                       self.caught = False
                                       self.countdown = 0
#---------------------------------------------------------------------------------------------
    #----------mercenaries---------
    hire_dunstan = StoredItem(display,units_img,0,troops_melee,Dunstan,True, False,'Your brother Dunstan',0,1)
    hire_bartelago = StoredItem(display,units_img,5,troops_melee,Bartelago,True, False,'Mighty warrior Bartelago',0,1)
    hire_anselm = StoredItem(display,units_img,6,troops_melee,Anselm,True, False,'Brother Anselm',0,1)
    hire_regina = StoredItem(display,units_img,7,troops_ranged,Regina,True, False,'Ranger Regina',0,1)
    hire_alba = StoredItem(display,units_img,9,troops_ranged,Alba,True, False,'Coven witch Alba',0,1)
    hire_severin = StoredItem(display,units_img,8,troops_ranged,Severin,True, False,'Battle mage Severin',0,1)

    hire_light_archers = StoredItem(display,units_img,2,troops_ranged,Light_Archers,True, False,'A regiment of light archers',2000,1)
    hire_chevaliers = StoredItem(display,units_img,3,troops_cavalry,Chevaliers,True, False,'Armored assault cavalry',4000,1)
    hire_light_infantry = StoredItem(display,units_img,1,troops_melee,Light_Infantry,True, False,'A regiment of light infantry led by a captain',2000,1)
    hire_scouts = StoredItem(display,units_img,4,troops_support,Scouts,True, False,'A group of trained scouts',1200,1)

    #----------------------------------miniquests-------------------------------------
    qst_0 = StoredItem(display,gold_img,4,60,45,True, False,'Protect caravan to Bellenau for 250 gold',0,'caravan')

#-------------potions----------
    ptn_0 = StoredItem(display,trader_potions_img,0,potions_dict,True,True, False,'Health potion',500,'potion')
    ptn_1 = StoredItem(display,trader_potions_img,1,potions_dict,True,True, False,'Defence potion',1400,'potion')
    ptn_2 = StoredItem(display,trader_potions_img,2,potions_dict,True,True, False,'Acid',750,'potion')
    ptn_3 = StoredItem(display,trader_potions_img,3,potions_dict,True,True, False,'Antidote',300,'potion')
    ptn_4 = StoredItem(display,trader_potions_img,4,potions_dict,True,True, False,'Berserk potion',1200,'potion')
    ptn_5 = StoredItem(display,trader_potions_img,5,potions_dict,True,True, False,'Cleansing potion',400,'potion')

    ptn_6 = StoredItem(display,trader_potions_img,6,potions_dict,True,True, False,'Frost shield',400,'potion')
    ptn_7 = StoredItem(display,trader_potions_img,7,potions_dict,True,True, False,'Fire shield',400,'potion')
    ptn_8 = StoredItem(display,trader_potions_img,8,potions_dict,True,True, False,'Energy shield',400,'potion')
    ptn_9 = StoredItem(display,trader_potions_img,9,potions_dict,True,True, False,'Moon potion',400,'potion')
    ptn_10 = StoredItem(display,trader_potions_img,10,potions_dict,True,True, False,'Rejuvenation',600,'potion')
    ptn_11 = StoredItem(display,trader_potions_img,11,potions_dict,True,True, False,'Poison',900,'potion')

    ptn_12 = StoredItem(display,trader_potions_img,12,potions_dict,True,True, False,'Deathkiss potion',500,'potion')
    ptn_13 = StoredItem(display,trader_potions_img,13,potions_dict,True,True, False,'Dark Cloud potion',1200,'potion')
    ptn_14 = StoredItem(display,trader_potions_img,14,potions_dict,True,True, False,'Celerity potion',850,'potion')
    ptn_15 = StoredItem(display,trader_potions_img,15,potions_dict,True,True, False,'Ironskin potion',500,'potion')
    ptn_16 = StoredItem(display,trader_potions_img,16,potions_dict,True,True, False,'Liquid frost',1100,'potion')
    ptn_17 = StoredItem(display,trader_potions_img,17,potions_dict,True,True, False,'Ritual potion',2400,'potion')

    ptn_18 = StoredItem(display,trader_potions_img,18,potions_dict,True,True, False,'Liquid fire',1100,'potion')
    ptn_19 = StoredItem(display,trader_potions_img,19,potions_dict,True,True, False,'Dream potion',1800,'potion')
    ptn_20 = StoredItem(display,trader_potions_img,20,potions_dict,True,True, False,'Vigor potion',250,'potion')
    ptn_21 = StoredItem(display,trader_potions_img,21,potions_dict,True,True, False,'Energy shard',1100,'potion')
    ptn_22 = StoredItem(display,trader_potions_img,22,potions_dict,True,True, False,'Fire grenade',2800,'potion')
    ptn_23 = StoredItem(display,trader_potions_img,23,potions_dict,True,True, False,'Shrapnel grenade',3000,'potion')
    ptn_24 = StoredItem(display,trader_potions_img,24,potions_dict,True,True, False,'Earth shard',2400,'potion')
    ptn_25 = StoredItem(display,trader_potions_img,25,potions_dict,True,True, False,'Concentration potion',950,'potion')

#--------------gold-----------
    gld_0 = StoredItem(display,gold_img,0,None,None,True, False,'gold',random.randint(100,250),'gold')
    gld_1 = StoredItem(display,gold_img,1,None,None,True, False,'gold',random.randint(250,500),'gold')
    gld_2 = StoredItem(display,gold_img,2,None,None,True, False,'gold',random.randint(500,1000),'gold')
    gld_3 = StoredItem(display,gold_img,3,None,None,True, False,'gold',random.randint(1000,2500),'gold')

    #-------------trinkets-----------
    itm_0 = StoredItem(display,trinkets_list_img,7,inv_list,seafarer_charm,True, False,seafarer_charm.descr,seafarer_charm.value,'item')
    itm_1 = StoredItem(display,trinkets_list_img,45,inv_list,crowbar,True, False,crowbar.descr,crowbar.value,'item')
    itm_2 = StoredItem(display,trinkets_list_img,47,inv_list,lockmaster_tools,True, False,lockmaster_tools.descr,lockmaster_tools.value,'item')
    itm_3 = StoredItem(display,trinkets_list_img,46,inv_list,alchemist_kit,True, False,alchemist_kit.descr,alchemist_kit.value,'item')

    #-------------cloak-----------
    clk_0 = StoredItem(display,cloak_list_img,0,cloak_list,travel_cloak,True, False,travel_cloak.descr,travel_cloak.value,'item')
    clk_1 = StoredItem(display,cloak_list_img,1,cloak_list,night_cloak,True, False,night_cloak.descr,night_cloak.value,'item')
    clk_2 = StoredItem(display,cloak_list_img,2,cloak_list,full_cloak,True, False,full_cloak.descr,full_cloak.value,'item')
    clk_3 = StoredItem(display,cloak_list_img,3,cloak_list,ranger_cloak,True, False,ranger_cloak.descr,ranger_cloak.value,'item')
    clk_4 = StoredItem(display,cloak_list_img,4,cloak_list,jester_cloak,True, False,jester_cloak.descr,jester_cloak.value,'item')
    clk_5 = StoredItem(display,cloak_list_img,5,cloak_list,war_cloak,True, False,war_cloak.descr,war_cloak.value,'item')
    clk_6 = StoredItem(display,cloak_list_img,6,cloak_list,noble_cloak,True, False,noble_cloak.descr,noble_cloak.value,'item')
    clk_7 = StoredItem(display,cloak_list_img,7,cloak_list,warlock_cloak,True, False,warlock_cloak.descr,warlock_cloak.value,'item')

#------------------gloves-----------
    glv_0 = StoredItem(display,gloves_list_img,0,gloves_list,travel_gloves,True, False,travel_gloves.descr,travel_gloves.value,'item')
    glv_1 = StoredItem(display,gloves_list_img,1,gloves_list,hand_wraps,True, False,hand_wraps.descr,hand_wraps.value,'item')
    glv_2 = StoredItem(display,gloves_list_img,2,gloves_list,light_leather_gloves,True, False,light_leather_gloves.descr,light_leather_gloves.value,'item')
    glv_3 = StoredItem(display,gloves_list_img,3,gloves_list,light_chain_gloves,True, False,light_chain_gloves.descr,light_chain_gloves.value,'item')
    glv_4 = StoredItem(display,gloves_list_img,4,gloves_list,light_plate_gloves,True, False,light_plate_gloves.descr,light_plate_gloves.value,'item')
    glv_5 = StoredItem(display,gloves_list_img,5,gloves_list,leather_gloves,True, False,leather_gloves.descr,leather_gloves.value,'item')
    glv_6 = StoredItem(display,gloves_list_img,6,gloves_list,reinforced_gloves,True, False,reinforced_gloves.descr,reinforced_gloves.value,'item')
    glv_7 = StoredItem(display,gloves_list_img,7,gloves_list,ranger_gloves,True, False,ranger_gloves.descr,ranger_gloves.value,'item')
    glv_8 = StoredItem(display,gloves_list_img,8,gloves_list,thieves_gloves,True, False,thieves_gloves.descr,thieves_gloves.value,'item')
    glv_9 = StoredItem(display,gloves_list_img,9,gloves_list,plate_gloves,True, False,plate_gloves.descr,plate_gloves.value,'item')
    glv_10 = StoredItem(display,gloves_list_img,10,gloves_list,tournament_gloves,True, False,tournament_gloves.descr,tournament_gloves.value,'item')
    glv_11 = StoredItem(display,gloves_list_img,11,gloves_list,war_gloves,True, False,war_gloves.descr,war_gloves.value,'item')
    glv_12 = StoredItem(display,gloves_list_img,12,gloves_list,basilisk_gloves,True, False,basilisk_gloves.descr,basilisk_gloves.value,'item')

#------------------bow-----------
    bow_0 = StoredItem(display,bows_list_img,0,bow_list,simple_bow,True, False,simple_bow.descr,simple_bow.value,'item')
    bow_1 = StoredItem(display,bows_list_img,1,bow_list,hunter_bow,True, False,hunter_bow.descr,hunter_bow.value,'item')
    bow_2 = StoredItem(display,bows_list_img,2,bow_list,war_bow,True, False,war_bow.descr,war_bow.value,'item')
    bow_3 = StoredItem(display,bows_list_img,3,bow_list,peasant_bow,True, False,peasant_bow.descr,peasant_bow.value,'item')
    bow_4 = StoredItem(display,bows_list_img,4,bow_list,metal_bow,True, False,metal_bow.descr,metal_bow.value,'item')
    bow_5 = StoredItem(display,bows_list_img,5,bow_list,militia_bow,True, False,militia_bow.descr,militia_bow.value,'item')
    bow_6 = StoredItem(display,bows_list_img,6,bow_list,redwood_bow,True, False,redwood_bow.descr,redwood_bow.value,'item')
    bow_7 = StoredItem(display,bows_list_img,7,bow_list,curved_bow,True, False,curved_bow.descr,curved_bow.value,'item')

    #------------------dagger-----------
    dag_0 = StoredItem(display,dagger_list_img,0,dagger_list,steel_dagger,True, False,steel_dagger.descr,steel_dagger.value,'item')
    dag_1 = StoredItem(display,dagger_list_img,1,dagger_list,thief_dagger,True, False,thief_dagger.descr,thief_dagger.value,'item')
    dag_2 = StoredItem(display,dagger_list_img,2,dagger_list,ranger_dagger,True, False,ranger_dagger.descr,ranger_dagger.value,'item')
    dag_3 = StoredItem(display,dagger_list_img,3,dagger_list,butcher_dagger,True, False,butcher_dagger.descr,butcher_dagger.value,'item')
    dag_4 = StoredItem(display,dagger_list_img,4,dagger_list,common_dagger,True, False,common_dagger.descr,common_dagger.value,'item')
    dag_5 = StoredItem(display,dagger_list_img,5,dagger_list,broad_dagger,True, False,broad_dagger.descr,broad_dagger.value,'item')
    dag_6 = StoredItem(display,dagger_list_img,6,dagger_list,hunt_knife,True, False,hunt_knife.descr,hunt_knife.value,'item')
    dag_7 = StoredItem(display,dagger_list_img,7,dagger_list,war_dagger,True, False,steel_dagger.descr,steel_dagger.value,'item')

    #------------------sword-----------
    srd_0 = StoredItem(display,sword_list_img,0,sword_list,steel_sword,True, False,steel_sword.descr,steel_sword.value,'item')
    srd_1 = StoredItem(display,sword_list_img,1,sword_list,simple_sword,True, False,simple_sword.descr,simple_sword.value,'item')
    srd_2 = StoredItem(display,sword_list_img,2,sword_list,short_sword,True, False,short_sword.descr,short_sword.value,'item')
    srd_3 = StoredItem(display,sword_list_img,3,sword_list,long_sword,True, False,long_sword.descr,long_sword.value,'item')
    srd_4 = StoredItem(display,sword_list_img,4,sword_list,the_sunrise,True, False,the_sunrise.descr,the_sunrise.value,'item')
    srd_5 = StoredItem(display,sword_list_img,5,sword_list,spider_sword,True, False,spider_sword.descr,spider_sword.value,'item')
    srd_6 = StoredItem(display,sword_list_img,6,sword_list,soldier_sword,True, False,soldier_sword.descr,soldier_sword.value,'item')
    srd_7 = StoredItem(display,sword_list_img,7,sword_list,mercenary_sword,True, False,mercenary_sword.descr,mercenary_sword.value,'item')

    #------------------armor-----------
    arm_0 = StoredItem(display,armor_list_img,0,armor_list,travel_clothes,True, False,travel_clothes.descr,travel_clothes.value,'item')
    arm_1 = StoredItem(display,armor_list_img,1,armor_list,robes,True, False,robes.descr,robes.value,'item')
    arm_2 = StoredItem(display,armor_list_img,2,armor_list,light_leather,True, False,light_leather.descr,light_leather.value,'item')
    arm_3 = StoredItem(display,armor_list_img,3,armor_list,light_chain_mail,True, False,light_chain_mail.descr,light_chain_mail.value,'item')
    arm_4 = StoredItem(display,armor_list_img,4,armor_list,light_plate_armor,True, False,light_plate_armor.descr,light_plate_armor.value,'item')
    arm_5 = StoredItem(display,armor_list_img,5,armor_list,leather_armor,True, False,leather_armor.descr,leather_armor.value,'item')
    arm_6 = StoredItem(display,armor_list_img,6,armor_list,reinforced_armor,True, False,reinforced_armor.descr,reinforced_armor.value,'item')
    arm_7 = StoredItem(display,armor_list_img,7,armor_list,nomad_armor,True, False,nomad_armor.descr,nomad_armor.value,'item')

    #----------pants-----------
    pnt_0 = StoredItem(display,pants_list_img,0,pants_list, cloth_pants,True, False,cloth_pants.descr,cloth_pants.value,'item')
    pnt_1 = StoredItem(display,pants_list_img,1,pants_list, monk_pants,True, False,monk_pants.descr,monk_pants.value,'item')
    pnt_2 = StoredItem(display,pants_list_img,2,pants_list, leather_pants,True, False,leather_pants.descr,leather_pants.value,'item')
    pnt_3 = StoredItem(display,pants_list_img,3,pants_list, light_chain_pants,True, False,light_chain_pants.descr,light_chain_pants.value,'item')
    pnt_4 = StoredItem(display,pants_list_img,4,pants_list, reinforced_pants,True, False,reinforced_pants.descr,reinforced_pants.value,'item')
    pnt_5 = StoredItem(display,pants_list_img,5,pants_list, light_plate_pants,True, False,light_plate_pants.descr,light_plate_pants.value,'item')
    pnt_6 = StoredItem(display,pants_list_img,6,pants_list, plate_pants,True, False,plate_pants.descr,plate_pants.value,'item')
    pnt_7 = StoredItem(display,pants_list_img,7,pants_list, heavy_plate_pants,True, False,heavy_plate_pants.descr,heavy_plate_pants.value,'item')

    #-------------shoes-----------
    sho_0 = StoredItem(display,shoes_list_img,0,shoes_list,simple_shoes,True, False,simple_shoes.descr,simple_shoes.value,'item')
    sho_1 = StoredItem(display,shoes_list_img,1,shoes_list,travel_shoes,True, False,travel_shoes.descr,travel_shoes.value,'item')
    sho_2 = StoredItem(display,shoes_list_img,2,shoes_list,light_plate_shoes,True, False,light_plate_shoes.descr,light_plate_shoes.value,'item')
    sho_3 = StoredItem(display,shoes_list_img,3,shoes_list,light_chain_shoes,True, False,light_chain_shoes.descr,light_chain_shoes.value,'item')
    sho_4 = StoredItem(display,shoes_list_img,4,shoes_list,plate_shoes,True, False,plate_shoes.descr,plate_shoes.value,'item')
    sho_5 = StoredItem(display,shoes_list_img,5,shoes_list,common_shoes,True, False,common_shoes.descr,common_shoes.value,'item')
    sho_6 = StoredItem(display,shoes_list_img,6,shoes_list,hunter_shoes,True, False,hunter_shoes.descr,hunter_shoes.value,'item')
    sho_7 = StoredItem(display,shoes_list_img,7,shoes_list,ranger_shoes,True, False,ranger_shoes.descr,ranger_shoes.value,'item')

    #------------helms------------
    hat_0 = StoredItem(display,helm_list_img,0,helm_list,travel_hat,True, False,travel_hat.descr,travel_hat.value,'item')
    hat_1 = StoredItem(display,helm_list_img,1,helm_list,steel_helm,True, False,steel_helm.descr,steel_helm.value,'item')
    hat_2 = StoredItem(display,helm_list_img,2,helm_list,tournament_helm,True, False,tournament_helm.descr,tournament_helm.value,'item')
    hat_3 = StoredItem(display,helm_list_img,3,helm_list,monk_hood,True, False,monk_hood.descr,monk_hood.value,'item')
    hat_4 = StoredItem(display,helm_list_img,4,helm_list,leather_hood,True, False,leather_hood.descr,leather_hood.value,'item')
    hat_5 = StoredItem(display,helm_list_img,5,helm_list,light_chain_helm,True, False,light_chain_helm.descr,light_chain_helm.value,'item')
    hat_6 = StoredItem(display,helm_list_img,6,helm_list,protector_helm,True, False,protector_helm.descr,protector_helm.value,'item')
    hat_7 = StoredItem(display,helm_list_img,7,helm_list,legion_helm,True, False,legion_helm.descr,legion_helm.value,'item')
    hat_8 = StoredItem(display,helm_list_img,8,helm_list,leather_helm,True, False,leather_helm.descr,leather_helm.value,'item')

    #------------------necklace-----------
    nek_0 = StoredItem(display,necklace_list_img,0,necklace_list,traders_luck,True, False,traders_luck.descr,traders_luck.value,'item')
    nek_1 = StoredItem(display,necklace_list_img,1,necklace_list,moon_crest,True, False,moon_crest.descr,moon_crest.value,'item')
    nek_2 = StoredItem(display,necklace_list_img,2,necklace_list,brothers_mark,True, False,brothers_mark.descr,brothers_mark.value,'item')
    nek_3 = StoredItem(display,necklace_list_img,3,necklace_list,the_eye,True, False,the_eye.descr,the_eye.value,'item')
    nek_4 = StoredItem(display,necklace_list_img,4,necklace_list,war_amulet,True, False,war_amulet.descr,war_amulet.value,'item')
    nek_5 = StoredItem(display,necklace_list_img,5,necklace_list,deep_endless,True, False,deep_endless.descr,deep_endless.value,'item')
    nek_6 = StoredItem(display,necklace_list_img,6,necklace_list,warlock_amulet,True, False,warlock_amulet.descr,warlock_amulet.value,'item')
    nek_7 = StoredItem(display,necklace_list_img,7,necklace_list,spider_amulet,True, False,spider_amulet.descr,spider_amulet.value,'item')

    #------------------ring-----------
    rng_0 = StoredItem(display,ring_list_img,0,ring_list,silver_ring,True, False,silver_ring.descr,silver_ring.value,'item')
    rng_1 = StoredItem(display,ring_list_img,1,ring_list,moon_ring,True, False,moon_ring.descr,moon_ring.value,'item')
    rng_2 = StoredItem(display,ring_list_img,2,ring_list,holy_ring,True, False,holy_ring.descr,holy_ring.value,'item')
    rng_3 = StoredItem(display,ring_list_img,3,ring_list,trinity_ring,True, False,trinity_ring.descr,trinity_ring.value,'item')
    rng_4 = StoredItem(display,ring_list_img,4,ring_list,minor_protection_ring,True, False,minor_protection_ring.descr,minor_protection_ring.value,'item')
    rng_5 = StoredItem(display,ring_list_img,5,ring_list,minor_health_ring,True, False,minor_health_ring.descr,minor_health_ring.value,'item')
    rng_6 = StoredItem(display,ring_list_img,6,ring_list,emerald_ring,True, False,emerald_ring.descr,emerald_ring.value,'item')
    rng_7 = StoredItem(display,ring_list_img,7,ring_list,unity_ring,True, False,unity_ring.descr,unity_ring.value,'item')

    #----------------belt--------------
    blt_0 = StoredItem(display,belt_list_img,0,belt_list,travel_belt,True, False,travel_belt.descr,travel_belt.value,'item')
    blt_1 = StoredItem(display,belt_list_img,1,belt_list,hunter_belt,True, False,hunter_belt.descr,hunter_belt.value,'item')
    blt_2 = StoredItem(display,belt_list_img,2,belt_list,war_belt,True, False,war_belt.descr,war_belt.value,'item')
    blt_3 = StoredItem(display,belt_list_img,3,belt_list,double_belt,True, False,double_belt.descr,double_belt.value,'item')
    blt_4 = StoredItem(display,belt_list_img,4,belt_list,noble_belt,True, False,noble_belt.descr,noble_belt.value,'item')
    blt_5 = StoredItem(display,belt_list_img,5,belt_list,night_belt,True, False,night_belt.descr,night_belt.value,'item')
    blt_6 = StoredItem(display,belt_list_img,6,belt_list,day_belt,True, False,day_belt.descr,day_belt.value,'item')
    blt_7 = StoredItem(display,belt_list_img,7,belt_list,warlock_belt,True, False,warlock_belt.descr,warlock_belt.value,'item')
    blt_8 = StoredItem(display,belt_list_img,8,belt_list,duel_belt,True, False,duel_belt.descr,duel_belt.value,'item')
    blt_9 = StoredItem(display,belt_list_img,9,belt_list,druid_belt,True, False,druid_belt.descr,druid_belt.value,'item')

#----------------------------------------------------------------------------------------------------
#------------------------------------------ItemInChest----------------------------------------------
    def remove_stored_items (list):
        for count,i in enumerate(list):
            if i != None:
                if i.in_chest == False:
                   list.remove(i)

#------------------------------------------------------------------------------------------
    path, dirs, traders= next(os.walk("WorldMap/settlement/icons"))
    traders_count = len(traders)
    TRADERS_TYPES = traders_count
    traders_img = []
    for x in range(TRADERS_TYPES):
        img = pygame.image.load(f'WorldMap/settlement/icons/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(TILE_SIZE), int(TILE_SIZE)))
        traders_img.append(img)

    path, dirs, settlement= next(os.walk("WorldMap/settlement/maps"))
    settlement_count = len(settlement)
    SETTLEMENT_TYPES = settlement_count
    settlement_img = []
    for x in range(SETTLEMENT_TYPES):
        img = pygame.image.load(f'WorldMap/settlement/maps/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(TILE_SIZE*4.28), int(TILE_SIZE*4.25)))
        settlement_img.append(img)

    settlement_window = pygame.image.load("WorldMap/settlement/settlement_window.png").convert_alpha()
    settlement_window = pygame.transform.scale(settlement_window, (int(TILE_SIZE*4.75), int(TILE_SIZE*6)))

#--------------------------------------Settlement------------------------------------------
    class Town (pygame.sprite.Sprite):
        def __init__(self, surface,img,x,y,status):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.clicked = False
            self.surface = surface
            self.status = status
            self.entered = False

        def enter_town(self, surface, scroll, scrollX, scrollY,map, mapX,mapY, text, font, text_col,textX,textY):
            if self.status != 'invisible':
                surface.blit(scroll,(scrollX, scrollY))
                surface.blit(map,(mapX, mapY))
                img = font.render(text, True, text_col)
                img2 = font12.render('Steal', True, text_col)
                surface.blit(img, (textX, textY))
                if Thief.status == 1:
                   steal_item.available = True
                if steal_item.toggled == True:
                    pygame.draw.circle(surface, "#000044", (steal_item.rect.centerx, steal_item.rect.centery), 10)
                    pygame.draw.circle(surface, "#eabb47", (steal_item.rect.centerx, steal_item.rect.centery), 8)
                steal_item.draw(surface)
                if steal_item.rect.collidepoint(mouse_position):
                   surface.blit(img2, (3.6*TILE_SIZE,5.6*TILE_SIZE))

        def hide_town(self):
            if self.rect.colliderect(player_party.rect) and encounter == False \
                    and self.status != 'invisible' and toggle_char_sheet == False:
                for count, l in enumerate(town_box):
                    if all(l.status) != 'invisible':
                        l.status = 'invisible'
                self.status = 'visible'
                for count, i in enumerate(chest_box):
                    if all(i.status) != 'invisible':
                        i.status = 'invisible'
                for count, j in enumerate(mines_box):
                    if all(j.status) != 'invisible':
                        j.status = 'invisible'
                for count, k in enumerate(quest_box):
                    if all(k.status) != 'invisible':
                        k.status = 'invisible'
            else:
                party_icon = True

        def initiate(self, surface,scroll, scrollX, scrollY, map, mapX,mapY, text, font, text_col,textX,textY):
            if self.rect.colliderect(player_party.rect) and encounter == False \
                    and self.status != 'invisible' and toggle_char_sheet == False:
                global party_icon
                party_icon = False
                self.entered = True
                if self.entered == True:
                   self.enter_town(surface, scroll, scrollX, scrollY, map, mapX,mapY, text, font, text_col,textX,textY)
                   for count, l in enumerate(town_box):
                       if all(l.status) != 'invisible':
                           l.status = 'invisible'
                   self.status = 'visible'
                   for count, i in enumerate(chest_box):
                       if all(i.status) != 'invisible':
                           i.status = 'invisible'
                   for count, j in enumerate(mines_box):
                        if all(j.status) != 'invisible':
                            j.status = 'invisible'
                   for count, k in enumerate(quest_box):
                        if all(k.status) != 'invisible':
                            k.status = 'invisible'
                   play_while_sound(town_enter_sound)

        # def town_event_handler(self, event):
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #             if event.button == 1:
        #                 if self.rect.collidepoint(event.pos):
        #                    pass
#---------------------------------------------------------------------------------------------
    list_of_traders = []
    alchemist_items = []
    smith_items = []
    trader_items = []
    tavern_items = []
    board_items = []

    class TownTrader():
        def __init__(self, surface, trader_list, list_image, n,available,type, description,value,status):
            self.type = type
            self.trader_list = trader_list
            self.status = status
            self.description = description
            self.scale = 0.5
            self.n = n
            self.list_image = list_image[n]
            self.rect = list_image[n].get_rect()
            width = list_image[n].get_width()
            height = list_image[n].get_height()
            self.rect.width = int(TILE_SIZE*0.5)
            self.rect.height = int(TILE_SIZE*0.5)
            self.list_image = pygame.transform.scale(list_image[n], (int(width * (self.scale-0.1)), int(height * self.scale)))
            self.trader_slot_icon = pygame.image.load("MainMenuRes/inventory/slots/10.png").convert_alpha()
            self.trader_slot_icon = pygame.transform.scale(self.trader_slot_icon,(int(TILE_SIZE*0.8), (int(TILE_SIZE*0.8))))
            self.surface = surface
            self.toggled = False
            self.clicked = False
            self.available = available
            self.value = value

        def initiate(self, item0,item1, item2,item3,item4,item5):
                if self.rect.collidepoint(mouse_position) and encounter == False \
                        and self.status != 'invisible' and toggle_char_sheet == False:
                    global party_icon
                    party_icon = False
                    if self.toggled == True:
                        self.trader_list.extend([item0,item1,item2,item3,item4,item5])
                        for count, l in enumerate(town_box):
                            if all(l.status) != 'invisible':
                                l.status = 'invisible'
                        for count, i in enumerate(chest_box):
                            if all(i.status) != 'invisible':
                                i.status = 'invisible'
                        for count, j in enumerate(mines_box):
                            if all(j.status) != 'invisible':
                                j.status = 'invisible'
                        for count, k in enumerate(quest_box):
                            if all(k.status) != 'invisible':
                                k.status = 'invisible'
                # elif self.toggled == False:
                #      self.trader_list = []
                     #play_while_sound(chest_open_sound)
        def draw(self, surface,font, text,text_col,textX, textY,x,y):
            self.x = x
            self.y = y
            self.rect.x = x
            self.rect.y = y
            self.rect_draw = (self.rect.x,self.rect.y,self.rect.width*0.8,self.rect.height)
            activate = False
            pos = pygame.mouse.get_pos()
            if self.available == True and toggle_char_sheet == False:
                if self.toggled == True:
                    pygame.draw.rect(surface, "#000044", self.rect_draw,5)
                    for y in range(1):
                        for x in range(6):
                            display.blit(self.trader_slot_icon, (TILE_SIZE*3.54 + x * 50, TILE_SIZE*6.2 + y * TILE_SIZE))
                surface.blit(self.list_image, (self.x,self.y))
                if self.rect.collidepoint(mouse_position):
                    img = font.render(text, True, text_col)
                    surface.blit(img, (textX, textY))
                if self.rect.collidepoint(mouse_position) and encounter == False:
                    if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                            activate = True
                            self.clicked = True
                            time.sleep(0.2)
                            if self.type == 'trader':
                                trader_sound.play()
                            elif self.type == 'board':
                                city_board_sound.play()
                            elif self.type == 'smith':
                                smith_sound.play()
                            elif self.type == 'tavern':
                                tavern_sound.play()
                            elif self.type == 'alchemist':
                                alchemy_sound.play()
                            elif self.type == 'temple':
                                if button.start_wealth >= 100+self.value*char_level:
                                   button.wealth -= 100+self.value*char_level
                                   button.start_wealth = button.wealth
                                   coins_sound.play()
                                   heal_sound.play()
                                button.PartyHealth = 100
                                button.PartyStartHealth = button.PartyHealth
                            elif self.type == 'port':
                                if button.start_wealth >= 100+100*char_level:
                                   button.wealth -= 100+100*char_level
                                   button.start_wealth = button.wealth
                                   coins_sound.play()
                                   port_sound.play()
                                party_movement[0],party_movement[1] = (self.value, self.status)
                        if pygame.mouse.get_pressed()[0] == 0:
                           self.clicked = False
                        return activate

        def event_handler(self, event):
            if self.available == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.toggled == False:
                        if self.rect.collidepoint(event.pos):
                            for i in list_of_traders:
                                i.toggled = False
                            self.toggled = True
                    elif event.button == 1 and self.toggled == True:
                        if self.rect.collidepoint(event.pos):
                            self.toggled = False
#----------------------------------------Traders-----------------------------------------
    CleonelTemple = TownTrader(display,None, traders_img,1,True,'temple', f'Temple. Heals party for {100} gold per level',100,'visible')
    CleonelTrader = TownTrader(display,trader_items, traders_img,2,True,'trader','Trader. Sells various goods',0,'visible')
    CleonelPort = TownTrader(display,None, traders_img,5,True,'port', f'Port. Travel to Westrad for {100} gold per level',-170,140)
    CleonelSmith = TownTrader(display,smith_items, traders_img,4,True,'smith','Smith. Sells armor and weapons',0,'visible')
    CleonelAlchemist = TownTrader(display,alchemist_items, traders_img,0,True,'alchemist','Alchemist. Sells potions, bombs and shards',0,'visible')
    CleonelTavern = TownTrader(display,tavern_items, traders_img,3,True,'tavern','Tavern. Hire troops and talk to people',0,'visible')
    CleonelBoard= TownTrader(display,board_items, traders_img,7,True,'board','Board with tasks. Find routine contracts here',0,'visible')

    list_of_traders.extend([CleonelPort,CleonelTemple,CleonelTrader,CleonelSmith,CleonelAlchemist,CleonelTavern,CleonelBoard])
#----------------------------------------Dialogs------------------------------------------
    fontDialog = pygame.font.Font('WorldMap/ESKARGOT.ttf', 2)

    path, dirs, portrait= next(os.walk("WorldMap/dialogs/portraits"))
    portrait_count = len(portrait)
    PORTRAIT_TYPES = portrait_count
    l_portrait_img = []
    r_portrait_img = []
    i_portrait_img = []
    for x in range(PORTRAIT_TYPES):
        imgl = pygame.image.load(f'WorldMap/dialogs/portraits/{x}.png').convert_alpha()
        imgl = pygame.transform.scale(imgl,  (int(TILE_SIZE), int(TILE_SIZE*1.2)))
        imgr = pygame.transform.flip(imgl, True, False)
        imgi = pygame.transform.scale(imgl,  (int(TILE_SIZE), int(TILE_SIZE)))
        l_portrait_img.append(imgl)
        r_portrait_img.append(imgr)
        i_portrait_img.append(imgi)
#------------------------------------------------------------------------------------------
    dialog_window = pygame.image.load("WorldMap/dialogs/dialog_window.png").convert_alpha()
    dialog_window = pygame.transform.scale(dialog_window, (int(WINDOW_SIZE[0] * 0.3), (int(WINDOW_SIZE[1] * 0.2))))

    class Dialog():
        def __init__(self, surface, status,max_lines,toggled):
            self.surface = surface
            self.status = status
            self.selection = 0
            self.clicked = False
            self.toggled = toggled
            self.phase = 0
            self.max_lines = max_lines

        def dialog_window(self, surface):
            self.wx = TILE_SIZE*3.5
            self.wy = TILE_SIZE*3
            self.window = dialog_window
            self.rect = dialog_window.get_rect()
            self.rect.x = TILE_SIZE*3.5
            self.rect.y = TILE_SIZE*3
            surface.blit(self.window,(self.wx, self.wy))

        def get_line(self,surface,jsonfile,leftchar,name,block,line,stepX,stepY,statname,stat,check):
            self.active = True
            self.font = fontDialog
            self.font_col = (0,0,0)
            self.statname = statname
            self.stat = stat
            self.check = check
            self.name = name
            self.line = line
            self.stepX = stepX
            self.stepY = stepY
            self.textX = TILE_SIZE*3.8
            self.textY = TILE_SIZE*3.5
            with open(f"WorldMap/dialogs/{jsonfile}.json",'r') as f:
                json_object = json.loads(f.read())
            self.say = json_object[name][block][line]
            self.key = json_object[name][block]
            self.keylist = self.key.keys()
            who = name.capitalize()
            img_who = font.render(who, True, (80,50,40)) #"#628B19"
            img_line = font.render(self.say, True, self.font_col)
            img_line_sel = font.render(self.say, True, '#6F762D')
            img_line_inactive = font.render(self.say, True, (120,120,120))
            #img_line.get_rect()
            #self.img_line_rect.x = self.textX +stepX
            #self.img_line_rect.y = self.textY +stepY
            if toggle_char_sheet == False:
                surface.blit(img_who, (self.textX, self.textY-TILE_SIZE*0.4))
                if self.stat < self.check:
                    surface.blit(img_line_inactive, (self.textX+stepX, self.textY+stepY))
                    self.img_inactive_rect = pygame.Rect(self.textX+stepX, self.textY+stepY, 200, 20)
                    if self.img_inactive_rect.collidepoint(mouse_position):
                        self.active = False
                        checker = font.render(f'{self.statname} ({self.stat}/{self.check})', True, (80,50,40))
                        surface.blit(checker, (TILE_SIZE*5.5, TILE_SIZE*4.9))
                if self.stat >= self.check:
                    self.img_line_rect = pygame.Rect(self.textX+stepX, self.textY+stepY, 350, 20)
                    self.active = True
                    #pygame.draw.rect(display, (255,0,0), self.img_line_rect)
                    surface.blit(img_line, (self.textX+stepX, self.textY+stepY))
                    if self.img_line_rect.collidepoint(mouse_position):
                       self.selection = self.line
                       surface.blit(img_line_sel, (self.textX+stepX, self.textY+stepY))
                       if self.name == 'rowan' and self.clicked == True:
                           self.selection = self.line
                           print(self.selection)
                self.leftchar = leftchar
                self.lx = TILE_SIZE*3.5
                self.ly = TILE_SIZE*4.0
                surface.blit(leftchar,(self.lx, self.ly))

        def get_resp(self,surface,jsonfile,rightchar,name,block,line,stepX,stepY):
            self.font = fontDialog
            self.font_col = (0,0,0)
            self.name = name
            self.line = line
            self.stepX = stepX
            self.stepY = stepY
            self.textX = TILE_SIZE*3.8
            self.textY = TILE_SIZE*3.5
            with open(f"WorldMap/dialogs/{jsonfile}.json",'r') as f:
                json_object = json.loads(f.read())
            self.say = json_object[name][block][line]
            self.key = json_object[name][block]
            self.keylist = self.key.keys()
            who = name.capitalize()
            img_who = font.render(who, True, (80,50,40))
            img_who = pygame.transform.flip(img_who, False, False)
            img_resp = font.render(self.say, True, self.font_col)
            self.img_line_rect = pygame.Rect(self.textX+stepX, self.textY+stepY, 350, 20)
            if self.name != 'rowan' and self.clicked == True:
                self.selection = 0
            self.img_resp_rect = img_resp.get_rect()
            self.img_resp_rect.x = self.textX
            self.img_resp_rect.y = self.textY
            if toggle_char_sheet == False:
                surface.blit(img_who, (self.textX+TILE_SIZE*4.2, self.textY-TILE_SIZE*0.4))
                surface.blit(img_resp, (self.textX+stepX, self.textY+stepY))
                self.rightchar = rightchar
                self.rx = TILE_SIZE*8.5
                self.ry = TILE_SIZE*4
                surface.blit(rightchar,(self.rx, self.ry))

        def initiate(self,surface):
            if self.toggled == True:
                for count, l in enumerate(town_box):
                    if all(l.status) != 'invisible':
                        l.status = 'invisible'
                for count, i in enumerate(chest_box):
                    if all(i.status) != 'invisible':
                        i.status = 'invisible'
                for count, j in enumerate(mines_box):
                    if all(j.status) != 'invisible':
                        j.status = 'invisible'
                for count, k in enumerate(quest_box):
                    if all(k.status) != 'invisible':
                        k.status = 'invisible'

                if toggle_char_sheet == False:
                   self.dialog_window(surface)

                action = False
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and encounter == False \
                    and self.img_line_rect.collidepoint(mouse_position):
                    time.sleep(0.1)
                    action = True
                    self.clicked = True
                    self.phase +=1
                    pygame.mixer.Sound(page_sound).play()
                    #if self.name != 'rowan' and self.clicked == True:
                    #     self.selection = self.line
                    # else:
                    #      self.selection = 0
                if self.phase >= self.max_lines:
                   self.phase = 0
                   self.toggled = False
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                return action

    #-----------------------------------------------------------------------------------------
    dialog_0 = Dialog(display,'visible',15,True)
    dialog_1 = Dialog(display,'visible',3,False)



    #----------------------------------npc-------------------------------------
    npc_0 = StoredItem(display,i_portrait_img,3,None,'npc',True, False,'City guard',0,1)


    #------------------------------------------------------------------------------------------------
    def restart_game():
        play_music('MainTheme')
        button.quest_old_ways = 'unlocked'

        # for loop for a quest box starting with 1
        button.start_wealth = 120
        button.wealth = 0 + button.start_wealth
        button.start_experience = 0
        button.experience = 0 + button.start_experience
        button.PartyHealth = 0 + PartyStartHealth
        button.PartyMaxHealth = 100
        button.PartyStartHealth = 100
        for i in list_of_skills:
            for j in i:
                j.status = 0

#--------------------------------------Chapters-------------------------------------------
    Chapter_0 = False     # Homecoming
    chapter_1 = False   # Troubles in the Land
    chapter_2 = False   # Charlatan Kings
    chapter_3 = False   # Blood and Honor
    chapter_4 = False   # The Great Assembly
    chapter_5 = False   # The Invasion
    chapter_6 = False   # The Expedition
    chapter_7 = False   # Games with Snakes
    chapter_8_a = False     # Path of the Seeker
    chapter_8_b = False     # Path of the Loyalist
    chapter_8_c = False     # Path of the Vagrant

#------------------------------------------------------------------------------------
    prologue_path = open('WorldMap/chapters/chapter_intro_text/prologue.txt', 'r')
    prologue_lore = prologue_path.read()
    prologue_path.close()
    # -----------------------------------QuestImg-----------------------------------
    path, dirs, chapter= next(os.walk("WorldMap/chapters/chapter_intro_img"))
    chapter_count = len(chapter)
    CHAPTER_TYPES = chapter_count
    chapter_img = []
    for x in range(CHAPTER_TYPES):
        img = pygame.image.load(f'WorldMap/chapters/chapter_intro_img/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * 0.2), (int(WINDOW_SIZE[1] * 0.44))))
        chapter_img.append(img)

#--------------------------------------Chapters-------------------------------------------
    class Chapter():
        def __init__(self, surface, available,status,list_image,n,chapter_text,lore):
            self.surface = surface
            self.status = status
            self.available = available
            self.chapter_text = chapter_text
            self.lore = lore
            self.clicked = False
            self.toggled = True
            self.scale = 1.75
            self.n = n
            self.story_image = list_image[n]
            self.rect = list_image[n].get_rect()
            self.width = list_image[n].get_width()
            self.height = list_image[n].get_height()
            self.rect.width = list_image[n].get_width()
            self.rect.height = list_image[n].get_height()
            self.rect.x = list_image[n].get_width()
            self.rect.y = list_image[n].get_height()
            self.story_image = pygame.transform.scale(list_image[n], (int(self.width * (self.scale)), int(self.height * self.scale)))

        def draw_story(self, surface,xmod, ymod):
            if toggle_char_sheet == False:
                if encounter == False and self.toggled == True:
                    surface.blit(self.story_image, (TILE_SIZE*2.8, TILE_SIZE*0.4))
                    gm_draw_text(self.chapter_text, fontStats, (255, 225, 100), TILE_SIZE*3.3, TILE_SIZE*0.8)
                    msg_list = []
                    line_spacing = 0
                    for line in self.lore.split('\n'):
                        msg = font.render(line, True, "#2c2d47")
                        msg_list.append(msg)
                        line_spacing += 20
                        surface.blit(msg, (TILE_SIZE*3.1 - xmod, TILE_SIZE*4.6 + ymod + (line_spacing * 1.1)))
                    play_while_sound(chorus_sound)

        def initiale (self):
            activate = False
            if self.rect.collidepoint(mouse_position):
                    if pygame.mouse.get_pressed()[0] == 1:
                        activate = True
                        self.clicked = True
                        self.toggled = False
                    return activate

#----------------------------------------Chapters------------------------------------
    chapter_box = []

    prologue = Chapter(display,True,'visible',chapter_img,0,"Prologue",prologue_lore)

    chapter_box.extend([prologue])
#---------------------------------------Game_Menu------------------------------------------
    def game_menu(surface):
       menu_yes_button = button.Button(surface, TILE_SIZE*6, TILE_SIZE*4, gm_check, 15, 20, 0, True, 'Yes')
       menu_no_button = button.Button(surface, TILE_SIZE*7, TILE_SIZE*4, gm_cross, 15, 20, 0, True, 'No')
       global toggle_game_menu
       global global_map_running
       surface.blit(menu_sheet,(TILE_SIZE*3.5, TILE_SIZE*2))
       img = fontMenu.render('Leave Game?', True, (0, 0, 0))
       surface.blit(img, (TILE_SIZE*5.4, TILE_SIZE*3))
       menu_yes_button.draw()
       menu_no_button.draw()
       if menu_yes_button.rect.collidepoint(mouse_position):
           surface.blit(gm_greencheck, (menu_yes_button.rect.x - 4, menu_yes_button.rect.y))
       elif menu_no_button.rect.collidepoint(mouse_position):
           surface.blit(gm_greencross, (menu_no_button.rect.x - 4, menu_no_button.rect.y))
       if  menu_no_button.clicked:
           toggle_game_menu = False
       elif menu_yes_button.clicked:
           pygame.mixer.fadeout(2500)
           restart_game()
           global_map_running = False

    def game_over (surface):
        global global_map_running
        global block_movement
        if button.PartyHealth <= 0:
            block_movement = True
            menu_yes_button = button.Button(surface, TILE_SIZE*6, TILE_SIZE*4.5, gm_check, 15, 20, 0, True, 'Yes')
            surface.blit(menu_sheet,(TILE_SIZE*3, TILE_SIZE*2))
            img = fontStats.render('Your journey ends', True, (0, 0, 0))
            img2 = font14.render('You have sustained too many wounds', True, (0, 0, 0))
            surface.blit(img, (TILE_SIZE*4.7, TILE_SIZE*3))
            surface.blit(img2, (TILE_SIZE*4.1, TILE_SIZE*3.6))
            menu_yes_button.draw()
            if menu_yes_button.rect.collidepoint(mouse_position):
                surface.blit(gm_greencheck, (menu_yes_button.rect.x - 4, menu_yes_button.rect.y))
            if menu_yes_button.clicked:
                pygame.mixer.fadeout(2500)
                restart_game()
                global_map_running = False
#--------------------------------------------------------------------------------------

# ----------------------------------WorldMapAnimations------------------------------------
    def change_action(action_var, frame, new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var, frame

    #global animation_frames
    animation_frames = {}

    def animation_load(scaleX,scaleY,path, frame_durations):
        global animation_frames
        animation_name = path.split('/')[-1]  # WorldMap/timewheel
        animation_frame_data = []  # list of animation names [frame_0]
        n = 0
        for frame in frame_durations:  # [100,100, etc
            animation_frame_id = animation_name + '_' + str(n)  # animation_name + #frame + n+=1
            img_loc = path + '/' + animation_frame_id + '.png'  # path+frame_0 +.png
            animation_image = pygame.image.load(img_loc).convert()  # animation_image = frame_0.png
            animation_image.set_colorkey((0, 0, 0))
            # animation_image = pygame.transform.flip(animation_image, False, False)
            animation_image = pygame.transform.scale(animation_image, (scaleX, scaleY))
            # right to left : copying png via its name to animation frames {} ---> animation_frames{frame_0[frame_0.png]}
            animation_frames[animation_frame_id] = animation_image.copy()  # animation_frames[frame_0] = frame_0.png
            for i in range(frame):  # [100]
                animation_frame_data.append(animation_frame_id)  # animation_frame_data[frame_0]
            n += 1
        return animation_frame_data

    animation_database = {}
    animation_database['timewheel'] = animation_load(180,100,'WorldMap/timewheel', [50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
                                                                            50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
                                                                            50, 50, 50, 50])
    timewheel_action = 'timewheel'
    timewheel_frame = 0
    timewheel_rect = pygame.Rect(622, 510, 80, 80)

    animation_database['apple'] = animation_load(160,160,'MainMenuRes/rowan/apple', [100, 200, 50, 50, 50, 50])
    animation_database['idle'] = animation_load(160,160,'MainMenuRes/rowan/idle', [50, 50])
    rowan_action = 'idle'
    rowan_frame = 0
    rowan_rect = pygame.Rect(80, 100, 80, 120)

    # GM_party_rect = pygame.Rect(10, 10, 10, 10)
    # ------------------------------------ColorChange--------------------------------
    # def palette_swap(surf, old_c,new_c):
    #     img_copy = gm_injury.copy()
    #     img_copy.fill(new_c)
    #     surf.set_colorkey(old_c)
    #     img_copy.blit(surf, (0,0))
    #     return img_copy
    #
    # gm_injury = palette_swap(gm_injury, (220,11,11),(255,255,255))
    # gm_injury = palette_swap(gm_injury, (169,8.png,8.png),(255,255,255))
    # gm_injury = palette_swap(gm_injury, (170,18,18),(255,255,255))
    # gm_injury = palette_swap(gm_injury, (85,0,0),(255,255,255))
    # gm_injury = palette_swap(gm_injury, (255,170,170),(255,255,255))
    # gm_injury.set_colorkey((0,0,0))
    # ----------------------------------------------------------------------------------
    def active_inactive_skill(surface,value,check,checkname,skill,x,y,inactive_value):
        inactive_rect = inactive_img[inactive_value].get_rect()
        inactive_rect.x,inactive_rect.y = x*TILE_SIZE,y*TILE_SIZE
        if check >= value:
            skill.draw(surface,x*TILE_SIZE,y*TILE_SIZE)
            #skill.status = 1
            if skill.rect.collidepoint(mouse_position):
                skill.item_text(f'{skill.id}. {skill.descr} || LP: {skill.value}', fontDescription, (0, 0, 0,), display, 490, 690)
        elif check < value and skills_active == True:
            #img_rect = inactive_img[inactive_value].get_rect()
            display.blit(inactive_img[inactive_value],(x*TILE_SIZE-5,y*TILE_SIZE-5))
        if inactive_rect.collidepoint(mouse_position) and check < value and skills_active == True:
            skill.item_text(f'{skill.id} || Required: {value} {checkname}', fontDescription, (0, 0, 0,), display, 490, 690)
    #---------------------------------------------------------------------------------------
    class HealthBar():
        def __init__(self, x, y, hp, max_hp):
            self.x = x
            self.y = y
            self.hp = hp
            self.max_hp = max_hp

        def draw(self, hp):
            self.hp = hp
            # health ration
            ratio = self.hp / self.max_hp
            pygame.draw.rect(display, (225, 225, 225), (self.x, self.y, 69, 17))
            pygame.draw.rect(display, (225, 25, 25), (self.x, self.y, 69 * ratio, 17))
            display.blit(gm_injury, (520, display.get_height() * 0.90))

    PartyStatus = HealthBar(528, 574, button.PartyHealth, button.PartyMaxHealth)
    # ------------------------------------------------------------------------------------

























































































#---------------------------------------------------------------------------------------
    while global_map_running:
        global party_icon
        party_icon = True
        if toggle_char_sheet == True:
            display.fill("#d5bc79")
            # screen.fill((0,0,0))
            draw_bg_char_sheet_lid(display)
            draw_empty_slots()
            # draw_grid()

#---------------------------------------------------------------------------------------
        draw_items_in_inventory(display, necklace_list, 6.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, helm_list, 7.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, cloak_list, 8.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, bow_list, 9.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, armor_list, 10.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, gloves_list, 11.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, pants_list, 12.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, dagger_list, 13.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, sword_list, 14.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, shoes_list, 15.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, ring_list, 16.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, belt_list, 17.1, 7.1+inv_modifier)
        draw_items_in_inventory(display, inv_list, 18.1, 7.1+inv_modifier)
#--------------------------------InvSideButtons----------------------------------------
        if inv_up.clicked:
            click_counter += 1
            time.sleep(0.2)
            pygame.mixer.Sound(inv_click_sound).play()
            inv_modifier -=1
            # for i in list_of_items:
            #     for j in i:
            #         j.y -= TILE_SIZE
        elif inv_down.clicked and click_counter > 0:
            click_counter -= 1
            time.sleep(0.2)
            pygame.mixer.Sound(inv_click_sound).play()
            # for i in list_of_items:
            #     for j in i:
            #         j.y += TILE_SIZE
            inv_modifier +=1
        elif inv_return.clicked and click_counter > 0:
            pygame.mixer.Sound(inv_click_sound).play()
            # for i in list_of_items:
            #     for j in i:
            #         j.y += TILE_SIZE*click_counter
            inv_modifier = 0
            click_counter = 0

        # -------------------------------------DrawingSELECTION--------------------------------
        item_count = 0
        for item_count, i in enumerate(inv_list):
            if i.draw(display, i.x, i.y):
                current_item = item_count
                if current_item == item_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_item == item_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'red_apple':
                                bonus_health_points += i.bonus
                            elif i.id == 'crowbar':
                                bonus_lockpicking.value += i.bonus
                            elif i.id == 'lockmaster_tools':
                                bonus_lockpicking.value += i.bonus
                            elif i.id == 'alchemist_kit':
                                bonus_alchemy.value += i.bonus

                    elif i.toggled == False and i.status == 1 and current_item == item_count:
                        i.status = 0
                        if i.id == 'red_apple':
                            bonus_health_points -= i.bonus
                        elif i.id == 'crowbar':
                            bonus_lockpicking.value -= i.bonus
                        elif i.id == 'lockmaster_tools':
                            bonus_lockpicking.value -= i.bonus
                        elif i.id == 'alchemist_kit':
                            bonus_alchemy.value -= i.bonus
            if current_item != item_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'red_apple':
                    bonus_health_points -= i.bonus
                elif i.id == 'crowbar':
                    bonus_lockpicking.value -= i.bonus
                elif i.id == 'lockmaster_tools':
                    bonus_lockpicking.value -= i.bonus
                elif i.id == 'alchemist_kit':
                    bonus_alchemy.value -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), inv_list[current_item].rect, 3)
        #-------------------------------------------------------------------------------------------
        bow_count = 0
        for bow_count, i in enumerate(bow_list):
            if i.draw(display, i.x, i.y):
                current_bow = bow_count
                if current_bow == bow_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_bow == bow_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'simple_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'hunter_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'war_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 5
                            if i.id == 'peasant_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'metal_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'militia_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'redwood_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'curved_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 3
                            if i.id == 'nomad_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 4
                            if i.id == 'bone_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 2
                                bonus_arcana_res += 20
                            if i.id == 'marksman_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 9
                            if i.id == 'forest_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 12
                                bonus_poison_res +=20
                                bonus_frost_res +=20
                            if i.id == 'blackwood_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 7
                            if i.id == 'flameguard':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 10
                                bonus_fire_res +=20
                            if i.id == 'mechanized_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 6
                            if i.id == 'soldier_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 4
                            if i.id == 'long_bow':
                                bonus_ranged_damage += i.bonus
                            if i.id == 'valley_bow':
                                bonus_ranged_damage += i.bonus
                                bonus_critical_strike += 1
                    elif i.toggled == False and i.status == 1 and current_bow == bow_count:
                        i.status = 0
                        if i.id == 'simple_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'hunter_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'war_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 5
                        if i.id == 'peasant_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'metal_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'militia_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'redwood_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'curved_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 3
                        if i.id == 'nomad_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 4
                        if i.id == 'bone_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 2
                            bonus_arcana_res -= 20
                        if i.id == 'marksman_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 9
                        if i.id == 'forest_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 12
                            bonus_poison_res -=20
                            bonus_frost_res -=20
                        if i.id == 'blackwood_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 7
                        if i.id == 'flameguard':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 10
                            bonus_fire_res -=20
                        if i.id == 'mechanized_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 6
                        if i.id == 'soldier_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 4
                        if i.id == 'long_bow':
                            bonus_ranged_damage -= i.bonus
                        if i.id == 'valley_bow':
                            bonus_ranged_damage -= i.bonus
                            bonus_critical_strike -= 1
            if current_bow != bow_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'simple_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'hunter_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'war_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 5
                if i.id == 'peasant_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'metal_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'militia_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'redwood_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'curved_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 3
                if i.id == 'nomad_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 4
                if i.id == 'bone_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 2
                    bonus_arcana_res -= 20
                if i.id == 'marksman_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 9
                if i.id == 'forest_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 12
                    bonus_poison_res -=20
                    bonus_frost_res -=20
                if i.id == 'blackwood_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 7
                if i.id == 'flameguard':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 10
                    bonus_fire_res -=20
                if i.id == 'mechanized_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 6
                if i.id == 'soldier_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 4
                if i.id == 'long_bow':
                    bonus_ranged_damage -= i.bonus
                if i.id == 'valley_bow':
                    bonus_ranged_damage -= i.bonus
                    bonus_critical_strike -= 1
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), bow_list[current_bow].rect, 3)
        #-------------------------------------------------------------------------------------------
        ring_count = 0
        for ring_count, i in enumerate(ring_list):
            if i.draw(display, i.x, i.y):
                current_ring = ring_count
                if current_ring == ring_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_ring == ring_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'silver_ring':
                                bonus_frost_res += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_energy_res += i.bonus
                            elif i.id == 'moon_ring':
                                bonus_arcana_res += i.bonus
                                bonus_tricks += i.bonus//10
                            elif i.id == 'holy_ring':
                                bonus_frost_res += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_energy_res += i.bonus
                                bonus_armor_points += i.bonus//2
                            elif i.id == 'trinity_ring':
                                bonus_defence += i.bonus
                                bonus_block += i.bonus
                                bonus_threshold += i.bonus
                            elif i.id == 'minor_protection_ring':
                                bonus_armor_points += i.bonus
                                bonus_threshold += i.bonus // 10
                            elif i.id == 'minor_health_ring':
                                bonus_health_points += i.bonus
                            elif i.id == 'emerald_ring':
                                bonus_poison_res += i.bonus
                            elif i.id == 'unity_ring':
                                bonus_melee_damage += i.bonus
                                bonus_ranged_damage += i.bonus
                            elif i.id == 'protection_ring':
                                bonus_armor_points += i.bonus
                                bonus_threshold += 3
                            elif i.id == 'health_ring':
                                bonus_health_points += i.bonus
                            elif i.id == 'medusa_ring':
                                bonus_health_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'health_ring':
                                bonus_critical_strike += i.bonus
                            elif i.id == 'duel_ring':
                                bonus_melee_damage += 4
                                bonus_block += i.bonus
                            elif i.id == 'snake_ring':
                                bonus_parry += i.bonus
                                bonus_defence += 4
                            elif i.id == 'obscurity_ring':
                                bonus_stealth.value += i.bonus
                                bonus_critical_strike += 2
                            elif i.id == 'ocean_ring':
                                bonus_energy_res += i.bonus
                                bonus_frost_res += i.bonus
                                bonus_tricks += 2
                            elif i.id == 'war_ring':
                                bonus_defence += i.bonus
                                bonus_block += 6
                                bonus_threshold += 3
                            elif i.id == 'bone_ring':
                                bonus_poison_res += i.bonus
                                bonus_armor_points += 20
                            elif i.id == 'sun_ring':
                                bonus_fire_res += i.bonus
                                bonus_arcana_res += i.bonus
                                bonus_tricks += 2
                    elif i.toggled == False and i.status == 1 and current_ring == ring_count:
                        i.status = 0
                        if i.id == 'silver_ring':
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                        elif i.id == 'moon_ring':
                            bonus_arcana_res -= i.bonus
                            bonus_tricks -= i.bonus//10
                        elif i.id == 'holy_ring':
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                            bonus_armor_points -= i.bonus//2
                        elif i.id == 'trinity_ring':
                            bonus_defence -= i.bonus
                            bonus_block -= i.bonus
                            bonus_threshold -= i.bonus
                        elif i.id == 'minor_protection_ring':
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= i.bonus // 10
                        elif i.id == 'minor_health_ring':
                            bonus_health_points -= i.bonus
                        elif i.id == 'emerald_ring':
                            bonus_poison_res -= i.bonus
                        elif i.id == 'unity_ring':
                            bonus_melee_damage -= i.bonus
                            bonus_ranged_damage -= i.bonus
                        elif i.id == 'protection_ring':
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 3
                        elif i.id == 'health_ring':
                            bonus_health_points -= i.bonus
                        elif i.id == 'medusa_ring':
                            bonus_health_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'health_ring':
                            bonus_critical_strike -= i.bonus
                        elif i.id == 'duel_ring':
                            bonus_melee_damage -= 4
                            bonus_block -= i.bonus
                        elif i.id == 'snake_ring':
                            bonus_parry -= i.bonus
                            bonus_defence -= 4
                        elif i.id == 'obscurity_ring':
                            bonus_stealth.value -= i.bonus
                            bonus_critical_strike -= 2
                        elif i.id == 'ocean_ring':
                            bonus_energy_res -= i.bonus
                            bonus_frost_res -= i.bonus
                            bonus_tricks -= 2
                        elif i.id == 'war_ring':
                            bonus_defence -= i.bonus
                            bonus_block -= 6
                            bonus_threshold -= 3
                        elif i.id == 'bone_ring':
                            bonus_poison_res -= i.bonus
                            bonus_armor_points -= 20
                        elif i.id == 'sun_ring':
                            bonus_fire_res -= i.bonus
                            bonus_arcana_res -= i.bonus
                            bonus_tricks -= 2
            if current_ring != ring_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'silver_ring':
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                elif i.id == 'moon_ring':
                    bonus_arcana_res -= i.bonus
                    bonus_tricks -= i.bonus//10
                elif i.id == 'holy_ring':
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                    bonus_armor_points -= i.bonus//2
                elif i.id == 'trinity_ring':
                    bonus_defence -= i.bonus
                    bonus_block -= i.bonus
                    bonus_threshold -= i.bonus
                elif i.id == 'minor_protection_ring':
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= i.bonus // 10
                elif i.id == 'minor_health_ring':
                    bonus_health_points -= i.bonus
                elif i.id == 'emerald_ring':
                    bonus_poison_res -= i.bonus
                elif i.id == 'unity_ring':
                    bonus_melee_damage -= i.bonus
                    bonus_ranged_damage -= i.bonus
                elif i.id == 'protection_ring':
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 3
                elif i.id == 'health_ring':
                    bonus_health_points -= i.bonus
                elif i.id == 'medusa_ring':
                    bonus_health_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'health_ring':
                    bonus_critical_strike -= i.bonus
                elif i.id == 'duel_ring':
                    bonus_melee_damage -= 4
                    bonus_block -= i.bonus
                elif i.id == 'snake_ring':
                    bonus_parry -= i.bonus
                    bonus_defence -= 4
                elif i.id == 'obscurity_ring':
                    bonus_stealth.value -= i.bonus
                    bonus_critical_strike -= 2
                elif i.id == 'ocean_ring':
                    bonus_energy_res -= i.bonus
                    bonus_frost_res -= i.bonus
                    bonus_tricks -= 2
                elif i.id == 'war_ring':
                    bonus_defence -= i.bonus
                    bonus_block -= 6
                    bonus_threshold -= 3
                elif i.id == 'bone_ring':
                    bonus_poison_res -= i.bonus
                    bonus_armor_points -= 20
                elif i.id == 'sun_ring':
                    bonus_fire_res -= i.bonus
                    bonus_arcana_res -= i.bonus
                    bonus_tricks -= 2
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), ring_list[current_ring].rect, 3)
        #-------------------------------------------------------------------------------------------
        necklace_count = 0
        for necklace_count, i in enumerate(necklace_list):
            if i.draw(display, i.x, i.y):
                current_necklace = necklace_count
                if current_necklace == necklace_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_necklace == necklace_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'traders_luck':
                                bonus_tricks += i.bonus
                            elif i.id == 'moon_crest':
                                bonus_tricks += 2
                                bonus_arcana_res += i.bonus
                            elif i.id == 'brothers_mark':
                                bonus_tricks += i.bonus
                                bonus_critical_strike += i.bonus
                            elif i.id == 'the_eye':
                                bonus_tricks += i.bonus
                            elif i.id == 'war_amulet':
                                bonus_tricks += 2
                                bonus_defence += 2
                                bonus_armor_points += i.bonus
                            elif i.id == 'deep_endless':
                                bonus_tricks += i.bonus
                            elif i.id == 'warlock_amulet':
                                bonus_tricks += 4
                                bonus_frost_res += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_energy_res += i.bonus
                                bonus_poison_res += i.bonus
                                bonus_arcane += i.bonus
                            elif i.id == 'spider_amulet':
                                bonus_tricks += 4
                                bonus_parry += i.bonus
                            elif i.id == 'defilers_amulet':
                                bonus_tricks += 6
                                bonus_poison_res += i.bonus
                                bonus_fire_res += i.bonus
                            elif i.id == 'grimshard_amulet':
                                bonus_tricks += 4
                                bonus_critical_strike+= i.bonus
                            elif i.id == 'the_shining':
                                bonus_block += 6
                                bonus_health_points += i.bonus
                            elif i.id == 'sailors_luck':
                                bonus_tricks += 4
                                bonus_energy_res += i.bonus
                                bonus_frost_res += i.bonus
                            elif i.id == 'crystal_amulet':
                                bonus_tricks += 10
                                bonus_defence+= i.bonus
                    elif i.toggled == False and i.status == 1 and current_necklace == necklace_count:
                        i.status = 0
                        if i.id == 'traders_luck':
                            bonus_tricks -= i.bonus
                        elif i.id == 'moon_crest':
                            bonus_tricks -= 2
                            bonus_arcana_res -= i.bonus
                        elif i.id == 'brothers_mark':
                            bonus_tricks -= i.bonus
                            bonus_critical_strike -= i.bonus
                        elif i.id == 'the_eye':
                            bonus_tricks -= i.bonus
                        elif i.id == 'war_amulet':
                            bonus_tricks -= 2
                            bonus_defence -= 2
                            bonus_armor_points -= i.bonus
                        elif i.id == 'deep_endless':
                            bonus_tricks -= i.bonus
                        elif i.id == 'warlock_amulet':
                            bonus_tricks -= 4
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                            bonus_poison_res -= i.bonus
                            bonus_arcane -= i.bonus
                        elif i.id == 'spider_amulet':
                            bonus_tricks -= 4
                            bonus_parry -= i.bonus
                        elif i.id == 'defilers_amulet':
                            bonus_tricks -= 6
                            bonus_poison_res -= i.bonus
                            bonus_fire_res -= i.bonus
                        elif i.id == 'grimshard_amulet':
                            bonus_tricks -= 4
                            bonus_critical_strike -= i.bonus
                        elif i.id == 'the_shining':
                            bonus_block -= 6
                            bonus_health_points -= i.bonus
                        elif i.id == 'sailors_luck':
                            bonus_tricks -= 4
                            bonus_energy_res -= i.bonus
                            bonus_frost_res -= i.bonus
                        elif i.id == 'crystal_amulet':
                            bonus_tricks -= 10
                            bonus_defence -= i.bonus
            if current_necklace != necklace_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'traders_luck':
                    bonus_tricks -= i.bonus
                elif i.id == 'moon_crest':
                    bonus_tricks -= 2
                    bonus_arcana_res -= i.bonus
                elif i.id == 'brothers_mark':
                    bonus_tricks -= i.bonus
                    bonus_critical_strike -= i.bonus
                elif i.id == 'the_eye':
                    bonus_tricks -= i.bonus
                elif i.id == 'war_amulet':
                    bonus_tricks -= 2
                    bonus_defence -= 2
                    bonus_armor_points -= i.bonus
                elif i.id == 'deep_endless':
                    bonus_tricks -= i.bonus
                elif i.id == 'warlock_amulet':
                    bonus_tricks -= 4
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                    bonus_poison_res -= i.bonus
                    bonus_arcane -= i.bonus
                elif i.id == 'spider_amulet':
                    bonus_tricks -= 4
                    bonus_parry -= i.bonus
                elif i.id == 'defilers_amulet':
                    bonus_tricks -= 6
                    bonus_poison_res -= i.bonus
                    bonus_fire_res -= i.bonus
                elif i.id == 'grimshard_amulet':
                    bonus_tricks -= 4
                    bonus_critical_strike -= i.bonus
                elif i.id == 'the_shining':
                    bonus_block -= 6
                    bonus_health_points -= i.bonus
                elif i.id == 'sailors_luck':
                    bonus_tricks -= 4
                    bonus_energy_res -= i.bonus
                    bonus_frost_res -= i.bonus
                elif i.id == 'crystal_amulet':
                    bonus_tricks -= 10
                    bonus_defence -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), necklace_list[current_necklace].rect, 3)
        #-------------------------------------------------------------------------------------------
        helm_count = 0
        for helm_count, i in enumerate(helm_list):
            if i.draw(display, i.x, i.y):
                current_helm = helm_count
                if current_helm == helm_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_helm == helm_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'travel_hat':
                                bonus_defence += i.bonus
                            elif i.id == 'steel_helm':
                                bonus_defence += 6
                                bonus_armor_points += i.bonus
                            elif i.id == 'tournament_helm':
                                bonus_defence += 10
                                bonus_armor_points += i.bonus
                                bonus_threshold += 6
                            elif i.id == 'monk_hood':
                                bonus_defence += i.bonus
                            elif i.id == 'leather_hood':
                                bonus_defence += 4
                                bonus_armor_points += i.bonus
                            elif i.id == 'light_chain_helm':
                                bonus_defence += 6
                                bonus_armor_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'protector_helm':
                                bonus_defence += 14
                                bonus_armor_points += i.bonus
                                bonus_threshold += 4
                            elif i.id == 'leather_helm':
                                bonus_defence += 4
                                bonus_armor_points += i.bonus
                            elif i.id == 'legion_helm':
                                bonus_defence += 9
                                bonus_armor_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'pretorian_helm':
                                bonus_defence += 14
                                bonus_armor_points += i.bonus
                                bonus_threshold += 4
                            elif i.id == 'inquisitor_hat':
                                bonus_defence += 6
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 3
                            elif i.id == 'brigade_helm':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                            elif i.id == 'mage_hat':
                                bonus_defence += 6
                                bonus_frost_res += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_energy_res += i.bonus
                            elif i.id == 'mercenary_helm':
                                bonus_defence += 6
                                bonus_armor_points += i.bonus
                                bonus_threshold += 3
                            elif i.id == 'turtle_helm':
                                bonus_defence += 14
                                bonus_armor_points += i.bonus
                                bonus_threshold += 7
                            elif i.id == 'pigface_helm':
                                bonus_defence += 20
                                bonus_armor_points += i.bonus
                                bonus_threshold += 5
                            elif i.id == 'full_helm':
                                bonus_defence += 10
                                bonus_armor_points += i.bonus
                                bonus_threshold += 5
                            elif i.id == 'ranger_hat':
                                bonus_defence += 6
                                bonus_critical_strike += 4
                                bonus_ranged_damage += i.bonus
                            elif i.id == 'hoplite_helm':
                                bonus_defence += 12
                                bonus_armor_points += i.bonus
                                bonus_threshold += 3
                    elif i.toggled == False and i.status == 1 and current_helm == helm_count:
                        i.status = 0
                        if i.id == 'travel_hat':
                            bonus_defence -= i.bonus
                        elif i.id == 'steel_helm':
                            bonus_defence -= 6
                            bonus_armor_points -= i.bonus
                        elif i.id == 'tournament_helm':
                            bonus_defence -= 10
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 6
                        elif i.id == 'monk_hood':
                            bonus_defence -= i.bonus
                        elif i.id == 'leather_hood':
                            bonus_defence -= 4
                            bonus_armor_points -= i.bonus
                        elif i.id == 'light_chain_helm':
                            bonus_defence -= 6
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'protector_helm':
                            bonus_defence -= 14
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 4
                        elif i.id == 'leather_helm':
                            bonus_defence -= 4
                            bonus_armor_points -= i.bonus
                        elif i.id == 'legion_helm':
                            bonus_defence -= 9
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'pretorian_helm':
                            bonus_defence -= 14
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 4
                        elif i.id == 'inquisitor_hat':
                            bonus_defence -= 6
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 3
                        elif i.id == 'brigade_helm':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                        elif i.id == 'mage_hat':
                            bonus_defence -= 6
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                        elif i.id == 'mercenary_helm':
                            bonus_defence -= 6
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 3
                        elif i.id == 'turtle_helm':
                            bonus_defence -= 14
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 7
                        elif i.id == 'pigface_helm':
                            bonus_defence -= 20
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 5
                        elif i.id == 'full_helm':
                            bonus_defence -= 10
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 5
                        elif i.id == 'ranger_hat':
                            bonus_defence -= 6
                            bonus_critical_strike -= 4
                            bonus_ranged_damage -= i.bonus
                        elif i.id == 'hoplite_helm':
                            bonus_defence -= 12
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 3
            if current_helm != helm_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'travel_hat':
                    bonus_defence -= i.bonus
                elif i.id == 'steel_helm':
                    bonus_defence -= 6
                    bonus_armor_points -= i.bonus
                elif i.id == 'tournament_helm':
                    bonus_defence -= 10
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 6
                elif i.id == 'monk_hood':
                    bonus_defence -= i.bonus
                elif i.id == 'leather_hood':
                    bonus_defence -= 4
                    bonus_armor_points -= i.bonus
                elif i.id == 'light_chain_helm':
                    bonus_defence -= 6
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'protector_helm':
                    bonus_defence -= 14
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 4
                elif i.id == 'leather_helm':
                    bonus_defence -= 4
                    bonus_armor_points -= i.bonus
                elif i.id == 'legion_helm':
                    bonus_defence -= 9
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'pretorian_helm':
                    bonus_defence -= 14
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 4
                elif i.id == 'inquisitor_hat':
                    bonus_defence -= 6
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 3
                elif i.id == 'brigade_helm':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                elif i.id == 'mage_hat':
                    bonus_defence -= 6
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                elif i.id == 'mercenary_helm':
                    bonus_defence -= 6
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 3
                elif i.id == 'turtle_helm':
                    bonus_defence -= 14
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 7
                elif i.id == 'pigface_helm':
                    bonus_defence -= 20
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 5
                elif i.id == 'full_helm':
                    bonus_defence -= 10
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 5
                elif i.id == 'ranger_hat':
                    bonus_defence -= 6
                    bonus_critical_strike -= 4
                    bonus_ranged_damage -= i.bonus
                elif i.id == 'hoplite_helm':
                    bonus_defence -= 12
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 3
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), helm_list[current_helm].rect, 3)
        #-------------------------------------------------------------------------------------------
        cloak_count = 0
        for cloak_count, i in enumerate(cloak_list):
            if i.draw(display, i.x, i.y):
                current_cloak = cloak_count
                if current_cloak == cloak_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_cloak == cloak_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'travel_cloak':
                                bonus_defence += i.bonus
                            elif i.id == 'night_cloak':
                                bonus_defence += i.bonus
                                bonus_critical_strike += i.bonus
                            elif i.id == 'full_cloak':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                            elif i.id == 'ranger_cloak':
                                bonus_defence += 6
                                bonus_block += 6
                                bonus_ranged_damage += i.bonus
                            elif i.id == 'jester_cloak':
                                bonus_defence += 8
                                bonus_parry += 8
                                bonus_health_points += i.bonus
                            elif i.id == 'war_cloak':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'noble_cloak':
                                bonus_defence += i.bonus
                                bonus_block += i.bonus
                                bonus_parry += i.bonus
                            elif i.id == 'warlock_cloak':
                                bonus_defence += 4
                                bonus_tricks += 4
                                bonus_frost_res += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_energy_res += i.bonus
                                bonus_poison_res += i.bonus
                                bonus_arcane += i.bonus
                            elif i.id == 'royal_cloak':
                                bonus_defence += 10
                                bonus_tricks += 2
                                bonus_health_points += i.bonus
                            elif i.id == 'thief_cloak':
                                bonus_defence += 4
                                bonus_tricks += 4
                                bonus_stealth.value += i.bonus
                    elif i.toggled == False and i.status == 1 and current_cloak == cloak_count:
                        i.status = 0
                        if i.id == 'travel_cloak':
                            bonus_defence -= i.bonus
                        elif i.id == 'night_cloak':
                            bonus_defence -= i.bonus
                            bonus_critical_strike -= i.bonus
                        elif i.id == 'full_cloak':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                        elif i.id == 'ranger_cloak':
                            bonus_defence -= 6
                            bonus_block -= 6
                            bonus_ranged_damage -= i.bonus
                        elif i.id == 'jester_cloak':
                            bonus_defence -= 8
                            bonus_parry -= 8
                            bonus_health_points -= i.bonus
                        elif i.id == 'war_cloak':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'noble_cloak':
                            bonus_defence -= i.bonus
                            bonus_block -= i.bonus
                            bonus_parry -= i.bonus
                        elif i.id == 'warlock_cloak':
                            bonus_defence -= 4
                            bonus_tricks -= 4
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                            bonus_poison_res -= i.bonus
                            bonus_arcane -= i.bonus
                        elif i.id == 'royal_cloak':
                            bonus_defence -= 10
                            bonus_tricks -= 2
                            bonus_health_points -= i.bonus
                        elif i.id == 'thief_cloak':
                            bonus_defence -= 4
                            bonus_tricks -= 4
                            bonus_stealth.value -= i.bonus
            if current_cloak != cloak_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'travel_cloak':
                    bonus_defence -= i.bonus
                elif i.id == 'night_cloak':
                    bonus_defence -= i.bonus
                    bonus_critical_strike -= i.bonus
                elif i.id == 'full_cloak':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                elif i.id == 'ranger_cloak':
                    bonus_defence -= 6
                    bonus_block -= 6
                    bonus_ranged_damage -= i.bonus
                elif i.id == 'jester_cloak':
                    bonus_defence -= 8
                    bonus_parry -= 8
                    bonus_health_points -= i.bonus
                elif i.id == 'war_cloak':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'noble_cloak':
                    bonus_defence -= i.bonus
                    bonus_block -= i.bonus
                    bonus_parry -= i.bonus
                elif i.id == 'warlock_cloak':
                    bonus_defence -= 4
                    bonus_tricks -= 4
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                    bonus_poison_res -= i.bonus
                    bonus_arcane -= i.bonus
                elif i.id == 'royal_cloak':
                    bonus_defence -= 10
                    bonus_tricks -= 2
                    bonus_health_points -= i.bonus
                elif i.id == 'thief_cloak':
                    bonus_defence -= 4
                    bonus_tricks -= 4
                    bonus_stealth.value -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), cloak_list[current_cloak].rect, 3)
        #-------------------------------------------------------------------------------------------
        armor_count = 0
        for armor_count, i in enumerate(armor_list):
            if i.draw(display, i.x, i.y):
                current_armor = armor_count
                if current_armor == armor_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_armor == armor_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'travel_clothes':
                                bonus_defence += i.bonus//2
                                bonus_armor_points += i.bonus
                            elif i.id == 'robes':
                                bonus_defence += i.bonus
                            elif i.id == 'light_leather':
                                bonus_defence += i.bonus//2
                                bonus_armor_points += i.bonus
                            elif i.id == 'light_chain_mail':
                                bonus_defence += 10
                                bonus_armor_points += i.bonus
                                bonus_threshold += 4
                            elif i.id == 'light_plate_armor':
                                bonus_defence += 12
                                bonus_armor_points += i.bonus
                                bonus_threshold += 6
                                bonus_block += 6
                            elif i.id == 'leather_armor':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                            elif i.id == 'reinforced_armor':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'nomad_armor':
                                bonus_defence += 16
                                bonus_armor_points += i.bonus
                            elif i.id == 'legion_armor':
                                bonus_defence += 16
                                bonus_armor_points += i.bonus
                                bonus_threshold += 4
                            elif i.id == 'cuirasse':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                                bonus_threshold += 3
                            elif i.id == 'tournament_armor':
                                bonus_defence += 30
                                bonus_armor_points += i.bonus
                                bonus_threshold += 12
                            elif i.id == 'heavy_plate':
                                bonus_defence += 26
                                bonus_armor_points += i.bonus
                                bonus_threshold += 10
                            elif i.id == 'reinforced_chain':
                                bonus_defence += 14
                                bonus_armor_points += i.bonus
                                bonus_threshold += 5
                            elif i.id == 'lamellar_armor':
                                bonus_defence += 20
                                bonus_armor_points += i.bonus
                                bonus_threshold += 6
                            elif i.id == 'plate_armor':
                                bonus_defence += 22
                                bonus_armor_points += i.bonus
                                bonus_threshold += 8
                    elif i.toggled == False and i.status == 1 and current_armor == armor_count:
                        i.status = 0
                        if i.id == 'travel_clothes':
                            bonus_defence -= i.bonus//2
                            bonus_armor_points -= i.bonus
                        elif i.id == 'robes':
                            bonus_defence -= i.bonus
                        elif i.id == 'light_leather':
                            bonus_defence -= i.bonus//2
                            bonus_armor_points -= i.bonus
                        elif i.id == 'light_chain_mail':
                            bonus_defence -= i.bonus//4
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 4
                        elif i.id == 'light_plate_armor':
                            bonus_defence -= 12
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 6
                            bonus_block -= 6
                        elif i.id == 'leather_armor':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                        elif i.id == 'reinforced_armor':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'nomad_armor':
                            bonus_defence -= 16
                            bonus_armor_points -= i.bonus
                        elif i.id == 'legion_armor':
                            bonus_defence -= 16
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 4
                        elif i.id == 'cuirasse':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 3
                        elif i.id == 'tournament_armor':
                            bonus_defence -= 30
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 12
                        elif i.id == 'heavy_plate':
                            bonus_defence -= 26
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 10
                        elif i.id == 'reinforced_chain':
                            bonus_defence -= 14
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 5
                        elif i.id == 'lamellar_armor':
                            bonus_defence -= 20
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 6
                        elif i.id == 'plate_armor':
                            bonus_defence -= 22
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 8
            if current_armor != armor_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'travel_clothes':
                    bonus_defence -= i.bonus//2
                    bonus_armor_points -= i.bonus
                elif i.id == 'robes':
                    bonus_defence -= i.bonus
                elif i.id == 'light_leather':
                    bonus_defence -= i.bonus//2
                    bonus_armor_points -= i.bonus
                elif i.id == 'light_chain_mail':
                    bonus_defence -= i.bonus//4
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 4
                elif i.id == 'light_plate_armor':
                    bonus_defence -= 12
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 6
                    bonus_block -= 6
                elif i.id == 'leather_armor':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                elif i.id == 'reinforced_armor':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'nomad_armor':
                    bonus_defence -= 16
                    bonus_armor_points -= i.bonus
                elif i.id == 'legion_armor':
                    bonus_defence -= 16
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 4
                elif i.id == 'cuirasse':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 3
                elif i.id == 'tournament_armor':
                    bonus_defence -= 30
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 12
                elif i.id == 'heavy_plate':
                    bonus_defence -= 26
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 10
                elif i.id == 'reinforced_chain':
                    bonus_defence -= 14
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 5
                elif i.id == 'lamellar_armor':
                    bonus_defence -= 20
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 6
                elif i.id == 'plate_armor':
                    bonus_defence -= 22
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 8
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), armor_list[current_armor].rect, 3)
        #-------------------------------------------------------------------------------------------
        gloves_count = 0
        for gloves_count, i in enumerate(gloves_list):
            if i.draw(display, i.x, i.y):
                current_gloves = gloves_count
                if current_gloves == gloves_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_gloves == gloves_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'travel_gloves':
                                bonus_defence += i.bonus
                                bonus_armor_points += i.bonus
                            elif i.id == 'hand_wraps':
                                bonus_defence += i.bonus
                            elif i.id == 'light_leather_gloves':
                                bonus_defence += 6
                                bonus_armor_points += i.bonus
                            elif i.id == 'light_chain_gloves':
                                bonus_defence += 10
                                bonus_armor_points += i.bonus
                                bonus_threshold += 1
                            elif i.id == 'light_plate_gloves':
                                bonus_defence += 12
                                bonus_armor_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'leather_gloves':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                            elif i.id == 'reinforced_gloves':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                            elif i.id == 'ranger_gloves':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                                bonus_ranged_damage += 8
                            elif i.id == 'thieves_gloves':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus // 2
                                bonus_thievery.value +=20
                            elif i.id == 'plate_gloves':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                                bonus_threshold += 4
                            elif i.id == 'tournament_gloves':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                                bonus_threshold += 6
                            elif i.id == 'war_gloves':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                                bonus_threshold += 3
                            elif i.id == 'basilisk_gloves':
                                bonus_defence += i.bonus // 2
                                bonus_armor_points += i.bonus
                                bonus_tricks +=4
                                bonus_fire_res += i.bonus*3
                                bonus_poison_res += i.bonus*3
                    elif i.toggled == False and i.status == 1 and current_gloves == gloves_count:
                        i.status = 0
                        if i.id == 'travel_gloves':
                            bonus_defence -= i.bonus
                            bonus_armor_points -= i.bonus
                        elif i.id == 'hand_wraps':
                            bonus_defence -= i.bonus
                        elif i.id == 'light_leather_gloves':
                            bonus_defence -= 6
                            bonus_armor_points -= i.bonus
                        elif i.id == 'light_chain_gloves':
                            bonus_defence -= 10
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 1
                        elif i.id == 'light_plate_gloves':
                            bonus_defence -= 12
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'leather_gloves':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                        elif i.id == 'reinforced_gloves':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                        elif i.id == 'ranger_gloves':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                            bonus_ranged_damage -= 8
                        elif i.id == 'thieves_gloves':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus // 2
                            bonus_thievery.value -=20
                        elif i.id == 'plate_gloves':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 4
                        elif i.id == 'tournament_gloves':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 6
                        elif i.id == 'war_gloves':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 3
                        elif i.id == 'basilisk_gloves':
                            bonus_defence -= i.bonus // 2
                            bonus_armor_points -= i.bonus
                            bonus_tricks -=4
                            bonus_fire_res -= i.bonus*3
                            bonus_poison_res -= i.bonus*3
            if current_gloves != gloves_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'travel_gloves':
                    bonus_defence -= i.bonus
                    bonus_armor_points -= i.bonus
                elif i.id == 'hand_wraps':
                    bonus_defence -= i.bonus
                elif i.id == 'light_leather_gloves':
                    bonus_defence -= 6
                    bonus_armor_points -= i.bonus
                elif i.id == 'light_chain_gloves':
                    bonus_defence -= 10
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 1
                elif i.id == 'light_plate_gloves':
                    bonus_defence -= 12
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'leather_gloves':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                elif i.id == 'reinforced_gloves':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                elif i.id == 'ranger_gloves':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                    bonus_ranged_damage -= 8
                elif i.id == 'thieves_gloves':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus // 2
                    bonus_thievery.value -=20
                elif i.id == 'plate_gloves':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 4
                elif i.id == 'tournament_gloves':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 6
                elif i.id == 'war_gloves':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 3
                elif i.id == 'basilisk_gloves':
                    bonus_defence -= i.bonus // 2
                    bonus_armor_points -= i.bonus
                    bonus_tricks -=4
                    bonus_fire_res -= i.bonus*3
                    bonus_poison_res -= i.bonus*3
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), gloves_list[current_gloves].rect, 3)
        #-------------------------------------------------------------------------------------------
        pants_count = 0
        for pants_count, i in enumerate(pants_list):
            if i.draw(display, i.x, i.y):
                current_pants = pants_count
                if current_pants == pants_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_pants == pants_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'cloth_pants':
                                bonus_defence += i.bonus
                                bonus_armor_points += i.bonus
                            elif i.id == 'monk_pants':
                                bonus_defence += i.bonus
                                bonus_block += i.bonus//2
                            elif i.id == 'leather_pants':
                                bonus_defence += 8
                                bonus_armor_points += i.bonus
                            elif i.id == 'light_chain_pants':
                                bonus_defence += 12
                                bonus_armor_points += i.bonus
                                bonus_threshold += 2
                            elif i.id == 'reinforced_pants':
                                bonus_defence += 10
                                bonus_armor_points += i.bonus
                            elif i.id == 'light_plate_pants':
                                bonus_defence += 10
                                bonus_armor_points += i.bonus
                                bonus_threshold += 4
                            elif i.id == 'plate_pants':
                                bonus_defence += 12
                                bonus_armor_points += i.bonus
                                bonus_threshold += 6
                            elif i.id == 'heavy_plate_pants':
                                bonus_defence += 16
                                bonus_armor_points += i.bonus
                                bonus_threshold += 8
                            elif i.id == 'tournament_pants':
                                bonus_defence += 16
                                bonus_armor_points += i.bonus
                                bonus_threshold += 10
                    elif i.toggled == False and i.status == 1 and current_pants == pants_count:
                        i.status = 0
                        if i.id == 'cloth_pants':
                            bonus_defence -= i.bonus
                            bonus_armor_points -= i.bonus
                        elif i.id == 'monk_pants':
                            bonus_defence -= i.bonus
                            bonus_block -= i.bonus//2
                        elif i.id == 'leather_pants':
                            bonus_defence -= 8
                            bonus_armor_points -= i.bonus
                        elif i.id == 'light_chain_pants':
                            bonus_defence -= 12
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 2
                        elif i.id == 'reinforced_pants':
                            bonus_defence -= 10
                            bonus_armor_points -= i.bonus
                        elif i.id == 'light_plate_pants':
                            bonus_defence -= 10
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 4
                        elif i.id == 'plate_pants':
                            bonus_defence -= 12
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 6
                        elif i.id == 'heavy_plate_pants':
                            bonus_defence -= 16
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 8
                        elif i.id == 'tournament_pants':
                            bonus_defence -= 16
                            bonus_armor_points -= i.bonus
                            bonus_threshold -= 10
            if current_pants != pants_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'cloth_pants':
                    bonus_defence -= i.bonus
                    bonus_armor_points -= i.bonus
                elif i.id == 'monk_pants':
                    bonus_defence -= i.bonus
                    bonus_block -= i.bonus//2
                elif i.id == 'leather_pants':
                    bonus_defence -= 8
                    bonus_armor_points -= i.bonus
                elif i.id == 'light_chain_pants':
                    bonus_defence -= 12
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 2
                elif i.id == 'reinforced_pants':
                    bonus_defence -= 10
                    bonus_armor_points -= i.bonus
                elif i.id == 'light_plate_pants':
                    bonus_defence -= 10
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 4
                elif i.id == 'plate_pants':
                    bonus_defence -= 12
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 6
                elif i.id == 'heavy_plate_pants':
                    bonus_defence -= 16
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 8
                elif i.id == 'tournament_pants':
                    bonus_defence -= 16
                    bonus_armor_points -= i.bonus
                    bonus_threshold -= 10
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), pants_list[current_pants].rect, 3)
        #-------------------------------------------------------------------------------------------
        dagger_count = 0
        for dagger_count, i in enumerate(dagger_list):
            if i.draw(display, i.x, i.y):
                current_dagger = dagger_count
                if current_dagger == dagger_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_dagger == dagger_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'steel_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += i.bonus//2
                                bonus_block += i.bonus
                            elif i.id == 'thief_dagger':
                                bonus_melee_damage += 4
                                bonus_critical_strike += i.bonus
                            elif i.id == 'ranger_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 8
                                bonus_block += 8
                            elif i.id == 'butcher_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 4
                            elif i.id == 'common_dagger':
                                bonus_melee_damage += i.bonus//3
                                bonus_block += i.bonus
                            elif i.id == 'broad_dagger':
                                bonus_melee_damage += 6
                                bonus_block += i.bonus
                            elif i.id == 'hunt_knife':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'war_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 3
                                bonus_block += 12
                            elif i.id == 'storm_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_energy_res += 20
                                bonus_block += 10
                            elif i.id == 'sting_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 8
                            elif i.id == 'bone_dagger':
                                bonus_melee_damage += 6
                                bonus_defence += 6
                                bonus_block += i.bonus
                            elif i.id == 'druid_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_health_points += i.bonus
                                bonus_parry += 12
                            elif i.id == 'sun_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_block+= 10
                            elif i.id == 'redsteel_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_block += 8
                            elif i.id == 'royal_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_parry += i.bonus
                            elif i.id == 'mercenary_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 2
                                bonus_block += 4
                            elif i.id == 'quality_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 1
                                bonus_block += 6
                            elif i.id == 'knight_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 4
                                bonus_block += 8
                            elif i.id == 'duel_dagger':
                                bonus_melee_damage += i.bonus
                                bonus_parry += 6
                                bonus_block += 6
                    elif i.toggled == False and i.status == 1 and current_dagger == dagger_count:
                        i.status = 0
                        if i.id == 'steel_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= i.bonus//2
                            bonus_block -= i.bonus
                        elif i.id == 'thief_dagger':
                            bonus_melee_damage -= 4
                            bonus_critical_strike -= i.bonus
                        elif i.id == 'ranger_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 8
                            bonus_block -= 8
                        elif i.id == 'butcher_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 4
                        elif i.id == 'common_dagger':
                            bonus_melee_damage -= i.bonus//3
                            bonus_block -= i.bonus
                        elif i.id == 'broad_dagger':
                            bonus_melee_damage -= 6
                            bonus_block -= i.bonus
                        elif i.id == 'hunt_knife':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'war_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 3
                            bonus_block -= 12
                        elif i.id == 'storm_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_energy_res -= 20
                            bonus_block -= 10
                        elif i.id == 'sting_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 8
                        elif i.id == 'bone_dagger':
                            bonus_melee_damage -= 6
                            bonus_defence -= 6
                            bonus_block -= i.bonus
                        elif i.id == 'druid_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_health_points -= i.bonus
                            bonus_parry -= 12
                        elif i.id == 'sun_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_block -= 10
                        elif i.id == 'redsteel_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 8
                        elif i.id == 'royal_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_parry -= i.bonus
                        elif i.id == 'mercenary_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 2
                            bonus_block -= 4
                        elif i.id == 'quality_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 1
                            bonus_block -= 6
                        elif i.id == 'knight_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 4
                            bonus_block -= 8
                        elif i.id == 'duel_dagger':
                            bonus_melee_damage -= i.bonus
                            bonus_parry -= 6
                            bonus_block -= 6
            if current_dagger != dagger_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'steel_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= i.bonus//2
                    bonus_block -= i.bonus
                elif i.id == 'thief_dagger':
                    bonus_melee_damage -= 4
                    bonus_critical_strike -= i.bonus
                elif i.id == 'ranger_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 8
                    bonus_block -= 8
                elif i.id == 'butcher_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 4
                elif i.id == 'common_dagger':
                    bonus_melee_damage -= i.bonus//3
                    bonus_block -= i.bonus
                elif i.id == 'broad_dagger':
                    bonus_melee_damage -= 6
                    bonus_block -= i.bonus
                elif i.id == 'hunt_knife':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'war_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 3
                    bonus_block -= 12
                elif i.id == 'storm_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_energy_res -= 20
                    bonus_block -= 10
                elif i.id == 'sting_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 8
                elif i.id == 'bone_dagger':
                    bonus_melee_damage -= 6
                    bonus_defence -= 6
                    bonus_block -= i.bonus
                elif i.id == 'druid_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_health_points -= i.bonus
                    bonus_parry -= 12
                elif i.id == 'sun_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_block -= 10
                elif i.id == 'redsteel_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 8
                elif i.id == 'royal_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_parry -= i.bonus
                elif i.id == 'mercenary_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 2
                    bonus_block -= 4
                elif i.id == 'quality_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 1
                    bonus_block -= 6
                elif i.id == 'knight_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 4
                    bonus_block -= 8
                elif i.id == 'duel_dagger':
                    bonus_melee_damage -= i.bonus
                    bonus_parry -= 6
                    bonus_block -= 6
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), dagger_list[current_dagger].rect, 3)
        #-------------------------------------------------------------------------------------------
        sword_count = 0
        for sword_count, i in enumerate(sword_list):
            if i.draw(display, i.x, i.y):
                current_sword = sword_count
                if current_sword == sword_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_sword == sword_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'steel_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'simple_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'short_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'long_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'the_sunrise':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 6
                            elif i.id == 'spider_sword':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 3
                            elif i.id == 'soldier_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'mercenary_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'broad_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'snake_sword':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 6
                            elif i.id == 'great_sword':
                                bonus_melee_damage += i.bonus
                                bonus_block += 4
                            elif i.id == 'paladin_sword':
                                bonus_melee_damage += i.bonus
                                bonus_block += 12
                            elif i.id == 'pirate_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'aircutter':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 8
                                bonus_parry += 12
                            elif i.id == 'captain_sword':
                                bonus_melee_damage += i.bonus
                                bonus_block += 8
                            elif i.id == 'sabre':
                                bonus_melee_damage += i.bonus
                                bonus_block += 4
                                bonus_parry += 4
                            elif i.id == 'temple_sword':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 6
                            elif i.id == 'nomad_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'curved_sword':
                                bonus_melee_damage += i.bonus
                            elif i.id == 'legion_sword':
                                bonus_melee_damage += i.bonus
                                bonus_block += 6
                            elif i.id == 'pretorian_sword':
                                bonus_melee_damage += i.bonus
                                bonus_block += 12
                            elif i.id == 'the_sorrow':
                                bonus_melee_damage += i.bonus
                                bonus_critical_strike += 10
                    elif i.toggled == False and i.status == 1 and current_sword == sword_count:
                        i.status = 0
                        if i.id == 'steel_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'simple_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'short_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'long_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'the_sunrise':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 6
                        elif i.id == 'spider_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 3
                        elif i.id == 'soldier_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'mercenary_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'broad_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'snake_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 6
                        elif i.id == 'great_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 4
                        elif i.id == 'paladin_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 12
                        elif i.id == 'pirate_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'aircutter':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 8
                            bonus_parry -= 12
                        elif i.id == 'captain_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 8
                        elif i.id == 'sabre':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 4
                            bonus_parry -= 4
                        elif i.id == 'temple_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 6
                        elif i.id == 'nomad_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'curved_sword':
                            bonus_melee_damage -= i.bonus
                        elif i.id == 'legion_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 6
                        elif i.id == 'pretorian_sword':
                            bonus_melee_damage -= i.bonus
                            bonus_block -= 12
                        elif i.id == 'the_sorrow':
                            bonus_melee_damage -= i.bonus
                            bonus_critical_strike -= 10
            if current_sword != sword_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'steel_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'simple_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'short_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'long_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'the_sunrise':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 6
                elif i.id == 'spider_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 3
                elif i.id == 'soldier_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'mercenary_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'broad_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'snake_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 6
                elif i.id == 'great_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 4
                elif i.id == 'paladin_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 12
                elif i.id == 'pirate_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'aircutter':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 8
                    bonus_parry -= 12
                elif i.id == 'captain_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 8
                elif i.id == 'sabre':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 4
                    bonus_parry -= 4
                elif i.id == 'temple_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 6
                elif i.id == 'nomad_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'curved_sword':
                    bonus_melee_damage -= i.bonus
                elif i.id == 'legion_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 6
                elif i.id == 'pretorian_sword':
                    bonus_melee_damage -= i.bonus
                    bonus_block -= 12
                elif i.id == 'the_sorrow':
                    bonus_melee_damage -= i.bonus
                    bonus_critical_strike -= 10
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), sword_list[current_sword].rect, 3)
        #-------------------------------------------------------------------------------------------
        shoes_count = 0
        for shoes_count, i in enumerate(shoes_list):
            if i.draw(display, i.x, i.y):
                current_shoes = shoes_count
                if current_shoes == shoes_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_shoes == shoes_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'simple_shoes':
                                bonus_defence += i.bonus
                            elif i.id == 'travel_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += i.bonus//2
                            elif i.id == 'light_plate_shoes':
                                bonus_defence += i.bonus //3
                                bonus_armor_points += i.bonus
                                bonus_threshold +=2
                            elif i.id == 'light_chain_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += 6
                                bonus_threshold +=1
                            elif i.id == 'plate_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += i.bonus//3
                                bonus_threshold +=3
                            elif i.id == 'common_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += i.bonus//2
                            elif i.id == 'hunter_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += i.bonus
                            elif i.id == 'ranger_shoes':
                                bonus_defence += i.bonus
                                bonus_armor_points += 6
                            elif i.id == 'heavy_plate_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += 12
                                bonus_threshold +=4
                            elif i.id == 'shadow_shoes':
                                bonus_armor_points += 10
                                bonus_defence += i.bonus
                                bonus_critical_strike +=4
                            elif i.id == 'arcane_shoes':
                                bonus_armor_points += 6
                                bonus_defence += 6
                                bonus_fire_res += i.bonus
                                bonus_frost_res += i.bonus
                                bonus_energy_res += i.bonus
                            elif i.id == 'trader_shoes':
                                bonus_armor_points += i.bonus
                                bonus_health_points += i.bonus
                                bonus_block +=8
                            elif i.id == 'leather_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += 6
                            elif i.id == 'tournament_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += 12
                                bonus_threshold +=6
                            elif i.id == 'snakeskin_shoes':
                                bonus_armor_points += i.bonus
                                bonus_defence += i.bonus
                                bonus_parry +=8
                    elif i.toggled == False and i.status == 1 and current_shoes == shoes_count:
                        i.status = 0
                        if i.id == 'simple_shoes':
                           bonus_defence -= i.bonus
                        elif i.id == 'travel_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= i.bonus//2
                        elif i.id == 'light_plate_shoes':
                            bonus_defence -= i.bonus //3
                            bonus_armor_points -= i.bonus
                            bonus_threshold -=2
                        elif i.id == 'light_chain_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= 6
                            bonus_threshold -=1
                        elif i.id == 'plate_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= i.bonus//3
                            bonus_threshold -=3
                        elif i.id == 'common_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= i.bonus//2
                        elif i.id == 'hunter_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= i.bonus
                        elif i.id == 'ranger_shoes':
                            bonus_defence -= i.bonus
                            bonus_armor_points -= 6
                        elif i.id == 'heavy_plate_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= 12
                            bonus_threshold -=4
                        elif i.id == 'shadow_shoes':
                            bonus_armor_points -= 10
                            bonus_defence -= i.bonus
                            bonus_critical_strike -=4
                        elif i.id == 'arcane_shoes':
                            bonus_armor_points -= 6
                            bonus_defence -= 6
                            bonus_fire_res -= i.bonus
                            bonus_frost_res -= i.bonus
                            bonus_energy_res -= i.bonus
                        elif i.id == 'trader_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_health_points -= i.bonus
                            bonus_block -=8
                        elif i.id == 'leather_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= 6
                        elif i.id == 'tournament_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= 12
                            bonus_threshold -=6
                        elif i.id == 'snakeskin_shoes':
                            bonus_armor_points -= i.bonus
                            bonus_defence -= i.bonus
                            bonus_parry -=8
            if current_shoes != shoes_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'simple_shoes':
                    bonus_defence -= i.bonus
                elif i.id == 'travel_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= i.bonus//2
                elif i.id == 'light_plate_shoes':
                    bonus_defence -= i.bonus //3
                    bonus_armor_points -= i.bonus
                    bonus_threshold -=2
                elif i.id == 'light_chain_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= 6
                    bonus_threshold -=1
                elif i.id == 'plate_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= i.bonus//3
                    bonus_threshold -=3
                elif i.id == 'common_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= i.bonus//2
                elif i.id == 'hunter_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= i.bonus
                elif i.id == 'ranger_shoes':
                    bonus_defence -= i.bonus
                    bonus_armor_points -= 6
                elif i.id == 'heavy_plate_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= 12
                    bonus_threshold -=4
                elif i.id == 'shadow_shoes':
                    bonus_armor_points -= 10
                    bonus_defence -= i.bonus
                    bonus_critical_strike -=4
                elif i.id == 'arcane_shoes':
                    bonus_armor_points -= 6
                    bonus_defence -= 6
                    bonus_fire_res -= i.bonus
                    bonus_frost_res -= i.bonus
                    bonus_energy_res -= i.bonus
                elif i.id == 'trader_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_health_points -= i.bonus
                    bonus_block -=8
                elif i.id == 'leather_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= 6
                elif i.id == 'tournament_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= 12
                    bonus_threshold -=6
                elif i.id == 'snakeskin_shoes':
                    bonus_armor_points -= i.bonus
                    bonus_defence -= i.bonus
                    bonus_parry -=8
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), shoes_list[current_shoes].rect, 3)
        #-------------------------------------------------------------------------------------------
        belt_count = 0
        for belt_count, i in enumerate(belt_list):
            if i.draw(display, i.x, i.y):
                current_belt = belt_count
                if current_belt == belt_count and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                    if i.toggled == True and i.status == 0 and current_belt == belt_count:
                        i.status = 1
                        if sell_item.toggled == False:
                            if i.id == 'travel_belt':
                                bonus_supply += i.bonus
                            elif i.id == 'hunter_belt':
                                bonus_supply += i.bonus
                            elif i.id == 'war_belt':
                                bonus_supply += 4
                                bonus_defence += 5
                                bonus_armor_points += i.bonus
                            elif i.id == 'double_belt':
                                bonus_supply += i.bonus
                            elif i.id == 'noble_belt':
                                bonus_supply += 2
                                bonus_parry += i.bonus
                            elif i.id == 'night_belt':
                                bonus_supply += 3
                                bonus_critical_strike += i.bonus
                            elif i.id == 'day_belt':
                                bonus_supply += 3
                                bonus_health_points += i.bonus
                            elif i.id == 'warlock_belt':
                                bonus_supply += 2
                                bonus_frost_res += i.bonus
                                bonus_fire_res += i.bonus
                                bonus_energy_res += i.bonus
                                bonus_poison_res += i.bonus
                                bonus_arcane += i.bonus
                            elif i.id == 'duel_belt':
                                bonus_supply += 4
                                bonus_parry += i.bonus
                                bonus_block += i.bonus
                            elif i.id == 'druid_belt':
                                bonus_supply += i.bonus//2
                                bonus_threshold += i.bonus
                    elif i.toggled == False and i.status == 1 and current_belt == belt_count:
                        i.status = 0
                        if i.id == 'travel_belt':
                            bonus_supply -= i.bonus
                        elif i.id == 'hunter_belt':
                            bonus_supply -= i.bonus
                        elif i.id == 'war_belt':
                            bonus_supply -= 4
                            bonus_defence -= 5
                            bonus_armor_points -= i.bonus
                        elif i.id == 'double_belt':
                            bonus_supply -= i.bonus
                        elif i.id == 'noble_belt':
                            bonus_supply -= 2
                            bonus_parry -= i.bonus
                        elif i.id == 'night_belt':
                            bonus_supply -= 3
                            bonus_critical_strike -= i.bonus
                        elif i.id == 'day_belt':
                            bonus_supply -= 3
                            bonus_health_points -= i.bonus
                        elif i.id == 'warlock_belt':
                            bonus_supply -= 2
                            bonus_frost_res -= i.bonus
                            bonus_fire_res -= i.bonus
                            bonus_energy_res -= i.bonus
                            bonus_poison_res -= i.bonus
                            bonus_arcana_res -= i.bonus
                        elif i.id == 'duel_belt':
                            bonus_supply -= 4
                            bonus_parry -= i.bonus
                            bonus_block -= i.bonus
                        elif i.id == 'druid_belt':
                            bonus_supply -= i.bonus//2
                            bonus_threshold -= i.bonus
            if current_belt != belt_count and i.status == 1 and 10*TILE_SIZE > i.y > 7*TILE_SIZE:
                if i.id == 'travel_belt':
                    bonus_supply -= i.bonus
                elif i.id == 'hunter_belt':
                    bonus_supply -= i.bonus
                elif i.id == 'war_belt':
                    bonus_supply -= 4
                    bonus_defence -= 5
                    bonus_armor_points -= i.bonus
                elif i.id == 'double_belt':
                    bonus_supply -= i.bonus
                elif i.id == 'noble_belt':
                    bonus_supply -= 2
                    bonus_parry -= i.bonus
                elif i.id == 'night_belt':
                    bonus_supply -= 3
                    bonus_critical_strike -= i.bonus
                elif i.id == 'day_belt':
                    bonus_supply -= 3
                    bonus_health_points -= i.bonus
                elif i.id == 'warlock_belt':
                    bonus_supply -= 2
                    bonus_frost_res -= i.bonus
                    bonus_fire_res -= i.bonus
                    bonus_energy_res -= i.bonus
                    bonus_poison_res -= i.bonus
                    bonus_arcana_res -= i.bonus
                elif i.id == 'duel_belt':
                    bonus_supply -= 4
                    bonus_parry -= i.bonus
                    bonus_block -= i.bonus
                elif i.id == 'druid_belt':
                    bonus_supply -= i.bonus//2
                    bonus_threshold -= i.bonus
                i.status = 0
                i.toggled = False
            if i.status == 1 and inventory_active == True:
                pygame.draw.rect(display, (125, 225, 125), belt_list[current_belt].rect, 3)
        # ----------------------------------------------------------------------------------------------
        if toggle_char_sheet == True:
            draw_bg_char_sheet(display)
            draw_inventory_slots()
            draw_empty_skill_slots()
            draw_empty_troops_slots()

        #---------------------------------------------------------------------------------------
        draw_troops_in_inventory(display, troops_melee,7.1, 6.1)
        draw_troops_in_inventory(display, troops_ranged,7.1, 7.1)
        draw_troops_in_inventory(display, troops_cavalry,7.1, 8.1)
        draw_troops_in_inventory(display, troops_support,7.1, 9.1)
        #------------------------------------InventoryButtons-----------------------------------
        if Haggler.status == 1:
            sell_item.available = True
        if inventory_active == True:
            inv_up.draw(display)
            inv_return.draw(display)
            inv_down.draw(display)
            if sell_item.toggled == True:
                pygame.draw.circle(display, "#000044", (sell_item.rect.centerx, sell_item.rect.centery+8), 20)
                pygame.draw.circle(display, "#eabb47", (sell_item.rect.centerx, sell_item.rect.centery+8), 15)
            sell_item.draw(display)

        #--------------------------------DescriptionOfItems----------------------------
        for i in list_of_items:
            for j in i:
                if j.rect.collidepoint(mouse_position) and 10*TILE_SIZE > j.y > 7*TILE_SIZE and sell_item.toggled == True:
                   j.item_text(f'Sell for {j.value}', fontDescription, (0, 0, 0,), display, 490, 690)
                elif j.rect.collidepoint(mouse_position) and 10*TILE_SIZE > j.y > 7*TILE_SIZE:
                    j.item_text(f'{j.descr}', fontDescription, (0, 0, 0,), display, 490, 690)

        for i in list_of_troops:
            for j in i:
                if j.rect.collidepoint(mouse_position):
                    j.item_text(f'{j.descr}', fontDescription, (0, 0, 0,), display, 490, 690)

        #---------------------------------------SellingItems--------------------------
        for i,j in enumerate(list_of_items):
            for k in j:
                if sell_item.toggled == True:
                    if k.rect.collidepoint(mouse_position) and k.clicked == True:
                        k.status = 0
                        k.bonus = 0
                        time.sleep(0.3)
                        if k in list_of_items[i]:
                           k.status = 0
                           k.bonus = 0
                           k.sell_item(list_of_items[i],k)

        #----------------------------------------Inventory/Skills_Toggle---------------------------
        pygame.draw.circle(display, "#F4E8B9", (inventory_button.rect.centerx, inventory_button.rect.centery), 30)
        pygame.draw.circle(display, "#F4E8B9", (troops_button.rect.centerx, troops_button.rect.centery), 30)

        troops_button.draw(display)

        if troops_button.rect.collidepoint(mouse_position):
            stats_draw_text(f'{troops_button.description}', fontDescription, (0, 0, 0,), display, 490, 690)
        if inventory_button.rect.collidepoint(mouse_position):
            stats_draw_text(f'{inventory_button.description}', fontDescription, (0, 0, 0,), display, 490, 690)

        # ----------------------------------Inventory/SkillsActivation-----------------------------
        if inventory_button.toggled == True:
            inventory_active = True
            skills_active = False
            troops_active = False
            inventory_button.draw(display)
        elif inventory_button.toggled == False:
            inventory_active = False
            skills_active = True
            troops_active = False
            display.blit(skills_icon, (inventory_button.rect.x, inventory_button.rect.y))
        if troops_button.toggled == True:
            inventory_active = False
            skills_active = False
            troops_active = True

        # -----------------------------------------------------------------------------------------------
        # draw_text('ESC to return', fontMenu, (0,225,0),screen, 10,0)  #Yvan\'s
        # draw_text('SPACE to continue', fontMenu, (0,225,0),screen, 1060,0)  #Yvan\'s
        # draw_rowan_portrait()
        stats_draw_text('Rowan', fontMenu, "#f4e8b9", display, 120, 280)
        # stats_draw_text('Attributes',fontStats, (0,0,0),screen, 120,368)
        stats_draw_text('Skirmish', fontStats, (0, 0, 0), display, 450, 10)
        stats_draw_text('Survival', fontStats, (0, 0, 0), display, 760, 10)
        stats_draw_text('Savviness', fontStats, (0, 0, 0), display, 1060, 10)
        # ----------------------------------ShowDescriptions------------------------------
        show_attributes_skills(attributes_lore, attributes_txt, 0, 26, 65, 382)
        show_attributes_skills(skirmish_lore, skirmish_txt, 0, 26, 405, 25)
        show_attributes_skills(survival_lore, survival_txt, 0, 26, 710, 25)
        show_attributes_skills(savviness_lore, savviness_txt, 0, 26, 1015, 25)
        show_attributes_skills(resistances_lore, resistances_txt, 110, 0, 340, 305)
        show_attributes_skills(attack_lore, attack_txt, 110, 0, 440, 335)
        # -----------------------------------DrawStatBonuses------------------------------
        draw_bonus_stats(582, 18, 512, 18, bonus_skirmish, 0, 27, 0, 27)
        draw_bonus_stats(900, 18, 830, 18, bonus_survival, 0, 27, 0, 27)
        draw_bonus_stats(1208, 18, 1140, 18, bonus_savviness, 0, 27, 0, 27)

        show_names(display, attributes_read, 80, 366, 0, 26.2, None, 10, None)
        show_names(display, skills_read, 390, 15, 0, 26.2, None, 8, None)
        show_names(display, skills_read, 710, 15, 0, 26.2, 8, 16, None)
        show_names(display, skills_read, 1010, 15, 0, 26.2, 16, 24, None)
        # ----------------------------Stats-------------------------------------
        # strength = int(randomlist[0])
        # constitution = int(randomlist[1])
        # dexterity = int(randomlist[2])
        # agility = int(randomlist[3])
        # awareness = int(randomlist[4])
        # personality = int(randomlist[5])
        # intelligence = int(randomlist[6])
        # wisdom = int(randomlist[7])
        # willpower = int(randomlist[8.png])
        # luck = int(randomlist[9])

        strength = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',1))
        constitution = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',2))
        dexterity = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',3))
        agility = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',4))
        awareness = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',5))
        personality = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',6))
        intelligence = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',7))
        wisdom = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',8))
        willpower = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',9))
        luck = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',10))

        no_random_stat_list = [strength,constitution, dexterity, agility,awareness, personality,
                               intelligence,wisdom,willpower,luck]
        stat_spacing = 0
        for i in no_random_stat_list:
            stat = fontStats.render(str(i), True, (0, 0, 0))
            stat_spacing += 27
            display.blit(stat, (220, 364 + (stat_spacing * 1)))

        # stat_spacing = 0
        # stat_list = []
        # for i in randomlist:
        #     stat = fontStats.render(str(i), True, (0, 0, 0))
        #     stat_list.append(stat)
        #     stat_spacing += 27
        #     display.blit(stat, (220, 364 + (stat_spacing * 1)))
        #
        # with open('MainMenuRes/char_statistic/charattributes.txt', 'w') as out:
        #     out.writelines([str(strength) + "\n", str(constitution) + "\n", str(dexterity) + "\n", str(agility) + "\n",
        #                     str(awareness) + "\n", str(personality) + "\n", str(intelligence) + "\n",
        #                     str(wisdom) + "\n",str(willpower) + "\n", str(luck) + "\n"])
        # ---------------------------------------------techniques-------------------------------------
        skirmish_tree = []
        melee = int((agility + dexterity) / 2 + strength + luck / 4 + bonus_melee.value)
        ranged = int((willpower + dexterity) / 2 + awareness + luck / 4 + bonus_ranged.value)
        parrying = int((willpower + dexterity) / 2 + agility + int(luck) / 4 + bonus_parrying.value)
        athletics = int((agility + willpower) / 2 + constitution + bonus_athletics.value)
        intimidation = int((personality + intelligence) / 2 + strength + bonus_intimidation.value)
        tactics = int((wisdom + willpower) / 2 + personality + bonus_tactics.value)
        arming = int((strength + willpower) / 2 + constitution + bonus_arming.value)
        siege = int((wisdom + intelligence) / 2 + willpower + bonus_siege.value)
        skirmish_tree.append(melee)
        skirmish_tree.extend((ranged, parrying, athletics, intimidation, tactics, arming, siege))
        with open('MainMenuRes/char_statistic/charskirmish.txt', 'w') as out:
            out.writelines([str(melee) + "\n", str(ranged) + "\n", str(parrying) + "\n", str(athletics) + "\n",
                            str(intimidation) + "\n", str(tactics) + "\n", str(arming) + "\n", str(siege)])

        survival_tree = []
        acrobatics = int((strength + dexterity) / 2 + agility + bonus_acrobatics.value)
        stealth = int((agility + dexterity) / 2 + awareness + luck / 4 + bonus_stealth.value)
        thievery = int((willpower + awareness) / 2 + dexterity + luck / 4 + bonus_thievery.value)
        lockpicking = int((intelligence + awareness) / 2 + dexterity + luck / 4 + bonus_lockpicking.value)
        deception = int((wisdom + personality) / 2 + intelligence + bonus_deception.value)
        traps = int((willpower + awareness) / 2 + dexterity + luck / 4 + bonus_traps.value)
        stupefy = int((willpower + dexterity) / 2 + strength + luck / 4 + bonus_stupefy.value)
        nature = int((willpower + wisdom) / 2 + awareness + bonus_nature.value)
        survival_tree.append(acrobatics)
        survival_tree.extend((stealth, thievery, lockpicking, deception, traps, stupefy, nature))
        with open('MainMenuRes/char_statistic/charsurvive.txt', 'w') as out:
            out.writelines([str(acrobatics) + "\n", str(stealth) + "\n", str(thievery) + "\n", str(lockpicking) + "\n",
                            str(deception) + "\n", str(traps) + "\n", str(stupefy) + "\n", str(nature)])

        savviness_tree = []
        investigation = int((wisdom + awareness) / 2 + intelligence + bonus_investigation.value)
        medicine = int((wisdom + dexterity) / 2 + intelligence + bonus_medicine.value)
        lore = int((intelligence + awareness) / 2 + wisdom + bonus_lore.value)
        persuasion = int((wisdom + intelligence) / 2 + personality + bonus_persuasion.value)
        arcane = int((intelligence + willpower) / 2 + wisdom + bonus_arcane.value)
        divine = int((intelligence + wisdom) / 2 + willpower + bonus_divine.value)
        alchemy = int((intelligence + dexterity) / 2 + wisdom + bonus_alchemy.value)
        engineering = int((dexterity + awareness) / 2 + intelligence + bonus_engineering.value)
        savviness_tree.append(investigation)
        savviness_tree.extend((medicine, lore, persuasion, arcane, divine, alchemy, engineering))
        with open('MainMenuRes/char_statistic/charsavviness.txt', 'w') as out:
            out.writelines([str(investigation) + "\n", str(medicine) + "\n", str(lore) + "\n", str(persuasion) + "\n",
                            str(arcane) + "\n", str(divine) + "\n", str(alchemy) + "\n", str(engineering)])

        resistance_box = []
        threshold = int((constitution + willpower) / 4 + athletics / 10 + bonus_threshold)
        defence = int((parrying + acrobatics) / 2 + bonus_defence)
        arcana_res = int((intelligence + luck) / 2 + arcane / 4 + bonus_arcana_res)
        energy_res = int((willpower + luck) / 2 + nature / 4 + bonus_energy_res)
        frost_res = int((willpower + luck) / 2 + nature / 4 + bonus_frost_res)
        fire_res = int((willpower + luck) / 2 + nature / 4 + bonus_fire_res)
        if Snake_Eater.status == 1:
            poison_res = 100
        else:
            poison_res = int((constitution + luck) / 2 + medicine / 4 + bonus_poison_res)
        resistance_box.append(threshold)
        resistance_box.extend((defence, arcana_res, energy_res, frost_res, fire_res, poison_res))
        with open('MainMenuRes/char_statistic/charres.txt', 'w') as out:
            out.writelines([str(threshold) + "\n", str(defence) + "\n", str(arcana_res) + "\n", str(energy_res) + "\n",
                            str(frost_res) + "\n", str(fire_res) + "\n", str(poison_res) + "\n"])

        attack_box = []
        melee_damage = int((melee / 2 + arming /4) + bonus_melee_damage)
        ranged_damage = int((ranged / 2 + arming/4) / 2 + bonus_ranged_damage)
        critical_strike = int(luck / 2 + medicine / 4 + bonus_critical_strike)
        block = int((arming + athletics) // 4 + luck//4 + bonus_block)
        parry = int((parrying + acrobatics) // 4 + luck//4 + bonus_parry)
        attack_box.append(melee_damage)
        attack_box.extend((block,ranged_damage,parry,critical_strike))
        #if toggle_char_sheet == False:
        with open('MainMenuRes/char_statistic/charattack.txt', 'w') as out:
            out.writelines([str(melee_damage) + "\n", str(ranged_damage) + "\n", str(critical_strike) + "\n", str(block) + "\n", str(parry)+"\n"])
        #print(ranged_damage)
        # stat_distributable = int((intelligence+luck)/4 + wisdom/2)
        tricks = int(char_level / 2 + luck / 4 + bonus_tricks)
        supply = int(char_level / 2 + luck / 4 + bonus_supply)
        health_points = int(10 + (strength + willpower) / 2 + constitution * 2 + athletics / 2 + char_level * 10 + bonus_health_points)
        armor_points = int(10 + (arming + acrobatics + tactics) / 2 + bonus_armor_points)
        leadership = int((tactics+persuasion+intimidation+deception)//2 + char_level*10 + bonus_leadership)
        with open('MainMenuRes/char_statistic/charsecondary.txt', 'w') as out:
             out.writelines([str(tricks) + "\n", str(supply) + "\n", str(health_points) + "\n", str(armor_points) + "\n", str(leadership)+"\n", str(char_level)+"\n"])
        # print(health_points)
        # print(button.health_points)
        #---------------------------------------RollDice------------------------------------
        # roll_button = button.Button(display, 140, 655, dice_icon, 40, 40, 0, True, 'Roll Dice')
        # if button.learning_points < 20:
        #     roll_button.available = False
        # else:
        #     roll_button.available = True
        #     # ----------------------------RollDiceButton------------------------------------
        # if roll_button.available == True:
        #     if roll_button.draw():
        #         randomlist = []
        #         for i in range(0, 10):
        #             n = random.randint(1, 10)
        #             randomlist.append(n)

            # if roll_button.rect.collidepoint(mouse_position):
            #     stats_draw_text(f'{roll_button.description}', fontMenu, (0, 225, 0), display, roll_button.rect.x + 50,
            #                     roll_button.rect.y)
        #------------------------------------RollDice---------------------------------------
        #----------------------------------Techniques---------------------------------------
        active_inactive_skill(display, 20,nature,'Nature',Cartographer,7.1, 9.1, 0)
        active_inactive_skill(display, 20,melee,'Melee',Combo,8.1, 9.1, 66)
        active_inactive_skill(display, 20,lore,'Lore',Educated,9.1, 9.1, 29)
        active_inactive_skill(display, 20,ranged,'Ranged',Quick_Shot,10.1, 9.1, 56)
        active_inactive_skill(display, 20,medicine,'Medicine',Camp_Doctor,11.1, 9.1, 42)
        active_inactive_skill(display, 20,thievery,'Thievery',Thief,12.1, 9.1, 30)
        active_inactive_skill(display, 20,arming,'Arming',Quartermaster,13.1, 9.1, 46)
        active_inactive_skill(display, 20,deception,'Deception',Scout,14.1, 9.1, 71)
        active_inactive_skill(display, 20,intimidation,'Intimidation',Haggler,15.1, 9.1, 73)
        active_inactive_skill(display, 20,persuasion,'Persuasion',Estates,16.1, 9.1, 6)
        active_inactive_skill(display, 20,arcane,'Arcane',Curse,17.1, 9.1, 7)
        active_inactive_skill(display, 20,divine,'Divine',Healing,18.1, 9.1, 35)
        with open('MainMenuRes/char_statistic/techniques_novice.txt', 'w') as out:
            out.writelines([str(Cartographer.status) + "\n", str(Combo.status) + "\n",str(Educated.status) + "\n", str(Quick_Shot.status) + "\n",
                            str(Camp_Doctor.status) + "\n", str(Thief.status) + "\n",str(Quartermaster.status) + "\n", str(Scout.status) + "\n",
                            str(Haggler.status) + "\n", str(Estates.status) + "\n",str(Curse.status) + "\n", str(Healing.status) + "\n"])
        #-------------------------------------------------------------------------------------
        if skill_counter >=6:
            active_inactive_skill(display, 40,medicine,'Medicine',Snake_Eater,7.1, 8.1, 18)
            active_inactive_skill(display, 40,melee,'Melee',Power_Blow,8.1, 8.1, 44)
            active_inactive_skill(display, 40,lore,'Lore',Scholar,9.1, 8.1, 4)
            active_inactive_skill(display, 40,ranged,'Ranged',Multiple_Shot,10.1, 8.1, 13)
            active_inactive_skill(display, 40,parrying,'Parrying',Duelist,11.1, 8.1, 45)
            active_inactive_skill(display, 40,traps,'Traps',Bear_Trap,12.1, 8.1, 27)
            active_inactive_skill(display, 40,alchemy,'Alchemy',Potion_Master,13.1, 8.1, 17)
            active_inactive_skill(display, 40,stupefy,'Stupefy',Knock_Down,14.1, 8.1, 74)
            active_inactive_skill(display, 40,acrobatics,'Acrobatics',Battle_Reflex,15.1, 8.1, 38)
            active_inactive_skill(display, 40,athletics,'Athletics',Persevere,16.1, 8.1, 49)
            active_inactive_skill(display, 40,arcane,'Arcane',Moon_Shield,17.1, 8.1, 34)
            active_inactive_skill(display, 40,divine,'Divine',Purifier,18.1, 8.1, 55)
        with open('MainMenuRes/char_statistic/techniques_adept.txt', 'w') as out:
                out.writelines([str(Snake_Eater.status) + "\n", str(Power_Blow.status) + "\n",str(Scholar.status) + "\n", str(Multiple_Shot.status) + "\n",
                                str(Duelist.status) + "\n", str(Bear_Trap.status) + "\n",str(Potion_Master.status) + "\n", str(Knock_Down.status) + "\n",
                                str(Battle_Reflex.status) + "\n", str(Persevere.status) + "\n",str(Moon_Shield.status) + "\n", str(Purifier.status) + "\n"])
        #-------------------------------------------------------------------------------------
        if skill_counter >=12:
            active_inactive_skill(display, 60,arming,'Arming',Readiness,7.1, 7.1, 33)
            active_inactive_skill(display, 60,melee,'Melee',Slice,8.1, 7.1, 28)
            active_inactive_skill(display, 60,engineering,'Engineering',War_Engineer,9.1, 7.1, 1)
            active_inactive_skill(display, 60,ranged,'Ranged',Deadeye,10.1, 7.1, 65)
            active_inactive_skill(display, 60,ranged,'Ranged',Barrage,11.1, 7.1, 39)
            active_inactive_skill(display, 60,tactics,'Tactics',Shields_Up,12.1, 7.1, 16)
            active_inactive_skill(display, 60,engineering,'Engineering',Field_Engineer,13.1, 7.1, 60)
            active_inactive_skill(display, 60,tactics,'Tactics',Charge,14.1, 7.1, 62)
            active_inactive_skill(display, 60,stupefy,'Stupefy',Reaper,15.1, 7.1, 75)
            active_inactive_skill(display, 60,athletics,'Athletics',Troll_Skin,16.1, 7.1, 32)
            active_inactive_skill(display, 60,arcane,'Arcane',Dream_Cloud,17.1, 7.1, 11)
            active_inactive_skill(display, 60,divine,'Divine',Second_Wind,18.1, 7.1, 9)
        with open('MainMenuRes/char_statistic/techniques_expert.txt', 'w') as out:
            out.writelines([str(Readiness.status) + "\n", str(Slice.status) + "\n",str(Field_Engineer.status) + "\n", str(Deadeye.status) + "\n",
                            str(Barrage.status) + "\n", str(Shields_Up.status) + "\n",str(War_Engineer.status) + "\n", str(Charge.status) + "\n",
                            str(Reaper.status) + "\n", str(Troll_Skin.status) + "\n",str(Dream_Cloud.status) + "\n", str(Second_Wind.status) + "\n"])
        #-------------------------------------------------------------------------------------
        if skill_counter >=18:
            active_inactive_skill(display, 80,stupefy,'Stupefy',Backstab,7.1, 6.1, 54)
            active_inactive_skill(display, 80,melee,'Melee',Weak_Spot,8.1, 6.1, 19)
            active_inactive_skill(display, 80,siege,'Siege',Siege_Master,9.1, 6.1, 12)
            active_inactive_skill(display, 80,ranged,'Ranged',Piercing_Arrows,10.1, 6.1, 2)
            active_inactive_skill(display, 80,investigation,'Investigation',Planewalker,11.1, 6.1, 22)
            active_inactive_skill(display, 80,tactics,'Tactics',Commander,12.1, 6.1, 63)
            active_inactive_skill(display, 80,engineering,'Engineering',Master_Mechanist,13.1, 6.1, 64)
            active_inactive_skill(display, 80,traps,'Traps',Battle_Prudence,14.1, 6.1, 43)
            active_inactive_skill(display, 80,arcane,'Arcane',Channelling,15.1, 6.1, 24)
            active_inactive_skill(display, 80,divine,'Divine',Divine_Intervention,16.1, 6.1, 67)
            active_inactive_skill(display, 80,arcane,'Arcane',Shadows,17.1, 6.1, 20)
            active_inactive_skill(display, 80,divine,'Divine',Blessing,18.1, 6.1, 41)
        with open('MainMenuRes/char_statistic/techniques_master.txt', 'w') as out:
            out.writelines([str(Backstab.status) + "\n", str(Weak_Spot.status) + "\n",str(Siege_Master.status) + "\n", str(Piercing_Arrows.status) + "\n",
                            str(Planewalker.status) + "\n", str(Commander.status) + "\n",str(Master_Mechanist.status) + "\n", str(Battle_Prudence.status) + "\n",
                            str(Channelling.status) + "\n", str(Divine_Intervention.status) + "\n",str(Shadows.status) + "\n", str(Blessing.status) + "\n"])

        #---------------------------------------------------------------------------------------------
        skill_counter = len([i for k in list_of_skills for i in k if i.status == 1])

        #---------------------------------------------------------------------------------------------
        # stat_list = []
        show_skills(display, skirmish_tree, 540, 14, 27, 0)
        show_skills(display, survival_tree, 856, 14, 27, 0)
        show_skills(display, savviness_tree, 1165, 14, 27, 0)
        show_skills(display, resistance_box, 365, 298, 0, 109)
        show_skills(display, attack_box, 475, 324, 0, 109)

        with open('MainMenuRes/char_statistic/charbonusstats.txt', 'w') as out:
            out.writelines(
                [str(bonus_melee.value) + "\n", str(bonus_ranged.value) + "\n", str(bonus_parrying.value) + "\n",
                 str(bonus_athletics.value) + "\n",
                 str(bonus_intimidation.value) + "\n", str(bonus_tactics.value) + "\n", str(bonus_arming.value) + "\n",
                 str(bonus_siege.value) + "\n",
                 str(bonus_acrobatics.value) + "\n", str(bonus_stealth.value) + "\n", str(bonus_thievery.value) + "\n",
                 str(bonus_lockpicking.value) + "\n",
                 str(bonus_deception.value) + "\n", str(bonus_traps.value) + "\n", str(bonus_stupefy.value) + "\n",
                 str(bonus_nature.value) + "\n",
                 str(bonus_investigation.value) + "\n", str(bonus_medicine.value) + "\n", str(bonus_lore.value) + "\n",
                 str(bonus_persuasion.value) + "\n",
                 str(bonus_arcane.value) + "\n", str(bonus_divine.value) + "\n", str(bonus_alchemy.value) + "\n",
                 str(bonus_engineering.value) + "\n"])

        # -----------------------------------ExperienceManagement------------------------------
        stats_draw_text(f'{learning_points}', fontStats, (0, 0, 0,), display, 1055, 652)
        exp_points_rect = pygame.Rect(1100, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), exp_points)
        if exp_points_rect.collidepoint(mouse_position):
            stats_draw_text('Learning points', fontDescription, (0, 0, 0,), display, 490, 690)

        stats_draw_text(f'{char_level}', fontStats, (0, 0, 0,), display, 538, 652)
        chat_level_rect = pygame.Rect(490, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), chat_level_rect)
        if chat_level_rect.collidepoint(mouse_position):
            stats_draw_text('Character level', fontDescription, (0, 0, 0,), display, 490, 690)

        stats_draw_text(f'{button.start_experience}', fontStats, (0, 0, 0,), display, 822, 652)
        char_experience_rect = pygame.Rect(760, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), char_experience_rect)
        if char_experience_rect.collidepoint(mouse_position):
            stats_draw_text('Experience', fontDescription, (0, 0, 0,), display, 490, 690)

        # -----------------------------------Tricks/Supply------------------------------
        stats_draw_text(str(tricks), fontStats, (0, 0, 0,), display, 410, 655)
        tricks_rect = pygame.Rect(360, 652, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), tricks_rect)
        if tricks_rect.collidepoint(mouse_position):
            stats_draw_text('Tricks are required to use abilities in battle',
                            fontDescription, (0, 0, 0,), display, 490, 690)

        stats_draw_text(str(supply), fontStats, (0, 0, 0,), display, 410, 688)
        supply_rect = pygame.Rect(360, 690, 30, 30)
        # pygame.draw.rect(screen, (255,0,0), supply_rect)
        if supply_rect.collidepoint(mouse_position):
            stats_draw_text('Supply is required to use consumables in battle',
                            fontDescription, (0, 0, 0,), display, 490, 690)

        # -----------------------------------HP/ARM-----------------------------
        button_hero_hp = pygame.Rect(1160, 652, 35, 35)
        # pygame.draw.rect(screen, (255,0,0), button_hero_hp)
        if button_hero_hp.collidepoint(mouse_position):
            stats_draw_text('Health points', fontDescription, (0, 0, 0,), display, 490, 690)
        stats_draw_text(f'{health_points}', fontStats, (0, 0, 0,), display, 1205, 654)

        button_hero_armor = pygame.Rect(1160, 690, 35, 35)
        # pygame.draw.rect(screen, (255,0,0), button_hero_armor)
        if button_hero_armor.collidepoint(mouse_position):
            stats_draw_text('Armor points', fontDescription, (0, 0, 0,), display, 490, 690)
        stats_draw_text(f'{armor_points}', fontStats, (0, 0, 0,), display, 1205, 685)

        # -------------------------------------------------------------------------
        menuClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), 0, 32)

            if event.type == KEYDOWN:
                #if event.key == K_ESCAPE:
                   #pass
                if event.key == K_o:
                    button.fullscreen = not button.fullscreen
                    fullscreen = button.fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

                #if event.key == K_p:
                   #movement_modifier +=0.5
                #    button.experience +=100
                #    button.start_experience = button.experience
                #    print(button.new_level)
                #    print(button.experience)
                # --------------------------------
                if event.key == K_v:
                    learning_points +=100
                if event.key == K_b:
                   pass
                # button.experience += 800
                # button.start_experience = button.experience
                # print(button.start_experience)

            player_movement = [0, 0]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    menuClick = True

            if event.type == KEYDOWN:
                #---------------------------------
                if event.key == K_c and toggle_char_sheet == False:
                    display = pygame.Surface((1280, 720))
                    toggle_char_sheet = True
                    block_movement = True
                    map_borders = False
                    scroll_sound.play()

                elif event.key == K_c and toggle_char_sheet == True:
                    display = pygame.Surface((800, 600))
                    toggle_char_sheet = False
                    block_movement = False
                    map_borders = True

                if event.key == K_j and toggle_journal == False:
                    toggle_journal = True
                    scroll_sound.play()
                elif event.key == K_j and toggle_journal == True:
                    toggle_journal = False

                if event.key == K_ESCAPE and toggle_game_menu == False:
                    toggle_game_menu = True
                elif event.key == K_ESCAPE and toggle_game_menu == True:
                    toggle_game_menu = False

                if event.key == K_ESCAPE and toggle_game_menu == False:
                    toggle_game_menu = True
                    scroll_sound.play()
                elif event.key == K_ESCAPE and toggle_game_menu == True:
                    toggle_game_menu = False

                    # --------------------------------
                if block_movement == False:
                    if event.key == K_d:
                        moving_right = True
                    if event.key == K_a:
                        moving_left = True
                    if event.key == K_s:
                        moving_down = True
                    if event.key == K_w:
                        moving_up = True

            if event.type == KEYUP:
                if event.key == K_d:
                    moving_right = False
                if event.key == K_a:
                    moving_left = False
                if event.key == K_w:
                    moving_up = False
                if event.key == K_s:
                    moving_down = False

            #----------------------------------EventHandlers---------------------------------
            for i in list_of_items:
                for j in i:
                    j.event_handler(event)
            for i in list_of_skills:
                for j in i:
                    j.event_handler(event)
            for i in items_in_chest:
                if i != None:
                    i.chest_event_handler(event)

            for i in list_of_traders:
                  i.event_handler(event)

            for i in trader_items:
                if i != None:
                    i.store_event_handler(event)
            for i in alchemist_items:
                if i != None:
                    i.store_event_handler(event)
            for i in smith_items:
                if i != None:
                    i.store_event_handler(event)
            for i in tavern_items:
                if i != None:
                    i.store_event_handler(event)
            for i in board_items:
                if i != None:
                    i.quest_npc_event_handler()

            sell_item.event_handler(event)
            steal_item.event_handler(event)
            inventory_button.event_handler(event)
            troops_button.event_handler(event)


        #--------------------------------------------------------------------------------

        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.mouse.set_visible(False)
        mouse_position = pygame.mouse.get_pos()
        player_rect.x, player_rect.y = mouse_position
        screen.blit(normal_icon, player_rect)















































        # display.fill((170,140,100))
        if toggle_char_sheet == False:
            display.fill('#192740')
            gm_draw_map()
            gm_draw_bag()
            # gm_draw_injury()

            gm_draw_text('Press ESC for Menu', fontDescription, (0, 225, 0), 10, 10)

        scroll[0] += (GM_player_rect.x - scroll[0] - 300) / 20
        scroll[1] += (GM_player_rect.y - scroll[1] - 200) / 20

        pygame.mouse.set_visible(False)

        mouse_position = pygame.mouse.get_pos()
        GM_player_rect.x, GM_player_rect.y = mouse_position
        # -----------------------------------MapCollisions---------------------------------------
        line_0 = pygame.Rect(590 - scroll[0], 60 - scroll[1], 335, 5)
        line_1 = pygame.Rect(590 - scroll[0], 55 - scroll[1], 5, 300)
        line_2 = pygame.Rect(590 - scroll[0], 350 - scroll[1], 170, 5)
        line_3 = pygame.Rect(920 - scroll[0], 65 - scroll[1], 10, 150)
        line_4 = pygame.Rect(805 - scroll[0], 260 - scroll[1], 90, 10)
        line_5 = pygame.Rect(805 - scroll[0], 260 - scroll[1], 10, 55)
        line_6 = pygame.Rect(885 - scroll[0], 215 - scroll[1], 10, 50)
        line_7 = pygame.Rect(760 - scroll[0], 310 - scroll[1], 50, 10)
        line_8 = pygame.Rect(890 - scroll[0], 210 - scroll[1], 40, 10)
        line_9 = pygame.Rect(755 - scroll[0], 305 - scroll[1], 10, 50)
        line_10 = pygame.Rect(760 - scroll[0], 60 - scroll[1], 60, 20)
        #------------------------------------CollisionTiles----------------------------
        tile_rects = []
        if westrad_borders == True:
           tile_rects.extend([line_0, line_1, line_2, line_3,line_4, line_5, line_6, line_7,line_8, line_9, line_10])
        # for i in tile_rects:
        #     pygame.draw.rect(display, (255,0,0), i)


# ---------------------------PartyMovement---------------------------------------
        player_party = PlayerParty(800-scroll[0], 180-scroll[1])
        player_party.move(tile_rects)
        if toggle_char_sheet == False and party_icon == True:
           player_party.draw()


        # ---------------------------SoundCounter---------------------------------------
        playSoundScroll_counter += 1
        if playSoundScroll_counter >= 11:
            playSoundScroll = True
            playSoundScroll_counter = 0

        whileSound_counter += 1
        if whileSound_counter >= 11:
            whileSound = True
            whileSound_counter = 0

        trapCounter += 1
        if trapCounter >= 101:
            trapSound = True
            trapCounter = 0

        #-----------------------------cartographer------------------------------------
        if Cartographer.status == 1:
           player_party.speed = 0.4
        # ---------------------------Healing-------------------------------------------
        if moving_right or moving_down or moving_left or moving_up == True:
            healing_timer += 1
            if Camp_Doctor.status == 1:
               healing_tick = 400 - (int((button.medicine * 400) / 100) * 0.5)
            else:
               healing_tick = 600 - (int((button.medicine * 600) / 100) * 0.5)
            if healing_timer >= healing_tick:
                healing_timer = 0
                if button.PartyHealth < 100:
                   button.PartyHealth += 1


        # ---------------------------PartyMovement---------------------------------
        if block_movement == False:
            if moving_right == True:
               party_movement[0] += player_party.speed
            if moving_left == True:
               party_movement[0] -= player_party.speed
            if moving_up == True:
               party_movement[1] -= player_party.speed
            if moving_down == True:
               party_movement[1] += player_party.speed
        # ---------------------RectMapBorders----------------------------------
        if map_borders == True:
            if GM_player_rect.x >= 740:
               GM_player_rect.x = 740
            if GM_player_rect.x <= 100:
               GM_player_rect.x = 100

            if GM_player_rect.y >= 460:
               GM_player_rect.y = 460
            if GM_player_rect.y <= 100:
               GM_player_rect.y = 100

# -----------------------------------Events-----------------------------------------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), 0, 32)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if event.button == 1:
                    pass
                    # for i in party_group.sprites():
                    #     i.set_target(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pass

            if event.type == KEYDOWN:
                # ---------------------------------
                if event.key == K_c and toggle_char_sheet == False:
                    display = pygame.Surface((1280, 720))
                    toggle_char_sheet = True
                    block_movement = True
                    map_borders = False
                    scroll_sound.play()
                elif event.key == K_c and toggle_char_sheet == True:
                    display = pygame.Surface((800, 600))
                    toggle_char_sheet = False
                    block_movement = False
                    map_borders = True

                if event.key == K_j and toggle_journal == False:
                    toggle_journal = True
                    scroll_sound.play()
                elif event.key == K_j and toggle_journal == True:
                    toggle_journal = False

                if event.key == K_ESCAPE and toggle_game_menu == False:
                    toggle_game_menu = True
                elif event.key == K_ESCAPE and toggle_game_menu == True:
                    toggle_game_menu = False

                if event.key == K_d:
                    moving_right = True
                if event.key == K_a:
                    moving_left = True
                if event.key == K_s:
                    moving_down = True
                if event.key == K_w:
                    moving_up = True
                # ---------------------------------
                if event.key == K_o:
                    fullscreen = not fullscreen
                    button.fullscreen = not button.fullscreen
                    fullscreen = button.fullscreen

                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

            if event.type == KEYUP:
                if event.key == K_d:
                    moving_right = False
                if event.key == K_a:
                    moving_left = False
                if event.key == K_w:
                    moving_up = False
                if event.key == K_s:
                    moving_down = False


# ------------------------------------Mines-------------------------------------------
        westrad_coal_mine = Mine(display,  840-scroll[0],155-scroll[1],mines_img[0], 'visible',250,f'{button.westrad_coal_mine}')
        westrad_ore_mine_0 = Mine(display,  725-scroll[0],240-scroll[1],mines_img[1], 'visible',500,f'{button.westrad_ore_mine_0}')
        westrad_ore_mine_1 = Mine(display,  715-scroll[0],150-scroll[1],mines_img[1], 'visible',500,f'{button.westrad_ore_mine_1}')
        westrad_gold_mine = Mine(display,  640-scroll[0],230-scroll[1],mines_img[3], 'visible',1000,f'{button.westrad_gold_mine}')

        charlatan_silver_mine = Mine(display,  965-scroll[0],240-scroll[1],mines_img[2], 'visible',750,f'{button.charlatan_silver_mine}')
        charlatan_coal_mine = Mine(display,  1000-scroll[0],330-scroll[1],mines_img[0], 'visible',250,f'{button.charlatan_coal_mine}')

        solomir_silver_mine = Mine(display,  700-scroll[0],550-scroll[1],mines_img[2], 'visible',750,f'{button.solomir_silver_mine}')
        solomir_gold_mine_0 = Mine(display,  450-scroll[0],560-scroll[1],mines_img[3], 'visible',1000,f'{button.solomir_gold_mine_0}')
        solomir_gems_mine = Mine(display,  260-scroll[0],630-scroll[1],mines_img[4], 'visible',1500,f'{button.solomir_gems_mine}')
        solomir_gold_mine_1 = Mine(display,  600-scroll[0],640-scroll[1],mines_img[3], 'visible',1000,f'{button.solomir_gold_mine_1}')

        kharfajian_gems_mine_0 = Mine(display,  310-scroll[0],100-scroll[1],mines_img[4], 'visible',1500,f'{button.kharfajian_gems_mine_0}')
        kharfajian_gems_mine_1 = Mine(display,  100-scroll[0],460-scroll[1],mines_img[4], 'visible',1500,f'{button.kharfajian_gems_mine_1}')
        kharfajian_krystal_mine = Mine(display,  220-scroll[0],280-scroll[1],mines_img[5], 'visible',2000,f'{button.kharfajian_krystal_mine}')

        mines_box.extend([westrad_coal_mine,westrad_ore_mine_0,westrad_ore_mine_1,westrad_gold_mine,charlatan_silver_mine,charlatan_coal_mine,
                          solomir_silver_mine,solomir_gold_mine_0,solomir_gold_mine_1,solomir_gems_mine,kharfajian_gems_mine_0,kharfajian_gems_mine_1,
                          kharfajian_krystal_mine])

        mines_group = pygame.sprite.Group()
        mines_group.add(westrad_coal_mine, westrad_ore_mine_0,westrad_ore_mine_1,westrad_gold_mine,charlatan_silver_mine,charlatan_coal_mine,
                        solomir_silver_mine,solomir_gold_mine_0,solomir_gold_mine_1,solomir_gems_mine,kharfajian_gems_mine_0,kharfajian_gems_mine_1,
                        kharfajian_krystal_mine)

        mine_encounter(display, westrad_coal_mine, scr_mines_img[0], 'Coal Mine',38,30)
        mine_encounter(display, westrad_ore_mine_0, scr_mines_img[1], 'Ore Mine',38,30)
        mine_encounter(display, westrad_ore_mine_1, scr_mines_img[1], 'Ore Mine',38,30)
        mine_encounter(display, westrad_gold_mine, scr_mines_img[3], 'Gold Mine',38,30)
        mine_encounter(display, charlatan_silver_mine, scr_mines_img[2], 'Silver Mine',38,30)
        mine_encounter(display, charlatan_coal_mine, scr_mines_img[0], 'Coal Mine',38,30)
        mine_encounter(display, solomir_gold_mine_0, scr_mines_img[3], 'Gold Mine',38,30)
        mine_encounter(display, solomir_gold_mine_1, scr_mines_img[3], 'Gold Mine',38,30)
        mine_encounter(display, solomir_gems_mine, scr_mines_img[4], 'Gems Mine',38,30)
        mine_encounter(display, solomir_silver_mine, scr_mines_img[2], 'Silver Mine',38,30)
        mine_encounter(display, kharfajian_gems_mine_0, scr_mines_img[4], 'Gems Mine',38,30)
        mine_encounter(display, kharfajian_gems_mine_1, scr_mines_img[4], 'Gems Mine',38,30)
        mine_encounter(display, kharfajian_krystal_mine, scr_mines_img[5], 'Krystal Mine',30,30)

        for i in mines_box:
            if i.initiate():
                if i == westrad_coal_mine: initiate_encounter(99,1)
                elif i == westrad_ore_mine_0: initiate_encounter(98,1)
                elif i == westrad_ore_mine_1: initiate_encounter(97,1)
                elif i == westrad_gold_mine: initiate_encounter(96,1)
                elif i == charlatan_silver_mine: initiate_encounter(95,1)
                elif i == charlatan_coal_mine: initiate_encounter(94,1)
                elif i == solomir_silver_mine: initiate_encounter(93,1)
                elif i == solomir_gold_mine_0: initiate_encounter(92,1)
                elif i == solomir_gold_mine_1: initiate_encounter(91,1)
                elif i == solomir_gems_mine: initiate_encounter(90,1)
                elif i == kharfajian_gems_mine_0: initiate_encounter(89,1)
                elif i == kharfajian_gems_mine_1: initiate_encounter(88,1)
                elif i == kharfajian_krystal_mine: initiate_encounter(87,1)

        # ------------------------------Income------------------------------------------
        #income = sum([i.value for i in mines_box if i.owner == 'player'])
        income = 0
        if westrad_ore_mine_0.owner == 'player': income +=westrad_ore_mine_0.value
        if westrad_ore_mine_1.owner == 'player': income +=westrad_ore_mine_1.value
        if westrad_coal_mine.owner == 'player': income +=westrad_coal_mine.value
        if westrad_gold_mine.owner == 'player': income +=westrad_gold_mine.value
        if charlatan_silver_mine.owner == 'player': income +=charlatan_silver_mine.value
        if charlatan_coal_mine.owner == 'player': income +=charlatan_coal_mine.value
        if solomir_gold_mine_0.owner == 'player': income +=solomir_gold_mine_0.value
        if solomir_gold_mine_1.owner == 'player': income +=solomir_gold_mine_1.value
        if solomir_gems_mine.owner == 'player': income +=solomir_gems_mine.value
        if kharfajian_gems_mine_0.owner == 'player': income +=kharfajian_gems_mine_0.value
        if kharfajian_gems_mine_1.owner == 'player': income +=kharfajian_gems_mine_1.value
        if kharfajian_krystal_mine.owner == 'player': income +=kharfajian_krystal_mine.value

    #-------------------------------------------------------------------------------
        if moving_right or moving_down or moving_left or moving_up == True:
            income_timer += 1
            if income_timer >= 800:
               if Estates.status == 1:
                  button.wealth += int(income*1.25)
               else:
                   button.wealth += income
               button.start_wealth = button.wealth
               if income > 0:
                  coins_sound.play()
               income_timer = 0
               print(f'Your income is {income}')

# ------------------------------------WorldMapQuestsList-------------------------------------
        old_ways = Quest(745 - scroll[0], 145 - scroll[1], gm_quest_icon, quest_img[0], 'Old Ways',
                         f'{button.quest_old_ways}')

        quest_box.append(old_ways)
        # quest_box.extend((dire_wolves,highwaymen,dragonhunt, finale))
        quest_group = pygame.sprite.Group()

        # party_group =pygame.sprite.Group()
        # party_group.add(party)
      # --------------------------------WorldMapQuestsDetails-----------------------------------
        if old_ways.status == 'unlocked':
            quest_group.add(old_ways)  # add quests here too
            if old_ways.initiate():
                pygame.mixer.music.fadeout(1500)
                initiate_encounter(1,1)

            old_ways.draw_story(old_ways_lore, 110, 155)
        elif old_ways.status == 'locked':
            if toggle_char_sheet == False:
                old_ways.quest_unavailable()

#-------------------------------------Settlements-----------------------------------
        town_group = pygame.sprite.Group()
        #--------------------------------Cleonel--------------------------------------
        cleonel = Town(display, city_icon,777-scroll[0], 190-scroll[1],'visible')
        if cleonel.rect.colliderect(player_party.rect):
           town_group.add(cleonel)
           cleonel.initiate(display,settlement_window,TILE_SIZE*3.5, TILE_SIZE*1,
                             settlement_img[0],TILE_SIZE*3.74, TILE_SIZE*1.15,
                             "Cleonel", fontMenu,(80,50,40),TILE_SIZE*3.80, TILE_SIZE*1.20)
           CleonelTemple.draw(display, font12, CleonelTemple.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*6, TILE_SIZE*2.2)
           CleonelTrader.draw(display, font12, CleonelTrader.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*4.5, TILE_SIZE*3)
           CleonelPort.draw(display, font12, CleonelPort.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*5.8, TILE_SIZE*4.4)
           CleonelSmith.draw(display, font12, CleonelSmith.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*5.5, TILE_SIZE*2.8)
           CleonelAlchemist.draw(display, font12, CleonelAlchemist.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*5.2, TILE_SIZE*3.6)
           CleonelTavern.draw(display, font12, CleonelTavern.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*4.6, TILE_SIZE*3.8)
           CleonelBoard.draw(display, font12, CleonelBoard.description, (80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE, TILE_SIZE*6.6, TILE_SIZE*3.5)
           #------------------------------------------Trader--------------------------
           CleonelTrader.initiate(nek_0,hat_0,rng_0,glv_0,bow_1,dag_4)
           item_col = 0
           item_row = 0
           if CleonelTrader.toggled == True and toggle_char_sheet == False:
              for count,i in enumerate(trader_items[:6]):
                    if i != None:
                        i.draw_chest_item(display,TILE_SIZE*3.5, TILE_SIZE*6.2, item_col*TILE_SIZE*0.8,item_row*TILE_SIZE*1.4)
                        i.available = True
                        i.stored_item_info(display,font12,i.info,i.value,(80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE)
                        item_col += 1
                        if item_col == 6:item_row += 1;item_col = 0
           elif CleonelTrader.toggled == False and toggle_char_sheet == False:
               for count,i in enumerate(trader_items[:6]):
                    if i != None:
                        i.available = False

        #---------------------------------------Smith-------------------------------
           CleonelSmith.initiate(hat_8,srd_0,blt_0,sho_1,pnt_2,dag_5)
           item_col = 0
           item_row = 0
           if CleonelSmith.toggled == True and toggle_char_sheet == False:
               for count,i in enumerate(smith_items[:6]):
                   if i != None:
                       i.draw_chest_item(display,TILE_SIZE*3.5, TILE_SIZE*6.2, item_col*TILE_SIZE*0.8,item_row*TILE_SIZE*1.4)
                       i.available = True
                       i.stored_item_info(display,font12,i.info,i.value,(80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE)
                       item_col += 1
                       if item_col == 6:item_row += 1;item_col = 0
           elif CleonelSmith.toggled == False and toggle_char_sheet == False:
               for count,i in enumerate(smith_items[:6]):
                   if i != None:
                       i.available = False

           #---------------------------------------Tavern-------------------------------
           CleonelTavern.initiate(hire_dunstan,hire_alba,hire_anselm,hire_regina,hire_bartelago,hire_severin)
           item_col = 0
           item_row = 0
           if CleonelTavern.toggled == True and toggle_char_sheet == False:
               for count,i in enumerate(tavern_items[:6]):
                   if i != None:
                       i.draw_chest_item(display,TILE_SIZE*3.5, TILE_SIZE*6.2, item_col*TILE_SIZE*0.8,item_row*TILE_SIZE*1.4)
                       i.available = True
                       i.stored_item_info(display,font12,i.info,i.value,(80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE)
                       item_col += 1
                       if item_col == 6:item_row += 1;item_col = 0
           elif CleonelTavern.toggled == False and toggle_char_sheet == False:
               for count,i in enumerate(tavern_items[:6]):
                   if i != None:
                       i.available = False

           #--------------------------------------Alchemist--------------------------------
           CleonelAlchemist.initiate(None,ptn_5,None,ptn_3,ptn_20,None)
           item_col = 0
           item_row = 0
           if CleonelAlchemist.toggled == True and toggle_char_sheet == False:
                for count,i in enumerate(alchemist_items[:6]):
                    if i != None:
                        i.draw_chest_item(display,TILE_SIZE*3.55, TILE_SIZE*6.2, item_col*TILE_SIZE*0.8,item_row*TILE_SIZE*1.4)
                        i.available = True
                        i.stored_item_info(display,font12,i.info,i.value,(80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE)
                        item_col += 1
                        if item_col == 6:item_row += 1;item_col = 0
           elif CleonelAlchemist.toggled == False and toggle_char_sheet == False:
                for count,i in enumerate(alchemist_items[:6]):
                    if i != None:
                       i.available = False
                       alchemist_items = []
           #--------------------------------------CityBoard--------------------------------
           CleonelBoard.initiate(qst_0,None,None,None,None,None)
           item_col = 0
           item_row = 0
           if CleonelBoard.toggled == True and toggle_char_sheet == False:
               for count,i in enumerate(board_items[:6]):
                   if i != None:
                       i.draw_chest_item(display,TILE_SIZE*3.55, TILE_SIZE*6.2, item_col*TILE_SIZE*0.8,item_row*TILE_SIZE*1.4)
                       i.available = True
                       i.stored_item_info(display,font12,i.info,None,(80,50,40),3.6*TILE_SIZE,5.6*TILE_SIZE)
                       item_col += 1
                       if item_col == 6:item_row += 1;item_col = 0
           elif CleonelBoard.toggled == False and toggle_char_sheet == False:
               for count,i in enumerate(board_items[:6]):
                   if i != None:
                       i.available = False

        #--------------------------------Bellenau--------------------------------------
        bellenau = Town(display, city_icon,860-scroll[0], 230-scroll[1],'visible')
        #--------------------------------Riversmouth--------------------------------------
        riversmouth = Town(display, city_icon,650-scroll[0], 130-scroll[1],'visible')
        #--------------------------------Westrad--------------------------------------
        westrad = Town(display, city_icon,640-scroll[0], 340-scroll[1],'visible')
        #--------------------------------Longdale--------------------------------------
        longdale = Town(display, city_icon,660-scroll[0], 270-scroll[1],'visible')
        #--------------------------------taernsby--------------------------------------
        taernsby = Town(display, city_icon,980-scroll[0], 280-scroll[1],'visible')
        #--------------------------------ramshorn--------------------------------------
        ramshorn = Town(display, city_icon,992-scroll[0], 390-scroll[1],'visible')
        #--------------------------------kilereth--------------------------------------
        kilereth = Town(display, city_icon,777-scroll[0], 535-scroll[1],'visible')
        #--------------------------------orilons_path--------------------------------------
        orilons_path = Town(display, city_icon,715-scroll[0], 510-scroll[1],'visible')
        #--------------------------------dalry--------------------------------------
        dalry = Town(display, city_icon,650-scroll[0], 600-scroll[1],'visible')
        #--------------------------------bellmare--------------------------------------
        bellmare = Town(display, city_icon,545-scroll[0], 625-scroll[1],'visible')
        #--------------------------------erimore--------------------------------------
        erimore = Town(display, city_icon,300-scroll[0], 590-scroll[1],'visible')
        #--------------------------------karas_vale--------------------------------------
        karas_vale = Town(display, city_icon,75-scroll[0], 555-scroll[1],'visible')
        #--------------------------------dawn_sister--------------------------------------
        dawn_sister = Town(display, city_icon,240-scroll[0], 360-scroll[1],'visible')
        #--------------------------------dusk_sister--------------------------------------
        dusk_sister = Town(display, city_icon,190-scroll[0], 420-scroll[1],'visible')
        #--------------------------------karak--------------------------------------
        karak = Town(display, city_icon,30-scroll[0], 450-scroll[1],'visible')
        #--------------------------------currinae---------------------------------
        currinae = Town(display, city_icon,77-scroll[0], 390-scroll[1],'visible')
        #--------------------------------maraketh---------------------------------
        maraketh = Town(display, city_icon,426-scroll[0], 186-scroll[1],'visible')
        #--------------------------------yarrin-----------------------------------
        yarrin = Town(display, city_icon,380-scroll[0], 115-scroll[1],'visible')
        #--------------------------------kharfageth-------------------------------
        kharfageth = Town(display, city_icon,297-scroll[0], 140-scroll[1],'visible')
        #--------------------------------hersoneth-------------------------------
        hersoneth = Town(display, city_icon,180-scroll[0], 200-scroll[1],'visible')


    #--------------------------------------------------------------------------------
        with open('MainMenuRes/inventory/unlocked_potions.json', 'w') as f:
            i = json.dumps(potions_dict, indent=2)
            f.write(i)
        f.close()

        with open('MainMenuRes/inventory/unlocked_troops.json', 'w') as g:
            l = json.dumps(troops_dict, indent=2)
            g.write(l)
        g.close()
        #--------------------------------------------------------------------------------
        town_box.extend([cleonel,bellenau,riversmouth,westrad,longdale,taernsby,ramshorn,
                         kilereth,orilons_path,dalry,bellmare,erimore, karas_vale, dawn_sister,
                         dusk_sister, karak, currinae, maraketh,yarrin, kharfageth, hersoneth])

        # town_group = pygame.sprite.Group()
        # town_group.add(cleonel,bellenau,riversmouth,westrad,longdale,taernsby,ramshorn,
        #                kilereth,orilons_path,dalry,bellmare,erimore, karas_vale, dawn_sister,
        #                dusk_sister, karak, currinae, maraketh,yarrin, kharfageth, hersoneth)


    #----------------------------------Chests------------------------------------------------
        #surface,x, y, img, investigation,difficulty, trap, status):
        chest1 = Chest(display,875 - scroll[0],215 - scroll[1], chest_icon, 0,0,0,'visible')
        if chest1.rect.colliderect(player_party.rect):
           chest1.initiate(bow_0, dag_6, srd_1, pnt_0,arm_0, sho_0, clk_0,glv_1) # add items by id
        item_col = 0
        item_row = 0
        if chest1.toggled == True and toggle_char_sheet == False:
           for count,i in enumerate(items_in_chest[:8]):
               if i != None:
                   i.draw_chest_item(display,TILE_SIZE*4.7, TILE_SIZE*3, item_col*TILE_SIZE*0.95,item_row*TILE_SIZE*1.3)
                   i.available = True
                   item_col += 1
                   if item_col == 4:item_row += 1;item_col = 0
        elif chest1.toggled == False and toggle_char_sheet == False:
           for count,i in enumerate(items_in_chest[:8]):
                if i != None:
                    i.available = False

        #----------------------------------------NewChests-------------------------------------
        chest_box.extend([chest1])

        chest_group = pygame.sprite.Group()
        chest_group.add(chest1)

        #add_stored_items(items_in_chest)
        #remove_stored_items(items_in_chest)    -  working
        #-------------------------------------dialogs--------------------------------------
        if npc_0.clicked:
           dialog_1.initiate(display)
           dialog_1.toggled = True
        if dialog_1.toggled == True:
            if dialog_1.phase == 0: dialog_1.get_line(display,"dialog",l_portrait_img[1],"rowan",1,"4",0,0,None,0,0)
            if dialog_1.phase == 1:
               dialog_1.get_resp(display,"dialog",r_portrait_img[3],"city guard",0,"1",0,0)
               if letter_1 in inv_list: inv_list.remove(letter_1)
            if dialog_1.phase == 2:
               npc_0.clicked = False
               dialog_1.toggled = False
        #------------------------------------------------------------------------------------
        dialog_0.toggled = False
        if dialog_0.toggled == True:
            dialog_0.initiate(display)
            if dialog_0.phase == 0: dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"1",0,0,None,0,0)
            if dialog_0.phase == 1:
                dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"2",0,0,None,0,0)
                #dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"5",0,25,'Deception',deception,20)
            if dialog_0.phase == 2:dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"3",0,0,None,0,0)
            if dialog_0.phase == 3:dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"1",0,0)
            if dialog_0.phase == 4:dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"4",0,0,None,0,0)
            if dialog_0.phase == 5:dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"5",0,0,None,0,0)
            if dialog_0.phase == 6:dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"2",0,0)
            if dialog_0.phase == 7:dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"3",0,0)
            if dialog_0.phase == 8:dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"4",0,0)
            if dialog_0.phase == 9:dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"6",0,0,None,0,0)
            if dialog_0.phase == 10:
                dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"5",0,0)
                dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"5_1",0,25)
            if dialog_0.phase == 11:dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"6",0,0)
            if dialog_0.phase == 12:dialog_0.get_resp(display,"dialog",r_portrait_img[2],"captain",0,"7",0,0)
            if dialog_0.phase == 13:dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"7",0,0,None,0,0)
            if dialog_0.phase == 14:prologue.draw_story(display,0,0)

        # -------------------------InvisibilityChecks-------------------------
        for i in mines_box:
            i.hide_mine()
        for i in quest_box:
            i.hide_quest()

        # for i in town_box:
        #     i.hide_town()
        # for i in chest_box:
        #     i.hide_chest()
        # ------------------------------------WorldMapQuests------------------------------------
        if toggle_char_sheet == False:
            for i in mines_group:
                if i.status != 'invisible':
                    quest_group.draw(display)
                    quest_group.update()
                if i.rect.colliderect(player_party.rect):
                    party_icon = False
            for j in mines_group:
                if j.status != 'invisible':
                    mines_group.draw(display)
                    mines_group.update()
                if j.rect.colliderect(player_party.rect):
                    party_icon = False
            for k in chest_group:
                if k.status != 'invisible' and k.rect.colliderect(player_party.view):
                    chest_group.draw(display)
                    chest_group.update()
                if k.rect.colliderect(player_party.rect):
                    party_icon = False

            for l in town_group:
                        #town_group.draw(display)
                        #town_group.update()
                if l.rect.colliderect(player_party.rect):
                    party_icon = False

            # for h in chapter_box:
            #     if h.toggled == True:
            #         party_icon = False

        # party_group.update()
        # party_group.draw(display)
        # ------------------------------------RandomEncounters----------------------------
        if Scout.status == 1:
           escape_chance = int((nature+stealth)/2 + luck/2)+25
        else:
            escape_chance = int((nature+stealth)/2 + luck/2)
        if moving_right or moving_down or moving_left or moving_up == True:
            encounter_timer += 1
        if encounter_timer <= 299:
            block_movement = False
        if encounter_timer == 300:
           encounter_chance = random.randint(0, 100)
           print(encounter_chance)
        if encounter_timer >= 300 and encounter_chance <= 50:
             encounter = True
             encounter_timer = 0
             throw_dice = True
        elif encounter_timer >= 300 and encounter_chance > 50:
             encounter_timer = 0
        if encounter == True:
            show_message('Your party is ambushed!', fontStats, (0, 0, 0), 300, 260)
            block_movement = True
            if throw_dice == True:
                dice = random.randint(0, 1)
                throw_dice = False
            for i, j in enumerate(encounter_box):
                if dice == j.probability:
                    global escape_attempt
                    escape_attempt = escape_chance - j.difficulty
                    j.encounter_text(f'{j.type}', fontStats, (0, 0, 0), j.x, j.y)
                    j.encounter_text(f'({escape_attempt}%)', fontDescription, (0, 0, 0), 460, 326)
            yes_button = button.Button(display, 385, 330, gm_check, 15, 20, 0, True, 'Yes')
            no_button = button.Button(display, 435, 330, gm_cross, 15, 20, 0, True, 'No')
            yes_button.draw()
            no_button.draw()
            if escape_dice == True:
                escape_difficulty = random.randint(0, 100)
                escape_dice = False
            if yes_button.rect.collidepoint(mouse_position):
                display.blit(gm_greencheck, (yes_button.rect.x - 4, yes_button.rect.y))
            elif no_button.rect.collidepoint(mouse_position):
                display.blit(gm_greencross, (no_button.rect.x - 4, no_button.rect.y))
            if yes_button.clicked == True:
                if dice == 0:
                    initiate_encounter(1,0)
                    encounter = False
                elif dice == 1:
                    initiate_encounter(2,0)
                    encounter = False
            # elif no_button.clicked == True and escape_attempt < escape_difficulty:
            #       gm_draw_text('No luck!', GM_font_Lore, (0,200,0), 420, 350)
            elif no_button.clicked == True: #and escape_attempt >= escape_difficulty:
                encounter = False
                block_movement = False
                encounter_timer = 0
            # elif escape_attempt < random.randint(0,100) and no_button.clicked == True:

        #------------------------------------BlockMovement-----------------------------------
        if toggle_char_sheet == True:
           block_movement = True
        #print(block_movement)
        # -----------------------------------timewheel-----------------------------------------------
        rowan_frame += 1
        try:
            if rowan_frame >= len(animation_database[rowan_action]):  # 2300
                rowan_frame = 0

            rowan_img_id = animation_database[rowan_action][rowan_frame]  # animation_database[timewheel][0]
            rowan_img = animation_frames[rowan_img_id]  # [frame_0] for frame_0.png
        except:
            pass
        if toggle_char_sheet == True:
            display.blit(rowan_img, (rowan_rect.x, rowan_rect.y))

        if moving_right or moving_down or moving_left or moving_up == True:
            timewheel_frame += 1
        if timewheel_frame >= len(animation_database[timewheel_action]):  # 2300
            timewheel_frame = 0

        timewheel_img_id = animation_database[timewheel_action][timewheel_frame]  # animation_database[timewheel][0]
        timewheel_img = animation_frames[timewheel_img_id]  # [frame_0] for frame_0.png
        #----------------------------------------------------------------------------------
        if toggle_char_sheet == False:
            display.blit(timewheel_img, (timewheel_rect.x, timewheel_rect.y))
            PartyStatus.draw(button.PartyHealth)
        # --------------------------------------------------------------------------------
        if toggle_game_menu == True and toggle_char_sheet == False:
           game_menu(display)

        if toggle_journal == True and toggle_char_sheet == False:
            journal.initiate()
       #-----------------------------------LevelUp--------------------------------------
        level_up()

        game_over(display)

        display.blit(GM_normal_icon, GM_player_rect)  # mouse cursor

        for i in quest_group:
            if i.rect.collidepoint(mouse_position):
                pygame.mouse.set_visible(False)
                display.blit(GM_select_icon, mouse_position)
        for i in mines_group:
            if i.rect.collidepoint(mouse_position):
                pygame.mouse.set_visible(False)
                display.blit(GM_select_icon, mouse_position)
        for i in chest_group:
            if i.rect.collidepoint(mouse_position):
                pygame.mouse.set_visible(False)
                display.blit(GM_select_icon, mouse_position)
        for i in town_group:
            if i.rect.collidepoint(mouse_position):
                pygame.mouse.set_visible(False)
                display.blit(GM_select_icon, mouse_position)
        # for i in town_box:
        #     if i.entered == False:
        #         alchemist_items = []
        #         smith_items = []
        #         trader_items = []
        #         tavern_items = []
        #         board_items = []

        # for event in pygame.event.get():
        #     for i in items_in_chest:
        #         i.event_handler(event)
        # ---------------------------------------------------------------------
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        # screen.blit(pygame.transform.scale(display,WINDOW_SIZE))

        pygame.display.update()
        clock.tick(60)








































































































































































































def battle_module():
    current_battle_running = True

    clock = pygame.time.Clock()
    pygame.init()

    pygame.mixer.set_num_channels(32)
    pygame.mixer.pre_init(44100, -16, 2, 512)
    # -----------------------------GameWindowSettings----------------------
    # pygame.display.set_caption("Old Ways")
    WINDOW_SIZE = (1280, 720)
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    # display = pygame.Surface((600,400))

    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

    fullscreen = button.fullscreen
    # not bool(linecache.getline('genericmap.txt',1))
    if fullscreen:
        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

    # -----------------------------------Battlemap,Interface------------------------
    bg_backscreen = pygame.image.load("BattleScreen/background.png").convert_alpha()
    bg_backscreen = pygame.transform.scale(bg_backscreen, (int(WINDOW_SIZE[0] * 1.00), (int(WINDOW_SIZE[1] * 0.75))))

    panel = pygame.image.load("BattleScreen/gamepanel1.png").convert_alpha()
    panel = pygame.transform.scale(panel, (int(WINDOW_SIZE[0] * 1.10), (int(WINDOW_SIZE[1] * 1.40))))

    bag_of_coins = pygame.image.load("BattleScreen/bag.png").convert_alpha()
    bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))
    # -----------------------------------Icons-------------------------------------
    attack_icon = pygame.image.load("BattleScreen/icon_fight.png").convert_alpha()
    attack_icon = pygame.transform.scale(attack_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.05))))

    normal_icon = pygame.image.load("BattleScreen/cursor_final.png").convert_alpha()
    normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0] * 0.04), (int(WINDOW_SIZE[1] * 0.05))))

    skip_turn_img = pygame.image.load("BattleScreen/resources/images/tent.png").convert_alpha()
    skip_turn_img = pygame.transform.scale(skip_turn_img, (int(WINDOW_SIZE[0] * 0.08), (int(WINDOW_SIZE[1] * 0.07))))

    # --------------------------------Items----------------------------------------
    inventory_bag = pygame.image.load("BattleScreen/resources/images/inventorybag.png").convert_alpha()
    inventory_bag = pygame.transform.scale(inventory_bag, (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))

    book_of_tricks = pygame.image.load("BattleScreen/resources/images/bookoftricks.png").convert_alpha()
    book_of_tricks = pygame.transform.scale(book_of_tricks, (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))

    troops = pygame.image.load("BattleScreen/resources/images/troops_icon.png").convert_alpha()
    troops = pygame.transform.scale(troops, (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))

    coins = pygame.image.load("BattleScreen/resources/images/coins.png").convert_alpha()
    coins = pygame.transform.scale(coins, (int(WINDOW_SIZE[0] * 0.025), (int(WINDOW_SIZE[1] * 0.045))))

    #----------------------------------------------------------------------------------------------
    no_potion = pygame.image.load("BattleScreen/resources/no_potion.png").convert_alpha()
    no_potion = pygame.transform.scale(no_potion, (int(WINDOW_SIZE[0] * 0.05), (int(WINDOW_SIZE[1] * 0.092))))

    no_icon = pygame.image.load("BattleScreen/resources/no_icon.png").convert_alpha()
    no_icon = pygame.transform.scale(no_icon, (int(WINDOW_SIZE[0] * 0.05), (int(WINDOW_SIZE[1] * 0.092))))

    doors_icon = pygame.image.load("BattleScreen/resources/images/castledoors.png").convert_alpha()
    doors_icon = pygame.transform.scale(doors_icon, (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))

    retry_icon = pygame.image.load("BattleScreen/resources/images/try_again.png").convert_alpha()
    retry_icon = pygame.transform.scale(retry_icon, (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))

    victory_icon = pygame.image.load("BattleScreen/resources/images/victory.png").convert_alpha()
    victory_icon = pygame.transform.scale(victory_icon, (int(WINDOW_SIZE[0] * 0.15), (int(WINDOW_SIZE[1] * 0.15))))

    # ------------------------------------------------------------------------------
    screen.fill((242, 238, 203))

    mouse_position = (0, 0)
    # ----------------------------------Music----------------------------------------
    # open_inventory_bag = pygame.mixer.Sound('sounds/OpenInventory.mp3')
    open_potion = pygame.mixer.Sound('BattleScreen/resources/sounds/open_potion.wav')
    break_potion = pygame.mixer.Sound('BattleScreen/resources/sounds/potion_break.wav')
    music_list = ['Battle','Battle1','Battle2','Battle3','Battle4']
    play_music(random.choice(music_list))

    coins_sound = pygame.mixer.Sound('WorldMap/coins.wav')
    # ------------------------------------AttackSounds---------------------------------
    block_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/block.wav')
    attack_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/attack_sound.wav')
    arrow_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/arrow.wav')
    snarl_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/snarl.wav')
    stone_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/throwingstone.wav')
    flame_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/flame.wav')
    axe_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/axe.wav')
    heavy_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/heavyhit.wav')
    catapult_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/catapult.wav')
    grenade_blast = pygame.mixer.Sound('BattleScreen/resources/sounds/bomb.wav')
    tremors_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/tremors.wav')
    heal_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/healing.wav')
    trap_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/snap_trap.wav')
    sharpening_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/sharpening.wav')
    bowstring_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/bowload.wav')
    gallop_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/gallop.wav')
    dragon_roar_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/dragon_roar.wav')
    #------------------------------------StatusSounds--------------------------------
    energy_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/energy.wav')
    fire_burn = pygame.mixer.Sound('BattleScreen/resources/sounds/fire_burn.wav')
    acid_burn = pygame.mixer.Sound('BattleScreen/resources/sounds/acid_burn.wav')
    frost_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/frost.wav')
    poison_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/poison.wav')
    dream_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/dream_sound.wav')
    bleed_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/bleed_sound.wav')
    clouded_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/clouded_sound.wav')
    wind_sound = pygame.mixer.Sound('BattleScreen/resources/sounds/wind.wav')

    # -------------------------------------ScaleOptions----------------------------
    cond_list = []
    with open('BattleScreen/encounter_conditions.txt') as f:
        cond = f.readlines()
    count = 0
    for cond in cond_list: count += 1
    battle_conditions = int(cond[0])
    battle_type = int(cond[1])
    auto_battle = 0
    full_auto_battle = 0

    global game_scale
    if battle_type == 0:
        game_scale = 1
    if battle_type == 1:
        game_scale = 0.5
    # if battle_type == 1:
    #     game_scale = 0.5

    animod = round(2 * game_scale)
    tilescale = 0.10 * game_scale
    rendermod = 1 * game_scale

    TILE_SIZE = 70
    scroll = [0,0]
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    ROWS = 16
    MAX_COLS = 30
    WAR_TILE = SCREEN_HEIGHT // ROWS
    grid = False
    def draw_grid(surface):
        for c in range(MAX_COLS + 1):
            pygame.draw.line(surface, (255,255,255), (c * WAR_TILE, 0),
                             (c * WAR_TILE, SCREEN_HEIGHT * 4))
        for c in range(ROWS + 1):
            pygame.draw.line(surface, (255,255,255), (0, c * WAR_TILE),
                             (SCREEN_WIDTH * 14, c * WAR_TILE))

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    # ------------------------------------ActionOrder--------------------------------
    global current_fighter
    current_fighter = 1
    # ----------------------------------------------------------------------------
    global action_cooldown
    action_cooldown = 0
    action_waittime = 100
    draw_cursor = False
    battle_status = 0  # 0 - nothing, 1 = lost, 2 = won

    # if battle_status ==0:
    #     play_music('Battle')
    # if battle_status ==2:
    # #     pygame.mixer.music.play(0)
    # #     play_music('BattleVictory')
    play_defeat_music = True
    play_victory_music = True
    # if battle_status ==1:
    #     play_music('BattleDefeat')
    # ------------------------------------------------------------------------------

    # ------------------------------------Techniques------------------------------------
    path, dirs, techniques = next(os.walk("MainMenuRes/techniques/all"))
    techniques_count = len(techniques)
    TECHNIQUE_TYPES = techniques_count
    techniques_img = []
    for x in range(TECHNIQUE_TYPES):
        img = pygame.image.load(f'MainMenuRes/techniques/all/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        techniques_img.append(img)
    #------------------------------------------------------------------------------------
    engage = False
    clicked = False
    clicked2 = False
    skip_turn = False
    show_indicators = True
    global auto_potion
    auto_potion = False

    stats_sk = []
    with open('MainMenuRes/char_statistic/charskirmish.txt') as f:
        skirmish = f.readlines()
    count = 0
    for skirmish in stats_sk:
        count += 1
    melee = int(skirmish[0])
    ranged = int(skirmish[1])
    parrying = int(skirmish[2])
    athletics = int(skirmish[3])
    intimidation = int(skirmish[4])
    tactics = int(skirmish[5])
    arming = int(skirmish[6])
    siege = int(skirmish[7])

    stats_sr = []
    with open('MainMenuRes/char_statistic/charsurvive.txt') as f:
        survival = f.readlines()
    count = 0
    for survival in stats_sr:
        count += 1
    acrobatics = int(survival[0])
    stealth = int(survival[1])
    thievery = int(survival[2])
    lockpicking = int(survival[3])
    deception = int(survival[4])
    traps = int(survival[5])
    stupefy = int(survival[6])
    nature = int(survival[7])

    stats_sv = []
    with open('MainMenuRes/char_statistic/charsavviness.txt') as f:
        savviness = f.readlines()
    count = 0
    for savviness in stats_sv:
        count += 1
    investigation = int(savviness[0])
    medicine = int(savviness[1])
    lore = int(savviness[2])
    persuasion = int(savviness[3])
    arcane = int(savviness[4])
    divine = int(savviness[5])
    alchemy = int(savviness[6])
    engineering = int(savviness[7])

    #-----------------------------------------UseTechniques--------------------------------
    battle_techniques_box = []
    technique_button = button.TechniqueButton(screen, 0, WINDOW_SIZE[1] * 0.91, techniques_img[66], int(TILE_SIZE*0.9), TILE_SIZE, 2,
                                        False, 'Attack target several times in melee')
    technique_button1 = button.TechniqueButton(screen, int(TILE_SIZE*0.92), WINDOW_SIZE[1] * 0.91, techniques_img[7], int(TILE_SIZE*0.9), TILE_SIZE, 1,
                                              False, 'Decreases enemy resistances and defence')
    technique_button2 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*2, WINDOW_SIZE[1] * 0.91, techniques_img[35], int(TILE_SIZE*0.9), TILE_SIZE, 1,
                                               False, 'Restores 25% of health')
    technique_button3 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*3, WINDOW_SIZE[1] * 0.91, techniques_img[44], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                               False, 'Bonus damage and a free action if enemy is defeated')
    technique_button4 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*4, WINDOW_SIZE[1] * 0.91, techniques_img[13], int(TILE_SIZE*0.9), TILE_SIZE, 2,
                                               False, 'Attack target several times with a secondary weapon')
    technique_button5 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*5, WINDOW_SIZE[1] * 0.91, techniques_img[45], int(TILE_SIZE*0.9), TILE_SIZE, 1,
                                               False, 'Defence party stance. Allows to always retaliate')
    technique_button6 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*6, WINDOW_SIZE[1] * 0.91, techniques_img[27], int(TILE_SIZE*0.9), TILE_SIZE, 2,
                                               False, 'Applies bleeding to multiple targets')
    technique_button7 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*7, WINDOW_SIZE[1] * 0.91, techniques_img[74], int(TILE_SIZE*0.9), TILE_SIZE, 1,
                                               False, 'Attack target and make it skip its turn')
    technique_button8 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*8, WINDOW_SIZE[1] * 0.91, techniques_img[55], int(TILE_SIZE*0.9), TILE_SIZE, 2,
                                               False, 'Removes all negative statuses from all troops')
    technique_button9 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*9, WINDOW_SIZE[1] * 0.91, techniques_img[28], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                               False, 'Hits multiple targets in melee')
    technique_button10 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*10, WINDOW_SIZE[1] * 0.91, techniques_img[39], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                               False, 'Hits multiple targets with a ranged weapon')
    technique_button11 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*11, WINDOW_SIZE[1] * 0.91, techniques_img[16], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                                False, 'Restores 25% armor of all troops')
    technique_button12 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*12, WINDOW_SIZE[1] * 0.91, techniques_img[62], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                                False, 'Increases damage of all troops by 10%')
    technique_button13 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*13, WINDOW_SIZE[1] * 0.91, techniques_img[11], int(TILE_SIZE*0.9), TILE_SIZE, 4,
                                                False, 'Several targets have a chance to skip turn')
    technique_button14 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*14, WINDOW_SIZE[1] * 0.91, techniques_img[9], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                                False, 'Restores full health')
    technique_button15 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*15, WINDOW_SIZE[1] * 0.91, techniques_img[54], int(TILE_SIZE*0.9), TILE_SIZE, 4,
                                                False, 'Tries to kill a human target instantly')
    technique_button16 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*16, WINDOW_SIZE[1] * 0.91, techniques_img[43], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                                False, 'Damages and applies poison or bleed to all enemy troops')
    technique_button17 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*17, WINDOW_SIZE[1] * 0.91, techniques_img[67], int(TILE_SIZE*0.9), TILE_SIZE, 3,
                                                False, 'Restores 25% health of all troops')
    technique_button18 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*18, WINDOW_SIZE[1] * 0.91, techniques_img[20], int(TILE_SIZE*0.9), TILE_SIZE, 6,
                                                False, 'Creates two shadow copies')
    technique_button19 = button.TechniqueButton(screen, int(TILE_SIZE*0.92)*19, WINDOW_SIZE[1] * 0.91, techniques_img[41], int(TILE_SIZE*0.9), TILE_SIZE, 4,
                                                False, 'All allied troops are hastened')

    battle_techniques_box.extend([technique_button,technique_button1,technique_button2,technique_button3,technique_button4,technique_button5,technique_button6,
                                  technique_button7,technique_button8,technique_button9,technique_button10,technique_button11,technique_button12,
                                  technique_button13,technique_button14,technique_button15,technique_button16,technique_button17,technique_button18,technique_button19])
    #-------------------------------------------------------------------------------------
    novice_list = []
    with open('MainMenuRes/char_statistic/techniques_novice.txt') as f:
        novice = f.readlines()
    count = 0
    for novice in novice_list: count += 1
    technique_button.available = True #Combo int(novice[1])
    Educated = True #int(novice[2])
    Quick_Shot = True #int(novice[3])
    Quartermaster = True #int(novice[6])
    technique_button1.available = True  # int(novice[10]) curse
    technique_button2.available = True  # int(novice[11])Healing

    adept_list = []
    with open('MainMenuRes/char_statistic/techniques_adept.txt') as f:
        adept = f.readlines()
    count = 0
    for adept in adept_list: count += 1
    technique_button3.available = True #int(adept[1]) Power_Blow
    technique_button4.available = True  #MultipleShot = int(adept[3])
    technique_button5.available = True  # Duelist =  int(adept[4])
    technique_button6.available = True #Bear_Trap = int(adept[5])
    Potion_Master = True #int(adept[6])
    technique_button7.available = True  #Knock_Down = int(adept[7])
    Battle_Reflex = int(adept[8])
    Persevere = int(adept[9])
    Moon_Shield = int(adept[10])
    technique_button8.available = True #Purifier = int(adept[11])

    expert_list = []
    with open('MainMenuRes/char_statistic/techniques_expert.txt') as f:
        expert = f.readlines()
    count = 0
    for expert in expert_list: count += 1
    Readiness = int(expert[0])
    technique_button9.available = True # Slice = int(expert[1])
    Field_Engineer = int(expert[2])
    Deadeye = int(expert[3])
    technique_button10.available = True #Barrage = int(expert[4])
    technique_button11.available = True #Shields_Up = int(expert[5])
    War_Engineer = int(expert[6])
    technique_button12.available = True #Charge = int(expert[7])
    Reaper = int(expert[8])
    Troll_Skin = int(expert[9])
    technique_button13.available = True #Dream_Cloud = int(expert[10])
    technique_button14.available = True #Second_Wind = int(expert[11])

    master_list = []
    with open('MainMenuRes/char_statistic/techniques_master.txt') as f:
        master = f.readlines()
    count = 0
    for master in master_list: count += 1
    technique_button15.available = True #Backstab = int(master[0])
    Weak_Spot = int(master[1])
    Siege_Master = int(master[2])
    Piercing_Arrows = int(master[3])
    Planewalker = int(master[4])
    Commander = int(master[5])
    Master_Mechanist = int(master[6])
    technique_button16.available = True #Battle_Prudence = int(master[7])
    Channelling = int(master[8])
    technique_button17.available = True #Divine_Intervention = int(master[9])
    technique_button18.available = True #Shadows = int(master[10])
    technique_button19.available = True #Blessing = int(master[11])

    if Potion_Master == 1:
        supply_modifier = -1
    else:
        supply_modifier = 0

    #-------------------------------------------------------------------------------------
    #-----------------------------------------UsePotions-----------------------------------
    use_health_potion = False
    health_potion_restores = 50 + int((alchemy * 50) / 100)

    use_defence_potion = False
    defence_potion_adds = 100 + int((alchemy * 100) / 100)

    use_berserk_potion = False
    berserk_potion_adds = 25 + int((alchemy * 25) / 100)

    use_antidote_potion = False
    antidote_potion_adds = 25 + int((alchemy * 25) / 100)

    use_vigor_potion = False
    vigor_potion_adds = 3 + int((alchemy * 3) / 100)

    use_celerity_potion = False
    celerity_potion_adds = 15 + int((alchemy * 15) / 100)
    celerity_potion_status = 'haste'

    use_ironskin_potion = False
    ironskin_potion_adds = 10 + int((alchemy * 10) / 100)

    use_deathkiss_potion = False
    deathkiss_potion_adds = 15 + int((alchemy * 15) / 100)

    use_rejuvenation_potion = False
    rejuvenation_potion_adds = 5 + int((alchemy * 5) / 100)

    use_fireshield_potion = False
    fireshield_potion_adds = 25 + int((alchemy * 25) / 100)

    use_frostshield_potion = False
    frostshield_potion_adds = 25 + int((alchemy * 25) / 100)

    use_energyshield_potion = False
    energyshield_potion_adds = 25 + int((alchemy * 25) / 100)

    use_moonlight_potion = False
    moonlight_potion_adds = 25 + int((alchemy * 25) / 100)

    use_liquidfire_potion = False
    liquidfire_potion_damage = 10 + int((alchemy * 5) / 100)
    liquidfire_potion_status = 'inflamed'

    use_liquidfrost_potion = False
    liquidfrost_potion_damage = 10 + int((alchemy * 5) / 100)
    liquidfrost_potion_status = 'frozen'

    use_darkcloud_potion = False
    darkcloud_potion_damage = 10 + int((alchemy * 5) / 100)
    darkcloud_potion_status = 'cursed'

    use_acid_potion = False
    acid_potion_damage = 10 + int((alchemy * 10) / 100)
    acid_potion_status = 'corrosion'

    use_poison_potion = False
    poison_potion_damage = 10 + int((alchemy * 10) / 100)
    poison_potion_status = 'poisoned'

    use_dream_potion = False
    dream_potion_prob = 10 + int((alchemy * 10) / 100)
    dream_potion_status = 'dreamy'

    use_cleansing_potion = False
    cleansing_potion_restores = 25 + int((alchemy * 25) / 100)
    cleansing_potion_status = 'healthy'

    use_ritual_potion = False #kills several unholy, demonic and wicked targets with 50% success
    ritual_potion_prob = 20 + int((alchemy * 20) / 100)
    ritual_potion_damage = 100+ int((alchemy * 100) / 100)

    use_energy_shard = False
    energy_shard_damage = 10+ int((alchemy * 10) / 100)
    energy_shard_status = 'shocked'

    use_earth_shard = False
    earth_shard_damage = 100+ int((alchemy * 100) / 100)

    use_grenade = False
    grenade_damage = random.randint(20,40) + int((alchemy * 40) / 100)

    use_shrapnel_grenade = False
    shrapnel_grenade_damage = random.randint(10,20) + int((alchemy * 20) / 100)
    shrapnel_grenade_status = 'bleed'

    use_concentration_potion = False
    concentration_potion_adds = 10 + int((alchemy * 10) / 100)
    # ----------------------------------ShowStats------------------------------------
    font = pygame.font.SysFont('Times New Roman', 18)
    fontBag = pygame.font.Font('WorldMap/ESKARGOT.ttf', 38)
    fontDMG = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
    fontActive = pygame.font.Font('WorldMap/ESKARGOT.ttf', 80)
    fontBattle = pygame.font.SysFont('Times New Roman', 70)
    fontMenuLarge = pygame.font.Font('WorldMap/ESKARGOT.ttf', 48)
    # pygame.font.Font('WorldMap/ESKARGOT.ttf', 70)

    red = (230, 16, 35)
    ginger = (245, 116, 34)
    green = (0, 255, 0)
    paper = (255, 150, 100)
    blue = (0, 0, 255)
    lightblue = (240, 248, 255)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    # --------------------------------------------------------------------------------
    def draw_bgBackscreen():
        screen.blit(bg_backscreen, (0, 0))

    def draw_bag():
        screen.blit(bag_of_coins, (0, 0))
        draw_text(f'{button.wealth}', fontBag, (255, 225, 100), 120, 30)

    def mouse_map_position_align(x, y):
        pyautogui.moveTo(x, y)

    # ------------------------------DrawingIndicators------------------------
    def draw_panel():
        screen.blit(panel, (-50, -35))
        # for count, i in enumerate(army_player):
        #       draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
        # for count, i in enumerate(army_hostiles):
        #     draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (100,0,0), ((panel.get_width())*0.58), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))

    # -----------------------------HeroStats-----------------------------
    stats_list = []
    with open('MainMenuRes/char_statistic/charres.txt') as f:
        stats = f.readlines()
    count = 0
    for stats in stats_list: count += 1
    rowan_threshold = int(stats[0])
    rowan_defence = int(stats[1])
    rowan_arcana_res = int(stats[2])
    rowan_energy_res = int(stats[3])
    rowan_frost_res = int(stats[4])
    rowan_fire_res = int(stats[5])
    rowan_poison_res = int(stats[6])

    offence_list = []
    with open('MainMenuRes/char_statistic/charattack.txt') as f:
        offence = f.readlines()
    count = 0
    for offence in offence_list: count += 1
    rowan_melee_damage = int(offence[0])
    rowan_ranged_damage = int(offence[1])
    rowan_critical_strike = int(offence[2])
    rowan_block = int(offence[3])
    rowan_parry = int(offence[4])

    aux_list = []
    with open('MainMenuRes/char_statistic/charsecondary.txt') as f:
        aux = f.readlines()
    count = 0
    for aux in aux_list: count += 1
    rowan_tricks = int(aux[0])
    rowan_supply = int(aux[1])
    rowan_health_points = int(aux[2])
    rowan_armor_points = int(aux[3])
    rowan_leadership = int(aux[4])
    rowan_level = int(aux[5])

    upgrade = 1 + ((3*rowan_level)/100)

    # ----------------------------------Characters------------------------------
    class Fighter():
        def __init__(self, x, y, id, max_hp, max_armor, strength, strength2, defence, threshold, reach, special,
                     alive, max_supply, max_tricks, hostile, arcane_res, fire_res, energy_res, frost_res, poison_res,
                     crit, experience, type, parry, block, attack_type, status):
            self.id = id
            self.max_hp = max_hp
            self.hp = max_hp
            self.max_armor = max_armor
            self.armor = max_armor
            self.defence = defence
            self.start_defence = defence
            self.strength = strength
            self.start_strength = strength
            self.strength2 = strength2
            self.start_strength2 = strength2
            self.reach = reach
            self.special = special
            self.max_supply = max_supply
            self.supply = max_supply
            self.threshold = threshold
            self.start_arcane_res = arcane_res
            self.start_fire_res = fire_res
            self.start_energy_res = energy_res
            self.start_frost_res = frost_res
            self.start_poison_res = poison_res
            self.arcane_res = arcane_res
            self.fire_res = fire_res
            self.energy_res = energy_res
            self.frost_res = frost_res
            self.poison_res = poison_res
            self.max_tricks = max_tricks
            self.tricks = max_tricks
            self.start_block = block
            self.block = block
            self.start_crit = crit
            self.crit = crit
            self.start_parry = parry
            self.parry = parry
            self.alive = True
            self.hostile = True
            self.experience = experience
            self.type = type
            self.status = status
            self.attack_type = attack_type
            self.x = x
            self.y = y
            self.animation_list = []  # list of lists (action/img)
            self.frame_index = 0
            self.action = 0  # 0-idle / 1-attack / 2-hurt / 3-death  updates via self.animation_list = []
            self.update_time = pygame.time.get_ticks()  # how much time has passed

            # -----------------------------Animations--------------------------------------------
            # loading idle action images
            temp_list = []
            for i in range(2):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/idle/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img, (img.get_width() * animod, img.get_height() * animod))
                temp_list.append(img)  # appends temp list to store img
            self.animation_list.append(temp_list)

            # loading attack action images
            temp_list = []
            for i in range(3):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/attack/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img, (img.get_width() * animod, img.get_height() * animod))
                temp_list.append(img)  # appends temp list to store img
            self.animation_list.append(temp_list)

            temp_list = []
            for i in range(1):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/hurt/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img, (img.get_width() * animod, img.get_height() * animod))
                temp_list.append(img)  # appends temp list to store img
            self.animation_list.append(temp_list)

            temp_list = []
            for i in range(3):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/dead/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img, (img.get_width() * animod, img.get_height() * animod))
                temp_list.append(img)  # appends temp list to store img
            self.animation_list.append(temp_list)
            # -----------------------------------------------------------------------------------
            if self.id == 'rowan' or self.id == 'dunstan' or self.id == 'bartelago' or self.id == 'anselm'\
                    or self.id == 'alba' or self.id == 'severin'or self.id == 'regina':
                temp_list = []
                for i in range(3):
                    img = pygame.image.load(f'BattleScreen/units/{self.id}/attack2/{i}.png')
                    img = pygame.transform.flip(img, hostile, False)
                    img = pygame.transform.scale(img, (img.get_width() * animod, img.get_height() * animod))
                    temp_list.append(img)  # appends temp list to store img
                self.animation_list.append(temp_list)
            # --------------------------------
            self.image = self.animation_list[self.action][self.frame_index]  # to control action/images
            # two lists (action/frames)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        # ---------------------------------------------------------------------
        def update(self, animation_modifier):  # animation
            animation_cooldown = 100
            if self.action == 0:
                animation_cooldown = 1000 * animation_modifier
            if self.action == 1:
                animation_cooldown = 150 * animation_modifier
            if self.action == 2:
                animation_cooldown = 300 * animation_modifier
            if self.action == 3:
                animation_cooldown = 250 * animation_modifier
            if self.action == 4:
                animation_cooldown = 150 * animation_modifier
            # animation_cooldown = cooldown
            self.image = self.animation_list[self.action][self.frame_index]  # adding action
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:  # if its more than 100 its time to update the animation stage
                self.update_time = pygame.time.get_ticks()  # resets timer
                self.frame_index += 1
            # if animation run out, reset
            if self.frame_index >= len(self.animation_list[self.action]):  # adding action
                # after death unit should stay at the last frame of the dead animation sequence
                if self.action == 3:  # dead animation in the list.
                    self.frame_index = len(self.animation_list[self.action]) - 1  # final frame
                else:
                    self.idle()  # sets to idle animation
        # -----------------------------------Idle----------------------------
        def idle(self):
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        # -----------------------------------Hurt----------------------------
        def hurt(self):
            self.action = 2
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        # -----------------------------------dead----------------------------
        def dead(self):
            self.action = 3
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        # -------------------------------------------------------------------
        def reset(self):
            self.alive = True
            self.supply = self.max_supply
            self.hp = self.max_hp
            self.armor = self.max_armor
            self.defence = self.start_defence
            self.strength = self.start_strength
            self.frame_index = 0
            self.action = 0
            self.update_time = pygame.time.get_ticks()

        def move_it(self):
            if moving_right:
                self.rect.x -= TILE_SIZE//6
            if moving_left:
                self.rect.x += TILE_SIZE//6
            if moving_up:
                self.rect.y += TILE_SIZE//6
            if moving_down:
                self.rect.y -= TILE_SIZE//6

        # -----------------------------------Attack----------------------------
        def attack(self, target):
            rand = random.randint(-5, 5)
            if random.randint(0, 100) < self.crit:
                damage = self.strength * 2 + rand
                if damage <= 0:damage = 0
                fint_text = DamageText(target.rect.centerx, target.rect.y - 90, 'Critical hit!', (255,140,0))
                damage_text_group.add(fint_text)
            elif random.randint(0, 100) < target.block:
                pygame.mixer.Sound(block_sound).play()
                damage = (self.strength + rand - target.threshold)//2
                if damage <= 0:damage = 0
                fint_text = DamageText(target.rect.centerx, target.rect.y - 75, 'Blocked!', (25,25,225))
                damage_text_group.add(fint_text)
            elif self.attack_type == 'fire':
                damage = (self.strength + rand) * (1-(target.fire_res//100))
                target.status = 'inflamed'
            elif self.attack_type == 'frost':
                damage = (self.strength + rand) * (1-(target.frost_res//100))
                target.status = 'frozen'
            elif self.attack_type == 'energy':
                damage = (self.strength + rand) * (1-(target.energy_res//100))
                target.status = 'shock'
            elif self.attack_type == 'acid':
                damage = self.strength + rand - target.threshold
                target.status = 'corroded'
            elif self.attack_type == 'poison':
                damage = (self.strength + rand) * (1-(target.poison_res//100))
                target.status = 'poisoned'
            elif self.attack_type == 'arcane':
                damage = (self.strength + rand) * (1-(target.arcane_res//100))
                target.status = random.choice(['cursed','dreamy'])
            elif self.attack_type == 'tear':
                damage = self.strength + rand - target.threshold
                target.status = 'bleed'
            else:
                damage = self.strength + rand - target.threshold
                if damage <= 0:damage = 0
            if self.special == 1:
                # target.armor -= 0
                target.hp -= damage
            elif self.special != 1:
                target.armor -= int(damage * (target.defence / 100))
                if target.armor > 0:
                    target.hp -= int(damage * (1 - target.defence / 100))
                if target.armor <= 0:
                    target.hp -= int((damage * (1 - target.defence / 100) - target.armor))
                    target.armor = 0

                if technique_button5.toggled == True and target.tricks >= technique_button5.price and target.type == 'hero':
                    target.tricks -= technique_button5.price
                    time.sleep(0.2)
                    target.attack(self)
                    fint_text = DamageText(target.rect.centerx, target.rect.y - 60, 'Retaliate!', (255,255,255))
                    damage_text_group.add(fint_text)

                if random.randint(0, 100) < target.parry:
                    time.sleep(0.1)
                    target.attack(self)
                    fint_text = DamageText(target.rect.centerx, target.rect.y - 60, 'Retaliate!', (255,255,255))
                    damage_text_group.add(fint_text)

            if technique_button.toggled == True and self.hostile == True:
                if self.tricks >= technique_button.price and self.status != 'haste':
                    self.status = 'haste'
                    self.tricks -= technique_button.price
                    technique_button.toggled = False

            if technique_button3.toggled == True and self.hostile == True:
                if self.tricks >= technique_button3.price and self.status != 'haste':
                    self.tricks -= technique_button3.price
                    damage = round(damage * 1.50)
                    if target.hp < 1:
                       self.status = 'haste'
                    technique_button3.toggled = False

            # runs hurn animation
            target.hurt()
            if target.hp < 1:
                target.hp = 0
                target.alive = False
                # runs death animation
                target.dead()

            #   if self.special != 1:
            #       damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage-(damage*(target.defence/100)))), red)
            #   else:
            #       damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
            # DamageText
            if self.special != 1:
                if target.armor > 1:
                    damage_text = DamageText(target.rect.centerx, target.rect.y - 35,
                                             str(int(damage * (1 - target.defence / 100))), red)
                if target.armor <= 1:
                    damage_text = DamageText(target.rect.centerx, target.rect.y - 35, str(damage), red)
                    # DamageText(target.rect.centerx,target.rect.y-35,str(int((damage*(1 - target.defence/100)))), red)
            else:
                damage_text = DamageText(target.rect.centerx, target.rect.y - 35, str(damage), red)

            damage_text_group.add(damage_text)
            # ---------------------------------AttackSounds---------------------------------------
            # attack sound # 0-standard blade; 1-arrow; 2-stone
            if self.special == 0:
                pygame.mixer.Sound(attack_sound).play()
            elif self.special == 1:
                pygame.mixer.Sound(arrow_sound).play()
            elif self.special == 2:
                pygame.mixer.Sound(stone_sound).play()
            elif self.special == 3:
                pygame.mixer.Sound(snarl_sound).play()
            elif self.special == 4:
                pygame.mixer.Sound(flame_sound).play()
            elif self.special == 5:
                pygame.mixer.Sound(heavy_sound).play()
            elif self.special == 6:
                pygame.mixer.Sound(axe_sound).play()
            elif self.special == 7:
                pygame.mixer.Sound(stone_sound).play()
                time.sleep(0.1)
                pygame.mixer.Sound(break_potion).play()

                # ------------------------------------------------------------------------------------
            # animations
            self.action = 1  # set action frames to as 1 as 1 = attack folder animation
            self.frame_index = 0  # frame 0 in the attack folder animation
            self.update_time = pygame.time.get_ticks()
        # -----------------------------------------------------------------------------------------
        def alternative_attack(self, target):
            rand = random.randint(-5, 5)
            if random.randint(0, 100) < self.crit:
                damage = self.strength2 * 2 + rand
                if damage <= 0:damage = 0
                fint_text = DamageText(target.rect.centerx, target.rect.y - 90, 'Critical hit!', (255,140,0))
                damage_text_group.add(fint_text)
            elif random.randint(0, 100) < target.block:
                pygame.mixer.Sound(block_sound).play()
                damage = (self.strength2 + rand - target.threshold)//2
                if damage <= 0:damage = 0
                fint_text = DamageText(target.rect.centerx, target.rect.y - 75, 'Blocked!', (25,25,225))
                damage_text_group.add(fint_text)
            elif self.attack_type == 'fire':
                damage = (self.strength2 + rand) * (1-(target.fire_res//100))
                target.status = 'inflamed'
            elif self.attack_type == 'frost':
                damage = (self.strength2 + rand) * (1-(target.frost_res//100))
                target.status = 'frozen'
            elif self.attack_type == 'energy':
                damage = (self.strength2 + rand) * (1-(target.energy_res//100))
                target.status = 'shocked'
            elif self.attack_type == 'acid':
                damage = self.strength2 + rand - target.threshold
                target.status = 'corroded'
            elif self.attack_type == 'poison':
                damage = (self.strength2 + rand) * (1-(target.poison_res//100))
                target.status = 'poisoned'
            elif self.attack_type == 'arcane':
                damage = (self.strength2 + rand) * (1-(target.arcane_res//100))
                target.status = random.choice(['cursed','dreamy'])
            elif self.attack_type == 'tear':
                damage = self.strength2 + rand - target.threshold
                target.status = 'bleed'
            else:
                damage = self.strength2 + rand - target.threshold
                if damage <= 0:damage = 0
            if self.special == 1:
                # target.armor -= 0
                target.hp -= damage
            elif self.special != 1:
                target.armor -= int(damage * (target.defence / 100))
                if target.armor > 0:
                    target.hp -= int(damage * (1 - target.defence / 100))
                if target.armor <= 0:
                    target.hp -= int((damage * (1 - target.defence / 100) - target.armor))
                    target.armor = 0

            if technique_button4.toggled == True:
                if self.tricks >= technique_button4.price and self.status != 'haste':
                    self.status = 'haste'
                    self.tricks -= technique_button4.price
                    technique_button4.toggled = False


            # runs hurn animation
            target.hurt()

            if target.hp < 1:
                target.hp = 0
                target.alive = False
                # runs death animation
                target.dead()

            if self.special != 1:
                if target.armor > 1:
                    damage_text = DamageText(target.rect.centerx, target.rect.y - 35,
                                             str(int(damage * (1 - target.defence / 100))), red)
                if target.armor <= 1:
                    damage_text = DamageText(target.rect.centerx, target.rect.y - 35, str(damage), red)
                    # DamageText(target.rect.centerx,target.rect.y-35,str(int((damage*(1 - target.defence/100)))), red)
            else:
                damage_text = DamageText(target.rect.centerx, target.rect.y - 35, str(damage), red)

            damage_text_group.add(damage_text)
            # ---------------------------------AttackSounds---------------------------------------
            # attack sound # 0-standard blade; 1-arrow; 2-stone
            if self.special == 0 and self.id == 'rowan' or self.id == 'dunstan' or self.id == 'bartelago':
                pygame.mixer.Sound(arrow_sound).play()
            elif self.special == 0:
                pygame.mixer.Sound(attack_sound).play()
            elif self.special == 1:
                pygame.mixer.Sound(arrow_sound).play()
            elif self.special == 2:
                pygame.mixer.Sound(stone_sound).play()
            elif self.special == 3:
                pygame.mixer.Sound(snarl_sound).play()
            elif self.special == 4:
                pygame.mixer.Sound(flame_sound).play()
            elif self.special == 5:
                pygame.mixer.Sound(heavy_sound).play()
            elif self.special == 6:
                pygame.mixer.Sound(axe_sound).play()
            elif self.special == 7:
                pygame.mixer.Sound(stone_sound).play()
                time.sleep(0.1)
                pygame.mixer.Sound(break_potion).play()
            # ------------------------------------------------------------------------------------

            # animations
            self.action = 4  # set action frames to as 1 as 1 = attack folder animation
            self.frame_index = 0  # frame 0 in the attack folder animation
            self.update_time = pygame.time.get_ticks()
            # ----------------------------------------------------------------------
        def draw(self):
            screen.blit(self.image, self.rect)
    # -----------------------------------HealthBar--------------------------
        class healthBar():
            def __init__(self, x, y, hp, max_hp):
                self.x = x
                self.y = y
                self.hp = hp
                self.max_hp = max_hp

            def draw(self, hp):
                self.hp = hp
                ratio = self.hp / self.max_hp
                pygame.draw.rect(screen, red, (self.x, self.y, 50, 5))
                pygame.draw.rect(screen, green, (self.x, self.y, 50 * ratio, 5))

        # -----------------------------------ArmorBar--------------------------
        class armorBar():
            def __init__(self, x, y, armor, max_armor):
                self.x = x
                self.y = y
                self.armor = armor
                self.max_armor = max_armor

            def draw(self, armor):
                self.armor = armor
                ratio = self.armor / self.max_armor
                pygame.draw.rect(screen, lightblue, (self.x, self.y, 50, 5))
                pygame.draw.rect(screen, blue, (self.x, self.y, 50 * ratio, 5))

    # -----------------------------------AttributeChangeBar-----------------
    class DamageText(pygame.sprite.Sprite):  # sprite is updated automatically
        def __init__(self, x, y, damage, color):
            pygame.sprite.Sprite.__init__(self)
            self.image = fontDMG.render(damage, True, color)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.counter = 0

        def update(self):
            # move text
            self.rect.y -= 1
            # delete after timer
            self.counter += 1
            if self.counter > 30:
                self.kill()

    damage_text_group = pygame.sprite.Group()
    #-------------------------------------------------------------------------------------

















    #----------------------------------------UnlockedTroops------------------------------
    summon_reserves = True
    summon_melee = True
    summon_ranged = True
    summon_cavalry = True
    summon_support = True
    summon_machine_support = True
    summon_machine_siege = True
    summon_machine_battle = True
    summon_dunstan = True
    summon_bartelago = True
    summon_regina = True
    summon_anselm = True
    summon_alba = True
    summon_severin = True
    #------------------------------------------------------------------------------------
    path, dirs, units = next(os.walk("MainMenuRes/troops/unit_img"))
    units_count = len(units)
    UNITS_TYPES = units_count
    units_img = []
    for x in range(UNITS_TYPES):
        img = pygame.image.load(f'MainMenuRes/troops/unit_img/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))
        units_img.append(img)
    #------------------------------------------------------------------------------------
    battle_units_box = []

    unit_button = button.TroopsButton(screen, 0, WINDOW_SIZE[1] * 0.91, units_img[0], int(TILE_SIZE*0.9), TILE_SIZE, 0,
                                      False, 'Dunstan is a heavily armored swordsman with a crossbow for ranged combat', 0,False)
    unit_button1 = button.TroopsButton(screen, int(TILE_SIZE*0.92), WINDOW_SIZE[1] * 0.91, units_img[1], int(TILE_SIZE*0.9), TILE_SIZE, 1200,
                                      False, 'A regiment of light infantry', 0,False)
    unit_button2 = button.TroopsButton(screen, int(TILE_SIZE*0.92)*2, WINDOW_SIZE[1] * 0.91, units_img[2], int(TILE_SIZE*0.9), TILE_SIZE, 1600,
                                       False, 'A regiment of light archers', 0,False)
    unit_button3 = button.TroopsButton(screen, int(TILE_SIZE*0.92)*3, WINDOW_SIZE[1] * 0.91, units_img[3], int(TILE_SIZE*0.9), TILE_SIZE, 2100,
                                       False, 'Armored assault cavalry', 0,False)
    unit_button4 = button.TroopsButton(screen, int(TILE_SIZE*0.92)*4, WINDOW_SIZE[1] * 0.91, units_img[4], int(TILE_SIZE*0.9), TILE_SIZE, 900,
                                       False, 'A trained group of scouts', 0,False)
    unit_button5 = button.TroopsButton(screen, 0, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, units_img[5], int(TILE_SIZE*0.9), TILE_SIZE, 0,
                                       False, 'Bartelago is your old friend. He prefers heavy swords and throwing daggers', 0,False)
    battle_units_box.append([unit_button,unit_button1,unit_button2,unit_button3,unit_button4,unit_button5])
    #------------------------------------------------------------------------------------
    with open(f"MainMenuRes/inventory/unlocked_troops.json",'r') as g:
        data = json.loads(g.read())

    if len(data):
        for count,i in enumerate(battle_units_box):
            for j in i:
                j.available = True
        #unit_button.available = data["0"]
        #unit_button5.available = data["5"]
        #if battle_type == 1:
            #unit_button1.available = data["1"]
            #unit_button2.available = data["2"]
            #unit_button3.available = data["3"]
            #unit_button4.available = data["4"]

    #----------------------------------------------------------------------------------
        # for i in range(1, 100):
        #     globals()[f"unit_name_{i}"] = i
        #
        # print()
        # print(unit_name_1)
        # print(unit_name_2)
    #_-----------------------------------------------------------------------------------
    # max_hp, max_armor, strength, strength2, defence, threshold, reach, special,
    # alive, max_supply, max_tricks, hostile, arcane_res, fire_res, energy_res,
    # frost_res, poison_res,crit, experience, allegiance, parry,block,status):
    # 690 170 - rowan
    # -----------------------------------PlayerArmy--------------------------
    dunstan = Fighter (590,190,'dunstan',round(120*upgrade),round(120*upgrade),round(40*upgrade),round(30*upgrade),round(65*upgrade),round(8*upgrade),1,0,True,
                       round(4*upgrade),round(4*upgrade),False,0,round(15*upgrade),round(15*upgrade),round(15*upgrade),round(25*upgrade),round(5*upgrade),0,'hero',
                       round(10*upgrade),round(35*upgrade),'weapon','healthy')
    bartelago = Fighter (550,210,'bartelago',round(160*upgrade),round(80*upgrade),round(60*upgrade),round(20*upgrade),round(50*upgrade),round(6*upgrade),1,0,True,
                       round(4*upgrade),round(4*upgrade),False,round(10*upgrade),round(10*upgrade),round(10*upgrade),round(10*upgrade),round(25*upgrade),round(8*upgrade),0,'hero',
                       round(15*upgrade),round(10*upgrade),'tear','healthy')
    rowan = Fighter(690, 170, 'rowan',rowan_health_points , rowan_armor_points, rowan_melee_damage, rowan_ranged_damage,
                    rowan_defence,rowan_threshold, 1, 0, True,20, rowan_tricks, False,
                    rowan_arcana_res, rowan_fire_res, rowan_energy_res, rowan_frost_res,
                    rowan_poison_res, rowan_critical_strike, 0, 'hero',rowan_parry,rowan_block,'weapon','healthy')

    #---------------------------------------light_infantry--------------------------------
    light_infantry = []
    for militia in range(10):
        militia = Fighter(random.randrange(500, 600, 30), random.randrange(240, 400, 30),
                           'militia', 50, 30, 35, 0, 35, 3,1, 0, True, 1, 0, False, 0, 5, 0, 5, 5, 3, 40, 'regular',5,10,'weapon','healthy')
        light_infantry.append(militia)
    for spearman in range(6):
        spearman = Fighter(random.randrange(500, 600, 30), random.randrange(220, 400, 30),
                             'spearman', 55, 30, 36, 0, 45, 4,1, 0, True, 1, 0, False, 0, 5, 5, 5, 5, 9, 45, 'regular',33,5,'weapon','healthy')
        light_infantry.append(spearman)
    for captain in range(2):
        captain = Fighter(random.randrange(540, 640, 30), random.randrange(220, 400, 30),
                'captain', 90, 65, 40, 0, 55, 6,1, 5, True, 2, 2, False, 0, 10, 10, 10, 10, 9, 85, 'regular',12,16,'weapon','healthy')
        light_infantry.append(captain)

    #---------------------------------------light_archers--------------------------------
    light_archers = []
    for archer in range(6):
        archer = Fighter(random.randrange(240, 280, 30), random.randrange(220, 380, 30),
                           'archer', 40, 30, 28, 0, 40, 2,2, 1, True, 2, 1, False, 0, 0, 0, 0, 25, 8, 70, 'regular',0,10,'weapon','healthy')
        light_archers.append(archer)
    for marksman in range(3):
        marksman = Fighter(random.randrange(240, 280, 30), random.randrange(220, 380, 30),
                            'marksman', 55, 40, 36, 0, 45, 4,2, 1, True, 2, 1, False, 0, 15, 15, 15, 40, 12, 95, 'regular',0,15,'weapon','healthy')
        light_archers.append(marksman)

    #-----------------------------------------chevaliers------------------------------------
    chevaliers = []
    for chevalier in range(5):
        chevalier = Fighter(random.randrange(500, 600, 30), random.randrange(400, 500, 30),
                            'chevalier', 120, 100, 60, 0,55, 8, 1, 0, True, 1, 2, False, 12, 12, 12, 12, 0, 6, 125, 'regular',0,20,'weapon','healthy')
        chevaliers.append(chevalier)
    #-------------------------------------scouts----------------------------------------
    scouts = []
    for scout_skirmisher in range(3):
        scout_skirmisher = Fighter(random.randrange(320, 420, 30), random.randrange(240, 420, 30),
                                   'scout_skirmisher', 65, 40, 32, 0, 55, 2,3, 0, True, 2, 2, False, 0, 20, 0, 20, 40, 12, 80, 'regular',66,20,'weapon','healthy')
        scouts.append(scout_skirmisher)
    for scout_saboteur in range(2):
        scout_saboteur  = Fighter(random.randrange(320, 420, 30), random.randrange(240, 420, 30),
                                      'scout_saboteur', 55, 35, 20, 0, 40, 2,2, 7, True, 4, 1, False, 20, 40, 20, 20, 40, 0, 110, 'regular',0,10,'weapon','healthy')
        scouts.append(scout_saboteur)
    for scout_hunter in range(3):
        scout_hunter = Fighter(random.randrange(320, 420, 30),  random.randrange(240, 420, 30),
                                 'scout_hunter', 45, 30, 32, 0, 30, 2,2, 1, True, 1, 1, False, 0, 10, 0, 10, 20, 10, 75, 'regular',0,15,'weapon','healthy')
        scouts.append(scout_hunter)


    # -----------------------------------------------------------------------
    #battle_roll_dice = random.randint(0, 2)
    army_player = []
    army_player.extend([rowan])
    army_player_reserves = []
    # -----------------------------------------------------------------------
    # max_hp, max_armor, strength, strength2, defence, threshold, reach, special,
    # alive, max_supply, max_tricks, hostile, arcane_res, fire_res, energy_res,
    # frost_res, poison_res,crit, experience, allegiance, parry,block,status):

    # ---------------------------------------ENEMY-----------------------------------
    #-------------------------------------riff_raff----------------------------------
    riff_raff = []
    for h_brigand in range(10):
        h_brigand = Fighter(random.randrange(720, 760, 30),  random.randrange(300, 400, 30),
                              'brigand', 40, 25, 30, 0, 30, 3,1, 0, True, 1, 0, True, 0, 0, 0, 0, 0, 0, 35, 'regular', 6, 10,'weapon', 'healthy')
        riff_raff.append(h_brigand)
    for h_spearman in range(8):
        h_spearman = Fighter(random.randrange(720, 760, 30), random.randrange(200, 300, 30),
                               'spearman', 55, 30, 36, 0, 45, 4,1, 0, True, 1, 0, True, 0, 5, 5, 5, 5, 9, 40, 'regular',33,5,'weapon','healthy')
        riff_raff.append(h_spearman)
    for h_thug in range(6):
        h_thug = Fighter(random.randrange(720, 760, 30), random.randrange(400, 500, 30),
                           'thug', 80, 60, 55, 0,50, 4, 1, 6, True, 1, 2, True, 0, 8, 8, 8, 15, 6, 110, 'regular',12,12,'weapon','healthy')
        riff_raff.append(h_thug)

    #-------------------------------------mercenary_gang----------------------------------
    mercenary_gang = []
    for h_landsknecht in range(6):
        h_landsknecht = Fighter(random.randrange(800, 880, 30), random.randrange(200, 480, 30),
                             'landsknecht', 70, 45, 40, 0, 35, 6, 1, 0, True, 1, 1, True, 0, 10, 0, 10, 10, 7, 90, 'regular',12,8,'weapon','healthy')
        mercenary_gang.append(h_landsknecht)
    for h_footman in range(8):
        h_footman = Fighter(random.randrange(800, 880, 30), random.randrange(200, 480, 30),
                             'footman', 90, 70, 45, 0, 60, 7,1, 0, True, 2, 1, True, 5, 10, 0, 10, 20, 0, 100, 'regular',8,20,'weapon','healthy')
        mercenary_gang.append(h_footman)

    #----------------------------------------bandit_bowmen-------------------------------
    bandit_bowmen = []
    for h_bowman in range(8):
        h_bowman = Fighter(random.randrange(980, 1020, 30), random.randrange(260, 460, 30),
                               'bowman', 35, 20, 25, 0, 25, 0, 2, 1, True, 1, 0, True, 0, 0, 0, 0, 10, 5, 30, 'regular',0,10,'weapon','healthy')
        bandit_bowmen.append(h_bowman)

    #-------------------------------------------red_dragon-----------------------------
    h_red_dragon= Fighter(900, 240, 'red_dragon', 2500, 200, 40, 0, 85, 20,3, 4, True, 0, 10, True, 25, 100, 25, 25, 100, 10, 3000,'monster',10,20,'fire','healthy')
    red_dragon = [h_red_dragon]

    #---------------------------------------------thugs---------------------------------
    thugs = []
    for h_thug in range(6):
        h_thug = Fighter(random.randrange(820, 860, 30),  random.randrange(200, 480, 30),
                           'thug', 80, 60, 55, 0,50, 4, 1, 6, True, 1, 2, True, 0, 8, 8, 8, 15, 6, 110, 'regular',12,12,'weapon','healthy')
        thugs.append(h_thug)

    #------------------------------------------------knechts-----------------------------
    knechts = []
    for h_landsknecht in range(6):
        h_landsknecht = Fighter(random.randrange(820, 860, 30), random.randrange(200, 480, 30),
                                  'landsknecht', 70, 45, 40, 0,35, 6, 1, 0, True, 1, 1, True, 0, 10, 0, 10, 10, 7, 90, 'regular',12,8,'weapon','healthy')
        knechts.append(h_landsknecht)

#------------------------------------------wolf_pack------------------------------------------
    wolf_pack = []
    for h_wolf in range(6):
        h_wolf = Fighter(700 + random.randint(-25, 25), random.randrange(200, 300, 30),'wolf',40,1,25,0,0,0,1,3,True,0,0,True,0,0,0,5,5,3,25,'regular',6,6,'tear','healthy')
        wolf_pack.append(h_wolf)
    for h_blackwolf in range(4):
        h_blackwolf = Fighter(700 + random.randint(-25, 25), random.randrange(200, 300, 30),'blackwolf',60,1,30,0,0,4,1,3,True,0,0,True,0,0,0,15,10,7,45,'regular',12,6,'tear','healthy')
        wolf_pack.append(h_blackwolf)

# ----------------------------------------------------------------------------------------
    battle_roll_dice = random.randint(0, 1)
    print(battle_roll_dice)
    # -----------------------------------------------------------------------
    army_hostiles = []
    if battle_conditions == 1:
        if battle_roll_dice == 0:
            army_hostiles.extend(riff_raff)
            army_hostiles.extend(bandit_bowmen)
            army_hostiles.extend(mercenary_gang)
        if battle_roll_dice == 1:
            army_hostiles.extend(riff_raff)
            army_hostiles.extend(thugs)
            army_hostiles.extend(knechts)
            army_hostiles.extend(bandit_bowmen)
        if battle_roll_dice == 2:
            army_hostiles.extend(red_dragon)

    if battle_conditions == 2:
       army_hostiles.extend(wolf_pack)

    army_hostiles_reserves = []
    enemy_reserves = True






    # ------------------------------ItemsUse(Button)---------------------------
    # inventory_button = button.Button(screen,WINDOW_SIZE[0]*0 + 110, WINDOW_SIZE[1]*0 - 6,inventory_bag,280,120,0, True, 'Inventory')
    book_button = button.ToggleButton(screen, 110, 455, book_of_tricks, 84, 76, 0, True, 'Book of Tricks')
    inventory_button = button.ToggleButton(screen, 20, 455, inventory_bag, 76, 74, 0, True, 'Inventory')
    troops_button = button.ToggleButton(screen, 205, 445, troops, 84, 84, 0, True, 'Troops')


    # ------------------------------ItemsUse(PotionButton)-------------------
    #--------------------------------------------Potions----------------------------------------
    path, dirs, potions = next(os.walk("BattleScreen/resources/battle_potions"))
    potions_count = len(potions)
    POTION_TYPES = potions_count
    potions_img = []
    for x in range(POTION_TYPES):
        img = pygame.image.load(f'BattleScreen/resources/battle_potions/{x}.png').convert_alpha()
        img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * 0.10), (int(WINDOW_SIZE[1] * 0.15))))
        potions_img.append(img)

 #-------------------------------------------------------------------------------------------
    battle_items_box = []
    potion_button = button.PotionButton(screen, 0, WINDOW_SIZE[1] * 0.91, potions_img[0], int(TILE_SIZE*0.9), TILE_SIZE, 45,
                                   False, f'Health Potion. Restores {health_potion_restores} health', 1)
    potion_button1 = button.PotionButton(screen, int(TILE_SIZE*0.92), WINDOW_SIZE[1] * 0.91, potions_img[1], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 80,
                                   False, f'Defence Potion. Restores {defence_potion_adds} armor. Maximizes defense', 2+supply_modifier)
    potion_button2 = button.PotionButton(screen, int(TILE_SIZE*0.92)*2, WINDOW_SIZE[1] * 0.91, potions_img[4], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 70,
                                   False,f'Berserk Potion. Adds {berserk_potion_adds} attack. Removes {int(berserk_potion_adds * 0.5)} defense', 1)
    potion_button3 = button.PotionButton(screen, int(TILE_SIZE*0.92)*3, WINDOW_SIZE[1] * 0.91, potions_img[3], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 50,
                                   False,f'Antidote. Adds {antidote_potion_adds} poison resistance. Removes poison', 1)
    potion_button4 = button.PotionButton(screen, int(TILE_SIZE*0.92)*4, WINDOW_SIZE[1] * 0.91, potions_img[20], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 60,
                                   False,f'Vigor Potion. Restores {vigor_potion_adds} tricks', 1)
    potion_button5 = button.PotionButton(screen, int(TILE_SIZE*0.92)*5, WINDOW_SIZE[1] * 0.91, potions_img[14], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 110,
                                   False,f'Celerity Potion. Gives a free action', 2+supply_modifier)
    potion_button6 = button.PotionButton(screen, int(TILE_SIZE*0.92)*6, WINDOW_SIZE[1] * 0.91, potions_img[15], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 75,
                                   False,f'Ironskin Potion. Adds {ironskin_potion_adds} threshold', 1)
    potion_button7 = button.PotionButton(screen, int(TILE_SIZE*0.92)*7, WINDOW_SIZE[1] * 0.91, potions_img[12], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 90,
                                   False,f'Deathkiss Potion. Adds {deathkiss_potion_adds}% critical hit chance', 1)
    potion_button8 = button.PotionButton(screen, int(TILE_SIZE*0.92)*8, WINDOW_SIZE[1] * 0.91, potions_img[10], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 85,
                                   False,f'Rejuvenation Potion. Regenerates {rejuvenation_potion_adds}% health each turn', 1)
    potion_button9 = button.PotionButton(screen, int(TILE_SIZE*0.92)*9, WINDOW_SIZE[1] * 0.91, potions_img[7], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 50,
                                   False,f'Fireshield Potion. Adds {fireshield_potion_adds} fire resistance', 1)
    potion_button10 = button.PotionButton(screen, int(TILE_SIZE*0.92)*10, WINDOW_SIZE[1] * 0.91, potions_img[6], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 50,
                                   False,f'Frostshield Potion. Adds {frostshield_potion_adds} frost resistance', 1)
    potion_button11 = button.PotionButton(screen, int(TILE_SIZE*0.92)*11, WINDOW_SIZE[1] * 0.91, potions_img[8], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 50,
                                   False,f'Energyshield Potion. Adds {energyshield_potion_adds} energy resistance', 1)
    potion_button12 = button.PotionButton(screen, int(TILE_SIZE*0.92)*12, WINDOW_SIZE[1] * 0.91, potions_img[9], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 50,
                                   False,f'Moonlight Potion. Adds {moonlight_potion_adds} arcana resistance', 1)
    potion_button13 = button.PotionButton(screen, int(TILE_SIZE*0.92)*5, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[11], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 120,
                                    False,f'Poison. Poisons multiple targets', 2+supply_modifier)
    potion_button14 = button.PotionButton(screen, int(TILE_SIZE*0.92)*6, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[18], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 130,
                                    False,f'Liquid Fire. Sets multiple targets on fire', 2+supply_modifier)
    potion_button15 = button.PotionButton(screen, int(TILE_SIZE*0.92)*7, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[2], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 75,
                                    False,f'Acid. Corrodes target\'s armor and threshold', 1)
    potion_button16 = button.PotionButton(screen, int(TILE_SIZE*0.92)*8, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[5], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 65,
                                    False,f'Cleansing Potion. Restores {cleansing_potion_restores} health. Removes effects', 1)
    potion_button17 = button.PotionButton(screen, int(TILE_SIZE*0.92)*9, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[19], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 150,
                                    False,f'Dream Potion. Targets have a chance to skip turn', 3+supply_modifier)
    potion_button18 = button.PotionButton(screen, int(TILE_SIZE*0.92)*10, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[17], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 125,
                                    False,f'Ritual Potion. Attempts to destroy wicked', 3+supply_modifier)
    potion_button19 = button.PotionButton(screen, int(TILE_SIZE*0.92)*11, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[16], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 140,
                                    False,f'Liquid Frost. Freezes multiple targets. Lowers target\'s defence', 2+supply_modifier)
    potion_button20 = button.PotionButton(screen, 0, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[13], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 135,
                                          False,f'Dark Cloud Potion. Curses multiple targets. Lowers target\'s resistances', 2+supply_modifier)
    potion_button21 = button.PotionButton(screen, int(TILE_SIZE*0.92), WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[21], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 115,
                                          False,f'Energy Shard. Shocks multiple targets. Lowers target\'s abilities', 2+supply_modifier)
    potion_button22 = button.PotionButton(screen, int(TILE_SIZE*0.92)*2, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[22], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 200,
                                          False,f'Fire Grenade. Damages multiple targets', 3+supply_modifier)
    potion_button23 = button.PotionButton(screen, int(TILE_SIZE*0.92)*3, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[23], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 225,
                                          False,f'Shrapnel Grenade. Damages multiple targets. Ignores armor and applies bleeding', 3+supply_modifier)
    potion_button24 = button.PotionButton(screen, int(TILE_SIZE*0.92)*4, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[24], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 250,
                                          False,f'Earth Shard. Damages constructs', 3+supply_modifier)
    potion_button25 = button.PotionButton(screen, int(TILE_SIZE*0.92)*12, WINDOW_SIZE[1] * 0.92 - TILE_SIZE, potions_img[25], int(TILE_SIZE*0.9), int(TILE_SIZE*0.95), 90,
                                          False,f'Concentration Potion. Increases block and parry by {concentration_potion_adds}', 1)

    battle_items_box.append([potion_button, potion_button1, potion_button2, potion_button3, potion_button4, potion_button5,
                             potion_button6,potion_button7, potion_button8,potion_button9, potion_button10, potion_button11,
                             potion_button12,potion_button13, potion_button14,potion_button15, potion_button16, potion_button17,
                             potion_button18, potion_button19, potion_button20, potion_button21, potion_button22, potion_button23,
                             potion_button24, potion_button25])

    #---------------------------------Consumables----------------------------------
    with open(f"MainMenuRes/inventory/unlocked_potions.json",'r') as f:
        info = json.loads(f.read())

    if len(info):
        for count,i in enumerate(battle_items_box):
            for j in i:
                j.available = True
        # potion_button.available = info["0"]
        # potion_button1.available = info["1"]
        # potion_button2.available = info["4"]
        # potion_button3.available = info["3"]
        # potion_button4.available = info["20"]
        # potion_button5.available = info["14"]
        # potion_button6.available = info["15"]
        # potion_button7.available = info["12"]
        # potion_button8.available = info["10"]
        # potion_button9.available = info["7"]
        # potion_button10.available = info["6"]
        # potion_button11.available = info["8"]
        # potion_button12.available = info["9"]
        # potion_button13.available = info["11"]
        # potion_button14.available = info["18"]
        # potion_button15.available = info["2"]
        # potion_button16.available = info["5"]
        # potion_button17.available = info["19"]
        # potion_button18.available = info["17"]
        # potion_button19.available = info["16"]
        # potion_button20.available = info["13"]
        # potion_button21.available = info["21"]
        # potion_button22.available = info["22"]
        # potion_button23.available = info["23"]
        # potion_button24.available = info["24"]
        # potion_button25.available = info["25"]

    # ------------------------------IconToggle(Reset)------------------------
    restart_button = button.Button(screen, 1100, 8, retry_icon, 84, 90, 25, False, 'Try Again')
    skip_turn_button = button.Button(screen, WINDOW_SIZE[0] * 0.92, WINDOW_SIZE[1] * 0.62, skip_turn_img, 84, 84, 60,False, f'Skip Turn')
    victory_button = button.Button(screen, 1170, 15, victory_icon, 86, 90, 25, True, 'Back to Map')
    leave_button = button.Button(screen, 1190, 15, doors_icon, 64, 80, 25, True, 'Leave Battlefield')

    # ------------------------------------------MapGeneration--------------------------
    if battle_type == 0:
        f = open('BattleScreen/battle_maps/genericmap.txt')
    if battle_type == 1:
        f = open('BattleScreen/battle_maps/grandmap.txt')
    if battle_type == 2:
        f = open('BattleScreen/battle_maps/epicmap.txt')

    map_data = [[int(c) for c in row] for row in f.read().split('\n')]
    f.close()

    # -----------------------------------------------------------------------------
    def items_info (item):
        pos = pygame.mouse.get_pos()
        if item.rect.collidepoint(pos):
            draw_text(f'{item.price}', fontDMG, (255, 225, 100), 35,TILE_SIZE*7.8)
            draw_text(f'{item.description} || Supply: {item.supply}', fontDMG, green,TILE_SIZE*1.1,TILE_SIZE*7.8)
            screen.blit(coins,(0,TILE_SIZE*7.8))

    def unit_info (item):
        pos = pygame.mouse.get_pos()
        if item.rect.collidepoint(pos):
            draw_text(f'{item.price}', fontDMG, (255, 225, 100), 35,TILE_SIZE*7.8)
            draw_text(f'{item.description}', fontDMG, green,TILE_SIZE*1.6,TILE_SIZE*7.8)
            screen.blit(coins,(0,TILE_SIZE*7.8))

    def technique_info (item):
        pos = pygame.mouse.get_pos()
        if item.rect.collidepoint(pos):
            draw_text(f'{item.description} || Tricks: {item.price}', fontDMG, green,10,TILE_SIZE*7.8)
    #---------------------------------------------------------------------------
    def start_full_auto_battle():
        for i in army_player:
            i.type = 'temporary'
    def start_auto_battle():
        for i in army_player:
            if i.type == 'regular':
               i.type = 'temporary'
    #---------------------------------------------------------------------------
    def aura(who):
        global current_fighter
        global action_cooldown


    def move_map():
        if moving_right:
            scroll[0] += TILE_SIZE//6
        if moving_left:
            scroll[0] -= TILE_SIZE//6
        if moving_up:
            scroll[1] -= TILE_SIZE//6
        if moving_down:
            scroll[1] += TILE_SIZE//6
        for i in army_player:
            i.move_it()
        for j in army_hostiles:
            j.move_it()
    #------------------------------------StatusesChecker--------------------------
    def status_checker(who):
        if who.status == 'bleed':
            pygame.mixer.Sound(bleed_sound).play()
            damage = (10*who.max_hp)//100
            if damage >= 0:
                who.hp -= int(damage)
                damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(damage),red)
                damage_text_group.add(damage_text)
            who.status = 'healthy'
            #------------------------------------
        if who.status == 'poisoned':
            damage = int((1-who.poison_res/100)*((20*who.max_hp)/100))
            pygame.mixer.Sound(poison_sound).play()
            if damage >= 0:
                who.hp -= int(damage)
                damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(damage),red)
                damage_text_group.add(damage_text)
            who.status = 'healthy'
            #------------------------------------
        if who.status == 'inflamed':
            pygame.mixer.Sound(fire_burn).play()
            damage = int((1-who.fire_res/100)*((20*who.max_hp)/100))
            if damage >= 0:
                who.hp -= int(damage)
                damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(damage),red)
                damage_text_group.add(damage_text)
            who.status = 'healthy'
            #------------------------------------
        if who.status == 'corroded':
            pygame.mixer.Sound(acid_burn).play()
            damage = int((20*who.max_armor)/100)
            who.armor -= int(damage)
            who.threshold -=5
            if who.armor <= int(damage):
                who.armor = 0
            if who.threshold < 1:
                who.threshold = 0
            who.status = 'healthy'
            #------------------------------------
        if who.status == 'frozen':
            pygame.mixer.Sound(frost_sound).play()
            damage = int((1-who.frost_res/100)*((10*who.max_hp)/100))
            if damage >= 0:
                who.hp -= int(damage)
                damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(damage),red)
                damage_text_group.add(damage_text)
            who.defence -= int(damage)
            who.block -= 5
            who.parry -= 5
            if who.defence <= int(damage):
                who.defence = 0
            if who.block <= int(damage):
                who.block = 0
            if who.parry <= int(damage):
                who.parry = 0
            who.status = 'healthy'
            #------------------------------------
        if who.status == 'shocked':
            pygame.mixer.Sound(energy_sound).play()
            damage = int((1-who.energy_res/100)*((15*who.max_hp)/100))
            if damage >= 0:
                who.hp -= int(damage)
                damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(damage),red)
                damage_text_group.add(damage_text)
            who.tricks -= 1
            who.supply -= 1
            if who.tricks < 1:
                who.tricks = 0
            if who.supply < 1:
                who.supply = 0
            who.status = 'healthy'
            #------------------------------------
        if who.status == 'cursed':
            pygame.mixer.Sound(clouded_sound).play()
            damage = int((1-who.arcane_res/100)*((10*who.max_hp)/100))
            if damage >= 0:
                who.hp -= int(damage)
                damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(damage),red)
                damage_text_group.add(damage_text)
            who.arcane_res -= 5
            who.fire_res -= 5
            who.poison_res -= 5
            who.frost_res -= 5
            who.energy_res -= 5
            if who.arcane_res < int(damage):
                who.arcane_res = 0
            if who.fire_res < int(damage):
                who.fire_res = 0
            if who.poison_res < int(damage):
                who.poison_res = 0
            if who.frost_res < int(damage):
                who.frost_res = 0
            if who.energy_res < int(damage):
                who.energy_res = 0
            who.status = 'healthy'
        #------------------------------------
        if who.status == 'dreamy' and who.type != 'monster':
            global current_fighter
            pygame.mixer.Sound(dream_sound).play()
            current_fighter += 1
            who.status = 'healthy'
    #------------------------------------------------------------------------------
    def regen_heal(who):
        if who.status == 'regen':
            heal_rate = int(5*who.max_hp/100)
            if who.max_hp - who.hp > heal_rate:
                heal_amount = heal_rate
            else:
                heal_amount = who.max_hp - who.hp
            who.hp += heal_amount
            damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(heal_amount),green)
            damage_text_group.add(damage_text)
            damage_text_group.update()
            damage_text_group.draw(screen)
    #------------------------------------------------------------------------------
    def hastened(who):
        global current_fighter
        global action_cooldown
        if who.status == 'haste':
            current_fighter -= 1
            action_cooldown = 0
            who.status = 'healthy'

    # ------------------------------AutoDefencePotion------------------
    def auto_defence_potion(who):
        global current_fighter
        global action_cooldown
        if (who.armor / who.max_armor) < 0.2 and who.armor < 100 and who.max_armor > 50 and who.supply > 0:
            if who.max_armor - who.armor > 100:
               add_defence_amount = 100
            else:
                add_defence_amount = who.max_armor - who.armor
            who.armor += add_defence_amount
            who.defence = 100
            who.supply -= 1
            pygame.mixer.Sound(open_potion).play()
            current_fighter += 1
            action_cooldown = 0

    #------------------------------AutoHealthPotion------------------
    def auto_health_potion(who):
        global current_fighter
        global action_cooldown
        if (who.hp / who.max_hp) < 0.5 and who.supply > 0:
            if who.max_hp - who.hp > 50:
                heal_amount = 50
            else:
                heal_amount = who.max_hp - who.hp
            who.hp += heal_amount
            who.status = 'healthy'
            who.supply -= 1
            damage_text = DamageText(who.rect.centerx, who.rect.y - 35, str(heal_amount), green)
            damage_text_group.add(damage_text)
            pygame.mixer.Sound(open_potion).play()
            current_fighter += 1
            action_cooldown = 0

    #------------------------------------------------------------------------------

    while current_battle_running:
        if full_auto_battle == 1:
           start_full_auto_battle()
        if auto_battle == 1:
           start_auto_battle()

    # ------------------------------TotalUnitNumber----------------------------
        total_hostiles = len(army_hostiles)
        total_allies = len(army_player)
        total_fighters = total_hostiles + total_allies

        army_player_front = [ally for ally in army_player if ally.reach != 2]
        army_player_back = [ally for ally in army_player if ally.reach == 2]
        army_hostiles_front = [enemy for enemy in army_hostiles if enemy.reach != 2]
        army_hostiles_back = [enemy for enemy in army_hostiles if enemy.reach == 2]
        # display.fill((146,244,255))
        draw_bgBackscreen()

        # draw_bg()

    # --------------------------------MapGeneration-------------------------------------
        path, dirs, tiles = next(os.walk("BattleScreen/battle_maps/cubes"))
        tiles_count = len(tiles)
        TILES_TYPES = tiles_count
        tiles_img = []
        for x in range(TILES_TYPES):
            img = pygame.image.load(f'BattleScreen/battle_maps/cubes/{x}.png').convert_alpha()
            img = pygame.transform.scale(img,  (int(WINDOW_SIZE[0] * tilescale), (int(WINDOW_SIZE[1] * tilescale))))
            tiles_img.append(img)

        #-----------------------------------------------------------------------------
        tiles = []
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    #screen.blit(tiles_img[6], (570 + (x * 60 - y * 60) * rendermod - scroll[0], 80* rendermod + (x * 18 + y * 18) * rendermod - scroll[1]))
                    # pygame.draw.rect(screen, (255,255,255), pygame.Rect(x*10, y*10,10,10),1)
                    screen.blit(tiles_img[14], (570 + (x * 60 - y * 60) * rendermod - scroll[0], 80* rendermod + (x * 18 + y * 18) * rendermod - scroll[1]))
                elif tile == 0:
                    #screen.blit(tiles_img[6], (570 + (x * 60 - y * 60) * rendermod - scroll[0], 80* rendermod + (x * 18 + y * 18) * rendermod - scroll[1]))
                    screen.blit(tiles_img[1], (570 + (x * 60 - y * 60) * rendermod - scroll[0], 80* rendermod + (x * 18 + y * 18) * rendermod - scroll[1]))
                tiles.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # -----------------------------DrawUnits/AnimationSpeedMod------------
        if summon_dunstan:
            if unit_button.summon == True:
                army_player.extend([dunstan])
                summon_dunstan = False
                unit_button.summon = False
        if summon_bartelago:
            if unit_button5.summon == True:
                army_player.extend([bartelago])
                summon_bartelago = False
                unit_button5.summon = False
        if summon_melee:
            if unit_button1.summon == True:
                army_player.extend(light_infantry)
                summon_melee = False
                unit_button1.summon = False
        if summon_ranged:
            if unit_button2.summon== True :
                army_player.extend(light_archers)
                summon_ranged = False
                unit_button2.summon = False
        if summon_cavalry:
            if unit_button3.summon == True:
                army_player.extend(chevaliers)
                summon_cavalry = False
                unit_button3.summon = False
        if summon_support:
            if unit_button4.summon == True:
                army_player.extend(scouts)
                summon_support = False
                unit_button4.summon = False

        for count,units in enumerate(army_player):
            units.update(round(random.uniform(0.7, 1.2), 2))
            units.draw()
            HealthBar = units.healthBar(units.rect.centerx-25,units.rect.centery-55,units.hp, units.max_hp)
            ArmorBar = units.armorBar(units.rect.centerx-25,units.rect.centery-50,units.armor, units.max_armor)
            if units.alive == True and show_indicators == True:
                HealthBar.draw(units.hp)
                ArmorBar.draw(units.armor)

        # ------------------Enemy--------------
        for count,hostile in enumerate(army_hostiles):
            hostile.update(round(random.uniform(0.7, 1.2), 2))
            hostile.draw()
            HealthBar = hostile.healthBar(hostile.rect.centerx-25,hostile.rect.centery-55,hostile.hp, hostile.max_hp)
            ArmorBar = hostile.armorBar(hostile.rect.centerx-25,hostile.rect.centery-50,hostile.armor, hostile.max_armor)
            if hostile.alive == True and show_indicators == True:
                HealthBar.draw(hostile.hp)
                ArmorBar.draw(hostile.armor)

        # ------------------------EnemyReserves------------------
        # if h_dragohare.alive == False:
        #     h_caerbannog.update(1.3)
        #     h_caerbannog.draw()
        #     if enemy_reserves == True:
        #        army_hostiles.append(h_caerbannog)
        #        army_hostiles = army_hostiles_reserves
        #        enemy_reserves = False
        #     if h_caerbannog.alive == True:
        #        h_caerbannog_healthbar.draw(h_caerbannog.hp)
        #        h_caerbannog_armorbar.draw(h_caerbannog.armor)
        # -------------------------------------------------------
        draw_panel()
        # -----------------------------Items/SkipTurn/Inventory/LeaveButton-----------------------------
        pos = pygame.mouse.get_pos()
        if skip_turn_button.rect.collidepoint(pos):
            draw_text(f'{skip_turn_button.description}', fontDMG, green, skip_turn_button.rect.x - 30,
                      skip_turn_button.rect.y + 100)
        if skip_turn_button.draw():
            skip_turn = True
        if battle_status != 2 and leave_button.available == True:
            if leave_button.rect.collidepoint(pos):
                draw_text(f'{leave_button.description}', fontDMG, green, leave_button.rect.x - 140,
                          leave_button.rect.y + 100)
            if leave_button.draw():
                play_music('Map')
                button.wealth = button.start_wealth
                button.PartyHealth -= random.randint(10, 25)
                button.PartyStartHealth = button.PartyHealth
                print(button.PartyHealth)
                print(button.PartyStartHealth)
                if battle_conditions == 99: button.westrad_coal_mine = 'neutral'
                if battle_conditions == 98: button.westrad_ore_mine_0 = 'neutral'
                if battle_conditions == 97: button.westrad_ore_mine_1 = 'neutral'
                if battle_conditions == 96: button.westrad_gold_mine = 'neutral'
                if battle_conditions == 95: button.charlatan_silver_mine = 'neutral'
                if battle_conditions == 94: button.charlatan_coal_mine = 'neutral'
                if battle_conditions == 93: button.solomir_silver_mine = 'neutral'
                if battle_conditions == 92: button.solomir_gold_mine_0 = 'neutral'
                if battle_conditions == 91: button.solomir_gold_mine_1 = 'neutral'
                if battle_conditions == 90: button.solomir_gems_mine = 'neutral'
                if battle_conditions == 89: button.kharfajian_gems_mine_0 = 'neutral'
                if battle_conditions == 88: button.kharfajian_gems_mine_1 = 'neutral'
                if battle_conditions == 87: button.kharfajian_krystal_mine = 'neutral'
                current_battle_running = False

        # --------------------------------------------------------------------------------
        if book_button.rect.collidepoint(pos) and book_button.available == True:
            draw_text(f'{book_button.description}', fontDMG, green, potion_button.rect.x + 5, potion_button.rect.y - 110)
        # --------------------------------------------------------------------------------
        if inventory_button.rect.collidepoint(pos) and inventory_button.available == True:
            draw_text(f'{inventory_button.description}', fontDMG, green, potion_button.rect.x + 5,
                      potion_button.rect.y - 110)
        # --------------------------------------------------------------------------------
        if troops_button.rect.collidepoint(pos) and troops_button.available == True:
            draw_text(f'{troops_button.description}', fontDMG, green, potion_button.rect.x + 5,
                      potion_button.rect.y - 110)

#------------------------------------------------------------------------------
        if inventory_button.toggled == True and battle_status == 0:
            book_button.toggled = False
            troops_button.toggled = False
            # ---------------------HealthP0otion----------------------------------------
            if potion_button.available == True:
                items_info(potion_button)
                if potion_button.draw():
                    use_health_potion = True
            #-----------DefencePotion--------------
            if potion_button1.available == True:
                items_info(potion_button1)
                if potion_button1.draw():
                    use_defence_potion = True
            # -------BerserkPotion--------------
            if potion_button2.available == True:
                items_info(potion_button2)
                if potion_button2.draw():
                    use_berserk_potion = True
            # ------------Antidote-------------
            if potion_button3.available == True:
                items_info(potion_button3)
                if potion_button3.draw():
                    use_antidote_potion = True
            # ------------Vigor-------------
            if potion_button4.available == True:
                items_info(potion_button4)
                if potion_button4.draw():
                    use_vigor_potion = True
            # ------------Celerity-------------
            if potion_button5.available == True:
                items_info(potion_button5)
                if potion_button5.draw():
                    use_celerity_potion = True
            # ------------Ironskin-------------
            if potion_button6.available == True:
                items_info(potion_button6)
                if potion_button6.draw():
                    use_ironskin_potion = True
            # ------------Deathkiss-------------
            if potion_button7.available == True:
                items_info(potion_button7)
                if potion_button7.draw():
                    use_deathkiss_potion = True
            # ------------Rejuvenation-------------
            if potion_button8.available == True:
                items_info(potion_button8)
                if potion_button8.draw():
                    use_rejuvenation_potion = True
            # ------------Fireshield-------------
            if potion_button9.available == True:
                items_info(potion_button9)
                if potion_button9.draw():
                    use_fireshield_potion = True
            # ------------Frostshield-------------
            if potion_button10.available == True:
                items_info(potion_button10)
                if potion_button10.draw():
                    use_frostshield_potion = True
            # ------------Energyshield-------------
            if potion_button11.available == True:
                items_info(potion_button11)
                if potion_button11.draw():
                    use_energyshield_potion = True
            # ------------Moonlight-------------
            if potion_button12.available == True:
                items_info(potion_button12)
                if potion_button12.draw():
                    use_moonlight_potion = True
            # ------------Poison-------------
            if potion_button13.available == True:
                items_info(potion_button13)
                if potion_button13.draw():
                    use_poison_potion = True
            # ------------Liquidfire-------------
            if potion_button14.available == True:
                items_info(potion_button14)
                if potion_button14.draw():
                    use_liquidfire_potion = True
            # ------------Acid-------------
            if potion_button15.available == True:
                items_info(potion_button15)
                if potion_button15.draw():
                    use_acid_potion = True
            # ------------Cleansing-------------
            if potion_button16.available == True:
                items_info(potion_button16)
                if potion_button16.draw():
                    use_cleansing_potion = True
            # ------------Dream-------------
            if potion_button17.available == True:
                items_info(potion_button17)
                if potion_button17.draw():
                    use_dream_potion = True
          # ------------Ritual-------------
            if potion_button18.available == True:
                items_info(potion_button18)
                if potion_button18.draw():
                   use_ritual_potion = True
           # ------------liquidfrost-------------
            if potion_button19.available == True:
                items_info(potion_button19)
                if potion_button19.draw():
                    use_liquidfrost_potion = True
            # ------------Darkcloud-------------
            if potion_button20.available == True:
                items_info(potion_button20)
                if potion_button20.draw():
                    use_darkcloud_potion = True
            # ------------EnergyShard-------------
            if potion_button21.available == True:
                items_info(potion_button21)
                if potion_button21.draw():
                    use_energy_shard = True
            # ------------Grenade-------------
            if potion_button22.available == True:
                items_info(potion_button22)
                if potion_button22.draw():
                    use_grenade = True
            # ------------ShrapnelGrenade-------------
            if potion_button23.available == True:
                items_info(potion_button23)
                if potion_button23.draw():
                    use_shrapnel_grenade = True
            # ------------EarthShard-------------
            if potion_button24.available == True:
                items_info(potion_button24)
                if potion_button24.draw():
                    use_earth_shard = True
            # ------------Concentration-------------
            if potion_button25.available == True:
                items_info(potion_button25)
                if potion_button25.draw():
                    use_concentration_potion = True
        # ---------------------InventoryStock--------------------------------------
            for count,i in enumerate(battle_items_box):
                for potion in i:
                    if potion.available == False:
                       screen.blit(no_potion, (potion.rect.x, potion.rect.y))

        #------------------------------------------------------------------------------
        if troops_button.toggled == True and battle_status == 0:
            book_button.toggled = False
            inventory_button.toggled = False
            for count,j in enumerate(battle_units_box):
                for unit in j:
                    if unit.available == True:
                        screen.blit(no_icon, (unit.rect.x, unit.rect.y))
# -----------------------------ArmySummon----------------------------------------
            if summon_dunstan == True:
                if unit_button.available == True:
                    unit_info(unit_button)
                    if unit_button.draw():
                       button.wealth -= unit_button.price
                       pygame.mixer.Sound(coins_sound).play()
                       unit_button.summon = True
            if summon_bartelago == True:
                if unit_button5.available == True:
                    unit_info(unit_button5)
                    if unit_button5.draw():
                        button.wealth -= unit_button5.price
                        pygame.mixer.Sound(coins_sound).play()
                        unit_button5.summon = True
            if summon_melee == True:
                if unit_button1.available == True:
                    unit_info(unit_button1)
                    if unit_button1.draw():
                        button.wealth -= unit_button1.price
                        pygame.mixer.Sound(coins_sound).play()
                        unit_button1.summon = True
            if summon_ranged == True:
                if unit_button2.available == True:
                    unit_info(unit_button2)
                    if unit_button2.draw():
                        button.wealth -= unit_button2.price
                        pygame.mixer.Sound(coins_sound).play()
                        unit_button2.summon = True
            if summon_cavalry == True:
                if unit_button3.available == True:
                    unit_info(unit_button3)
                    if unit_button3.draw():
                        button.wealth -= unit_button3.price
                        pygame.mixer.Sound(coins_sound).play()
                        unit_button3.summon = True
            if summon_support == True:
                if unit_button4.available == True:
                    unit_info(unit_button4)
                    if unit_button4.draw():
                        button.wealth -= unit_button4.price
                        pygame.mixer.Sound(coins_sound).play()
                        unit_button4.summon = True
        #print(total_fighters)
    #------------------------------------------------------------------------------
        if book_button.toggled == True and battle_status == 0:
            troops_button.toggled = False
            inventory_button.toggled = False
            for count,technique in enumerate(battle_techniques_box):
                #for technique in j:
                    if technique.available == True:
                        screen.blit(no_icon, (technique.rect.x, technique.rect.y))
                        technique_info(technique)
                        technique.draw()

    # --------------------------------------------------------------------------
        if battle_status == 0:  # win/loose check
            # -----------------------------PlayerAttacking---------------------------
            for count, ally in enumerate(army_player):
                alive_enemy_targets = sum(enemy.alive == True for enemy in army_hostiles)
                alive_enemy_front_targets = sum(enemy.alive == True for enemy in army_hostiles_front)
                if current_fighter == 1 + count:
                    draw_text('^', fontActive, "#FFA500", ally.rect.centerx - 20, ally.rect.y - 65)
                    if ally.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_waittime:
                            #------------------------------------
                            status_checker(ally)
                            #------------------------------------
                            if ally.type == 'temporary':
                                if (ally.armor / ally.max_armor) < 0.2 and ally.armor < 100 and ally.max_armor > 50 and ally.supply > 0:
                                    auto_defence_potion(ally)
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                elif (ally.hp / ally.max_hp) < 0.5 and ally.supply > 0:
                                    auto_health_potion(ally)
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                elif ally.id == 'scout_saboteur':
                                    splash = alive_enemy_targets
                                    ally.attack(random.choice([enemy for enemy in army_hostiles if enemy.alive == True]))
                                    for enemy in army_hostiles[:splash]:
                                        if 25 >= random.randint(0,100) and enemy.alive == True:
                                            enemy.status = random.choice(['inflamed','poisoned','corroded'])
                                elif ally.reach != 2 and all(enemy.alive == False for enemy in army_hostiles_front):
                                    ally.attack(random.choice([enemy for enemy in army_hostiles if enemy.alive == True]))
                                elif ally.reach != 2:
                                    ally.attack(random.choice([enemy for enemy in army_hostiles_front if enemy.alive == True]))
                                else:
                                    ally.attack(random.choice([enemy for enemy in army_hostiles if enemy.alive == True]))
                                current_fighter += 1
                                action_cooldown = 0
                                hastened(ally)

                            elif ally.id == 'scout_saboteur':
                                if engage == True and target != None:
                                   ally.attack(target)
                                   target.status = random.choice(['inflamed','poisoned','corroded'])
                                   if alive_enemy_targets >= 6: splash = 6
                                   else: splash = alive_enemy_targets
                                   for enemy in army_hostiles[:splash]:
                                       if 70 >= random.randint(0,100) and enemy.alive == True:
                                              enemy.status = random.choice(['inflamed','poisoned','corroded'])
                                   current_fighter += 1
                                   action_cooldown = 0
                                   hastened(ally)
                                   regen_heal(ally)

                            elif ally.reach == 2 or ally.reach == 3:
                                if engage == True and target != None:
                                    ally.attack(target)
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                    regen_heal(ally)

                            elif ally.reach == 1:
                                if engage == True and target != None and target.reach != 2:
                                    ally.attack(target)
                                    current_fighter += 1
                                    action_cooldown = 0
                                    aura(ally)
                                    hastened(ally)
                                    regen_heal(ally)

                            for enemy in army_hostiles_front:
                                if all(enemy.alive == False for enemy in army_hostiles_front):
                                    if ally.reach == 1:
                                        if engage == True and target != None and target.reach == 2:
                                            ally.reach = 2
                                            ally.attack(target)
                                            current_fighter += 1
                                            action_cooldown = 0
                                            aura(ally)
                                            hastened(ally)
                                            regen_heal(ally)

                            for enemy in army_hostiles_back:
                                if all(enemy.alive == False for enemy in army_hostiles_front):
                                    if ally.reach == 1:
                                        if engage == True and target != None and target.reach == 2:
                                            ally.reach = 2
                                            ally.attack(target)
                                            current_fighter += 1
                                            action_cooldown = 0
                                            aura(ally)
                                            hastened(ally)
                                            regen_heal(ally)

                            if ally.id == 'rowan' or 'dunstan' or 'bartelago' or 'anselm' or 'regina' or 'alba' or 'severin':
                                if engage2 == True and target != None:
                                    ally.alternative_attack(target)
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if Quick_Shot == 1 and ally.status != 'haste' and ally.id == 'rowan' and random.randint(0,100) <= 25:
                                           current_fighter -= 1
                                           action_cooldown = 0
                                    hastened(ally)
                                    regen_heal(ally)
            # -----------------------------------------SkipTurn-----------------------------------------
                            if skip_turn == True:
                                current_fighter += 1
                                action_cooldown = 0
                                if Quartermaster == 1:
                                    skip_turn_heal = 20
                                    skip_turn_tricks = 2
                                else:
                                    skip_turn_heal = 10
                                    skip_turn_tricks = 1
                                if ally.max_hp - ally.hp > skip_turn_heal:  # 50
                                    skip_turn_heal = skip_turn_heal
                                else:
                                    skip_turn_heal = ally.max_hp - ally.hp
                                ally.hp += skip_turn_heal
                                if ally.tricks < ally.max_tricks:
                                    ally.tricks +=skip_turn_tricks
                                if ally.supply < ally.max_supply and Quartermaster==1:
                                   ally.supply += 1

                                # DamageText
                                damage_text = DamageText(ally.rect.centerx, ally.rect.y - 35, str(skip_turn_heal),green)
                                damage_text_group.add(damage_text)
                            skip_turn = False

                            # ------------HealthPotion---------------------------
                            if use_health_potion == True and button.wealth >= potion_button.price:
                                if ally.supply >= potion_button.supply:
                                    # not healing beyond max_hp
                                    if ally.max_hp - ally.hp > health_potion_restores:  # 50
                                        heal_amount = health_potion_restores
                                    else:
                                        heal_amount = ally.max_hp - ally.hp
                                    ally.hp += heal_amount
                                    ally.supply -= potion_button.supply
                                    button.wealth -= potion_button.price
                                    # DamageText
                                    damage_text = DamageText(ally.rect.centerx, ally.rect.y - 35, str(heal_amount),green)
                                    damage_text_group.add(damage_text)
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_health_potion = False
                            # ------------DefencePotion---------------
                            if use_defence_potion == True and button.wealth >= potion_button1.price:
                                if ally.supply >= potion_button1.supply:
                                    # not healing beyond max_hp
                                    if ally.max_armor - ally.armor > defence_potion_adds:  # 50
                                        add_defence_amount = defence_potion_adds
                                    else:
                                        add_defence_amount = ally.max_armor - ally.armor
                                    ally.armor += add_defence_amount
                                    ally.defence = 100
                                    ally.supply -= potion_button1.supply
                                    button.wealth -= potion_button1.price  # Change price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_defence_potion = False
                            # ------------BerserkPotion---------------
                            if use_berserk_potion == True and button.wealth >= potion_button2.price:
                                if ally.supply >= potion_button2.supply:
                                    ally.strength += berserk_potion_adds
                                    if ally.defence < int(berserk_potion_adds * 0.5):
                                        ally.defence = 0
                                    else:
                                        ally.defence -= int(berserk_potion_adds * 0.5)
                                    ally.supply -= potion_button.supply
                                    button.wealth -= potion_button2.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_berserk_potion = False
                            # ------------Antidote---------------
                            if use_antidote_potion == True and button.wealth >= potion_button3.price:
                                if ally.supply >= potion_button3.supply:
                                    ally.poison_res += antidote_potion_adds
                                    ally.supply -= potion_button3.supply
                                    button.wealth -= potion_button3.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if ally.status == 'poisoned':
                                        ally.status = 'healthy'
                                    hastened(ally)
                                use_antidote_potion = False
                            # ------------VigorPotion---------------
                            if use_vigor_potion == True and button.wealth >= potion_button4.price:
                                if ally.supply >= potion_button4.supply:
                                    if ally.max_tricks-ally.tricks <= vigor_potion_adds:
                                        ally.tricks += vigor_potion_adds
                                    elif ally.tricks > ally.max_tricks:
                                        ally.tricks = ally.max_tricks
                                    else:
                                        ally.tricks = ally.max_tricks
                                    ally.supply -= potion_button4.supply
                                    button.wealth -= potion_button4.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_vigor_potion = False
                            # ------------Celerity---------------
                            if use_celerity_potion == True and button.wealth >= potion_button5.price:
                                if ally.supply >= potion_button5.supply:
                                    ally.status = 'haste'
                                    ally.supply -= potion_button5.supply
                                    button.wealth -= potion_button5.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 0
                                    action_cooldown = 0
                                use_celerity_potion = False
                            # ------------ironskin---------------
                            if use_ironskin_potion == True and button.wealth >= potion_button6.price:
                                if ally.supply >= potion_button6.supply:
                                    ally.threshold += ironskin_potion_adds
                                    ally.supply -= potion_button6.supply
                                    button.wealth -= potion_button6.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_ironskin_potion = False
                            # ------------deathkiss---------------
                            if use_deathkiss_potion == True and button.wealth >= potion_button7.price:
                                if ally.supply >= potion_button7.supply:
                                    ally.crit += deathkiss_potion_adds
                                    ally.supply -= potion_button7.supply
                                    button.wealth -= potion_button7.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_deathkiss_potion = False
                            # ------------rejuvenation---------------
                            if use_rejuvenation_potion == True and button.wealth >= potion_button8.price:
                                if ally.supply >= potion_button8.supply:
                                    ally.status = 'regen'
                                    ally.supply -= potion_button8.supply
                                    button.wealth -= potion_button8.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_rejuvenation_potion = False
                                # ------------fire---------------
                            if use_fireshield_potion == True and button.wealth >= potion_button9.price:
                                if ally.supply >= potion_button9.supply:
                                    ally.fire_res += fireshield_potion_adds
                                    ally.supply -= potion_button9.supply
                                    button.wealth -= potion_button9.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_fireshield_potion = False
                                # ------------frost---------------
                            if use_frostshield_potion == True and button.wealth >= potion_button10.price:
                                if ally.supply >= potion_button10.supply:
                                    ally.frost_res += frostshield_potion_adds
                                    ally.supply -= potion_button10.supply
                                    button.wealth -= potion_button10.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_frostshield_potion = False
                                # ------------energy---------------
                            if use_energyshield_potion == True and button.wealth >= potion_button11.price:
                                if ally.supply >= potion_button11.supply:
                                    ally.energy_res += energyshield_potion_adds
                                    ally.supply -= potion_button11.supply
                                    button.wealth -= potion_button11.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_energyshield_potion = False
                                # ------------moonlight---------------
                            if use_moonlight_potion == True and button.wealth >= potion_button12.price:
                                if ally.supply >= potion_button12.supply:
                                    ally.arcane_res += moonlight_potion_adds
                                    ally.supply -= potion_button12.supply
                                    button.wealth -= potion_button12.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_moonlight_potion = False
                                # ------------poison---------------
                            if use_poison_potion == True and button.wealth >= potion_button13.price:
                                if ally.supply >= potion_button13.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 10: target = 10
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                                 enemy.status = 'poisoned'
                                    ally.supply -= potion_button13.supply
                                    button.wealth -= potion_button13.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_poison_potion = False

                            # ------------liquidfire---------------
                            if use_liquidfire_potion == True and button.wealth >= potion_button14.price:
                                if ally.supply >= potion_button14.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 10: target = 10
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                           enemy.status = 'inflamed'
                                    ally.supply -= potion_button14.supply
                                    button.wealth -= potion_button14.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_liquidfire_potion = False
                                # ------------liquidfrost---------------
                            if use_liquidfrost_potion== True and button.wealth >= potion_button19.price:
                                if ally.supply >= potion_button19.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 10: target = 10
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                             enemy.status = 'frozen'
                                    ally.supply -= potion_button19.supply
                                    button.wealth -= potion_button19.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_liquidfrost_potion = False
                            # ------------darkcloud---------------
                            if use_darkcloud_potion== True and button.wealth >= potion_button20.price:
                                if ally.supply >= potion_button20.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 10: target = 10
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                                enemy.status = 'cursed'
                                    ally.supply -= potion_button20.supply
                                    button.wealth -= potion_button20.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_darkcloud_potion = False
                            # ------------acid---------------
                            if use_acid_potion == True and button.wealth >= potion_button15.price:
                                if ally.supply >= potion_button15.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 10: target = 10
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                            enemy.status = 'corroded'
                                    ally.supply -= potion_button15.supply
                                    button.wealth -= potion_button15.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_acid_potion = False
                            # ------------cleansing---------------------------
                            if use_cleansing_potion == True and button.wealth >= potion_button16.price:
                                if ally.supply >= potion_button16.supply:
                                    ally.status = 'healthy'
                                    if ally.max_hp - ally.hp > cleansing_potion_restores:  # 50
                                        heal_amount = cleansing_potion_restores
                                    else:
                                        heal_amount = ally.max_hp - ally.hp
                                    ally.hp += heal_amount
                                    ally.supply -= potion_button16.supply
                                    button.wealth -= potion_button16.price
                                    # DamageText
                                    damage_text = DamageText(ally.rect.centerx, ally.rect.y - 35, str(heal_amount),green)
                                    damage_text_group.add(damage_text)
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_cleansing_potion = False
                            # ------------dreams---------------
                            if use_dream_potion == True and button.wealth >= potion_button17.price:
                                if ally.supply >= potion_button17.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 6: target = 6
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                                enemy.status = 'dreamy'
                                    ally.supply -= potion_button17.supply
                                    button.wealth -= potion_button17.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_dream_potion = False
                            # ------------ritual---------------
                            if use_ritual_potion == True and button.wealth >= potion_button18.price:
                                if ally.supply >= potion_button18.supply:
                                    alive_targets = sum(enemy.alive == True and enemy.type == 'wicked' for enemy in army_hostiles)
                                    if alive_targets >= 6: target = 6
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True and enemy.type == 'wicked':
                                              enemy.hp -= 100
                                    ally.supply -= potion_button18.supply
                                    button.wealth -= potion_button18.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_ritual_potion = False
                            # ------------energyshard---------------
                            if use_energy_shard == True and button.wealth >= potion_button21.price:
                                if ally.supply >= potion_button21.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 10: target = 10
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True:
                                                enemy.status = 'shocked'
                                    ally.supply -= potion_button21.supply
                                    button.wealth -= potion_button21.price
                                    pygame.mixer.Sound(break_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_energy_shard = False
                            # ------------Grenade---------------
                            if use_grenade == True and button.wealth >= potion_button22.price:
                                if ally.supply >= potion_button22.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 6: target = 6
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True and enemy.hp >0:
                                                enemy.armor -= int(grenade_damage * (enemy.defence / 100))
                                                if enemy.armor > 0:
                                                    enemy.hp -= int(grenade_damage * (1 - enemy.defence / 100))
                                                if enemy.armor <= 0:
                                                    enemy.hp -= int((grenade_damage * (1 - enemy.defence / 100) - enemy.armor))
                                                    enemy.armor = 0
                                                enemy.hurt()
                                                if enemy.armor > 1:
                                                    damage_text = DamageText(enemy.rect.centerx, enemy.rect.y - 35,str(int(grenade_damage * (1 - enemy.defence / 100))), red)
                                                else:
                                                    damage_text = DamageText(enemy.rect.centerx, enemy.rect.y - 35, str(grenade_damage), red)
                                                damage_text_group.add(damage_text)
                                                damage_text_group.update()
                                                damage_text_group.draw(screen)
                                    ally.supply -= potion_button22.supply
                                    button.wealth -= potion_button22.price
                                    pygame.mixer.Sound(grenade_blast).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_grenade = False
                            # ------------ShrapnelGrenade---------------
                            if use_shrapnel_grenade == True and button.wealth >= potion_button23.price:
                                if ally.supply >= potion_button23.supply:
                                    alive_targets = sum(enemy.alive == True for enemy in army_hostiles)
                                    if alive_targets >= 6:target = 6
                                    else:target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True and enemy.hp >0:
                                                enemy.status = 'bleed'
                                                enemy.hp -= int(shrapnel_grenade_damage)
                                                enemy.hurt()
                                                damage_text = DamageText(enemy.rect.centerx, enemy.rect.y - 35, str(shrapnel_grenade_damage), red)
                                                damage_text_group.add(damage_text)
                                                damage_text_group.update()
                                                damage_text_group.draw(screen)
                                    ally.supply -= potion_button23.supply
                                    button.wealth -= potion_button23.price
                                    pygame.mixer.Sound(grenade_blast).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_shrapnel_grenade = False
                            # ------------EarthShard---------------
                            if use_earth_shard == True and button.wealth >= potion_button24.price:
                                if ally.supply >= potion_button24.supply:
                                    alive_targets = sum(enemy.alive == True and enemy.type == 'construct' for enemy in army_hostiles)
                                    if alive_targets >= 6: target = 6
                                    else: target = alive_targets
                                    for enemy in army_hostiles[:target]:
                                        if 50 >= random.randint(0,100) and enemy.alive == True and enemy.type == 'construct':
                                                if enemy.armor >= earth_shard_damage:
                                                   enemy.armor -= int(earth_shard_damage)
                                                else:
                                                     enemy.armor = 0
                                                if enemy.threshold >= earth_shard_damage//10:
                                                   enemy.threshold -= earth_shard_damage//10
                                                else:
                                                     enemy.threshold = 0
                                    ally.supply -= potion_button24.supply
                                    button.wealth -= potion_button24.price
                                    pygame.mixer.Sound(tremors_sound).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_earth_shard = False
                            # ------------Concentration---------------
                            if use_concentration_potion == True and button.wealth >= potion_button25.price:
                                if ally.supply >= potion_button25.supply:
                                    ally.block += concentration_potion_adds
                                    ally.parry += concentration_potion_adds
                                    ally.supply -= potion_button25.supply
                                    button.wealth -= potion_button25.price
                                    pygame.mixer.Sound(open_potion).play()
                                    current_fighter += 1
                                    action_cooldown = 0
                                    hastened(ally)
                                use_concentration_potion = False
                    else:
                        current_fighter += 1

            # -----------------------------EnemyAttacking----------------------------
            for count, enemy in enumerate(army_hostiles):
                alive_targets = sum(ally.alive == True for ally in army_player)
                alive_front_targets = sum(ally.alive == True for ally in army_player_front)
                if current_fighter == 1 + total_allies + count:  # "3 + count" - checks with the max_fighter var and number of units in army_player
                    draw_text('^', fontActive, "#FFA500", enemy.rect.centerx - 20, enemy.rect.y - 65)
                    if enemy.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_waittime:
                            #---------------------------------StatusCheck----------------------------------
                            status_checker(enemy)
                            regen_heal(enemy)
                            # ------------------------------EnemyDefencePotion------------------
                            if (enemy.armor / enemy.max_armor) < 0.2 and enemy.armor < 100 and enemy.max_armor > 50 and enemy.supply > 0:
                                if enemy.max_armor - enemy.armor > 100:
                                    add_defence_amount = 100
                                else:
                                    add_defence_amount = enemy.max_armor - enemy.armor
                                enemy.armor += add_defence_amount
                                enemy.defence = 100
                                enemy.supply -= 1
                                pygame.mixer.Sound(open_potion).play()
                                current_fighter += 1
                                action_cooldown = 0
                                hastened(enemy)

                            #------------------------------EnemyHealthPotion------------------
                            elif (enemy.hp / enemy.max_hp) < 0.5 and enemy.supply > 0:
                                if enemy.max_hp - enemy.hp > 50:
                                    heal_amount = 50
                                else:
                                    heal_amount = enemy.max_hp - enemy.hp
                                enemy.hp += heal_amount
                                enemy.status = 'healthy'
                                enemy.supply -= 1
                                damage_text = DamageText(enemy.rect.centerx, enemy.rect.y - 35, str(heal_amount), green)
                                damage_text_group.add(damage_text)
                                pygame.mixer.Sound(open_potion).play()
                                current_fighter += 1
                                action_cooldown = 0
                                hastened(enemy)
                            # ------------------------------EnemyAbilities------------------
                            elif enemy.id == 'footman' and enemy.tricks >0 and 25 >= random.randint(0,100):
                                    enemy.status = 'haste'
                                    enemy.tricks -= 1
                                    pygame.mixer.Sound(wind_sound).play()
                            elif enemy.id == 'landsknecht' and enemy.tricks >0 and 25 >= random.randint(0,100):
                                if alive_front_targets >=2:
                                    for i in range(2):
                                       target = random.choice([ally for ally in army_player_front if ally.alive == True])
                                       enemy.attack(target)
                                       target.status = 'bleed'
                                else:
                                    for i in range(2):
                                       target =random.choice([ally for ally in army_player if ally.alive == True])
                                       enemy.attack(target)
                                       target.status = 'bleed'
                                pygame.mixer.Sound(sharpening_sound).play()
                                enemy.tricks -= 1
                                current_fighter += 1
                                action_cooldown = 0
                                hastened(enemy)
                            elif enemy.id == 'thug' and enemy.tricks >0 and 25 >= random.randint(0,100):
                                if alive_front_targets >=1:
                                    target = random.choice([ally for ally in army_player_front if ally.alive == True])
                                    enemy.attack(target)
                                else:
                                    target =random.choice([ally for ally in army_player if ally.alive == True])
                                    enemy.attack(target)
                                if target.threshold >= 3: target.threshold -=3
                                if target.armor >= 30: target.armor -= 30
                                if target.defence >= 10: target.defence -=10
                                pygame.mixer.Sound(sharpening_sound).play()
                                enemy.tricks -= 1
                                current_fighter += 1
                                action_cooldown = 0
                                hastened(enemy)
                            elif enemy.reach == 3 and enemy.id == 'red_dragon':
                                alive_targets = sum(ally.alive == True for ally in army_player)
                                target = random.choice([ally for ally in army_player if ally.alive == True])
                                if enemy.tricks >0 and 25 >= random.randint(0,100):
                                    enemy.attack_type = 'fire'
                                    enemy.tricks -= 1
                                    for ally in army_player:
                                        if ally.alive == True:
                                           enemy.attack(ally)
                                           pygame.mixer.Sound(dragon_roar_sound).play()
                                elif alive_targets >= 6:
                                    for ally in army_player[:6]:
                                           enemy.attack_type = random.choice(['fire','tear'])
                                           enemy.attack(target)
                                elif alive_targets < 6:
                                    for ally in army_player[:alive_targets]:
                                           enemy.attack_type = random.choice(['fire','tear'])
                                           enemy.attack(target)
                                else:
                                    enemy.attack_type = 'tear'
                                    enemy.attack(target)
                                enemy.armor = enemy.max_armor
                                current_fighter += 1
                                action_cooldown = 0
                                hastened(enemy)

                            # -------------------------------------------------------------------
                            elif enemy.reach == 2:
                                if enemy.strength >= ally.hp and ally.alive == True:
                                    enemy.attack(ally)
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if enemy.status == 'haste' and enemy.alive == True:
                                        current_fighter -= 1
                                        action_cooldown = 0
                                        enemy.status = 'healthy'
                                else:
                                    enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if enemy.status == 'haste' and enemy.alive == True:
                                        current_fighter -= 1
                                        action_cooldown = 0
                                        enemy.status = 'healthy'

                            elif enemy.reach == 1:
                                if all(ally.alive == True for ally in army_player_front):
                                    enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach != 2]))
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if enemy.status == 'haste' and enemy.alive == True:
                                        current_fighter -= 1
                                        action_cooldown = 0
                                        enemy.status = 'healthy'
                                elif all(ally.alive == False for ally in army_player_front):
                                    enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 2]))
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if enemy.status == 'haste' and enemy.alive == True:
                                        current_fighter -= 1
                                        action_cooldown = 0
                                        enemy.status = 'healthy'
                                else:
                                    enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach != 2]))
                                    current_fighter += 1
                                    action_cooldown = 0
                                    if enemy.status == 'haste' and enemy.alive == True:
                                        current_fighter -= 1
                                        action_cooldown = 0
                                        enemy.status = 'healthy'

                            else:
                                current_fighter += 1
                    else:
                        current_fighter += 1

            # ----------------------------Turns------------------------------
            for count,i in enumerate(army_hostiles):
                if i.hp < 1:
                    i.hp = 0
                    i.alive = False
                    i.action = 3
                    i.update(1)
            for count,i in enumerate(army_player):
                if i.hp < 1:
                    i.hp = 0
                    i.alive = False
                    i.action = 3
                    i.update(1)
                    # if all have had a turn, reset

            if current_fighter > total_fighters:
                current_fighter = 1

            # -----------------------------DamageText-----------------------------
            damage_text_group.update()
            damage_text_group.draw(screen)

        # -----------------------------DefeatStatus-------------------------
        # checking alive/dead status
        alive_allies = 0
        for ally in army_player:
            if ally.alive == True:
                alive_allies += 1
        if alive_allies == 0:
            battle_status = 1

        # ---------------------------------VictoryStatus--------------------
        alive_enemies = 0
        for enemy in army_hostiles:
            if enemy.alive == True:
                alive_enemies += 1
        if alive_enemies == 0 and all(enemy.alive == False for enemy in army_hostiles_reserves):
            battle_status = 2

        # -------------------Defeat/VictoryStatusDisplay-------------------
        if battle_status != 0:
            if battle_status == 1:
                draw_text(f'Defeat!', fontMenuLarge, (155, 0, 0), screen.get_width() * 0.46, 0)
                if play_defeat_music == True:
                    play_music('BattleDefeat')
                play_defeat_music = False
                # -------------------ResetButton-----------------------------------
                if restart_button.available == True:
                    if restart_button.draw():
                        play_music('Battle')
                        for ally in army_player:
                            ally.reset()
                        for enemy in army_hostiles:
                            enemy.reset()
                        button.wealth = button.start_wealth  # restart gold here
                        current_fighter = 1
                        action_cooldown = 0
                        battle_status = 0
                        pos = pygame.mouse.get_pos()  # text over the button
                    if restart_button.rect.collidepoint(pos):
                        draw_text(f'{restart_button.description}', fontDMG, green, restart_button.rect.x + 30,
                                  leave_button.rect.y + 100)

            # -------------------Defeat/VictoryStatusDisplay-------------------
            if battle_status == 2:
                #button.quest_old_ways = 'locked'
                draw_text(f'Victory!', fontMenuLarge, green, screen.get_width() * 0.46, 0)
                if play_victory_music == True:
                    play_music('BattleVictory')
                play_victory_music = False
                if victory_button.available == True:
                    if victory_button.draw():
                        button.wealth += int(sum([enemy.experience for enemy in army_hostiles]) / 2)
                        button.start_wealth = button.wealth
                        if Educated == 1:
                            bonus_experience = int(((sum([enemy.experience for enemy in army_hostiles])) *
                                               (button.lore + button.investigation) / 75))
                        else:
                            bonus_experience = int(((sum([enemy.experience for enemy in army_hostiles])) *
                                               (button.lore + button.investigation) / 100))
                        button.experience += sum([enemy.experience for enemy in army_hostiles]) + bonus_experience
                        button.start_experience = button.experience
                        if battle_conditions == 99: button.westrad_coal_mine = 'player'
                        if battle_conditions == 98: button.westrad_ore_mine_0 = 'player'
                        if battle_conditions == 97: button.westrad_ore_mine_1 = 'player'
                        if battle_conditions == 96: button.westrad_gold_mine = 'player'
                        if battle_conditions == 95: button.charlatan_silver_mine = 'player'
                        if battle_conditions == 94: button.charlatan_coal_mine = 'player'
                        if battle_conditions == 93: button.solomir_silver_mine = 'player'
                        if battle_conditions == 92: button.solomir_gold_mine_0 = 'player'
                        if battle_conditions == 91: button.solomir_gold_mine_1 = 'player'
                        if battle_conditions == 90: button.solomir_gems_mine = 'player'
                        if battle_conditions == 89: button.kharfajian_gems_mine_0 = 'player'
                        if battle_conditions == 88: button.kharfajian_gems_mine_1 = 'player'
                        if battle_conditions == 87: button.kharfajian_krystal_mine = 'player'
                        # button.quest_finale= 'unlocked'
                        print(button.start_wealth)
                        print(button.wealth)
                        print(button.start_experience)
                        print(button.experience)
                        print(bonus_experience)
                        if Educated == 1:
                            print(f'Educated: {bonus_experience}')
                        pyautogui.moveTo(750, 400)
                        play_music('Map')
                        current_battle_running = False
                    if victory_button.rect.collidepoint(pos):
                        draw_text(f'{victory_button.description}', fontDMG, green, victory_button.rect.x - 75,
                                  leave_button.rect.y + 100)
        # ------------------------------End/Controls------------------------

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), 0, 32)

            if event.type == KEYDOWN:
                if event.key == K_f and show_indicators == True:
                    show_indicators = False
                elif event.key == K_f and show_indicators == False:
                    show_indicators = True
                if event.key == K_g and grid == True:
                    grid = False
                elif event.key == K_g and grid == False:
                    grid = True

                if event.key == K_u and full_auto_battle == 0:
                    full_auto_battle = 1
                if event.key == K_y and auto_battle == 0:
                    auto_battle = 1
                elif event.key == K_y and auto_battle == 1:
                    auto_battle = 0
                    for i in army_player:
                        if i.type == 'temporary':
                            i.type = 'regular'

                if event.key == K_d:
                    moving_right = True
                if event.key == K_a:
                    moving_left = True
                if event.key == K_w:
                    moving_up = True
                if event.key == K_s:
                    moving_down = True

                # if event.key == K_j:
                #     for i in battle_units_box:
                #         for j in i:
                #             j.clicked=False
                #             j.summoned=False
                #

                if event.key == K_o:
                    # fullscreen = not fullscreen
                    # with open('genericmap.txt', 'w') as file:
                    #     file.write(str(fullscreen))
                    button.fullscreen = not button.fullscreen
                    # with open('genericmap.txt', 'w') as file:
                    #     file.write(str(fullscreen))
                    fullscreen = button.fullscreen

                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), 0, 32)

            if event.type == KEYUP:
                if event.key == K_d:
                   moving_right = False
                if event.key == K_a:
                   moving_left = False
                if event.key == K_w:
                   moving_up = False
                if event.key == K_s:
                   moving_down = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                tile_x = (pos[0]) // WAR_TILE
                tile_y = (pos[1]) // WAR_TILE
                WAR_TILE_LOC = tile_x,tile_y
                if grid == True:
                    print(pos)
                    print(WAR_TILE_LOC)
                if event.button == 1:
                    pass

            # ---------------------ToggleButton------------------------
            inventory_button.event_handler(event)
            book_button.event_handler(event)
            troops_button.event_handler(event)
            if book_button.toggled == True:
                for count,i in enumerate(battle_techniques_box):
                       i.event_handler(event)

                # ---------------------ToggleButton------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                elif event.button == 3:
                    clicked2 = True
            else:
                clicked = False
                clicked2 = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         pass
            #     if event.button == 5:
            #         pass

        if leave_button.clicked == True or victory_button.clicked == True:
            mouse_map_position_align(750, 400)
        # -----------------------------Action/TargetSearch-------------------
        engage = False
        engage2 = False
        target = None

        #---------------------------------inventory,troops and tricks------------------------
        inventory_button.draw(screen)  # ToggleButton
        book_button.draw(screen)
        troops_button.draw(screen)
        draw_bag()
        #------------------------------------------------------------------------------------
        pygame.mouse.set_visible(False)
        pos = pygame.mouse.get_pos()
        screen.blit(normal_icon, pos)
        move_map()
        #---------------------------------------Grid-----------------------------------
        if grid == True:
            draw_grid(screen)

        for count, ally in enumerate(army_player):
            if ally.rect.collidepoint(pos) and ally.alive == True:
                draw_text(
                    f'{ally.id} | HP: {ally.hp} | ARM: {ally.armor} | ATK: {ally.strength} | RNG: {ally.strength2} | TYP: {ally.attack_type} | THR: {ally.threshold} | DEF: {ally.defence} | CRT: {ally.crit}  | BLK: {ally.block} | RTL: {ally.parry}',
                    font, (0, 100, 0), ((panel.get_width()) * 0.01),
                    (((screen.get_height() + bg_backscreen.get_height()) / 2.32)))
                draw_text(
                    f'SPL: {ally.supply} | TRK: {ally.tricks} | Arcane: {ally.arcane_res} | Fire: {ally.fire_res} | Energy: {ally.energy_res} | Frost: {ally.frost_res} | Poison: {ally.poison_res} | Status: {ally.status}',
                    font, (0, 100, 0), ((panel.get_width()) * 0.01),
                    (((screen.get_height() + bg_backscreen.get_height()) / 2.25)))

        for count, enemy in enumerate(army_hostiles):
            if enemy.rect.collidepoint(pos) and enemy.alive == True:
                pygame.mouse.set_visible(False)
                screen.blit(attack_icon, pos)
                draw_text(
                    f'{enemy.id} | HP: {enemy.hp} | ARM: {enemy.armor} | ATK: {enemy.strength} | TYP: {enemy.attack_type} | THR: {enemy.threshold} | DEF: {enemy.defence} | CRT: {enemy.crit} | BLK: {enemy.block}  | RTL: {enemy.parry}',
                    font, (100, 0, 0), ((panel.get_width()) * 0.01),
                    (((screen.get_height() + bg_backscreen.get_height()) / 2.32)))
                draw_text(
                    f'SPL: {enemy.supply} | TRK: {enemy.tricks} | Arcane: {enemy.arcane_res} | Fire: {enemy.fire_res} | Energy: {enemy.energy_res} | Frost: {enemy.frost_res} | Poison: {enemy.poison_res} | Status: {enemy.status}',
                    font, (100, 0, 0), ((panel.get_width()) * 0.01),
                    (((screen.get_height() + bg_backscreen.get_height()) / 2.25)))
                # show attack icon | ATKB: {enemy.strength2}
                # --------------chooseTarget&Attack-------------------------
                if clicked == True and enemy.alive == True:
                    engage = True
                    target = army_hostiles[count]
                if clicked2 == True and enemy.alive == True:
                    engage2 = True
                    target = army_hostiles[count]

        # -----------------------------------------------------------------------
        # surf = pygame.transform.scale(display, WINDOW_SIZE)
        # screen.blit(surf, (0,0))

        pygame.display.update()
        clock.tick(60)

# def adventure():
#     adventure_running = True
#     while adventure_running:
#         screen.fill((0,0,0))
#         draw_text('Adventure Begins', fontMenu, (255,225,100),screen, 20,20)
#         draw_text('Press ESC to return', fontMenu, (255,225,100),screen, 20,60)  #Yvan\'s
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     MainMusic.play_music()
#                     adventure_running = False
#
#         pygame.mouse.set_visible(False)
#         mouse_position = pygame.mouse.get_pos()
#         player_rect.x, player_rect.y = mouse_position
#         screen.blit(normal_icon, player_rect)
#
#         pygame.display.update()
#         mainClock.tick(60)


def leave():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Quit', fontMenu, (255, 225, 100), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    main_menu()
