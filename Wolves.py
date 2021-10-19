import inspect
import pyautogui
from button import *
import pygame,sys,random
from pygame.locals import *
import pygame as py
vec = pygame.math.Vector2
from abc import ABC, abstractmethod
import threading
import os
from tkinter import *
from pygame.locals import *
import numpy as np
import button
import time
import linecache
from itertools import cycle
from PIL import Image
from scipy.ndimage import zoom
import scipy
#from VagrantsLot import play_music

#if __name__=='__main__':
def wolves_encounter ():
    wolves_encounter_running = True

    clock = pygame.time.Clock()
    pygame.init()

    pygame.mixer.set_num_channels(32)
    pygame.mixer.pre_init(44100,-16,2,512)
    #-----------------------------GameWindowSettings----------------------
    pygame.display.set_caption("Wolves")
    WINDOW_SIZE = (1280,720)
    screen = pygame.display.set_mode((1280,720),0,32)
    #display = pygame.Surface((600,400))


    monitor_size =[pygame.display.Info().current_w, pygame.display.Info().current_h]

    fullscreen = button.fullscreen
    #not bool(linecache.getline('genericmap.txt',1))
    if fullscreen:
        screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
    else:
        screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)


    #-----------------------------------Battlemap,Interface------------------------
    bg_backscreen = pygame.image.load("BattleScreen/background.png").convert_alpha()
    bg_backscreen = pygame.transform.scale(bg_backscreen, (int(WINDOW_SIZE[0]*1.00),(int(WINDOW_SIZE[1]*0.75))))

    # note_map = pygame.image.load("BattleScreen/note_Faroak0.png").convert_alpha()
    # note_map = pygame.transform.scale(note_map, (int(WINDOW_SIZE[0]*0.21),(int(WINDOW_SIZE[1]*0.28))))

    bg_map = pygame.image.load("BattleScreen/BattleMap0.png").convert_alpha()
    bg_map = pygame.transform.scale(bg_map, (int(WINDOW_SIZE[0]*0.70),(int(WINDOW_SIZE[1]*0.70))))

    panel = pygame.image.load("BattleScreen/gamepanel0.png").convert_alpha()
    panel = pygame.transform.scale(panel, (int(WINDOW_SIZE[0]*1.10),(int(WINDOW_SIZE[1]*1.40))))

    bag_of_coins = pygame.image.load("BattleScreen/bag.png").convert_alpha()
    bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    #-----------------------------------Icons-------------------------------------
    attack_icon = pygame.image.load("BattleScreen/icon_fight.png").convert_alpha()
    attack_icon = pygame.transform.scale(attack_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))

    normal_icon = pygame.image.load("BattleScreen/cursor_final.png").convert_alpha()
    normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))

    skip_turn_img = pygame.image.load("BattleScreen/resources/tent.png").convert_alpha()
    skip_turn_img = pygame.transform.scale(skip_turn_img, (int(WINDOW_SIZE[0]*0.06),(int(WINDOW_SIZE[1]*0.05))))

    #-----------------------------------Characters---------------------------------
    # militia_image = pygame.image.load("BattleScreen/militia/idle/idle_0.png").convert_alpha()
    # landsknecht_image = pygame.image.load("BattleScreen/landsknecht/idle/idle_0.png").convert_alpha()

    #------------------------------------------------------------------------------
    #--------------------------------Items----------------------------------------
    inventory_bag = pygame.image.load("BattleScreen/resources/inventorybag.png").convert_alpha()
    inventory_bag = pygame.transform.scale(inventory_bag, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    book_of_tricks = pygame.image.load("BattleScreen/resources/bookoftricks.png").convert_alpha()
    book_of_tricks = pygame.transform.scale(book_of_tricks, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    health_potion = pygame.image.load("BattleScreen/resources/health_potion.png").convert_alpha()
    health_potion = pygame.transform.scale(health_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    defence_potion = pygame.image.load("BattleScreen/resources/reflexes_potion.png").convert_alpha()
    defence_potion = pygame.transform.scale(defence_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    berserk_potion = pygame.image.load("BattleScreen/resources/berserk_potion.png").convert_alpha()
    berserk_potion = pygame.transform.scale(berserk_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    doors_icon = pygame.image.load("BattleScreen/resources/castledoors.png").convert_alpha()
    doors_icon = pygame.transform.scale(doors_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    retry_icon = pygame.image.load("BattleScreen/resources/try_again.png").convert_alpha()
    retry_icon = pygame.transform.scale(retry_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))

    victory_icon = pygame.image.load("BattleScreen/resources/victory.png").convert_alpha()
    victory_icon = pygame.transform.scale(victory_icon, (int(WINDOW_SIZE[0]*0.15),(int(WINDOW_SIZE[1]*0.15))))

    #------------------------------------------------------------------------------
    screen.fill((242,238,203))

    mouse_position = (0, 0)
    #----------------------------------Music----------------------------------------
    #open_inventory_bag = pygame.mixer.Sound('sounds/OpenInventory.mp3')
    def play_music(type):
        global play_music
        if type == 'Battle':
            pygame.mixer.music.load('BattleScreen/battlemusic.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        elif type == 'Map':
            pygame.mixer.music.load('WorldMap/WorldMapOst.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.02)
    play_music('Battle')

    #------------------------   -------------------------------------------------------
    attack_sound = pygame.mixer.Sound('BattleScreen/resources/attack_sound.wav')
    arrow_sound = pygame.mixer.Sound('BattleScreen/resources/arrow.wav')
    snarl_sound = pygame.mixer.Sound('BattleScreen/resources/snarl.wav')
    stone_sound = pygame.mixer.Sound('BattleScreen/resources/throwingstone.wav')
    flame_sound = pygame.mixer.Sound('BattleScreen/resources/flame.wav')
    #------------------------------------ActionOrder--------------------------------
    current_fighter = 1

    action_cooldown = 0
    action_waittime = 100
    draw_cursor = False
    battle_status = 0    #0 - nothing, 1 = lost, 2 = won

    # if battle_status ==0:
    #     play_music('Battle')
    # if battle_status ==2:
    # #     pygame.mixer.music.play(0)
    # #     play_music('BattleVictory')
    play_defeat_music = True
    play_victory_music = True
    # if battle_status ==1:
    #     play_music('BattleDefeat')

    #------------------------------------BattleInterface (line 315)-------------------
    engage = False
    clicked = False
    clicked2 = False
    skip_turn = False
    show_indicators = True

    use_health_potion = False
    health_potion_restores = 50

    use_defence_potion = False
    defence_potion_adds = 100

    use_berserk_potion = False
    berserk_potion_adds = 30

    #----------------------------------ShowStats------------------------------------
    font =pygame.font.SysFont('Times New Roman', 18)
    fontBag = pygame.font.Font('WorldMap/ESKARGOT.ttf', 38)
    fontDMG = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
    fontActive = pygame.font.Font('WorldMap/ESKARGOT.ttf', 80)
    fontBattle = pygame.font.SysFont('Times New Roman', 70)
    fontMenuLarge = pygame.font.Font('WorldMap/ESKARGOT.ttf', 48)
    #pygame.font.Font('WorldMap/ESKARGOT.ttf', 70)

    red = (230,16,35)
    ginger = (245,116,34)
    green = (0,255,0)
    paper =  (255,150,100)
    blue = (0,0,255)
    lightblue = (240,248,255)

    def draw_text(text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        screen.blit(img,(x,y))
    #--------------------------------------------------------------------------------

    def draw_bgBackscreen ():
        screen.blit(bg_backscreen,(0,0))

    # def draw_noteMap():
    #     screen.blit(note_map,(998,12))

    def draw_bg():
        screen.blit(bg_map,(210,40))

    def draw_bag():
        screen.blit(bag_of_coins,(0,0))
        draw_text(f'{button.wealth}', fontBag, (255,225,100), 120, 30)

    def mouse_map_position_align(x,y):
        pyautogui.moveTo(x,y)
    #------------------------------DrawingIndicators------------------------
    def draw_panel():
        screen.blit(panel,(-50,-35))
        # for count, i in enumerate(army_player):
        #       draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
        # for count, i in enumerate(army_hostiles):
        #     draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (100,0,0), ((panel.get_width())*0.58), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))

    def countX(lst, x):
        return lst.count(x)

    #----------------------------------HeroStats-----------------------------
    #----------------------------------Charaters------------------------------
    class Fighter():
        def __init__(self, x,y,id,max_hp,max_armor, strength,strength2 ,defence, threshold, reach, special, alive,max_supply,max_tricks,hostile, arcane_res, fire_res, energy_res, frost_res, poison_res, crit):
            self.id=id
            self.max_hp = max_hp
            self.hp = max_hp
            self.max_armor = max_armor
            self.armor = max_armor
            self.defence = defence
            self.start_defence = defence
            self.strength = strength
            self.start_strength = strength
            self.strength2 = strength2
            self.start_strength2  = strength2
            self.reach = reach
            self.special = special
            self.max_supply= max_supply
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
            self.frost_res= frost_res
            self.poison_res = poison_res
            self.max_tricks = max_tricks
            self.tricks = max_tricks
            self.crit = crit
            self.alive = True
            self.hostile = True
            self.animation_list = [] #list of lists (action/img)
            self.frame_index = 0
            self.action = 0 #0-idle / 1-attack / 2-hurt / 3-death  updates via self.animation_list = []
            self.update_time = pygame.time.get_ticks()  # how much time has passed

            #-----------------------------Animations--------------------------------------------
            #loading idle action images
            temp_list = []
            for i in range(2):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/idle/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
                temp_list.append(img) #appends temp list to store img
            self.animation_list.append(temp_list)

            #loading attack action images
            temp_list = []
            for i in range(3):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/attack/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
                temp_list.append(img) #appends temp list to store img
            self.animation_list.append(temp_list)

            temp_list = []
            for i in range(1):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/hurt/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
                temp_list.append(img) #appends temp list to store img
            self.animation_list.append(temp_list)

            temp_list = []
            for i in range(3):
                img = pygame.image.load(f'BattleScreen/units/{self.id}/dead/{i}.png')
                img = pygame.transform.flip(img, hostile, False)
                img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
                temp_list.append(img) #appends temp list to store img
            self.animation_list.append(temp_list)
            #-----------------------------------------------------------------------------------
            if self.id == 'rowan':
                temp_list = []
                for i in range(3):
                    img = pygame.image.load(f'BattleScreen/units/{self.id}/attack2/{i}.png')
                    img = pygame.transform.flip(img, hostile, False)
                    img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
                    temp_list.append(img) #appends temp list to store img
                self.animation_list.append(temp_list)
            #--------------------------------

            self.image = self.animation_list[self.action][self.frame_index]     # to control action/images
            # two lists (action/frames)
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

        #---------------------------------------------------------------------
        def update(self,animation_modifier): #animation
            animation_cooldown = 100
            if self.action == 0:
                animation_cooldown = 1000*animation_modifier
            if self.action == 1:
                animation_cooldown = 150*animation_modifier
            if self.action == 2:
                animation_cooldown = 300*animation_modifier
            if self.action == 3 :
                animation_cooldown = 250*animation_modifier
            if self.action == 4:
                animation_cooldown = 150*animation_modifier
            #animation_cooldown = cooldown
            self.image = self.animation_list[self.action][self.frame_index]  #adding action
            if pygame.time.get_ticks() - self.update_time > animation_cooldown: #if its more than 100 its time to update the animation stage
                self.update_time = pygame.time.get_ticks() #resets timer
                self.frame_index += 1
            # if animation run out, reset
            if self.frame_index >= len(self.animation_list[self.action]):  #adding action

                #after death unit should stay at the last frame of the dead animation sequence
                if self.action == 3:    #dead animation in the list.
                    self.frame_index = len(self.animation_list[self.action])-1  #final frame
                else:
                    self.idle() # sets to idle animation

        #-----------------------------------Idle----------------------------
        def idle(self):
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        #-----------------------------------Hurt----------------------------
        def hurt(self):
            self.action = 2
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        #-----------------------------------dead----------------------------
        def dead(self):
            self.action = 3
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        #-------------------------------------------------------------------
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
        #-----------------------------------Attack----------------------------
        def attack(self,target):
            rand = random.randint(-5,5)
            if random.randint(0,100) < self.crit:
                damage = self.strength*2 + rand - target.threshold
                if damage <=0:
                    damage =0
            else:
                damage = self.strength + rand - target.threshold
                if damage <=0:
                    damage =0
            if self.special == 1:
                #target.armor -= 0
                target.hp -= damage
            elif self.special != 1:
                target.armor -= int(damage*(target.defence/100))
                if target.armor > 0:
                    target.hp -= int(damage*(1 - target.defence/100))
                if target.armor <= 0:
                    target.hp -= int((damage*(1 - target.defence/100)-target.armor))
                    target.armor = 0
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
            #DamageText
            if self.special != 1:
                if target.armor > 1:
                    damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage*(1 - target.defence/100))), red)
                if target.armor <=1:
                    damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
                    #DamageText(target.rect.centerx,target.rect.y-35,str(int((damage*(1 - target.defence/100)))), red)
            else:
                damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)

            damage_text_group.add(damage_text)
            #---------------------------------AttackSounds---------------------------------------
            #attack sound # 0-standard blade; 1-arrow; 2-stone
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
            #------------------------------------------------------------------------------------

            #animations
            self.action = 1   # set action frames to as 1 as 1 = attack folder animation
            self.frame_index = 0 # frame 0 in the attack folder animation
            self.update_time = pygame.time.get_ticks()

        #-----------------------------------------------------------------------------------------
        def alternative_attack(self,target):
            rand = random.randint(-5,5)
            if random.randint(0,100) < self.crit:
                damage = self.strength2*2 + rand - target.threshold
                if damage <=0:
                    damage =0
            else:
                damage = self.strength2 + rand - target.threshold
                if damage <=0:
                    damage =0
            if self.special == 1:
                #target.armor -= 0
                target.hp -= damage
            elif self.special != 1:
                target.armor -= int(damage*(target.defence/100))
                if target.armor > 0:
                    target.hp -= int(damage*(1 - target.defence/100))
                if target.armor <= 0:
                    target.hp -= int((damage*(1 - target.defence/100)-target.armor))
                    target.armor = 0
            # runs hurn animation
            target.hurt()

            if target.hp < 1:
                target.hp = 0
                target.alive = False
                # runs death animation
                target.dead()

            if self.special != 1:
                if target.armor > 1:
                    damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage*(1 - target.defence/100))), red)
                if target.armor <=1:
                    damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
                    #DamageText(target.rect.centerx,target.rect.y-35,str(int((damage*(1 - target.defence/100)))), red)
            else:
                damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)

            damage_text_group.add(damage_text)
            #---------------------------------AttackSounds---------------------------------------
            #attack sound # 0-standard blade; 1-arrow; 2-stone
            if self.special == 0 and self.id == 'rowan':
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
            #------------------------------------------------------------------------------------

            #animations
            self.action = 4  # set action frames to as 1 as 1 = attack folder animation
            self.frame_index = 0 # frame 0 in the attack folder animation
            self.update_time = pygame.time.get_ticks()

            #----------------------------------------------------------------------
        def draw(self):
            screen.blit(self.image, self.rect)

    #-----------------------------------HealthBar--------------------------
    class healthBar ():
        def __init__(self, x,y, hp, max_hp):
            self.x = x
            self.y = y
            self.hp = hp
            self.max_hp = max_hp
        def draw (self, hp):
            self.hp = hp
            # health ration
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen,red,(self.x, self.y, 50,5))
            pygame.draw.rect(screen,green,(self.x, self.y, 50*ratio,5))

    #-----------------------------------ArmorBar--------------------------
    class armorBar ():
        def __init__(self, x,y, armor, max_armor):
            self.x = x
            self.y = y
            self.armor = armor
            self.max_armor = max_armor
        def draw (self, armor):
            self.armor = armor
            # health ration
            ratio = self.armor / self.max_armor
            pygame.draw.rect(screen,lightblue,(self.x, self.y, 50,5))
            pygame.draw.rect(screen,blue,(self.x, self.y, 50*ratio,5))

    #-----------------------------------AttributeChangeBar-----------------
    class DamageText(pygame.sprite.Sprite):   # sprite is updated automatically
        def __init__(self,x,y,damage, color):
            pygame.sprite.Sprite.__init__(self)
            self.image = fontDMG.render(damage, True, color)
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
            self.counter = 0

        def update(self):
            #move text
            self.rect.y -=1
            #delete after timer
            self.counter +=1
            if self.counter > 30:
                self.kill()

    damage_text_group = pygame.sprite.Group()    #python list
    #(self, x,y,id,max_hp,max_armor, strength,defence, threshold, reach, special,
    # max_supply,alive,hostile,max_tricks, arcane_res, fire_res, energy_res,
    # frost_res, poison_res, crit):
    #-----------------------------------PlayerArmy--------------------------
    # militia = Fighter (350,300, 'militia',60,30,35,30,5,1,0,1,True,False,1,12)
    # militia_healthbar = healthBar (militia.rect.centerx-25,militia.rect.centery-55,militia.hp, militia.max_hp)
    # militia_armorbar = armorBar (militia.rect.centerx-25,militia.rect.centery-50,militia.armor, militia.max_armor)
    # #-----------------------------------------------------------------------
    rowan = Fighter (540,210, 'rowan',button.health_points,button.armor_points,button.melee_damage,button.ranged_damage,button.defence,button.threshold,1,0,True,button.supply,button.tricks,False,button.arcana_res,button.fire_res,button.energy_res,button.frost_res,button.poison_res,button.critical_strike)
    rowan_healthbar = healthBar (rowan.rect.centerx-30,rowan.rect.centery-60,rowan.hp, rowan.max_hp)
    rowan_armorbar = armorBar (rowan.rect.centerx-30,rowan.rect.centery-55,rowan.armor, rowan.max_armor)
    # #-----------------------------------------------------------------------
    # landsknecht = Fighter (540,210,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
    # landsknecht_healthbar = healthBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-55,landsknecht.hp, landsknecht.max_hp)
    # landsknecht_armorbar = armorBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-50,landsknecht.armor, landsknecht.max_armor)
    # #-----------------------------------------------------------------------
    # landsknecht1 = Fighter (620,170,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
    # landsknecht1_healthbar = healthBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-55,landsknecht1.hp, landsknecht1.max_hp)
    # landsknecht1_armorbar = armorBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-50,landsknecht1.armor, landsknecht1.max_armor)
    # #-----------------------------------------------------------------------
    # chevalier = Fighter (720,100,'chevalier',120,100,65,70,1,0,1,True,False,0,0)
    # chevalier_healthbar = healthBar (chevalier.rect.centerx-25,chevalier.rect.centery-65,chevalier.hp, chevalier.max_hp)
    # chevalier_armorbar = armorBar (chevalier.rect.centerx-25,chevalier.rect.centery-60,chevalier.armor, chevalier.max_armor)
    # #-----------------------------------------------------------------------
    # militia1 = Fighter (440,350, 'militia',60,30,35,30,1,0,1,True,False,0,0)
    # militia1_healthbar = healthBar (militia1.rect.centerx-25,militia1.rect.centery-55,militia1.hp, militia1.max_hp)
    # militia1_armorbar = armorBar (militia1.rect.centerx-25,militia1.rect.centery-50,militia1.armor, militia1.max_armor)
    # #-----------------------------------------------------------------------
    # militia2 = Fighter (840,110, 'militia',60,30,35,30,1,0,1,True,False,0,0)
    # militia2_healthbar = healthBar (militia2.rect.centerx-25,militia2.rect.centery-55,militia2.hp, militia2.max_hp)
    # militia2_armorbar = armorBar (militia2.rect.centerx-25,militia2.rect.centery-50,militia2.armor, militia2.max_armor)
    # #-----------------------------------------------------------------------
    # militia3 = Fighter (930,110, 'militia',60,30,35,30,1,0,1,True,False,0,0)
    # militia3_healthbar = healthBar (militia3.rect.centerx-25,militia3.rect.centery-55,militia3.hp, militia3.max_hp)
    # militia3_armorbar = armorBar (militia3.rect.centerx-25,militia3.rect.centery-50,militia3.armor, militia3.max_armor)
    # #-----------------------------------------------------------------------
    # archer = Fighter (530,115, 'archer',65,30,40,32,2,1,1,True,False,0,0)
    # archer_healthbar = healthBar (archer.rect.centerx-25,archer.rect.top-20,archer.hp, archer.max_hp)
    # archer_armorbar = armorBar (archer.rect.centerx-25,archer.rect.top-15,archer.armor, archer.max_armor)
    # #-----------------------------------------------------------------------
    # archer1 = Fighter (440,160, 'archer',65,30,40,32,2,1,1,True,False,0,0)
    # archer1_healthbar = healthBar (archer1.rect.centerx-25,archer1.rect.top-20,archer1.hp, archer.max_hp)
    # archer1_armorbar = armorBar (archer1.rect.centerx-25,archer1.rect.top-15,archer1.armor, archer.max_armor)
    # #-----------------------------------------------------------------------

    # +125 HealthBar / -45  amd +5 Armor
    #x: +90-100; y: -45
    #-----------------------------------------------------------------------
    army_player = []
    army_player.append(rowan)

    army_player_front = [ally for ally in army_player if ally.reach == 1]
    #army_player[:7]

    #(self, x,y,id,max_hp,max_armor, strength,strength2 ,defence, threshold, reach, special,
    # alive,max_supply,max_tricks,hostile, arcane_res, fire_res, energy_res,
    # frost_res, poison_res, crit):
    # #-----------------------------------------------------------------------
    # h_brigand = Fighter(660,325,'brigand',50,25,30,0,30,3,1,0,1,True,True,1,0,0,0,0,0,0)
    # h_brigand_healthbar = healthBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-55,h_brigand.hp, h_brigand.max_hp)
    # h_brigand_armorbar = armorBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-50,h_brigand.armor, h_brigand.max_armor)
    #-----------------------------------------------------------------------
    h_wolf = Fighter(570,370,'wolf',40,1,25,0,0,0,1,3,True,0,0,True,0,8,0,8,8,3)
    h_wolf_healthbar = healthBar(h_wolf.rect.centerx-25,h_wolf.rect.centery-55,h_wolf.hp, h_wolf.max_hp)
    h_wolf_armorbar = armorBar(h_wolf.rect.centerx-25,h_wolf.rect.centery-50,h_wolf.armor, h_wolf.max_armor)
    #-----------------------------------------------------------------------
    h_blackwolf = Fighter(840,245,'blackwolf',60,1,30,0,0,4,1,3,True,0,0,True,0,12,0,12,12,7)
    h_blackwolf_healthbar = healthBar(h_blackwolf.rect.centerx-25,h_blackwolf.rect.centery-55,h_blackwolf.hp, h_blackwolf.max_hp)
    h_blackwolf_armorbar = armorBar(h_blackwolf.rect.centerx-25,h_blackwolf.rect.centery-50,h_blackwolf.armor, h_blackwolf.max_armor)
    #-----------------------------------------------------------------------
    #-----------------------------HostileArmy-------------------------------
    # h_dragohare = Fighter (760,230,'dragohare',400,300,85,40,3,4,0,True,True,0,0)
    # h_dragohare_healthbar = healthBar (h_dragohare.rect.centerx+90,h_dragohare.rect.centery+70,h_dragohare.hp, h_dragohare.max_hp)
    # h_dragohare_armorbar = armorBar (h_dragohare.rect.centerx+90,h_dragohare.rect.centery+75,h_dragohare.armor, h_dragohare.max_armor)
    # #-----------------------------HostileArmy-------------------------------
    # h_caerbannog = Fighter (850,280,'caerbannog',750,400,85,60,3,4,0,True,True,0,0)
    # h_caerbannog_healthbar = healthBar (h_caerbannog.rect.centerx+20,h_caerbannog.rect.centery-105,h_caerbannog.hp, h_caerbannog.max_hp)
    # h_caerbannog_armorbar = armorBar (h_caerbannog.rect.centerx+20,h_caerbannog.rect.centery-100,h_caerbannog.armor, h_caerbannog.max_armor)

    # h_militia = Fighter(570,365,'militia',60,30,35,30,1,0,1,True,True,0,0)
    # h_militia_healthbar = healthBar(h_militia.rect.centerx-25,h_militia.rect.centery-55,h_militia.hp, h_militia.max_hp)
    # h_militia_armorbar = armorBar(h_militia.rect.centerx-25,h_militia.rect.centery-50,h_militia.armor, h_militia.max_armor)
    # #-----------------------------------------------------------------------
    # h_landsknecht2 = Fighter (570,365,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
    # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
    # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
    # # #-----------------------------------------------------------------------
    # # h_brigand1 = Fighter(660,325,'brigand',50,25,30,30,1,0,1,True,True,0,0)
    # # h_brigand1_healthbar = healthBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-55,h_brigand1.hp, h_brigand1.max_hp)
    # # h_brigand1_armorbar = armorBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-50,h_brigand1.armor, h_brigand1.max_armor)
    # # # # #-----------------------------------------------------------------------
    # h_landsknecht3 = Fighter (660,325,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
    # h_landsknecht3_healthbar = healthBar (h_landsknecht3.rect.centerx-25,h_landsknecht3.rect.centery-55,h_landsknecht3.hp, h_landsknecht3.max_hp)
    # h_landsknecht3_armorbar = armorBar (h_landsknecht3.rect.centerx-25,h_landsknecht3.rect.centery-50,h_landsknecht3.armor, h_landsknecht3.max_armor)
    # #-----------------------------------------------------------------------
    # h_landsknecht = Fighter (750,280,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
    # h_landsknecht_healthbar = healthBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-55,h_landsknecht.hp, h_landsknecht.max_hp)
    # h_landsknecht_armorbar = armorBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-50,h_landsknecht.armor, h_landsknecht.max_armor)
    # #-----------------------------------------------------------------------
    # h_landsknecht1 = Fighter (840,235,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
    # h_landsknecht1_healthbar = healthBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-55,h_landsknecht1.hp, h_landsknecht1.max_hp)
    # h_landsknecht1_armorbar = armorBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-50,h_landsknecht1.armor, h_landsknecht1.max_armor)
    # #-----------------------------------------------------------------------
    # #-----------------------------------------------------------------------
    # # h_brigand2 = Fighter(940,195,'brigand',50,25,30,30,1,0,1,True,True,0,0)
    # # h_brigand2_healthbar = healthBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-55,h_brigand2.hp, h_brigand2.max_hp)
    # # h_brigand2_armorbar = armorBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-50,h_brigand2.armor, h_brigand2.max_armor)
    # h_chevalier = Fighter (930,150,'chevalier',120,100,60,65,1,0,1,True,True,0,0)
    # h_chevalier_healthbar = healthBar (h_chevalier.rect.centerx-25,h_chevalier.rect.centery-65,h_chevalier.hp, h_chevalier.max_hp)
    # h_chevalier_armorbar = armorBar (h_chevalier.rect.centerx-25,h_chevalier.rect.centery-60,h_chevalier.armor, h_chevalier.max_armor)
    # #-----------------------------------------------------------------------
    # # h_landsknecht2 = Fighter (790,340,'landsknecht',90,55,40,50,2,0,1,True,True,0,0)
    # # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
    # # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
    # #-----------------------------------------------------------------------
    # h_bowman = Fighter (790,350, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
    # h_bowman_healthbar = healthBar (h_bowman.rect.centerx-25,h_bowman.rect.top-20,h_bowman.hp, h_bowman.max_hp)
    # h_bowman_armorbar = armorBar (h_bowman.rect.centerx-25,h_bowman.rect.top-15,h_bowman.armor, h_bowman.max_armor)
    # #-----------------------------------------------------------------------
    # h_bowman1 = Fighter (695,400, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
    # h_bowman1_healthbar = healthBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-20,h_bowman1.hp, h_bowman1.max_hp)
    # h_bowman1_armorbar = armorBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-15,h_bowman1.armor, h_bowman1.max_armor)
    # #-----------------------------------------------------------------------
    # h_bowman2 = Fighter (880,310, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
    # h_bowman2_healthbar = healthBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-20,h_bowman2.hp, h_bowman2.max_hp)
    # h_bowman2_armorbar = armorBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-15,h_bowman2.armor, h_bowman2.max_armor)
    # #-----------------------------------------------------------------------
    # h_bowman3 = Fighter (960,260, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
    # h_bowman3_healthbar = healthBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-20,h_bowman3.hp, h_bowman3.max_hp)
    # h_bowman3_armorbar = armorBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-15,h_bowman3.armor, h_bowman3.max_armor)

    # +125 HealthBar / -45  amd +5 Armor
    #x: +90-100; y: -45
    #-----------------------------------------------------------------------
    army_hostiles = []
    army_hostiles.append(h_wolf)
    army_hostiles.append(h_blackwolf)

    army_hostiles_front = [enemy for enemy in army_hostiles if enemy.reach == 1]
    #army_hostiles

    enemy_reserves = True
    army_hostiles_reserves = []
    #army_hostiles_reserves.append(h_caerbannog)

    #------------------------------TotalUnitNumber----------------------------
    total_hostiles = len(army_hostiles)
    total_allies = len(army_player)
    total_fighters = total_hostiles + total_allies

    #------------------------------ItemsUse(Button)---------------------------
    #inventory_button = button.Button(screen,WINDOW_SIZE[0]*0 + 110, WINDOW_SIZE[1]*0 - 6,inventory_bag,280,120,0, True, 'Inventory')
    book_button = button.ToggleButton(screen,120, 450,book_of_tricks,110,80,0, True, 'Book of Tricks')
    inventory_button = button.ToggleButton(screen,20, 445,inventory_bag,90,80,0, True, 'Inventory')
    #------------------------------ItemsUse(PotionButton)-------------------
    potion_button = button.Button(screen, WINDOW_SIZE[0]*0.01, WINDOW_SIZE[1]*0.90, health_potion, 48,72,30, False,f'Health Potion. Restores {health_potion_restores} HP')
    potion_button1 = button.Button(screen, WINDOW_SIZE[0]*0.06, WINDOW_SIZE[1]*0.90, defence_potion, 48,72,40, False,f'Defence Potion. Gives {defence_potion_adds} DEF/ARM')
    potion_button2 = button.Button(screen, WINDOW_SIZE[0]*0.11, WINDOW_SIZE[1]*0.90, berserk_potion, 48,72,60, False,f'Berserk Potion. Gives {berserk_potion_adds} ATK / Removes {int(berserk_potion_adds*0.75)} DEF')

    #------------------------------IconToggle(Reset)------------------------
    restart_button = button.Button(screen, 1100, 8, retry_icon, 84,90,25, False,'Try Again')
    skip_turn_button = button.Button(screen, WINDOW_SIZE[0]*0.92, WINDOW_SIZE[1]*0.61, skip_turn_img, 86,82,60, False,f'Skip Turn')
    victory_button = button.Button(screen, 1170, 15, victory_icon, 86,90,25, True,'Back to Map')
    leave_button = button.Button(screen, 1190, 15, doors_icon, 64,80,25, True,'Leave Battlefield')

    #-----------------------------------------------------------------------

    while wolves_encounter_running:
        #display.fill((146,244,255))
        draw_bgBackscreen()
        #draw_noteMap()  # location map
        draw_bg()
        draw_panel()
        draw_bag()

        #-----------------------------DrawingUnits/AnimatioSpeedMod------------
        for units in army_player:
            rowan.update(0.8)
            rowan.draw()
            #------------

        #----------------------------EnemyUnitsDraw---------------------------
        for hostile in army_hostiles:
            # h_brigand.update(0.8)
            # h_brigand.draw()
            #------------
            h_wolf.update(0.8)
            h_wolf.draw()
            #------------
            h_blackwolf.update(0.8)
            h_blackwolf.draw()
            #------------

        #-----------------------------HealthBar/ArmorBar-----------------------
        if show_indicators == True:
            #-------------Player------------------------
            if rowan.alive == True:
                rowan_healthbar.draw(rowan.hp)
                rowan_armorbar.draw(rowan.armor)

            #------------------Enemy--------------------
            # if h_brigand.alive == True:
            #     h_brigand_healthbar.draw(h_brigand.hp)
            #     h_brigand_armorbar.draw(h_brigand.armor)
            if h_wolf.alive == True:
                h_wolf_healthbar.draw(h_wolf.hp)
                h_wolf_armorbar.draw(h_wolf.armor)
            if h_blackwolf.alive == True:
                h_blackwolf_healthbar.draw(h_blackwolf.hp)
                h_blackwolf_armorbar.draw(h_blackwolf.armor)

        #------------------------------------EnemyReserves-------------------------------------
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

        #-----------------------------DamageText-----------------------------
        damage_text_group.update()
        damage_text_group.draw(screen)
        #methods update and draw are parts of the sprite.

        #-----------------------------Items/SkipTurn/-----------------------------------
        pos = pygame.mouse.get_pos()
        if skip_turn_button.rect.collidepoint(pos):
            draw_text(f'{skip_turn_button.description}', fontDMG, green, skip_turn_button.rect.x-30,skip_turn_button.rect.y+100)
        if skip_turn_button.draw():
            skip_turn=True
        #------------------------------------LeaveButton-------------------------------
        if battle_status != 2 and leave_button.available == True:
            if leave_button.rect.collidepoint(pos):
                draw_text(f'{leave_button.description}', fontDMG, green, leave_button.rect.x-140,leave_button.rect.y+100)
            if leave_button.draw():
                play_music('Map')
                button.wealth = button.start_wealth
                wolves_encounter_running = False
        #--------------------------------------------------------------------------------
        if book_button.rect.collidepoint(pos):
            draw_text(f'{book_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)

        #---------------------------------Inventory--------------------------------
        if inventory_button.rect.collidepoint(pos):
            draw_text(f'{inventory_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
        if inventory_button.toggled == True and battle_status ==0:
            potion_button.available = True
            potion_button1.available = True
            potion_button2.available = True

            #---------------------HealthPotion--------------------------------------
            if potion_button.available == True:
                if potion_button.draw():
                    use_health_potion = True
                draw_text(f'{potion_button.price}', fontBag, (255,225,100), potion_button.rect.x+5, potion_button.rect.y-60)
                pos = pygame.mouse.get_pos()
                if potion_button.rect.collidepoint(pos):
                    draw_text(f'{potion_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)

            #-------DefencePotion--------------
            if potion_button1.available == True:
                if potion_button1.draw():
                    use_defence_potion = True
                draw_text(f'{potion_button1.price}', fontBag, (255,225,100), potion_button.rect.x+65, potion_button.rect.y-60)
                pos = pygame.mouse.get_pos()
                if potion_button1.rect.collidepoint(pos):
                    draw_text(f'{potion_button1.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)

                #-------BerserkPotion--------------
            if potion_button2.available == True:
                if potion_button2.draw():
                    use_berserk_potion = True
                draw_text(f'{potion_button2.price}', fontBag, (255,225,100), potion_button.rect.x+130, potion_button.rect.y-60)
                pos = pygame.mouse.get_pos()
                if potion_button2.rect.collidepoint(pos):
                    draw_text(f'{potion_button2.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)

        #---------------------InventoryStock--------------------------------------
        else:
            potion_button.available = False

        #--------------------------------------------------------------------------
        if battle_status ==0:   #win/loose check

            #-----------------------------PlayerAttacking---------------------------
            for count, ally in enumerate(army_player):
                if current_fighter == 1+count:
                    draw_text('^', fontActive, "#FFA500", ally.rect.centerx-20,ally.rect.y -65)
                    if ally.alive == True:
                        action_cooldown +=1
                        if action_cooldown >= action_waittime:

                            if ally.reach == 2:
                                if engage == True and target != None:
                                    # conditioned upon engage below & def attack above
                                    ally.attack(target)
                                    current_fighter += 1
                                    action_cooldown = 0

                            elif ally.reach == 1:
                                if engage == True and target != None and target.reach != 2:
                                    ally.attack(target)
                                    current_fighter += 1
                                    action_cooldown = 0

                            for enemy in army_hostiles_front:
                                if all(enemy.alive == False for enemy in army_hostiles_front):
                                    #enemy.alive == False:
                                    if ally.reach == 1:
                                        if engage == True and target != None and target.reach == 2:
                                            ally.reach = 2
                                            ally.attack(target)
                                            current_fighter += 1
                                            action_cooldown = 0

                            if ally.id == 'rowan':
                                if engage2 == True and target != None:
                                    # conditioned upon engage below & def attack above
                                    ally.alternative_attack(target)
                                    current_fighter += 1
                                    action_cooldown = 0
                            #-----------------------------------------SkipTurn-----------------------------------------
                            if skip_turn == True:
                                current_fighter += 1
                                action_cooldown = 0
                                skip_turn_heal = 10
                                if ally.max_hp - ally.hp > skip_turn_heal:    #50
                                    skip_turn_heal = skip_turn_heal
                                else:
                                    skip_turn_heal = ally.max_hp - ally.hp
                                ally.hp += skip_turn_heal
                                #DamageText
                                damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(skip_turn_heal), green)
                                damage_text_group.add(damage_text)
                            skip_turn = False

                            #------------UsingItem(HealthPotion)---------------------------
                            if use_health_potion == True and button.wealth >= potion_button.price:
                                if ally.supply > 0:
                                    # not healing beyond max_hp
                                    if ally.max_hp - ally.hp > health_potion_restores:    #50
                                        heal_amount = health_potion_restores
                                    else:
                                        heal_amount = ally.max_hp - ally.hp
                                    ally.hp += heal_amount
                                    ally.supply -= 1
                                    button.wealth -= potion_button.price
                                    #DamageText
                                    damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(heal_amount), green)
                                    damage_text_group.add(damage_text)

                                    current_fighter +=1
                                    action_cooldown = 0
                                use_health_potion = False

                            #----------------------------------------------------
                            #------------UsingItem(DefencePotion)---------------
                            if use_defence_potion == True and button.wealth >= potion_button1.price:
                                if ally.supply > 0:
                                    # not healing beyond max_hp
                                    if ally.max_armor - ally.armor > defence_potion_adds:    #50
                                        add_defence_amount = defence_potion_adds
                                    else:
                                        add_defence_amount = ally.max_armor - ally.armor
                                    ally.armor += add_defence_amount
                                    ally.defence = 100
                                    ally.supply -= 1
                                    button.wealth -= potion_button1.price     #Change price

                                    current_fighter +=1
                                    action_cooldown = 0
                                use_defence_potion = False


                            #------------UsingItem(BerserkPotion)---------------
                            if use_berserk_potion == True and button.wealth >= potion_button2.price:
                                if ally.supply > 0:
                                    ally.strength += berserk_potion_adds
                                    if ally.defence < int(berserk_potion_adds):
                                        ally.defence = 0
                                    else:
                                        ally.defence -= int(berserk_potion_adds)
                                    ally.supply -= 1
                                    button.wealth -= potion_button2.price

                                    current_fighter +=1
                                    action_cooldown = 0
                                    #Change price
                                use_berserk_potion = False

                    else:
                        current_fighter +=1   #if dead = skip turn

            #-----------------------------EnemyAttacking----------------------------
            for count, enemy in enumerate(army_hostiles ):
                if current_fighter == 1+ total_allies + count:   # "3 + count" - checks with the max_fighter var and number of units in army_player
                    draw_text('^', fontActive, "#FFA500", enemy.rect.centerx-20,enemy.rect.y -65)
                    if enemy.alive == True:
                        action_cooldown +=1
                        if action_cooldown >= action_waittime:
                            #------------------------------EnemyDefencePotion------------------
                            if (enemy.armor / enemy.max_armor) <0.2 and enemy.armor < defence_potion_adds and enemy.max_armor > health_potion_restores and enemy.supply >0:
                                if enemy.max_armor - enemy.armor > defence_potion_adds:
                                    add_defence_amount = defence_potion_adds
                                else:
                                    add_defence_amount = enemy.max_armor - enemy.armor
                                enemy.armor += add_defence_amount
                                enemy.defence = 100
                                enemy.supply -= 1
                                current_fighter +=1
                                action_cooldown = 0

                            #------------------------------EnemyHealthPotion------------------
                            elif (enemy.hp / enemy.max_hp) <0.5 and enemy.supply >0:
                                if enemy.max_hp - enemy.hp > health_potion_restores:
                                    heal_amount = health_potion_restores
                                else:
                                    heal_amount = enemy.max_hp - enemy.hp

                                enemy.hp += heal_amount
                                enemy.supply -= 1

                                #DamageText
                                damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(heal_amount), green)
                                damage_text_group.add(damage_text)

                                current_fighter +=1
                                action_cooldown = 0

                            #-------------------------------------------------------------------
                            elif enemy.reach == 2:
                                if enemy.strength >= ally.hp and ally.alive == True:
                                    enemy.attack(ally)
                                    current_fighter += 1
                                    action_cooldown = 0
                                else:
                                    enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
                                    current_fighter += 1
                                    action_cooldown = 0

                            elif enemy.reach == 1:
                                if all(ally.alive == True for ally in army_player_front):
                                    enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
                                    current_fighter += 1
                                    action_cooldown = 0
                                elif all(ally.alive == False for ally in army_player_front):
                                    enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 2]))
                                    current_fighter += 1
                                    action_cooldown = 0
                                else:
                                    enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
                                    current_fighter += 1
                                    action_cooldown = 0

                            # elif enemy.reach == 3 and enemy.id == 'dragohare':
                            #     alive_targets = sum(ally.alive == True for ally in army_player)
                            #     if alive_targets >= 6:
                            #         for i in range(6):
                            #             enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
                            #     elif alive_targets < 6:
                            #         for j in range (alive_targets):
                            #             enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
                            #     enemy.armor = enemy.max_armor
                            #     current_fighter += 1
                            #     action_cooldown = 0

                            else:
                                current_fighter +=1

                    #     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
                    #     # enemy.hp += 10
                    #     current_fighter += 1
                    #     action_cooldown = 0
                    #     # damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(10), green)
                    #     # damage_text_group.add(damage_text)

                    else:
                        current_fighter +=1

            #---------------------------------Turns----------------------------
            # if all have had a turn, reset
            if current_fighter > total_fighters:
                current_fighter = 1

        #-----------------------------DefeatStatus-------------------------
        # checking alive/dead status
        alive_allies = 0
        for ally in army_player:
            if ally.alive == True:
                alive_allies +=1
        if alive_allies ==0:
            battle_status =1

        #---------------------------------VictoryStatus--------------------
        alive_enemies = 0
        for enemy in army_hostiles:
            if enemy.alive == True:
                alive_enemies +=1
        if alive_enemies ==0 and all(enemy.alive == False for enemy in army_hostiles_reserves):
            battle_status =2

        #-------------------Defeat/VictoryStatusDisplay-------------------
        if battle_status !=0:
            if battle_status ==1:
                draw_text(f'Defeat!', fontMenuLarge, (155,0,0), screen.get_width()*0.46,0)
                if play_defeat_music == True:
                   play_music('BattleDefeat')
                play_defeat_music = False
                #-------------------ResetButton-----------------------------------
                if restart_button.available == True:
                    if restart_button.draw():
                        play_music('Battle')
                        for ally in army_player:
                            ally.reset()
                        for enemy in army_hostiles:
                            enemy.reset()


                        button.wealth = button.start_wealth         #restart gold here
                        current_fighter = 1
                        action_cooldown = 0
                        battle_status = 0

                        pos = pygame.mouse.get_pos() # text over the button
                    if restart_button.rect.collidepoint(pos):
                        draw_text(f'{restart_button.description}', fontDMG, green, restart_button.rect.x+30,leave_button.rect.y+100)

            #-------------------Defeat/VictoryStatusDisplay-------------------
            if battle_status ==2:
                button.quest_old_ways= 'locked'
                draw_text(f'Victory!', fontMenuLarge, green, screen.get_width()*0.46,0)
                if play_victory_music == True:
                   play_music('BattleVictory')
                play_victory_music = False
                if victory_button.available == True:
                    if victory_button.draw():
                        button.wealth += 100
                        button.start_wealth = button.wealth
                        #button.quest_finale= 'unlocked'
                        print(button.start_wealth)
                        print(button.wealth)
                        pyautogui.moveTo(750, 400)
                        play_music('Map')
                        wolves_encounter_running = False
                    if victory_button.rect.collidepoint(pos):
                        draw_text(f'{victory_button.description}', fontDMG, green, victory_button.rect.x-75,leave_button.rect.y+100)
        #------------------------------End/Controls------------------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w,event.h),0,32)

            if event.type == KEYDOWN:
                if event.key == K_f and show_indicators == True:
                    show_indicators = False
                elif event.key == K_f and show_indicators == False:
                    show_indicators = True

                if event.key == K_o:
                    # fullscreen = not fullscreen
                    # with open('genericmap.txt', 'w') as file:
                    #     file.write(str(fullscreen))
                    button.fullscreen = not button.fullscreen
                    # with open('genericmap.txt', 'w') as file:
                    #     file.write(str(fullscreen))
                    fullscreen = button.fullscreen

                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)

            #---------------------ToggleButton------------------------
            inventory_button.event_handler(event) #ToggleButton
            #---------------------ToggleButton------------------------

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                elif event.button == 3:
                    clicked2 = True
            else:
                clicked = False
                clicked2 = False

        if leave_button.clicked == True or victory_button.clicked == True:
            mouse_map_position_align(750,400)
        #-----------------------------Action/TargetSearch-------------------
        engage = False
        engage2 = False
        target = None

        inventory_button.draw(screen) #ToggleButton
        book_button.draw(screen) #ToggleButton

        pygame.mouse.set_visible(False)
        pos = pygame.mouse.get_pos()
        screen.blit(normal_icon,pos)

        for count, ally in enumerate(army_player):
            if ally.rect.collidepoint(pos) and ally.alive == True:
                draw_text(f'{ally.id} | HP: {ally.hp} | ARM: {ally.armor} | ATK: {ally.strength} | RNG: {ally.strength2} | DEF: {ally.defence} | SPL: {ally.supply} | TRK: {ally.tricks}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
                draw_text(f'CRT:{ally.crit} | THR:{ally.threshold} | ARC: {ally.arcane_res} | FRE: {ally.fire_res} | ERE: {ally.energy_res} | FRO: {ally.frost_res} | PRE: {ally.poison_res}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.16)))
        for count, enemy in enumerate(army_hostiles):
            if enemy.rect.collidepoint(pos) and enemy.alive == True:
                pygame.mouse.set_visible(False)
                screen.blit(attack_icon,pos)
                draw_text(f'{enemy.id} | HP: {enemy.hp} | ARM: {enemy.armor} | ATK: {enemy.strength} | RNG: {enemy.strength2} | DEF: {enemy.defence} | SPL: {enemy.supply} | TRK: {enemy.tricks}', font, (100,0,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
                draw_text(f'CRT:{enemy.crit} | THR:{enemy.threshold} | ARC: {enemy.arcane_res} | FRE: {enemy.fire_res} | ERE: {enemy.energy_res} | FRO: {enemy.frost_res} | PRE: {enemy.poison_res}', font, (100,0,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.16)))
                # show attack icon
                #--------------chooseTarget&Attack-------------------------
                if clicked == True and enemy.alive == True:
                    engage = True
                    target = army_hostiles[count]
                if clicked2 == True and enemy.alive == True:
                    engage2 = True
                    target = army_hostiles[count]

        #-----------------------------------------------------------------------
        #surf = pygame.transform.scale(display, WINDOW_SIZE)
        #screen.blit(surf, (0,0))

        pygame.display.update()
        clock.tick(60)










































































































