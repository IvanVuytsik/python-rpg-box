
# dragonhunt_path = open('WorldMap/quest/dragonhunt.txt','r')
# dragonhunt_lore = dragonhunt_path.read()
# dragonhunt_path.close()

# dire_wolves_path = open('WorldMap/quest/dire_wolves.txt','r')
# dire_wolves_lore = dire_wolves_path.read()
# dire_wolves_path.close()
#
# highwaymen_path = open('WorldMap/quest/highwaymen.txt','r')
# highwaymen_lore = highwaymen_path.read()
# highwaymen_path.close()
#
# finale_path = open('WorldMap/quest/finale.txt','r')
# finale_lore = finale_path.read()
# finale_path.close()


# button.quest_dire_wolves = 'invisible'
# button.quest_highwaymen = 'invisible'
# button.quest_dragonhunt = 'invisible'
# button.quest_finale = 'invisible'


# dire_wolves = Quest (720-scroll[0],100-scroll[1], gm_quest_icon, gm_dire_wolves,'Dire Wolves', f'{button.quest_dire_wolves}')
# highwaymen = Quest (755-scroll[0],110-scroll[1], gm_quest_icon, gm_highwaymen,'Highwaymen', f'{button.quest_highwaymen}')
# dragonhunt = Quest (730-scroll[0],190-scroll[1], gm_quest_icon, gm_dragonhunt,'Dragonhunt', f'{button.quest_dragonhunt}')
# finale = Quest (710-scroll[0],140-scroll[1], gm_victory_icon, gm_finale,'', f'{button.quest_finale}')


#quest_box.extend((dire_wolves,highwaymen,dragonhunt, finale))


# dire_wolves.hide_quest()
# highwaymen.hide_quest()
# dragonhunt.hide_quest()
# finale.hide_quest()


# #-------------------------DireWolves-------------------------
#         if dire_wolves.status == 'unlocked':
#             quest_group.add(dire_wolves)
#             if dire_wolves.initiate():
#                 pygame.mixer.music.fadeout(1500)
#                 dire_wolves_battle()             #battle file load here
#
#             dire_wolves.draw_story(dire_wolves_lore, 110, 152)
#
#             if dire_wolves.rect.collidepoint(mouse_position):
#                 if playSoundScroll == True :
#                     scroll_sound.play()
#                     playSoundScroll = False
#                 elif playSoundScroll_counter == 10:
#                     playSoundScroll_counter = 0
#
#         elif dire_wolves.status == 'locked':
#             dire_wolves.quest_unavailable()
#
# #-------------------------Highwaymen-------------------------
#         if highwaymen.status == 'unlocked':
#             quest_group.add(highwaymen)
#             if highwaymen.initiate():
#                 pygame.mixer.music.fadeout(1500)
#                 highwaymen_battle()             #battle file load here
#
#             highwaymen.draw_story(highwaymen_lore,110,165)
#
#             if highwaymen.rect.collidepoint(mouse_position):
#                 if playSoundScroll == True :
#                     scroll_sound.play()
#                     playSoundScroll = False
#                 elif playSoundScroll_counter == 10:
#                     playSoundScroll_counter = 0
#
#         elif highwaymen.status == 'locked':
#             highwaymen.quest_unavailable()
#
#
# #-------------------------Dragonhunt-------------------------
#         if dragonhunt.status == 'unlocked':
#             quest_group.add(dragonhunt)
#             if dragonhunt.initiate():
#                 pygame.mixer.music.fadeout(1500)
#                 dragonhunt_battle()             #battle file load here
#
#             dragonhunt.draw_story(dragonhunt_lore,110,133)
#
#             if dragonhunt.rect.collidepoint(mouse_position):
#                 if playSoundScroll == True :
#                     scroll_sound.play()
#                     playSoundScroll = False
#                 elif playSoundScroll_counter == 10:
#                     playSoundScroll_counter = 0
#
#         elif dragonhunt.status == 'locked':
#             dragonhunt.quest_unavailable()
#
#         #-------------------------Finale-------------------------
#         if finale.status == 'unlocked':
#             quest_group.add(finale)
#             if finale.initiate():
#                 pygame.mixer.music.fadeout(1500)
#                 restart_game()
#                 global_map_running = False
#
#             finale.draw_story(finale_lore,110,0)
#
#             if finale.rect.collidepoint(mouse_position):
#                 if playSoundScroll == True :
#                     scroll_sound.play()
#                     playSoundScroll = False
#                 elif playSoundScroll_counter == 10:
#                     playSoundScroll_counter = 0
#
#         elif finale.status == 'locked':
#             finale.quest_unavailable()




#
#
# def new_beginnings_battle ():
#     new_beginnings_battle_running = True
#
#     clock = pygame.time.Clock()
#     pygame.init()
#
#     pygame.mixer.set_num_channels(32)
#     pygame.mixer.pre_init(44100,-16,2,512)
#     #-----------------------------GameWindowSettings----------------------
#     pygame.display.set_caption("New Beginnings")
#     WINDOW_SIZE = (1280,720)
#     screen = pygame.display.set_mode((1280,720),0,32)
#     #display = pygame.Surface((600,400))
#
#
#     monitor_size =[pygame.display.Info().current_w, pygame.display.Info().current_h]
#
#     fullscreen = button.fullscreen
#     #not bool(linecache.getline('genericmap.txt',1))
#     if fullscreen:
#         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#     else:
#         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#
#     #-----------------------------------Battlemap,Interface------------------------
#     bg_backscreen = pygame.image.load("BattleScreen/background.png").convert_alpha()
#     bg_backscreen = pygame.transform.scale(bg_backscreen, (int(WINDOW_SIZE[0]*1.00),(int(WINDOW_SIZE[1]*0.75))))
#
#     note_map = pygame.image.load("BattleScreen/note_Faroak0.png").convert_alpha()
#     note_map = pygame.transform.scale(note_map, (int(WINDOW_SIZE[0]*0.21),(int(WINDOW_SIZE[1]*0.28))))
#
#     bg_map = pygame.image.load("BattleScreen/BattleMap0.png").convert_alpha()
#     bg_map = pygame.transform.scale(bg_map, (int(WINDOW_SIZE[0]*0.70),(int(WINDOW_SIZE[1]*0.70))))
#
#     panel = pygame.image.load("BattleScreen/gamepanel0.png").convert_alpha()
#     panel = pygame.transform.scale(panel, (int(WINDOW_SIZE[0]*1.10),(int(WINDOW_SIZE[1]*1.40))))
#
#     bag_of_coins = pygame.image.load("BattleScreen/bag.png").convert_alpha()
#     bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     #-----------------------------------Icons-------------------------------------
#     attack_icon = pygame.image.load("BattleScreen/icon_fight.png").convert_alpha()
#     attack_icon = pygame.transform.scale(attack_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#     normal_icon = pygame.image.load("BattleScreen/cursor_final.png").convert_alpha()
#     normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#
#     skip_turn_img = pygame.image.load("BattleScreen/skip_turn.png").convert_alpha()
#     skip_turn_img = pygame.transform.scale(skip_turn_img, (int(WINDOW_SIZE[0]*0.06),(int(WINDOW_SIZE[1]*0.05))))
#
#     #-----------------------------------Characters---------------------------------
#     # militia_image = pygame.image.load("BattleScreen/militia/idle/idle_0.png").convert_alpha()
#     # landsknecht_image = pygame.image.load("BattleScreen/landsknecht/idle/idle_0.png").convert_alpha()
#
#     #------------------------------------------------------------------------------
#     #--------------------------------Items----------------------------------------
#     inventory_bag = pygame.image.load("BattleScreen/resources/inventorybag.png").convert_alpha()
#     inventory_bag = pygame.transform.scale(inventory_bag, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     health_potion = pygame.image.load("BattleScreen/resources/health_potion.png").convert_alpha()
#     health_potion = pygame.transform.scale(health_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     defence_potion = pygame.image.load("BattleScreen/resources/reflexes_potion.png").convert_alpha()
#     defence_potion = pygame.transform.scale(defence_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     berserk_potion = pygame.image.load("BattleScreen/resources/berserk_potion.png").convert_alpha()
#     berserk_potion = pygame.transform.scale(berserk_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#
#     doors_icon = pygame.image.load("BattleScreen/resources/castledoors.png").convert_alpha()
#     doors_icon = pygame.transform.scale(doors_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     retry_icon = pygame.image.load("BattleScreen/resources/try_again.png").convert_alpha()
#     retry_icon = pygame.transform.scale(retry_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     victory_icon = pygame.image.load("BattleScreen/resources/victory.png").convert_alpha()
#     victory_icon = pygame.transform.scale(victory_icon, (int(WINDOW_SIZE[0]*0.15),(int(WINDOW_SIZE[1]*0.15))))
#
#     #------------------------------------------------------------------------------
#     screen.fill((242,238,203))
#
#     mouse_position = (0, 0)
#     #----------------------------------Music----------------------------------------
#     #open_inventory_bag = pygame.mixer.Sound('sounds/OpenInventory.mp3')
#
#     play_music('Battle')
#
#     #------------------------   -------------------------------------------------------
#     attack_sound = pygame.mixer.Sound('BattleScreen/resources/attack_sound.wav')
#     arrow_sound = pygame.mixer.Sound('BattleScreen/resources/arrow.wav')
#     snarl_sound = pygame.mixer.Sound('BattleScreen/resources/snarl.wav')
#     stone_sound = pygame.mixer.Sound('BattleScreen/resources/throwingstone.wav')
#     #------------------------------------ActionOrder--------------------------------
#     current_fighter = 1
#
#     action_cooldown = 0
#     action_waittime = 100
#     draw_cursor = False
#     battle_status = 0    #0 - nothing, 1 = lost, 2 = won
#
#     play_victory_music = True
#     # if battle_status ==0:
#     #     play_music('Battle')
#     # if battle_status ==2:
#     #     play_music('BattleVictory')
#     if battle_status ==1:
#         play_music('BattleDefeat')
#
#
#     #------------------------------------BattleInterface (line 315)-------------------
#     engage = False
#     clicked = False
#     skip_turn = False
#     #total_fighters = 11
#     show_indicators = True
#
#     use_health_potion = False
#     health_potion_restores = 50
#
#     use_defence_potion = False
#     defence_potion_adds = 100
#
#     use_berserk_potion = False
#     berserk_potion_adds = 30
#
#
#     #----------------------------------ShowStats------------------------------------
#     font =pygame.font.SysFont('Times New Roman', 18)
#     fontBag = pygame.font.Font('WorldMap/ESKARGOT.ttf', 38)
#     fontDMG = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
#     fontActive = pygame.font.Font('WorldMap/ESKARGOT.ttf', 80)
#     fontBattle = pygame.font.SysFont('Times New Roman', 70)
#     #pygame.font.Font('WorldMap/ESKARGOT.ttf', 70)
#
#
#     red = (230,16,35)
#     ginger = (245,116,34)
#     green = (0,255,0)
#     paper =  (255,150,100)
#     blue = (0,0,255)
#     lightblue = (240,248,255)
#
#
#
#
#     def draw_text(text,font,text_col,x,y):
#         img = font.render(text,True,text_col)
#         screen.blit(img,(x,y))
#     #--------------------------------------------------------------------------------
#
#     def draw_bgBackscreen ():
#         screen.blit(bg_backscreen,(0,0))
#
#     # def draw_noteMap():
#     #     screen.blit(note_map,(998,12))
#
#     def draw_bg():
#         screen.blit(bg_map,(210,40))
#
#     def draw_bag():
#         screen.blit(bag_of_coins,(0,0))
#         draw_text(f'{button.wealth}', fontBag, (255,225,100), 120, 30)
#
#     #------------------------------DrawingIndicators------------------------
#     def draw_panel():
#         screen.blit(panel,(-50,-35))
#         # for count, i in enumerate(army_player):
#         #       draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#         # for count, i in enumerate(army_hostiles):
#         #     draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (100,0,0), ((panel.get_width())*0.58), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#
#     #-------------------------------------------------------------------------
#     yvan_hp = int(linecache.getline('charstats.txt',1))
#     yvan_armor = int(linecache.getline('charstats.txt',2))
#     yvan_defene = int(linecache.getline('charstats.txt',3))
#     yvan_attack = int(linecache.getline('charstats.txt',4))
#
#     #----------------------------------Charaters------------------------------
#     class Fighter():
#         def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#             self.id=id
#             self.max_hp = max_hp
#             self.hp = max_hp
#             self.max_armor = max_armor
#             self.armor = max_armor
#             self.defence = defence
#             self.start_defence = defence
#             self.strength = strength
#             self.start_strength = strength
#             self.reach = reach
#             self.special = special
#             self.max_inventory = max_inventory
#             self.inventory = max_inventory
#             self.start_resistance = resistance
#             self.resistance = resistance
#             self.start_tricks = tricks
#             self.tricks = tricks
#             self.alive = True
#             self.hostile = True
#             self.animation_list = [] #list of lists (action/img)
#             self.frame_index = 0
#             self.action = 0 #0-idle / 1-attack / 2-hurt / 3-death  updates via self.animation_list = []
#             self.update_time = pygame.time.get_ticks()  # how much time has passed
#
#             #-----------------------------Animations--------------------------------------------
#             #loading idle action images
#             temp_list = []
#             for i in range(2):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/idle/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             #loading attack action images
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/attack/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(1):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/hurt/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/dead/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#
#             #-----------------------------------------------------------------------------------
#             self.animation_list.append(temp_list)
#             self.image = self.animation_list[self.action][self.frame_index]     # to control action/images
#             # two lists (action/frames)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#
#         #---------------------------------------------------------------------
#         def update(self,animation_modifier): #animation
#             animation_cooldown = 100
#             if self.action == 0:
#                 animation_cooldown = 1000*animation_modifier
#             if self.action == 1:
#                 animation_cooldown = 150*animation_modifier
#             if self.action == 2:
#                 animation_cooldown = 300*animation_modifier
#             if self.action == 3:
#                 animation_cooldown = 250*animation_modifier
#
#             #animation_cooldown = cooldown
#             self.image = self.animation_list[self.action][self.frame_index]  #adding action
#             if pygame.time.get_ticks() - self.update_time > animation_cooldown: #if its more than 100 its time to update the animation stage
#                 self.update_time = pygame.time.get_ticks() #resets timer
#                 self.frame_index += 1
#             # if animation run out, reset
#             if self.frame_index >= len(self.animation_list[self.action]):  #adding action
#
#                 #after death unit should stay at the last frame of the dead animation sequence
#                 if self.action == 3:    #dead animation in the list.
#                     self.frame_index = len(self.animation_list[self.action])-1  #final frame
#                 else:
#                     self.idle() # sets to idle animation
#
#         #-----------------------------------Idle----------------------------
#         def idle(self):
#             self.action = 0
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def hurt(self):
#             self.action = 2
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def dead(self):
#             self.action = 3
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def reset(self):
#             self.alive = True
#             self.inventory = self.max_inventory
#             self.hp = self.max_hp
#             self.armor = self.max_armor
#             self.defence = self.start_defence
#             self.strength = self.start_strength
#             self.frame_index = 0
#             self.action = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Attack----------------------------
#         def attack(self,target):
#             rand = random.randint(-5,5)
#             damage = self.strength + rand
#             if self.special == 1:
#                 #target.armor -= 0
#                 target.hp -= damage
#             elif self.special != 1:
#                 target.armor -= int(damage*(target.defence/100))
#                 if target.armor > 0:
#                     target.hp -= int(damage*(1 - target.defence/100))
#                 if target.armor <= 0:
#                     target.hp -= int((damage*(1 - target.defence/100)-target.armor))
#                     target.armor = 0
#             # runs hurn animation
#             target.hurt()
#
#             if target.hp < 1:
#                 target.hp = 0
#                 target.alive = False
#                 # runs death animation
#                 target.dead()
#
#             #DamageText
#             if self.special != 1:
#                 if target.armor > 1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage*(1 - target.defence/100))), red)
#                 if target.armor <=1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#             else:
#                 damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#
#             damage_text_group.add(damage_text)
#             #---------------------------------AttackSounds---------------------------------------
#             #attack sound # 0-standard blade; 1-arrow; 2-stone
#             if self.special == 0:
#                 pygame.mixer.Sound(attack_sound).play()
#             elif self.special == 1:
#                 pygame.mixer.Sound(arrow_sound).play()
#             elif self.special == 2:
#                 pygame.mixer.Sound(stone_sound).play()
#             elif self.special == 3:
#                 pygame.mixer.Sound(snarl_sound).play()
#             #------------------------------------------------------------------------------------
#
#
#             #animations
#             self.action = 1   # set action frames to as 1 as 1 = attack folder animation
#             self.frame_index = 0 # frame 0 in the attack folder animation
#             self.update_time = pygame.time.get_ticks()
#
#         #----------------------------------------------------------------------
#         def draw(self):
#             screen.blit(self.image, self.rect)
#
#     #-----------------------------------HealthBar--------------------------
#     class healthBar ():
#         def __init__(self, x,y, hp, max_hp):
#             self.x = x
#             self.y = y
#             self.hp = hp
#             self.max_hp = max_hp
#         def draw (self, hp):
#             self.hp = hp
#             # health ration
#             ratio = self.hp / self.max_hp
#             pygame.draw.rect(screen,red,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,green,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------ArmorBar--------------------------
#     class armorBar ():
#         def __init__(self, x,y, armor, max_armor):
#             self.x = x
#             self.y = y
#             self.armor = armor
#             self.max_armor = max_armor
#         def draw (self, armor):
#             self.armor = armor
#             # health ration
#             ratio = self.armor / self.max_armor
#             pygame.draw.rect(screen,lightblue,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,blue,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------AttributeChangeBar-----------------
#     class DamageText(pygame.sprite.Sprite):   # sprite is updated automatically
#         def __init__(self,x,y,damage, color):
#             pygame.sprite.Sprite.__init__(self)
#             self.image = fontDMG.render(damage, True, color)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#             self.counter = 0
#
#         def update(self):
#             #move text
#             self.rect.y -=1
#             #delete after timer
#             self.counter +=1
#             if self.counter > 30:
#                 self.kill()
#
#     damage_text_group = pygame.sprite.Group()    #python list
#     #def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#     #-----------------------------------PlayerArmy--------------------------
#     # militia = Fighter (435,295, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia_healthbar = healthBar (militia.rect.centerx-25,militia.rect.centery-55,militia.hp, militia.max_hp)
#     # militia_armorbar = armorBar (militia.rect.centerx-25,militia.rect.centery-50,militia.armor, militia.max_armor)
#     #-----------------------------------------------------------------------
#     boy = Fighter (435,305, 'boy',120,60,35,40,1,3,0,True,False,0,0)
#     boy_healthbar = healthBar (boy.rect.centerx-25,boy.rect.centery-55,boy.hp, boy.max_hp)
#     boy_armorbar = armorBar (boy.rect.centerx-25,boy.rect.centery-50,boy.armor, boy.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht = Fighter (530,250,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht_healthbar = healthBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-55,landsknecht.hp, landsknecht.max_hp)
#     landsknecht_armorbar = armorBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-50,landsknecht.armor, landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht1 = Fighter (620,205,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht1_healthbar = healthBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-55,landsknecht1.hp, landsknecht1.max_hp)
#     landsknecht1_armorbar = armorBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-50,landsknecht1.armor, landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     chevalier = Fighter (720,135,'chevalier',120,100,65,70,1,0,1,True,False,0,0)
#     chevalier_healthbar = healthBar (chevalier.rect.centerx-25,chevalier.rect.centery-65,chevalier.hp, chevalier.max_hp)
#     chevalier_armorbar = armorBar (chevalier.rect.centerx-25,chevalier.rect.centery-60,chevalier.armor, chevalier.max_armor)
#     #-----------------------------------------------------------------------
#     # militia1 = Fighter (700,165, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia1_healthbar = healthBar (militia1.rect.centerx-25,militia1.rect.centery-55,militia1.hp, militia1.max_hp)
#     # militia1_armorbar = armorBar (militia1.rect.centerx-25,militia1.rect.centery-50,militia1.armor, militia1.max_armor)
#     # #-----------------------------------------------------------------------
#     # militia2 = Fighter (790,115, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia2_healthbar = healthBar (militia2.rect.centerx-25,militia2.rect.centery-55,militia2.hp, militia2.max_hp)
#     # militia2_armorbar = armorBar (militia2.rect.centerx-25,militia2.rect.centery-50,militia2.armor, militia2.max_armor)
#     # #-----------------------------------------------------------------------
#     archer = Fighter (530,115, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer_healthbar = healthBar (archer.rect.centerx-25,archer.rect.top-20,archer.hp, archer.max_hp)
#     archer_armorbar = armorBar (archer.rect.centerx-25,archer.rect.top-15,archer.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     archer1 = Fighter (440,160, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer1_healthbar = healthBar (archer1.rect.centerx-25,archer1.rect.top-20,archer1.hp, archer.max_hp)
#     archer1_armorbar = armorBar (archer1.rect.centerx-25,archer1.rect.top-15,archer1.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     yvan = Fighter (350,210, 'yvan',yvan_hp,yvan_armor,yvan_defene,yvan_attack,2,2,0,True,False,0,0)
#     yvan_healthbar = healthBar (yvan.rect.centerx-25,yvan.rect.top-20,yvan.hp, yvan.max_hp)
#     yvan_armorbar = armorBar (yvan.rect.centerx-25,yvan.rect.top-15,yvan.armor, yvan.max_armor)
#     #max_hp,max_armor, defence, strength,
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_player = []
#     #army_player.append(militia)
#     army_player.append(boy)
#     army_player.append(landsknecht)
#     army_player.append(landsknecht1)
#     army_player.append(chevalier)
#     #army_player.append(militia1)
#     #army_player.append(militia2)
#     army_player.append(archer)
#     army_player.append(archer1)
#     army_player.append(yvan)
#
#     army_player_front = army_player[:4]
#
#     #-----------------------------HostileArmy-------------------------------
#     # h_militia = Fighter(570,365,'militia',60,30,35,30,1,0,1,True,True,0,0)
#     # h_militia_healthbar = healthBar(h_militia.rect.centerx-25,h_militia.rect.centery-55,h_militia.hp, h_militia.max_hp)
#     # h_militia_armorbar = armorBar(h_militia.rect.centerx-25,h_militia.rect.centery-50,h_militia.armor, h_militia.max_armor)
#     #-----------------------------------------------------------------------
#     h_brigand = Fighter(570,365,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     h_brigand_healthbar = healthBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-55,h_brigand.hp, h_brigand.max_hp)
#     h_brigand_armorbar = armorBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-50,h_brigand.armor, h_brigand.max_armor)
#
#     #-----------------------------------------------------------------------
#     h_brigand1 = Fighter(660,325,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     h_brigand1_healthbar = healthBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-55,h_brigand1.hp, h_brigand1.max_hp)
#     h_brigand1_armorbar = armorBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-50,h_brigand1.armor, h_brigand1.max_armor)
#
#     #-----------------------------------------------------------------------
#     h_landsknecht = Fighter (750,280,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     h_landsknecht_healthbar = healthBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-55,h_landsknecht.hp, h_landsknecht.max_hp)
#     h_landsknecht_armorbar = armorBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-50,h_landsknecht.armor, h_landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     h_landsknecht1 = Fighter (840,235,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     h_landsknecht1_healthbar = healthBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-55,h_landsknecht1.hp, h_landsknecht1.max_hp)
#     h_landsknecht1_armorbar = armorBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-50,h_landsknecht1.armor, h_landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     #-----------------------------------------------------------------------
#     h_brigand2 = Fighter(940,195,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     h_brigand2_healthbar = healthBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-55,h_brigand2.hp, h_brigand2.max_hp)
#     h_brigand2_armorbar = armorBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-50,h_brigand2.armor, h_brigand2.max_armor)
#     #-----------------------------------------------------------------------
#     # h_landsknecht2 = Fighter (790,340,'landsknecht',90,55,40,50,2,0,1,True,True,0,0)
#     # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
#     # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman = Fighter (790,350, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman_healthbar = healthBar (h_bowman.rect.centerx-25,h_bowman.rect.top-20,h_bowman.hp, h_bowman.max_hp)
#     h_bowman_armorbar = armorBar (h_bowman.rect.centerx-25,h_bowman.rect.top-15,h_bowman.armor, h_bowman.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman1 = Fighter (695,400, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman1_healthbar = healthBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-20,h_bowman1.hp, h_bowman1.max_hp)
#     h_bowman1_armorbar = armorBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-15,h_bowman1.armor, h_bowman1.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman2 = Fighter (880,310, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman2_healthbar = healthBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-20,h_bowman2.hp, h_bowman2.max_hp)
#     h_bowman2_armorbar = armorBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-15,h_bowman2.armor, h_bowman2.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman3 = Fighter (960,260, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman3_healthbar = healthBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-20,h_bowman3.hp, h_bowman3.max_hp)
#     h_bowman3_armorbar = armorBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-15,h_bowman3.armor, h_bowman3.max_armor)
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_hostiles = []
#     army_hostiles.append(h_brigand)
#     army_hostiles.append(h_brigand1)
#     army_hostiles.append(h_landsknecht)
#     army_hostiles.append(h_landsknecht1)
#     army_hostiles.append(h_brigand2)
#     army_hostiles.append(h_bowman)
#     army_hostiles.append(h_bowman1)
#     army_hostiles.append(h_bowman2)
#     army_hostiles.append(h_bowman3)
#
#     army_hostiles_front = army_hostiles[:5]
#
#
#     #------------------------------TotalUnitNumber----------------------------
#     total_hostiles = len(army_hostiles)
#     total_allies = len(army_player)
#     total_fighters = total_hostiles + total_allies
#
#     #------------------------------ItemsUse(Button)---------------------------
#     #inventory_button = button.Button(screen,WINDOW_SIZE[0]*0 + 110, WINDOW_SIZE[1]*0 - 6,inventory_bag,280,120,0, True, 'Inventory')
#
#     inventory_button = button.ToggleButton(screen,-65, 425,inventory_bag,260,120,0, True, 'Inventory')
#     #------------------------------ItemsUse(PotionButton)-------------------
#     potion_button = button.Button(screen, WINDOW_SIZE[0]*0.01, WINDOW_SIZE[1]*0.90, health_potion, 48,72,30, False,f'Health Potion. Restores {health_potion_restores} HP')
#     potion_button1 = button.Button(screen, WINDOW_SIZE[0]*0.06, WINDOW_SIZE[1]*0.90, defence_potion, 48,72,40, False,f'Defence Potion. Gives {defence_potion_adds} DEF/ARM')
#     potion_button2 = button.Button(screen, WINDOW_SIZE[0]*0.11, WINDOW_SIZE[1]*0.90, berserk_potion, 48,72,60, False,f'Berserk Potion. Gives {berserk_potion_adds} ATK / Removes {int(berserk_potion_adds*1)} DEF')
#
#
#     #------------------------------IconToggle(Reset)------------------------
#     restart_button = button.Button(screen, 1100, 8, retry_icon, 84,90,25, True,'Try Again')
#     skip_turn_button = button.Button(screen, WINDOW_SIZE[0]*0.92, WINDOW_SIZE[1]*0.62, skip_turn_img, 86,82,60, False,f'Skip Turn')
#     victory_button = button.Button(screen, 1170, 15, victory_icon, 86,90,25, True,'Back to Map')
#     leave_button = button.Button(screen, 1190, 0, doors_icon, 64,90,25, True,'Leave Battlefield')
#
#
#     #-----------------------------------------------------------------------
#
#     while new_beginnings_battle_running:
#         #display.fill((146,244,255))
#         draw_bgBackscreen()
#         #draw_noteMap()  # location map
#         draw_bg()
#         draw_panel()
#         draw_bag()
#
#         #-----------------------------DrawingUnits/AnimatioSpeedMod------------
#         for units in army_player:
#             # militia.update(0.9)
#             # militia.draw()
#             #------------
#             landsknecht.update(1)
#             landsknecht.draw()
#             #------------
#             chevalier.update(1.3)
#             chevalier.draw()
#             #------------
#             # militia1.update(0.88)
#             # militia1.draw()
#             #------------
#             boy.update(0.88)
#             boy.draw()
#             #------------
#             landsknecht1.update(1.1)
#             landsknecht1.draw()
#             #------------
#             # militia2.update(0.84)
#             # militia2.draw()
#             #------------
#             archer.update(0.95)
#             archer.draw()
#             #------------
#             archer1.update(0.92)
#             archer1.draw()
#             #------------
#             yvan.update(1.05)
#             yvan.draw()
#
#         for hostile in army_hostiles:
#             h_brigand.update(0.9)
#             h_brigand.draw()
#             #------------
#             h_brigand2.update(0.85)
#             h_brigand2.draw()
#             #------------
#             h_landsknecht.update(0.95)
#             h_landsknecht.draw()
#             #------------
#             h_landsknecht1.update(0.98)
#             h_landsknecht1.draw()
#             #------------
#             h_brigand1.update(0.9)
#             h_brigand1.draw()
#             #------------
#             h_bowman.update(0.89)
#             h_bowman.draw()
#             #------------
#             h_bowman1.update(0.85)
#             h_bowman1.draw()
#             #------------
#             h_bowman2.update(0.92)
#             h_bowman2.draw()
#             #------------
#             h_bowman3.update(0.90)
#             h_bowman3.draw()
#         #-----------------------------HealthBar/ArmorBar-----------------------
#         #-------------Player------------------------
#         if show_indicators == True:
#             if chevalier.alive == True:
#                 chevalier_healthbar.draw(chevalier.hp)
#                 chevalier_armorbar.draw(chevalier.armor)
#             # if militia.alive == True:
#             #     militia_healthbar.draw(militia.hp)
#             #     militia_armorbar.draw(militia.armor)
#             if boy.alive == True:
#                 boy_healthbar.draw(boy.hp)
#                 boy_armorbar.draw(boy.armor)
#             if landsknecht.alive == True:
#                 landsknecht_healthbar.draw(landsknecht.hp)
#                 landsknecht_armorbar.draw(landsknecht.armor)
#             # if militia1.alive == True:
#             #     militia1_healthbar.draw(militia1.hp)
#             #     militia1_armorbar.draw(militia1.armor)
#             if landsknecht1.alive == True:
#                 landsknecht1_healthbar.draw(landsknecht1.hp)
#                 landsknecht1_armorbar.draw(landsknecht1.armor)
#             # if militia2.alive == True:
#             #     militia2_healthbar.draw(militia2.hp)
#             #     militia2_armorbar.draw(militia2.armor)
#             if archer.alive == True:
#                 archer_healthbar.draw(archer.hp)
#                 archer_armorbar.draw(archer.armor)
#             if archer1.alive == True:
#                 archer1_healthbar.draw(archer1.hp)
#                 archer1_armorbar.draw(archer1.armor)
#             if yvan.alive == True:
#                 yvan_healthbar.draw(yvan.hp)
#                 yvan_armorbar.draw(yvan.armor)
#
#             #------------------Enemy--------------------
#             if h_brigand.alive == True:
#                 h_brigand_healthbar.draw(h_brigand.hp)
#                 h_brigand_armorbar.draw(h_brigand.armor)
#             if h_brigand2.alive == True:
#                 h_brigand2_healthbar.draw(h_brigand2.hp)
#                 h_brigand2_armorbar.draw(h_brigand2.armor)
#             if h_landsknecht.alive == True:
#                 h_landsknecht_healthbar.draw(h_landsknecht.hp)
#                 h_landsknecht_armorbar.draw(h_landsknecht.armor)
#             if h_landsknecht1.alive == True:
#                 h_landsknecht1_healthbar.draw(h_landsknecht1.hp)
#                 h_landsknecht1_armorbar.draw(h_landsknecht1.armor)
#             if h_brigand1.alive == True:
#                 h_brigand1_healthbar.draw(h_brigand1.hp)
#                 h_brigand1_armorbar.draw(h_brigand1.armor)
#             if h_bowman.alive == True:
#                 h_bowman_healthbar.draw(h_bowman.hp)
#                 h_bowman_armorbar.draw(h_bowman.armor)
#             if h_bowman1.alive == True:
#                 h_bowman1_healthbar.draw(h_bowman1.hp)
#                 h_bowman1_armorbar.draw(h_bowman1.armor)
#             if h_bowman2.alive == True:
#                 h_bowman2_healthbar.draw(h_bowman2.hp)
#                 h_bowman2_armorbar.draw(h_bowman2.armor)
#             if h_bowman3.alive == True:
#                 h_bowman3_healthbar.draw(h_bowman3.hp)
#                 h_bowman3_armorbar.draw(h_bowman3.armor)
#         #----------------------------------------------------------------------
#
#         #-----------------------------DamageText-----------------------------
#         damage_text_group.update()
#         damage_text_group.draw(screen)
#         #methods update and draw are parts of the sprite.
#
#         #-----------------------------Items/SkipTurn/Inventory-----------------------------
#         pos = pygame.mouse.get_pos()
#         if skip_turn_button.rect.collidepoint(pos):
#             draw_text(f'{skip_turn_button.description}', fontDMG, green, skip_turn_button.rect.x-30,skip_turn_button.rect.y+100)
#         if skip_turn_button.draw():
#             skip_turn=True
#         if battle_status != 2 and leave_button.available == True:
#             if leave_button.rect.collidepoint(pos):
#                 draw_text(f'{leave_button.description}', fontDMG, green, leave_button.rect.x-140,leave_button.rect.y+100)
#             if leave_button.draw():
#                 #pyautogui.moveTo(750, 400)
#                 play_music('Map')
#                 button.wealth = button.start_wealth
#                 new_beginnings_battle_running = False
#
#
#         if inventory_button.rect.collidepoint(pos):
#             draw_text(f'{inventory_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#         if inventory_button.toggled == True and battle_status ==0:
#             potion_button.available = True
#             potion_button1.available = True
#             potion_button2.available = True
#
#
#             #---------------------HealthPotion--------------------------------------
#             if potion_button.available == True:
#                 if potion_button.draw():
#                     use_health_potion = True
#                 draw_text(f'{potion_button.price}', fontBag, (255,225,100), potion_button.rect.x+5, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button.rect.collidepoint(pos):
#                     draw_text(f'{potion_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#             #-------DefencePotion--------------
#             if potion_button1.available == True:
#                 if potion_button1.draw():
#                     use_defence_potion = True
#                 draw_text(f'{potion_button1.price}', fontBag, (255,225,100), potion_button.rect.x+65, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button1.rect.collidepoint(pos):
#                     draw_text(f'{potion_button1.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#                 #-------BerserkPotion--------------
#             if potion_button2.available == True:
#                 if potion_button2.draw():
#                     use_berserk_potion = True
#                 draw_text(f'{potion_button2.price}', fontBag, (255,225,100), potion_button.rect.x+130, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button2.rect.collidepoint(pos):
#                     draw_text(f'{potion_button2.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#
#         #---------------------InventoryStock--------------------------------------
#         else:
#             potion_button.available = False
#
#         #--------------------------------------------------------------------------
#         if battle_status ==0:   #win/loose check
#
#
#             #-----------------------------PlayerAttacking---------------------------
#             for count, ally in enumerate(army_player):
#                 if current_fighter == 1+count:
#                     draw_text('^', fontActive, "#FFA500", ally.rect.centerx-20,ally.rect.y -65)
#                     if ally.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#
#                             if ally.reach == 2:
#                                 if engage == True and target != None:
#                                     # conditioned upon engage below & def attack above
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif ally.reach == 1:
#                                 if engage == True and target != None and target.reach == 1:
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             for enemy in army_hostiles_front:
#                                 if all(enemy.alive == False for enemy in army_hostiles_front):
#                                     #enemy.alive == False:
#                                     if ally.reach == 1:
#                                         if engage == True and target != None and target.reach == 2:
#                                             ally.reach = 2
#                                             ally.attack(target)
#                                             current_fighter += 1
#                                             action_cooldown = 0
#
#
#                             #-----------------------------------------SkipTurn-----------------------------------------
#                             if skip_turn == True:
#                                 current_fighter += 1
#                                 action_cooldown = 0
#                                 skip_turn_heal = 10
#                                 if ally.max_hp - ally.hp > skip_turn_heal:    #50
#                                     skip_turn_heal = skip_turn_heal
#                                 else:
#                                     skip_turn_heal = ally.max_hp - ally.hp
#                                 ally.hp += skip_turn_heal
#                                 #DamageText
#                                 damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(skip_turn_heal), green)
#                                 damage_text_group.add(damage_text)
#                             skip_turn = False
#
#                             #------------UsingItem(HealthPotion)---------------------------
#                             if use_health_potion == True and button.wealth >= potion_button.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_hp - ally.hp > health_potion_restores:    #50
#                                         heal_amount = health_potion_restores
#                                     else:
#                                         heal_amount = ally.max_hp - ally.hp
#                                     ally.hp += heal_amount
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button.price
#                                     #DamageText
#                                     damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(heal_amount), green)
#                                     damage_text_group.add(damage_text)
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_health_potion = False
#
#                             #----------------------------------------------------
#                             #------------UsingItem(DefencePotion)---------------
#                             if use_defence_potion == True and button.wealth >= potion_button1.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_armor - ally.armor > defence_potion_adds:    #50
#                                         add_defence_amount = defence_potion_adds
#                                     else:
#                                         add_defence_amount = ally.max_armor - ally.armor
#                                     ally.armor += add_defence_amount
#                                     ally.defence = 100
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button1.price     #Change price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_defence_potion = False
#
#
#                             #------------UsingItem(BerserkPotion)---------------
#                             if use_berserk_potion == True and button.wealth >= potion_button2.price:
#                                 if ally.inventory > 0:
#                                     ally.strength += berserk_potion_adds
#                                     if ally.defence < int(berserk_potion_adds):
#                                         ally.defence = 0
#                                     else:
#                                         ally.defence -= int(berserk_potion_adds)
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button2.price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                     #Change price
#                                 use_berserk_potion = False
#
#                     else:
#                         current_fighter +=1   #if dead = skip turn
#
#             #-----------------------------EnemyAttacking----------------------------
#             for count, enemy in enumerate(army_hostiles):
#                 if current_fighter == 1+ total_allies + count:   # "3 + count" - checks with the max_fighter var and number of units in army_player
#                     draw_text('^', fontActive, "#FFA500", enemy.rect.centerx-20,enemy.rect.y -65)
#                     if enemy.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#                             #health_check
#                             if (enemy.hp / enemy.max_hp) <0.5 and enemy.inventory >0:
#                                 if enemy.max_hp - enemy.hp > health_potion_restores:
#                                     heal_amount = health_potion_restores
#                                 else:
#                                     heal_amount = enemy.max_hp - enemy.hp
#
#                                 enemy.hp += heal_amount
#                                 enemy.inventory -= 1
#
#                                 #DamageText
#                                 damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(heal_amount), green)
#                                 damage_text_group.add(damage_text)
#
#                                 current_fighter +=1
#                                 action_cooldown = 0
#
#                             elif enemy.reach == 2:
#                                 if enemy.strength >= ally.hp and ally.alive == True:
#                                     enemy.attack(ally)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif enemy.reach == 1:
#                                 if all(ally.alive == True for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 elif all(ally.alive == False for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 2]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                             #else:
#                             #     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                             #     # enemy.hp += 10
#                             #     current_fighter += 1
#                             #     action_cooldown = 0
#                             #     # damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(10), green)
#                             #     # damage_text_group.add(damage_text)
#
#                     else:
#                         current_fighter +=1
#
#             #---------------------------------Turns----------------------------
#             # if all have had a turn, reset
#             if current_fighter > total_fighters:
#                 current_fighter = 1
#
#         #-----------------------------DefeatStatus-------------------------
#         # checking alive/dead status
#         alive_allies = 0
#         for ally in army_player:
#             if ally.alive == True:
#                 alive_allies +=1
#         if alive_allies ==0:
#             battle_status =1
#
#         #---------------------------------VictoryStatus--------------------
#         alive_enemies = 0
#         for enemy in army_hostiles:
#             if enemy.alive == True:
#                 alive_enemies +=1
#         if alive_enemies ==0:
#             battle_status =2
#
#         #-------------------Defeat/VictoryStatusDisplay-------------------
#         if battle_status !=0:
#             if battle_status ==1:
#                 draw_text(f'Defeat!', fontMenuLarge, (155,0,0), screen.get_width()*0.46,0)
#                 #-------------------ResetButton-----------------------------------
#                 if restart_button.available == True:
#                     if restart_button.draw():
#                         play_music('Battle')
#                         for ally in army_player:
#                             ally.reset()
#                         for enemy in army_hostiles:
#                             enemy.reset()
#                         button.wealth = button.start_wealth         #restart gold here
#                         current_fighter = 1
#                         action_cooldown = 0
#                         battle_status = 0
#
#                         pos = pygame.mouse.get_pos() # text over the button
#                     if restart_button.rect.collidepoint(pos):
#                         draw_text(f'{restart_button.description}', fontDMG, green, restart_button.rect.x+30,leave_button.rect.y+100)
#
#             #-------------------Defeat/VictoryStatusDisplay-------------------
#             if battle_status ==2:
#                 button.quest_new_beginnings = 'locked'
#                 draw_text(f'Victory!', fontMenuLarge, green, screen.get_width()*0.46,0)
#                 if play_victory_music == True:
#                     play_music('BattleVictory')
#                 play_victory_music = False
#                 if victory_button.available == True:
#                     if victory_button.draw():
#                         button.wealth += 200
#                         button.start_wealth = button.wealth
#                         button.quest_dire_wolves = 'unlocked'
#                         print(button.start_wealth)
#                         print(button.wealth)
#                         play_music('Map')
#                         new_beginnings_battle_running = False
#                     if victory_button.rect.collidepoint(pos):
#                         draw_text(f'{victory_button.description}', fontDMG, green, victory_button.rect.x-75,leave_button.rect.y+100)
#         #------------------------------End/Controls------------------------
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == VIDEORESIZE:
#                 if not fullscreen:
#                     screen = pygame.display.set_mode((event.w,event.h),0,32)
#
#             if event.type == KEYDOWN:
#                 if event.key == K_f and show_indicators == True:
#                     show_indicators = False
#                 elif event.key == K_f and show_indicators == False:
#                     show_indicators = True
#
#                 if event.key == K_o:
#                     # fullscreen = not fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     button.fullscreen = not button.fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     fullscreen = button.fullscreen
#
#                     if fullscreen:
#                         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#                     else:
#                         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#             #---------------------ToggleButton------------------------
#             inventory_button.event_handler(event) #ToggleButton
#             #---------------------ToggleButton------------------------
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 clicked = True
#             else:
#                 clicked = False
#
#         if leave_button.clicked == True or victory_button.clicked == True:
#             mouse_map_position_align(750,400)
#             #pyautogui.moveTo(750, 400)
#         #-----------------------------Action/TargetSearch-------------------
#         engage = False
#         target = None
#
#         inventory_button.draw(screen) #ToggleButton
#
#         pygame.mouse.set_visible(False)
#         pos = pygame.mouse.get_pos()
#         screen.blit(normal_icon,pos)
#
#         for count, ally in enumerate(army_player):
#             if ally.rect.collidepoint(pos) and ally.alive == True:
#                 draw_text(f'{ally.id} | HP: {ally.hp} | ARM: {ally.armor} | ATK: {ally.strength} | DEF: {ally.defence} | INV: {ally.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#         for count, enemy in enumerate(army_hostiles):
#             if enemy.rect.collidepoint(pos) and enemy.alive == True:
#                 pygame.mouse.set_visible(False)
#                 screen.blit(attack_icon,pos)
#                 draw_text(f'{enemy.id} | HP: {enemy.hp} | ARM: {enemy.armor} | ATK: {enemy.strength} | DEF: {enemy.defence} | INV: {enemy.inventory}', font, (100,0,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#
#                 # show attack icon
#                 #--------------chooseTarget&Attack-------------------------
#                 if clicked == True and enemy.alive == True:
#                     engage = True
#                     target = army_hostiles[count]
#
#
#         #-----------------------------------------------------------------------
#         #surf = pygame.transform.scale(display, WINDOW_SIZE)
#         #screen.blit(surf, (0,0))
#
#         pygame.display.update()
#         clock.tick(60)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def dire_wolves_battle ():
#     dire_wolves_battle_running = True
#
#     clock = pygame.time.Clock()
#     pygame.init()
#
#     pygame.mixer.set_num_channels(32)
#     pygame.mixer.pre_init(44100,-16,2,512)
#     #-----------------------------GameWindowSettings----------------------
#     pygame.display.set_caption("Dire Wolves")
#     WINDOW_SIZE = (1280,720)
#     screen = pygame.display.set_mode((1280,720),0,32)
#     #display = pygame.Surface((600,400))
#
#
#     monitor_size =[pygame.display.Info().current_w, pygame.display.Info().current_h]
#
#     fullscreen = button.fullscreen
#         #not bool(linecache.getline('genericmap.txt',1))
#     if fullscreen:
#         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#     else:
#         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#
# #-----------------------------------Battlemap,Interface------------------------
#     bg_backscreen = pygame.image.load("BattleScreen/background.png").convert_alpha()
#     bg_backscreen = pygame.transform.scale(bg_backscreen, (int(WINDOW_SIZE[0]*1.00),(int(WINDOW_SIZE[1]*0.75))))
#
#     note_map = pygame.image.load("BattleScreen/note_Faroak0.png").convert_alpha()
#     note_map = pygame.transform.scale(note_map, (int(WINDOW_SIZE[0]*0.21),(int(WINDOW_SIZE[1]*0.28))))
#
#     bg_map = pygame.image.load("BattleScreen/BattleMap0.png").convert_alpha()
#     bg_map = pygame.transform.scale(bg_map, (int(WINDOW_SIZE[0]*0.70),(int(WINDOW_SIZE[1]*0.70))))
#
#     panel = pygame.image.load("BattleScreen/gamepanel0.png").convert_alpha()
#     panel = pygame.transform.scale(panel, (int(WINDOW_SIZE[0]*1.10),(int(WINDOW_SIZE[1]*1.40))))
#
#     bag_of_coins = pygame.image.load("BattleScreen/bag.png").convert_alpha()
#     bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     #-----------------------------------Icons-------------------------------------
#     attack_icon = pygame.image.load("BattleScreen/icon_fight.png").convert_alpha()
#     attack_icon = pygame.transform.scale(attack_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#     normal_icon = pygame.image.load("BattleScreen/cursor_final.png").convert_alpha()
#     normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#
#     skip_turn_img = pygame.image.load("BattleScreen/skip_turn.png").convert_alpha()
#     skip_turn_img = pygame.transform.scale(skip_turn_img, (int(WINDOW_SIZE[0]*0.06),(int(WINDOW_SIZE[1]*0.05))))
#
#     #-----------------------------------Characters---------------------------------
#     # militia_image = pygame.image.load("BattleScreen/militia/idle/idle_0.png").convert_alpha()
#     # landsknecht_image = pygame.image.load("BattleScreen/landsknecht/idle/idle_0.png").convert_alpha()
#
#     #------------------------------------------------------------------------------
#     #--------------------------------Items----------------------------------------
#     inventory_bag = pygame.image.load("BattleScreen/resources/inventorybag.png").convert_alpha()
#     inventory_bag = pygame.transform.scale(inventory_bag, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     health_potion = pygame.image.load("BattleScreen/resources/health_potion.png").convert_alpha()
#     health_potion = pygame.transform.scale(health_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     defence_potion = pygame.image.load("BattleScreen/resources/reflexes_potion.png").convert_alpha()
#     defence_potion = pygame.transform.scale(defence_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     berserk_potion = pygame.image.load("BattleScreen/resources/berserk_potion.png").convert_alpha()
#     berserk_potion = pygame.transform.scale(berserk_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#
#     doors_icon = pygame.image.load("BattleScreen/resources/castledoors.png").convert_alpha()
#     doors_icon = pygame.transform.scale(doors_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     retry_icon = pygame.image.load("BattleScreen/resources/try_again.png").convert_alpha()
#     retry_icon = pygame.transform.scale(retry_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     victory_icon = pygame.image.load("BattleScreen/resources/victory.png").convert_alpha()
#     victory_icon = pygame.transform.scale(victory_icon, (int(WINDOW_SIZE[0]*0.15),(int(WINDOW_SIZE[1]*0.15))))
#
#     #------------------------------------------------------------------------------
#     screen.fill((242,238,203))
#
#     mouse_position = (0, 0)
#     #----------------------------------Music----------------------------------------
#     #open_inventory_bag = pygame.mixer.Sound('sounds/OpenInventory.mp3')
#
#     play_music('Battle')
#
#     #------------------------   -------------------------------------------------------
#     attack_sound = pygame.mixer.Sound('BattleScreen/resources/attack_sound.wav')
#     arrow_sound = pygame.mixer.Sound('BattleScreen/resources/arrow.wav')
#     snarl_sound = pygame.mixer.Sound('BattleScreen/resources/snarl.wav')
#     stone_sound = pygame.mixer.Sound('BattleScreen/resources/throwingstone.wav')
#     #------------------------------------ActionOrder--------------------------------
#     current_fighter = 1
#
#     action_cooldown = 0
#     action_waittime = 100
#     draw_cursor = False
#     battle_status = 0    #0 - nothing, 1 = lost, 2 = won
#
#     # if battle_status ==0:
#     #     play_music('Battle')
#     # if battle_status ==2:
#     #     pygame.mixer.music.play(0)
#     #     play_music('BattleVictory')
#     play_victory_music =  True
#     if battle_status ==1:
#         play_music('BattleDefeat')
#
#     #------------------------------------BattleInterface (line 315)-------------------
#     engage = False
#     clicked = False
#     skip_turn = False
#     #total_fighters = 11
#     show_indicators = True
#
#     use_health_potion = False
#     health_potion_restores = 50
#
#     use_defence_potion = False
#     defence_potion_adds = 100
#
#     use_berserk_potion = False
#     berserk_potion_adds = 30
#
#
#     #----------------------------------ShowStats------------------------------------
#     font =pygame.font.SysFont('Times New Roman', 18)
#     fontBag = pygame.font.Font('WorldMap/ESKARGOT.ttf', 38)
#     fontDMG = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
#     fontActive = pygame.font.Font('WorldMap/ESKARGOT.ttf', 80)
#     fontBattle = pygame.font.SysFont('Times New Roman', 70)
#     #pygame.font.Font('WorldMap/ESKARGOT.ttf', 70)
#
#
#     red = (230,16,35)
#     ginger = (245,116,34)
#     green = (0,255,0)
#     paper =  (255,150,100)
#     blue = (0,0,255)
#     lightblue = (240,248,255)
#
#
#
#
#     def draw_text(text,font,text_col,x,y):
#         img = font.render(text,True,text_col)
#         screen.blit(img,(x,y))
#     #--------------------------------------------------------------------------------
#
#     def draw_bgBackscreen ():
#         screen.blit(bg_backscreen,(0,0))
#
#     # def draw_noteMap():
#     #     screen.blit(note_map,(998,12))
#
#     def draw_bg():
#         screen.blit(bg_map,(210,40))
#
#     def draw_bag():
#         screen.blit(bag_of_coins,(0,0))
#         draw_text(f'{button.wealth}', fontBag, (255,225,100), 120, 30)
#
#     #------------------------------DrawingIndicators------------------------
#     def draw_panel():
#         screen.blit(panel,(-50,-35))
#         # for count, i in enumerate(army_player):
#         #       draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#         # for count, i in enumerate(army_hostiles):
#         #     draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (100,0,0), ((panel.get_width())*0.58), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#
#     #-------------------------------------------------------------------------
#     yvan_hp = int(linecache.getline('charstats.txt',1))
#     yvan_armor = int(linecache.getline('charstats.txt',2))
#     yvan_defene = int(linecache.getline('charstats.txt',3))
#     yvan_attack = int(linecache.getline('charstats.txt',4))
#
#     #----------------------------------Charaters------------------------------
#     class Fighter():
#         def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#             self.id=id
#             self.max_hp = max_hp
#             self.hp = max_hp
#             self.max_armor = max_armor
#             self.armor = max_armor
#             self.defence = defence
#             self.start_defence = defence
#             self.strength = strength
#             self.start_strength = strength
#             self.reach = reach
#             self.special = special
#             self.max_inventory = max_inventory
#             self.inventory = max_inventory
#             self.start_resistance = resistance
#             self.resistance = resistance
#             self.start_tricks = tricks
#             self.tricks = tricks
#             self.alive = True
#             self.hostile = True
#             self.animation_list = [] #list of lists (action/img)
#             self.frame_index = 0
#             self.action = 0 #0-idle / 1-attack / 2-hurt / 3-death  updates via self.animation_list = []
#             self.update_time = pygame.time.get_ticks()  # how much time has passed
#
#             #-----------------------------Animations--------------------------------------------
#             #loading idle action images
#             temp_list = []
#             for i in range(2):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/idle/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             #loading attack action images
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/attack/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(1):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/hurt/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/dead/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#
#             #-----------------------------------------------------------------------------------
#             self.animation_list.append(temp_list)
#             self.image = self.animation_list[self.action][self.frame_index]     # to control action/images
#             # two lists (action/frames)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#
#         #---------------------------------------------------------------------
#         def update(self,animation_modifier): #animation
#             animation_cooldown = 100
#             if self.action == 0:
#                 animation_cooldown = 1000*animation_modifier
#             if self.action == 1:
#                 animation_cooldown = 150*animation_modifier
#             if self.action == 2:
#                 animation_cooldown = 300*animation_modifier
#             if self.action == 3:
#                 animation_cooldown = 250*animation_modifier
#
#             #animation_cooldown = cooldown
#             self.image = self.animation_list[self.action][self.frame_index]  #adding action
#             if pygame.time.get_ticks() - self.update_time > animation_cooldown: #if its more than 100 its time to update the animation stage
#                 self.update_time = pygame.time.get_ticks() #resets timer
#                 self.frame_index += 1
#             # if animation run out, reset
#             if self.frame_index >= len(self.animation_list[self.action]):  #adding action
#
#                 #after death unit should stay at the last frame of the dead animation sequence
#                 if self.action == 3:    #dead animation in the list.
#                     self.frame_index = len(self.animation_list[self.action])-1  #final frame
#                 else:
#                     self.idle() # sets to idle animation
#
#         #-----------------------------------Idle----------------------------
#         def idle(self):
#             self.action = 0
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def hurt(self):
#             self.action = 2
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def dead(self):
#             self.action = 3
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def reset(self):
#             self.alive = True
#             self.inventory = self.max_inventory
#             self.hp = self.max_hp
#             self.armor = self.max_armor
#             self.defence = self.start_defence
#             self.strength = self.start_strength
#             self.frame_index = 0
#             self.action = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Attack----------------------------
#         def attack(self,target):
#             rand = random.randint(-5,5)
#             damage = self.strength + rand
#             if self.special == 1:
#                 #target.armor -= 0
#                 target.hp -= damage
#             elif self.special != 1:
#                 target.armor -= int(damage*(target.defence/100))
#                 if target.armor > 0:
#                     target.hp -= int(damage*(1 - target.defence/100))
#                 if target.armor <= 0:
#                     target.hp -= int((damage*(1 - target.defence/100)-target.armor))
#                     target.armor = 0
#             # runs hurn animation
#             target.hurt()
#
#             if target.hp < 1:
#                 target.hp = 0
#                 target.alive = False
#                 # runs death animation
#                 target.dead()
#
#             #DamageText
#             if self.special != 1:
#                 if target.armor > 1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage*(1 - target.defence/100))), red)
#                 if target.armor <=1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#             else:
#                 damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#
#             damage_text_group.add(damage_text)
# #---------------------------------AttackSounds---------------------------------------
#             #attack sound # 0-standard blade; 1-arrow; 2-stone
#             if self.special == 0:
#                 pygame.mixer.Sound(attack_sound).play()
#             elif self.special == 1:
#                 pygame.mixer.Sound(arrow_sound).play()
#             elif self.special == 2:
#                 pygame.mixer.Sound(stone_sound).play()
#             elif self.special == 3:
#                 pygame.mixer.Sound(snarl_sound).play()
# #------------------------------------------------------------------------------------
#
#
#             #animations
#             self.action = 1   # set action frames to as 1 as 1 = attack folder animation
#             self.frame_index = 0 # frame 0 in the attack folder animation
#             self.update_time = pygame.time.get_ticks()
#
#         #----------------------------------------------------------------------
#         def draw(self):
#             screen.blit(self.image, self.rect)
#
#     #-----------------------------------HealthBar--------------------------
#     class healthBar ():
#         def __init__(self, x,y, hp, max_hp):
#             self.x = x
#             self.y = y
#             self.hp = hp
#             self.max_hp = max_hp
#         def draw (self, hp):
#             self.hp = hp
#             # health ration
#             ratio = self.hp / self.max_hp
#             pygame.draw.rect(screen,red,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,green,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------ArmorBar--------------------------
#     class armorBar ():
#         def __init__(self, x,y, armor, max_armor):
#             self.x = x
#             self.y = y
#             self.armor = armor
#             self.max_armor = max_armor
#         def draw (self, armor):
#             self.armor = armor
#             # health ration
#             ratio = self.armor / self.max_armor
#             pygame.draw.rect(screen,lightblue,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,blue,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------AttributeChangeBar-----------------
#     class DamageText(pygame.sprite.Sprite):   # sprite is updated automatically
#         def __init__(self,x,y,damage, color):
#             pygame.sprite.Sprite.__init__(self)
#             self.image = fontDMG.render(damage, True, color)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#             self.counter = 0
#
#         def update(self):
#             #move text
#             self.rect.y -=1
#             #delete after timer
#             self.counter +=1
#             if self.counter > 30:
#                 self.kill()
#
#     damage_text_group = pygame.sprite.Group()    #python list
#     #def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#     #-----------------------------------PlayerArmy--------------------------
#     # militia = Fighter (435,295, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia_healthbar = healthBar (militia.rect.centerx-25,militia.rect.centery-55,militia.hp, militia.max_hp)
#     # militia_armorbar = armorBar (militia.rect.centerx-25,militia.rect.centery-50,militia.armor, militia.max_armor)
#     #-----------------------------------------------------------------------
#     boy = Fighter (435,305, 'boy',120,60,35,40,1,3,0,True,False,0,0)
#     boy_healthbar = healthBar (boy.rect.centerx-25,boy.rect.centery-55,boy.hp, boy.max_hp)
#     boy_armorbar = armorBar (boy.rect.centerx-25,boy.rect.centery-50,boy.armor, boy.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht = Fighter (530,250,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht_healthbar = healthBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-55,landsknecht.hp, landsknecht.max_hp)
#     landsknecht_armorbar = armorBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-50,landsknecht.armor, landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht1 = Fighter (620,205,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht1_healthbar = healthBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-55,landsknecht1.hp, landsknecht1.max_hp)
#     landsknecht1_armorbar = armorBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-50,landsknecht1.armor, landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     chevalier = Fighter (720,135,'chevalier',120,100,65,70,1,0,1,True,False,0,0)
#     chevalier_healthbar = healthBar (chevalier.rect.centerx-25,chevalier.rect.centery-65,chevalier.hp, chevalier.max_hp)
#     chevalier_armorbar = armorBar (chevalier.rect.centerx-25,chevalier.rect.centery-60,chevalier.armor, chevalier.max_armor)
#     #-----------------------------------------------------------------------
#     # militia1 = Fighter (700,165, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia1_healthbar = healthBar (militia1.rect.centerx-25,militia1.rect.centery-55,militia1.hp, militia1.max_hp)
#     # militia1_armorbar = armorBar (militia1.rect.centerx-25,militia1.rect.centery-50,militia1.armor, militia1.max_armor)
#     # #-----------------------------------------------------------------------
#     # militia2 = Fighter (790,115, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia2_healthbar = healthBar (militia2.rect.centerx-25,militia2.rect.centery-55,militia2.hp, militia2.max_hp)
#     # militia2_armorbar = armorBar (militia2.rect.centerx-25,militia2.rect.centery-50,militia2.armor, militia2.max_armor)
#     # #-----------------------------------------------------------------------
#     archer = Fighter (530,115, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer_healthbar = healthBar (archer.rect.centerx-25,archer.rect.top-20,archer.hp, archer.max_hp)
#     archer_armorbar = armorBar (archer.rect.centerx-25,archer.rect.top-15,archer.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     archer1 = Fighter (440,160, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer1_healthbar = healthBar (archer1.rect.centerx-25,archer1.rect.top-20,archer1.hp, archer.max_hp)
#     archer1_armorbar = armorBar (archer1.rect.centerx-25,archer1.rect.top-15,archer1.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     yvan = Fighter (350,210, 'yvan',yvan_hp,yvan_armor,yvan_defene,yvan_attack,2,2,0,True,False,0,0)
#     yvan_healthbar = healthBar (yvan.rect.centerx-25,yvan.rect.top-20,yvan.hp, yvan.max_hp)
#     yvan_armorbar = armorBar (yvan.rect.centerx-25,yvan.rect.top-15,yvan.armor, yvan.max_armor)
#     #max_hp,max_armor, defence, strength,
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_player = []
#     #army_player.append(militia)
#     army_player.append(boy)
#     army_player.append(landsknecht)
#     army_player.append(landsknecht1)
#     army_player.append(chevalier)
#     #army_player.append(militia1)
#     #army_player.append(militia2)
#     army_player.append(archer)
#     army_player.append(archer1)
#     army_player.append(yvan)
#
#     army_player_front = army_player[:4]
#
#     #-----------------------------HostileArmy-------------------------------
#     # h_militia = Fighter(570,365,'militia',60,30,35,30,1,0,1,True,True,0,0)
#     # h_militia_healthbar = healthBar(h_militia.rect.centerx-25,h_militia.rect.centery-55,h_militia.hp, h_militia.max_hp)
#     # h_militia_armorbar = armorBar(h_militia.rect.centerx-25,h_militia.rect.centery-50,h_militia.armor, h_militia.max_armor)
#     #-----------------------------------------------------------------------
#     # h_brigand = Fighter(570,365,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand_healthbar = healthBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-55,h_brigand.hp, h_brigand.max_hp)
#     # h_brigand_armorbar = armorBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-50,h_brigand.armor, h_brigand.max_armor)
#     #-----------------------------------------------------------------------
#     h_wolf = Fighter(570,370,'wolf',80,1,0,40,1,3,0,True,True,0,0)
#     h_wolf_healthbar = healthBar(h_wolf.rect.centerx-25,h_wolf.rect.centery-55,h_wolf.hp, h_wolf.max_hp)
#     h_wolf_armorbar = armorBar(h_wolf.rect.centerx-25,h_wolf.rect.centery-50,h_wolf.armor, h_wolf.max_armor)
#     #-----------------------------------------------------------------------
#     # h_brigand1 = Fighter(660,325,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand1_healthbar = healthBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-55,h_brigand1.hp, h_brigand1.max_hp)
#     # h_brigand1_armorbar = armorBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-50,h_brigand1.armor, h_brigand1.max_armor)
#     # #-----------------------------------------------------------------------
#     h_wolf1 = Fighter(660,330,'wolf',80,1,0,40,1,3,0,True,True,0,0)
#     h_wolf1_healthbar = healthBar(h_wolf1.rect.centerx-25,h_wolf1.rect.centery-55,h_wolf1.hp, h_wolf1.max_hp)
#     h_wolf1_armorbar = armorBar(h_wolf1.rect.centerx-25,h_wolf1.rect.centery-50,h_wolf1.armor, h_wolf1.max_armor)
#     #-----------------------------------------------------------------------
#     # h_landsknecht = Fighter (750,280,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     # h_landsknecht_healthbar = healthBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-55,h_landsknecht.hp, h_landsknecht.max_hp)
#     # h_landsknecht_armorbar = armorBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-50,h_landsknecht.armor, h_landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     h_wolf2 = Fighter(750,290,'wolf',80,1,0,40,1,3,0,True,True,0,0)
#     h_wolf2_healthbar = healthBar(h_wolf2.rect.centerx-25,h_wolf2.rect.centery-55,h_wolf2.hp, h_wolf2.max_hp)
#     h_wolf2_armorbar = armorBar(h_wolf2.rect.centerx-25,h_wolf2.rect.centery-50,h_wolf2.armor, h_wolf2.max_armor)
#     #-----------------------------------------------------------------------
#     # h_landsknecht1 = Fighter (840,235,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     # h_landsknecht1_healthbar = healthBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-55,h_landsknecht1.hp, h_landsknecht1.max_hp)
#     # h_landsknecht1_armorbar = armorBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-50,h_landsknecht1.armor, h_landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     h_blackwolf = Fighter(840,245,'blackwolf',120,1,0,60,1,3,0,True,True,0,0)
#     h_blackwolf_healthbar = healthBar(h_blackwolf.rect.centerx-25,h_blackwolf.rect.centery-55,h_blackwolf.hp, h_blackwolf.max_hp)
#     h_blackwolf_armorbar = armorBar(h_blackwolf.rect.centerx-25,h_blackwolf.rect.centery-50,h_blackwolf.armor, h_blackwolf.max_armor)
#     #-----------------------------------------------------------------------
#     # h_brigand2 = Fighter(940,195,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand2_healthbar = healthBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-55,h_brigand2.hp, h_brigand2.max_hp)
#     # h_brigand2_armorbar = armorBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-50,h_brigand2.armor, h_brigand2.max_armor)
#     # #-----------------------------------------------------------------------
#     h_blackwolf1 = Fighter(935,200,'blackwolf',120,1,0,60,1,3,0,True,True,0,0)
#     h_blackwolf1_healthbar = healthBar(h_blackwolf1.rect.centerx-25,h_blackwolf1.rect.centery-55,h_blackwolf1.hp, h_blackwolf1.max_hp)
#     h_blackwolf1_armorbar = armorBar(h_blackwolf1.rect.centerx-25,h_blackwolf1.rect.centery-50,h_blackwolf1.armor, h_blackwolf1.max_armor)
#     #-----------------------------------------------------------------------
#     # h_landsknecht2 = Fighter (790,340,'landsknecht',90,55,40,50,2,0,1,True,True,0,0)
#     # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
#     # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
#     #-----------------------------------------------------------------------
#     # h_bowman = Fighter (790,350, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman_healthbar = healthBar (h_bowman.rect.centerx-25,h_bowman.rect.top-20,h_bowman.hp, h_bowman.max_hp)
#     # h_bowman_armorbar = armorBar (h_bowman.rect.centerx-25,h_bowman.rect.top-15,h_bowman.armor, h_bowman.max_armor)
#     # #-----------------------------------------------------------------------
#     h_blackwolf2 = Fighter(790,350,'blackwolf',120,1,0,60,1,3,0,True,True,0,0)
#     h_blackwolf2_healthbar = healthBar(h_blackwolf2.rect.centerx-25,h_blackwolf2.rect.centery-55,h_blackwolf2.hp, h_blackwolf2.max_hp)
#     h_blackwolf2_armorbar = armorBar(h_blackwolf2.rect.centerx-25,h_blackwolf2.rect.centery-50,h_blackwolf2.armor, h_blackwolf2.max_armor)
#     #-----------------------------------------------------------------------
#     h_blackwolf3 = Fighter(695,405,'blackwolf',120,1,0,60,1,3,0,True,True,0,0)
#     h_blackwolf3_healthbar = healthBar(h_blackwolf3.rect.centerx-25,h_blackwolf3.rect.centery-55,h_blackwolf3.hp, h_blackwolf3.max_hp)
#     h_blackwolf3_armorbar = armorBar(h_blackwolf3.rect.centerx-25,h_blackwolf3.rect.centery-50,h_blackwolf3.armor, h_blackwolf3.max_armor)
#     #-----------------------------------------------------------------------
# #-----------------------------------------------------------------------
#     # h_bowman1 = Fighter (695,400, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman1_healthbar = healthBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-20,h_bowman1.hp, h_bowman1.max_hp)
#     # h_bowman1_armorbar = armorBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-15,h_bowman1.armor, h_bowman1.max_armor)
#     # #-----------------------------------------------------------------------
#     h_wolf3 = Fighter(880,310,'wolf',80,1,0,40,1,3,0,True,True,0,0)
#     h_wolf3_healthbar = healthBar(h_wolf3.rect.centerx-25,h_wolf3.rect.centery-55,h_wolf3.hp, h_wolf3.max_hp)
#     h_wolf3_armorbar = armorBar(h_wolf3.rect.centerx-25,h_wolf3.rect.centery-50,h_wolf3.armor, h_wolf3.max_armor)
#     #-----------------------------------------------------------------------
#     # h_bowman2 = Fighter (880,310, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman2_healthbar = healthBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-20,h_bowman2.hp, h_bowman2.max_hp)
#     # h_bowman2_armorbar = armorBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-15,h_bowman2.armor, h_bowman2.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_bowman3 = Fighter (960,260, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman3_healthbar = healthBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-20,h_bowman3.hp, h_bowman3.max_hp)
#     # h_bowman3_armorbar = armorBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-15,h_bowman3.armor, h_bowman3.max_armor)
#     # # #-----------------------------------------------------------------------
#     h_wolf4 = Fighter(960,270,'wolf',80,1,0,40,1,3,0,True,True,0,0)
#     h_wolf4_healthbar = healthBar(h_wolf4.rect.centerx-25,h_wolf4.rect.centery-55,h_wolf4.hp, h_wolf4.max_hp)
#     h_wolf4_armorbar = armorBar(h_wolf4.rect.centerx-25,h_wolf4.rect.centery-50,h_wolf4.armor, h_wolf4.max_armor)
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_hostiles = []
#     army_hostiles.append(h_wolf)
#     army_hostiles.append(h_wolf1)
#     army_hostiles.append(h_wolf2)
#     army_hostiles.append(h_blackwolf)
#     army_hostiles.append(h_blackwolf1)
#     army_hostiles.append(h_blackwolf2)
#     army_hostiles.append(h_blackwolf3)
#     army_hostiles.append(h_wolf3)
#     army_hostiles.append(h_wolf4)
#
#     army_hostiles_front = army_hostiles
#
#
# #------------------------------TotalUnitNumber----------------------------
#     total_hostiles = len(army_hostiles)
#     total_allies = len(army_player)
#     total_fighters = total_hostiles + total_allies
#
# #------------------------------ItemsUse(Button)---------------------------
#     #inventory_button = button.Button(screen,WINDOW_SIZE[0]*0 + 110, WINDOW_SIZE[1]*0 - 6,inventory_bag,280,120,0, True, 'Inventory')
#
#     inventory_button = button.ToggleButton(screen,-65, 425,inventory_bag,260,120,0, True, 'Inventory')
#     #------------------------------ItemsUse(PotionButton)-------------------
#     potion_button = button.Button(screen, WINDOW_SIZE[0]*0.01, WINDOW_SIZE[1]*0.90, health_potion, 48,72,30, False,f'Health Potion. Restores {health_potion_restores} HP')
#     potion_button1 = button.Button(screen, WINDOW_SIZE[0]*0.06, WINDOW_SIZE[1]*0.90, defence_potion, 48,72,40, False,f'Defence Potion. Gives {defence_potion_adds} DEF/ARM')
#     potion_button2 = button.Button(screen, WINDOW_SIZE[0]*0.11, WINDOW_SIZE[1]*0.90, berserk_potion, 48,72,60, False,f'Berserk Potion. Gives {berserk_potion_adds} ATK / Removes {int(berserk_potion_adds*1)} DEF')
#
#
#     #------------------------------IconToggle(Reset)------------------------
#     restart_button = button.Button(screen, 1100, 8, retry_icon, 84,90,25, True,'Try Again')
#     skip_turn_button = button.Button(screen, WINDOW_SIZE[0]*0.92, WINDOW_SIZE[1]*0.62, skip_turn_img, 86,82,60, False,f'Skip Turn')
#     victory_button = button.Button(screen, 1170, 15, victory_icon, 86,90,25, True,'Back to Map')
#     leave_button = button.Button(screen, 1190, 0, doors_icon, 64,90,25, True,'Leave Battlefield')
#
#
# #-----------------------------------------------------------------------
#
#     while dire_wolves_battle_running:
#         #display.fill((146,244,255))
#         draw_bgBackscreen()
#         #draw_noteMap()  # location map
#         draw_bg()
#         draw_panel()
#         draw_bag()
#
#         #-----------------------------DrawingUnits/AnimatioSpeedMod------------
#         for units in army_player:
#             # militia.update(0.9)
#             # militia.draw()
#             #------------
#             landsknecht.update(1)
#             landsknecht.draw()
#             #------------
#             chevalier.update(1.3)
#             chevalier.draw()
#             #------------
#             # militia1.update(0.88)
#             # militia1.draw()
#             #------------
#             boy.update(0.88)
#             boy.draw()
#             #------------
#             landsknecht1.update(1.1)
#             landsknecht1.draw()
#             #------------
#             # militia2.update(0.84)
#             # militia2.draw()
#             #------------
#             archer.update(0.95)
#             archer.draw()
#             #------------
#             archer1.update(0.92)
#             archer1.draw()
#             #------------
#             yvan.update(1.05)
#             yvan.draw()
#
#         for hostile in army_hostiles:
#             h_wolf.update(0.94)
#             h_wolf.draw()
#             #------------
#             h_wolf1.update(0.92)
#             h_wolf1.draw()
#             #------------
#             h_wolf2.update(0.98)
#             h_wolf2.draw()
#             #------------
#             h_wolf3.update(1.1)
#             h_wolf3.draw()
#             #------------
#             h_wolf4.update(1)
#             h_wolf4.draw()
#             #------------
#             h_blackwolf.update(0.89)
#             h_blackwolf.draw()
#             #------------
#             h_blackwolf1.update(0.92)
#             h_blackwolf1.draw()
#             #------------
#             h_blackwolf2.update(0.86)
#             h_blackwolf2.draw()
#             #------------
#             h_blackwolf3.update(1)
#             h_blackwolf3.draw()
#             #------------
#             # h_brigand.update(0.9)
#             # h_brigand.draw()
#             # #------------
#             # h_brigand2.update(0.85)
#             # h_brigand2.draw()
#             # #------------
#             # h_landsknecht.update(0.95)
#             # h_landsknecht.draw()
#             # #------------
#             # h_landsknecht1.update(0.98)
#             # h_landsknecht1.draw()
#             # #------------
#             # h_brigand1.update(0.9)
#             # h_brigand1.draw()
#             # #------------
#             # h_bowman.update(0.89)
#             # h_bowman.draw()
#             # #------------
#             # h_bowman1.update(0.85)
#             # h_bowman1.draw()
#             # #------------
#             # h_bowman2.update(0.92)
#             # h_bowman2.draw()
#             # #------------
#             # h_bowman3.update(0.90)
#             # h_bowman3.draw()
#         #-----------------------------HealthBar/ArmorBar-----------------------
#         #-------------Player------------------------
#         if show_indicators == True:
#             if chevalier.alive == True:
#                 chevalier_healthbar.draw(chevalier.hp)
#                 chevalier_armorbar.draw(chevalier.armor)
#             # if militia.alive == True:
#             #     militia_healthbar.draw(militia.hp)
#             #     militia_armorbar.draw(militia.armor)
#             if boy.alive == True:
#                 boy_healthbar.draw(boy.hp)
#                 boy_armorbar.draw(boy.armor)
#             if landsknecht.alive == True:
#                 landsknecht_healthbar.draw(landsknecht.hp)
#                 landsknecht_armorbar.draw(landsknecht.armor)
#             # if militia1.alive == True:
#             #     militia1_healthbar.draw(militia1.hp)
#             #     militia1_armorbar.draw(militia1.armor)
#             if landsknecht1.alive == True:
#                 landsknecht1_healthbar.draw(landsknecht1.hp)
#                 landsknecht1_armorbar.draw(landsknecht1.armor)
#             # if militia2.alive == True:
#             #     militia2_healthbar.draw(militia2.hp)
#             #     militia2_armorbar.draw(militia2.armor)
#             if archer.alive == True:
#                 archer_healthbar.draw(archer.hp)
#                 archer_armorbar.draw(archer.armor)
#             if archer1.alive == True:
#                 archer1_healthbar.draw(archer1.hp)
#                 archer1_armorbar.draw(archer1.armor)
#             if yvan.alive == True:
#                 yvan_healthbar.draw(yvan.hp)
#                 yvan_armorbar.draw(yvan.armor)
#
#             #------------------Enemy--------------------
#             if h_wolf.alive == True:
#                 h_wolf_healthbar.draw(h_wolf.hp)
#                 h_wolf_armorbar.draw(h_wolf.armor)
#             if h_wolf1.alive == True:
#                 h_wolf1_healthbar.draw(h_wolf1.hp)
#                 h_wolf1_armorbar.draw(h_wolf1.armor)
#             if h_wolf2.alive == True:
#                 h_wolf2_healthbar.draw(h_wolf2.hp)
#                 h_wolf2_armorbar.draw(h_wolf2.armor)
#             if h_wolf3.alive == True:
#                 h_wolf3_healthbar.draw(h_wolf3.hp)
#                 h_wolf3_armorbar.draw(h_wolf3.armor)
#             if h_wolf4.alive == True:
#                 h_wolf4_healthbar.draw(h_wolf4.hp)
#                 h_wolf4_armorbar.draw(h_wolf4.armor)
#             if h_blackwolf.alive == True:
#                 h_blackwolf_healthbar.draw(h_blackwolf.hp)
#                 h_blackwolf_armorbar.draw(h_blackwolf.armor)
#             if h_blackwolf1.alive == True:
#                 h_blackwolf1_healthbar.draw(h_blackwolf1.hp)
#                 h_blackwolf1_armorbar.draw(h_blackwolf1.armor)
#             if h_blackwolf2.alive == True:
#                 h_blackwolf2_healthbar.draw(h_blackwolf2.hp)
#                 h_blackwolf2_armorbar.draw(h_blackwolf2.armor)
#             if h_blackwolf3.alive == True:
#                 h_blackwolf3_healthbar.draw(h_blackwolf3.hp)
#                 h_blackwolf3_armorbar.draw(h_blackwolf3.armor)
#         #----------------------------------------------------------------------
#
#         #-----------------------------DamageText-----------------------------
#         damage_text_group.update()
#         damage_text_group.draw(screen)
#         #methods update and draw are parts of the sprite.
#
#         #-----------------------------Items/SkipTurn/Inventory-----------------------------
#         pos = pygame.mouse.get_pos()
#         if skip_turn_button.rect.collidepoint(pos):
#             draw_text(f'{skip_turn_button.description}', fontDMG, green, skip_turn_button.rect.x-30,skip_turn_button.rect.y+100)
#         if skip_turn_button.draw():
#             skip_turn=True
#         if battle_status != 2 and leave_button.available == True:
#             if leave_button.rect.collidepoint(pos):
#                 draw_text(f'{leave_button.description}', fontDMG, green, leave_button.rect.x-140,leave_button.rect.y+100)
#             if leave_button.draw():
#                 play_music('Map')
#                 button.wealth = button.start_wealth
#                 dire_wolves_battle_running = False
#
#
#         if inventory_button.rect.collidepoint(pos):
#             draw_text(f'{inventory_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#         if inventory_button.toggled == True and battle_status ==0:
#             potion_button.available = True
#             potion_button1.available = True
#             potion_button2.available = True
#
#
#             #---------------------HealthPotion--------------------------------------
#             if potion_button.available == True:
#                 if potion_button.draw():
#                     use_health_potion = True
#                 draw_text(f'{potion_button.price}', fontBag, (255,225,100), potion_button.rect.x+5, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button.rect.collidepoint(pos):
#                     draw_text(f'{potion_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#             #-------DefencePotion--------------
#             if potion_button1.available == True:
#                 if potion_button1.draw():
#                     use_defence_potion = True
#                 draw_text(f'{potion_button1.price}', fontBag, (255,225,100), potion_button.rect.x+65, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button1.rect.collidepoint(pos):
#                     draw_text(f'{potion_button1.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#                 #-------BerserkPotion--------------
#             if potion_button2.available == True:
#                 if potion_button2.draw():
#                     use_berserk_potion = True
#                 draw_text(f'{potion_button2.price}', fontBag, (255,225,100), potion_button.rect.x+130, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button2.rect.collidepoint(pos):
#                     draw_text(f'{potion_button2.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#
#         #---------------------InventoryStock--------------------------------------
#         else:
#             potion_button.available = False
#
#         #--------------------------------------------------------------------------
#         if battle_status ==0:   #win/loose check
#
#
#             #-----------------------------PlayerAttacking---------------------------
#             for count, ally in enumerate(army_player):
#                 if current_fighter == 1+count:
#                     draw_text('^', fontActive, "#FFA500", ally.rect.centerx-20,ally.rect.y -65)
#                     if ally.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#
#                             if ally.reach == 2:
#                                 if engage == True and target != None:
#                                     # conditioned upon engage below & def attack above
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif ally.reach == 1:
#                                 if engage == True and target != None and target.reach == 1:
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             for enemy in army_hostiles_front:
#                                 if all(enemy.alive == False for enemy in army_hostiles_front):
#                                         #enemy.alive == False:
#                                     if ally.reach == 1:
#                                      if engage == True and target != None and target.reach == 2:
#                                         ally.reach = 2
#                                         ally.attack(target)
#                                         current_fighter += 1
#                                         action_cooldown = 0
#
#
# #-----------------------------------------SkipTurn-----------------------------------------
#                             if skip_turn == True:
#                                 current_fighter += 1
#                                 action_cooldown = 0
#                                 skip_turn_heal = 10
#                                 if ally.max_hp - ally.hp > skip_turn_heal:    #50
#                                     skip_turn_heal = skip_turn_heal
#                                 else:
#                                     skip_turn_heal = ally.max_hp - ally.hp
#                                 ally.hp += skip_turn_heal
#                                 #DamageText
#                                 damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(skip_turn_heal), green)
#                                 damage_text_group.add(damage_text)
#                             skip_turn = False
#
#                             #------------UsingItem(HealthPotion)---------------------------
#                             if use_health_potion == True and button.wealth >= potion_button.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_hp - ally.hp > health_potion_restores:    #50
#                                         heal_amount = health_potion_restores
#                                     else:
#                                         heal_amount = ally.max_hp - ally.hp
#                                     ally.hp += heal_amount
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button.price
#                                     #DamageText
#                                     damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(heal_amount), green)
#                                     damage_text_group.add(damage_text)
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_health_potion = False
#
#                             #----------------------------------------------------
#                             #------------UsingItem(DefencePotion)---------------
#                             if use_defence_potion == True and button.wealth >= potion_button1.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_armor - ally.armor > defence_potion_adds:    #50
#                                         add_defence_amount = defence_potion_adds
#                                     else:
#                                         add_defence_amount = ally.max_armor - ally.armor
#                                     ally.armor += add_defence_amount
#                                     ally.defence = 100
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button1.price     #Change price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_defence_potion = False
#
#
#                             #------------UsingItem(BerserkPotion)---------------
#                             if use_berserk_potion == True and button.wealth >= potion_button2.price:
#                                 if ally.inventory > 0:
#                                     ally.strength += berserk_potion_adds
#                                     if ally.defence < int(berserk_potion_adds):
#                                         ally.defence = 0
#                                     else:
#                                         ally.defence -= int(berserk_potion_adds)
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button2.price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                     #Change price
#                                 use_berserk_potion = False
#
#                     else:
#                         current_fighter +=1   #if dead = skip turn
#
#             #-----------------------------EnemyAttacking----------------------------
#             for count, enemy in enumerate(army_hostiles):
#                 if current_fighter == 1+ total_allies + count:   # "3 + count" - checks with the max_fighter var and number of units in army_player
#                     draw_text('^', fontActive, "#FFA500", enemy.rect.centerx-20,enemy.rect.y -65)
#                     if enemy.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#                             #health_check
#                             if (enemy.hp / enemy.max_hp) <0.5 and enemy.inventory >0:
#                                 if enemy.max_hp - enemy.hp > health_potion_restores:
#                                     heal_amount = health_potion_restores
#                                 else:
#                                     heal_amount = enemy.max_hp - enemy.hp
#
#                                 enemy.hp += heal_amount
#                                 enemy.inventory -= 1
#
#                                 #DamageText
#                                 damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(heal_amount), green)
#                                 damage_text_group.add(damage_text)
#
#                                 current_fighter +=1
#                                 action_cooldown = 0
#
#                             elif enemy.reach == 2:
#                                 if enemy.strength >= ally.hp and ally.alive == True:
#                                    enemy.attack(ally)
#                                    current_fighter += 1
#                                    action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif enemy.reach == 1:
#                                 if all(ally.alive == True for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 elif all(ally.alive == False for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 2]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                             #else:
#                             #     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                             #     # enemy.hp += 10
#                             #     current_fighter += 1
#                             #     action_cooldown = 0
#                             #     # damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(10), green)
#                             #     # damage_text_group.add(damage_text)
#
#                     else:
#                         current_fighter +=1
#
#             #---------------------------------Turns----------------------------
#             # if all have had a turn, reset
#             if current_fighter > total_fighters:
#                 current_fighter = 1
#
#         #-----------------------------DefeatStatus-------------------------
#         # checking alive/dead status
#         alive_allies = 0
#         for ally in army_player:
#             if ally.alive == True:
#                 alive_allies +=1
#         if alive_allies ==0:
#             battle_status =1
#
#         #---------------------------------VictoryStatus--------------------
#         alive_enemies = 0
#         for enemy in army_hostiles:
#             if enemy.alive == True:
#                 alive_enemies +=1
#         if alive_enemies ==0:
#             battle_status =2
#
#         #-------------------Defeat/VictoryStatusDisplay-------------------
#         if battle_status !=0:
#             if battle_status ==1:
#                 draw_text(f'Defeat!', fontMenuLarge, (155,0,0), screen.get_width()*0.46,0)
# #-------------------ResetButton-----------------------------------
#                 if restart_button.available == True:
#                     if restart_button.draw():
#                         play_music('Battle')
#                         for ally in army_player:
#                             ally.reset()
#                         for enemy in army_hostiles:
#                             enemy.reset()
#                         button.wealth = button.start_wealth         #restart gold here
#                         current_fighter = 1
#                         action_cooldown = 0
#                         battle_status = 0
#
#                         pos = pygame.mouse.get_pos() # text over the button
#                     if restart_button.rect.collidepoint(pos):
#                         draw_text(f'{restart_button.description}', fontDMG, green, restart_button.rect.x+30,leave_button.rect.y+100)
#
#             #-------------------Defeat/VictoryStatusDisplay-------------------
#             if battle_status ==2:
#                 button.quest_dire_wolves= 'locked'
#                 draw_text(f'Victory!', fontMenuLarge, green, screen.get_width()*0.46,0)
#                 if play_victory_music == True:
#                       play_music('BattleVictory')
#                 play_victory_music = False
#                 if victory_button.available == True:
#                     if victory_button.draw():
#                         button.wealth += 150
#                         button.start_wealth = button.wealth
#                         button.quest_highwaymen = 'unlocked'
#                         print(button.start_wealth)
#                         print(button.wealth)
#                         play_music('Map')
#                         dire_wolves_battle_running = False
#                     if victory_button.rect.collidepoint(pos):
#                         draw_text(f'{victory_button.description}', fontDMG, green, victory_button.rect.x-75,leave_button.rect.y+100)
#         #------------------------------End/Controls------------------------
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == VIDEORESIZE:
#                 if not fullscreen:
#                     screen = pygame.display.set_mode((event.w,event.h),0,32)
#
#
#             if event.type == KEYDOWN:
#                 if event.key == K_f and show_indicators == True:
#                         show_indicators = False
#                 elif event.key == K_f and show_indicators == False:
#                         show_indicators = True
#
#                 if event.key == K_o:
#                     # fullscreen = not fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     button.fullscreen = not button.fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     fullscreen = button.fullscreen
#
#                     if fullscreen:
#                         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#                     else:
#                         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#             inventory_button.event_handler(event) #ToggleButton
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 clicked = True
#             else:
#                 clicked = False
#
#         if leave_button.clicked == True or victory_button.clicked == True:
#             mouse_map_position_align(750,400)
#         #-----------------------------Action/TargetSearch-------------------
#         engage = False
#         target = None
#
#         inventory_button.draw(screen) #ToggleButton
#
#         pygame.mouse.set_visible(False)
#         pos = pygame.mouse.get_pos()
#         screen.blit(normal_icon,pos)
#
#         for count, ally in enumerate(army_player):
#             if ally.rect.collidepoint(pos) and ally.alive == True:
#                 draw_text(f'{ally.id} | HP: {ally.hp} | ARM: {ally.armor} | ATK: {ally.strength} | DEF: {ally.defence} | INV: {ally.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#         for count, enemy in enumerate(army_hostiles):
#             if enemy.rect.collidepoint(pos) and enemy.alive == True:
#                 pygame.mouse.set_visible(False)
#                 screen.blit(attack_icon,pos)
#                 draw_text(f'{enemy.id} | HP: {enemy.hp} | ARM: {enemy.armor} | ATK: {enemy.strength} | DEF: {enemy.defence} | INV: {enemy.inventory}', font, (100,0,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#
#                 # show attack icon
#                 #--------------chooseTarget&Attack-------------------------
#                 if clicked == True and enemy.alive == True:
#                     engage = True
#                     target = army_hostiles[count]
#
#
#         #-----------------------------------------------------------------------
#         #surf = pygame.transform.scale(display, WINDOW_SIZE)
#         #screen.blit(surf, (0,0))
#
#         pygame.display.update()
#         clock.tick(60)





















































#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def highwaymen_battle ():
#     highwaymen_battle_running = True
#
#     clock = pygame.time.Clock()
#     pygame.init()
#
#     pygame.mixer.set_num_channels(32)
#     pygame.mixer.pre_init(44100,-16,2,512)
#     #-----------------------------GameWindowSettings----------------------
#     pygame.display.set_caption("Highwaymen")
#     WINDOW_SIZE = (1280,720)
#     screen = pygame.display.set_mode((1280,720),0,32)
#     #display = pygame.Surface((600,400))
#
#
#     monitor_size =[pygame.display.Info().current_w, pygame.display.Info().current_h]
#
#     fullscreen = button.fullscreen
#     #not bool(linecache.getline('genericmap.txt',1))
#     if fullscreen:
#         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#     else:
#         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#
#     #-----------------------------------Battlemap,Interface------------------------
#     bg_backscreen = pygame.image.load("BattleScreen/background.png").convert_alpha()
#     bg_backscreen = pygame.transform.scale(bg_backscreen, (int(WINDOW_SIZE[0]*1.00),(int(WINDOW_SIZE[1]*0.75))))
#
#     note_map = pygame.image.load("BattleScreen/note_Faroak0.png").convert_alpha()
#     note_map = pygame.transform.scale(note_map, (int(WINDOW_SIZE[0]*0.21),(int(WINDOW_SIZE[1]*0.28))))
#
#     bg_map = pygame.image.load("BattleScreen/BattleMap0.png").convert_alpha()
#     bg_map = pygame.transform.scale(bg_map, (int(WINDOW_SIZE[0]*0.70),(int(WINDOW_SIZE[1]*0.70))))
#
#     panel = pygame.image.load("BattleScreen/gamepanel0.png").convert_alpha()
#     panel = pygame.transform.scale(panel, (int(WINDOW_SIZE[0]*1.10),(int(WINDOW_SIZE[1]*1.40))))
#
#     bag_of_coins = pygame.image.load("BattleScreen/bag.png").convert_alpha()
#     bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     #-----------------------------------Icons-------------------------------------
#     attack_icon = pygame.image.load("BattleScreen/icon_fight.png").convert_alpha()
#     attack_icon = pygame.transform.scale(attack_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#     normal_icon = pygame.image.load("BattleScreen/cursor_final.png").convert_alpha()
#     normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#
#     skip_turn_img = pygame.image.load("BattleScreen/skip_turn.png").convert_alpha()
#     skip_turn_img = pygame.transform.scale(skip_turn_img, (int(WINDOW_SIZE[0]*0.06),(int(WINDOW_SIZE[1]*0.05))))
#
#     #-----------------------------------Characters---------------------------------
#     # militia_image = pygame.image.load("BattleScreen/militia/idle/idle_0.png").convert_alpha()
#     # landsknecht_image = pygame.image.load("BattleScreen/landsknecht/idle/idle_0.png").convert_alpha()
#
#     #------------------------------------------------------------------------------
#     #--------------------------------Items----------------------------------------
#     inventory_bag = pygame.image.load("BattleScreen/resources/inventorybag.png").convert_alpha()
#     inventory_bag = pygame.transform.scale(inventory_bag, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     health_potion = pygame.image.load("BattleScreen/resources/health_potion.png").convert_alpha()
#     health_potion = pygame.transform.scale(health_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     defence_potion = pygame.image.load("BattleScreen/resources/reflexes_potion.png").convert_alpha()
#     defence_potion = pygame.transform.scale(defence_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     berserk_potion = pygame.image.load("BattleScreen/resources/berserk_potion.png").convert_alpha()
#     berserk_potion = pygame.transform.scale(berserk_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#
#     doors_icon = pygame.image.load("BattleScreen/resources/castledoors.png").convert_alpha()
#     doors_icon = pygame.transform.scale(doors_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     retry_icon = pygame.image.load("BattleScreen/resources/try_again.png").convert_alpha()
#     retry_icon = pygame.transform.scale(retry_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     victory_icon = pygame.image.load("BattleScreen/resources/victory.png").convert_alpha()
#     victory_icon = pygame.transform.scale(victory_icon, (int(WINDOW_SIZE[0]*0.15),(int(WINDOW_SIZE[1]*0.15))))
#
#     #------------------------------------------------------------------------------
#     screen.fill((242,238,203))
#
#     mouse_position = (0, 0)
#     #----------------------------------Music----------------------------------------
#     #open_inventory_bag = pygame.mixer.Sound('sounds/OpenInventory.mp3')
#
#     play_music('Battle')
#
#     #------------------------   -------------------------------------------------------
#     attack_sound = pygame.mixer.Sound('BattleScreen/resources/attack_sound.wav')
#     arrow_sound = pygame.mixer.Sound('BattleScreen/resources/arrow.wav')
#     snarl_sound = pygame.mixer.Sound('BattleScreen/resources/snarl.wav')
#     stone_sound = pygame.mixer.Sound('BattleScreen/resources/throwingstone.wav')
#     #------------------------------------ActionOrder--------------------------------
#     current_fighter = 1
#
#     action_cooldown = 0
#     action_waittime = 100
#     draw_cursor = False
#     battle_status = 0    #0 - nothing, 1 = lost, 2 = won
#
#     # if battle_status ==0:
#     #     play_music('Battle')
#     # if battle_status ==2:
#     #     pygame.mixer.music.play(0)
#     #     play_music('BattleVictory')
#     play_victory_music = True
#     if battle_status ==1:
#         play_music('BattleDefeat')
#
#     #------------------------------------BattleInterface (line 315)-------------------
#     engage = False
#     clicked = False
#     skip_turn = False
#     #total_fighters = 11
#     show_indicators = True
#
#     use_health_potion = False
#     health_potion_restores = 50
#
#     use_defence_potion = False
#     defence_potion_adds = 100
#
#     use_berserk_potion = False
#     berserk_potion_adds = 30
#
#
#     #----------------------------------ShowStats------------------------------------
#     font =pygame.font.SysFont('Times New Roman', 18)
#     fontBag = pygame.font.Font('WorldMap/ESKARGOT.ttf', 38)
#     fontDMG = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
#     fontActive = pygame.font.Font('WorldMap/ESKARGOT.ttf', 80)
#     fontBattle = pygame.font.SysFont('Times New Roman', 70)
#     #pygame.font.Font('WorldMap/ESKARGOT.ttf', 70)
#
#
#     red = (230,16,35)
#     ginger = (245,116,34)
#     green = (0,255,0)
#     paper =  (255,150,100)
#     blue = (0,0,255)
#     lightblue = (240,248,255)
#
#
#
#
#     def draw_text(text,font,text_col,x,y):
#         img = font.render(text,True,text_col)
#         screen.blit(img,(x,y))
#     #--------------------------------------------------------------------------------
#
#     def draw_bgBackscreen ():
#         screen.blit(bg_backscreen,(0,0))
#
#     # def draw_noteMap():
#     #     screen.blit(note_map,(998,12))
#
#     def draw_bg():
#         screen.blit(bg_map,(210,40))
#
#     def draw_bag():
#         screen.blit(bag_of_coins,(0,0))
#         draw_text(f'{button.wealth}', fontBag, (255,225,100), 120, 30)
#
#     #------------------------------DrawingIndicators------------------------
#     def draw_panel():
#         screen.blit(panel,(-50,-35))
#         # for count, i in enumerate(army_player):
#         #       draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#         # for count, i in enumerate(army_hostiles):
#         #     draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (100,0,0), ((panel.get_width())*0.58), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#
#     #-------------------------------------------------------------------------
#     yvan_hp = int(linecache.getline('charstats.txt',1))
#     yvan_armor = int(linecache.getline('charstats.txt',2))
#     yvan_defene = int(linecache.getline('charstats.txt',3))
#     yvan_attack = int(linecache.getline('charstats.txt',4))
#
#     #----------------------------------Charaters------------------------------
#     class Fighter():
#         def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#             self.id=id
#             self.max_hp = max_hp
#             self.hp = max_hp
#             self.max_armor = max_armor
#             self.armor = max_armor
#             self.defence = defence
#             self.start_defence = defence
#             self.strength = strength
#             self.start_strength = strength
#             self.reach = reach
#             self.special = special
#             self.max_inventory = max_inventory
#             self.inventory = max_inventory
#             self.start_resistance = resistance
#             self.resistance = resistance
#             self.start_tricks = tricks
#             self.tricks = tricks
#             self.alive = True
#             self.hostile = True
#             self.animation_list = [] #list of lists (action/img)
#             self.frame_index = 0
#             self.action = 0 #0-idle / 1-attack / 2-hurt / 3-death  updates via self.animation_list = []
#             self.update_time = pygame.time.get_ticks()  # how much time has passed
#
#             #-----------------------------Animations--------------------------------------------
#             #loading idle action images
#             temp_list = []
#             for i in range(2):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/idle/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             #loading attack action images
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/attack/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(1):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/hurt/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/dead/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#
#             #-----------------------------------------------------------------------------------
#             self.animation_list.append(temp_list)
#             self.image = self.animation_list[self.action][self.frame_index]     # to control action/images
#             # two lists (action/frames)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#
#         #---------------------------------------------------------------------
#         def update(self,animation_modifier): #animation
#             animation_cooldown = 100
#             if self.action == 0:
#                 animation_cooldown = 1000*animation_modifier
#             if self.action == 1:
#                 animation_cooldown = 150*animation_modifier
#             if self.action == 2:
#                 animation_cooldown = 300*animation_modifier
#             if self.action == 3:
#                 animation_cooldown = 250*animation_modifier
#
#             #animation_cooldown = cooldown
#             self.image = self.animation_list[self.action][self.frame_index]  #adding action
#             if pygame.time.get_ticks() - self.update_time > animation_cooldown: #if its more than 100 its time to update the animation stage
#                 self.update_time = pygame.time.get_ticks() #resets timer
#                 self.frame_index += 1
#             # if animation run out, reset
#             if self.frame_index >= len(self.animation_list[self.action]):  #adding action
#
#                 #after death unit should stay at the last frame of the dead animation sequence
#                 if self.action == 3:    #dead animation in the list.
#                     self.frame_index = len(self.animation_list[self.action])-1  #final frame
#                 else:
#                     self.idle() # sets to idle animation
#
#         #-----------------------------------Idle----------------------------
#         def idle(self):
#             self.action = 0
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def hurt(self):
#             self.action = 2
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def dead(self):
#             self.action = 3
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def reset(self):
#             self.alive = True
#             self.inventory = self.max_inventory
#             self.hp = self.max_hp
#             self.armor = self.max_armor
#             self.defence = self.start_defence
#             self.strength = self.start_strength
#             self.frame_index = 0
#             self.action = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Attack----------------------------
#         def attack(self,target):
#             rand = random.randint(-5,5)
#             damage = self.strength + rand
#             if self.special == 1:
#                 #target.armor -= 0
#                 target.hp -= damage
#             elif self.special != 1:
#                 target.armor -= int(damage*(target.defence/100))
#                 if target.armor > 0:
#                     target.hp -= int(damage*(1 - target.defence/100))
#                 if target.armor <= 0:
#                     target.hp -= int((damage*(1 - target.defence/100)-target.armor))
#                     target.armor = 0
#
#             # runs hurn animation
#             target.hurt()
#
#             if target.hp < 1:
#                 target.hp = 0
#                 target.alive = False
#                 # runs death animation
#                 target.dead()
#
#
#             #   if self.special != 1:
#             #       damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage-(damage*(target.defence/100)))), red)
#             #   else:
#             #       damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#             #DamageText
#             if self.special != 1:
#                 if target.armor > 1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage*(1 - target.defence/100))), red)
#                 if target.armor <=1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#                     #DamageText(target.rect.centerx,target.rect.y-35,str(int((damage*(1 - target.defence/100)))), red)
#             else:
#                 damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#
#             damage_text_group.add(damage_text)
#             #---------------------------------AttackSounds---------------------------------------
#             #attack sound # 0-standard blade; 1-arrow; 2-stone
#             if self.special == 0:
#                 pygame.mixer.Sound(attack_sound).play()
#             elif self.special == 1:
#                 pygame.mixer.Sound(arrow_sound).play()
#             elif self.special == 2:
#                 pygame.mixer.Sound(stone_sound).play()
#             elif self.special == 3:
#                 pygame.mixer.Sound(snarl_sound).play()
#             #------------------------------------------------------------------------------------
#
#
#             #animations
#             self.action = 1   # set action frames to as 1 as 1 = attack folder animation
#             self.frame_index = 0 # frame 0 in the attack folder animation
#             self.update_time = pygame.time.get_ticks()
#
#         #----------------------------------------------------------------------
#         def draw(self):
#             screen.blit(self.image, self.rect)
#
#     #-----------------------------------HealthBar--------------------------
#     class healthBar ():
#         def __init__(self, x,y, hp, max_hp):
#             self.x = x
#             self.y = y
#             self.hp = hp
#             self.max_hp = max_hp
#         def draw (self, hp):
#             self.hp = hp
#             # health ration
#             ratio = self.hp / self.max_hp
#             pygame.draw.rect(screen,red,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,green,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------ArmorBar--------------------------
#     class armorBar ():
#         def __init__(self, x,y, armor, max_armor):
#             self.x = x
#             self.y = y
#             self.armor = armor
#             self.max_armor = max_armor
#         def draw (self, armor):
#             self.armor = armor
#             # health ration
#             ratio = self.armor / self.max_armor
#             pygame.draw.rect(screen,lightblue,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,blue,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------AttributeChangeBar-----------------
#     class DamageText(pygame.sprite.Sprite):   # sprite is updated automatically
#         def __init__(self,x,y,damage, color):
#             pygame.sprite.Sprite.__init__(self)
#             self.image = fontDMG.render(damage, True, color)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#             self.counter = 0
#
#         def update(self):
#             #move text
#             self.rect.y -=1
#             #delete after timer
#             self.counter +=1
#             if self.counter > 30:
#                 self.kill()
#
#     damage_text_group = pygame.sprite.Group()    #python list
#     #def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#     #-----------------------------------PlayerArmy--------------------------
#     # militia = Fighter (435,295, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia_healthbar = healthBar (militia.rect.centerx-25,militia.rect.centery-55,militia.hp, militia.max_hp)
#     # militia_armorbar = armorBar (militia.rect.centerx-25,militia.rect.centery-50,militia.armor, militia.max_armor)
#     #-----------------------------------------------------------------------
#     boy = Fighter (435,305, 'boy',120,60,35,40,1,3,0,True,False,0,0)
#     boy_healthbar = healthBar (boy.rect.centerx-25,boy.rect.centery-55,boy.hp, boy.max_hp)
#     boy_armorbar = armorBar (boy.rect.centerx-25,boy.rect.centery-50,boy.armor, boy.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht = Fighter (530,250,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht_healthbar = healthBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-55,landsknecht.hp, landsknecht.max_hp)
#     landsknecht_armorbar = armorBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-50,landsknecht.armor, landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht1 = Fighter (620,205,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht1_healthbar = healthBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-55,landsknecht1.hp, landsknecht1.max_hp)
#     landsknecht1_armorbar = armorBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-50,landsknecht1.armor, landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     chevalier = Fighter (720,135,'chevalier',120,100,65,70,1,0,1,True,False,0,0)
#     chevalier_healthbar = healthBar (chevalier.rect.centerx-25,chevalier.rect.centery-65,chevalier.hp, chevalier.max_hp)
#     chevalier_armorbar = armorBar (chevalier.rect.centerx-25,chevalier.rect.centery-60,chevalier.armor, chevalier.max_armor)
#     #-----------------------------------------------------------------------
#     # militia1 = Fighter (700,165, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia1_healthbar = healthBar (militia1.rect.centerx-25,militia1.rect.centery-55,militia1.hp, militia1.max_hp)
#     # militia1_armorbar = armorBar (militia1.rect.centerx-25,militia1.rect.centery-50,militia1.armor, militia1.max_armor)
#     # #-----------------------------------------------------------------------
#     # militia2 = Fighter (790,115, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     # militia2_healthbar = healthBar (militia2.rect.centerx-25,militia2.rect.centery-55,militia2.hp, militia2.max_hp)
#     # militia2_armorbar = armorBar (militia2.rect.centerx-25,militia2.rect.centery-50,militia2.armor, militia2.max_armor)
#     # #-----------------------------------------------------------------------
#     archer = Fighter (530,115, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer_healthbar = healthBar (archer.rect.centerx-25,archer.rect.top-20,archer.hp, archer.max_hp)
#     archer_armorbar = armorBar (archer.rect.centerx-25,archer.rect.top-15,archer.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     archer1 = Fighter (440,160, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer1_healthbar = healthBar (archer1.rect.centerx-25,archer1.rect.top-20,archer1.hp, archer.max_hp)
#     archer1_armorbar = armorBar (archer1.rect.centerx-25,archer1.rect.top-15,archer1.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     yvan = Fighter (350,210, 'yvan',yvan_hp,yvan_armor,yvan_defene,yvan_attack,2,2,0,True,False,0,0)
#     yvan_healthbar = healthBar (yvan.rect.centerx-25,yvan.rect.top-20,yvan.hp, yvan.max_hp)
#     yvan_armorbar = armorBar (yvan.rect.centerx-25,yvan.rect.top-15,yvan.armor, yvan.max_armor)
#     #max_hp,max_armor, defence, strength,
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_player = []
#     #army_player.append(militia)
#     army_player.append(boy)
#     army_player.append(landsknecht)
#     army_player.append(landsknecht1)
#     army_player.append(chevalier)
#     #army_player.append(militia1)
#     #army_player.append(militia2)
#     army_player.append(archer)
#     army_player.append(archer1)
#     army_player.append(yvan)
#
#     army_player_front = army_player[:4]
#
#     #-----------------------------HostileArmy-------------------------------
#     # h_militia = Fighter(570,365,'militia',60,30,35,30,1,0,1,True,True,0,0)
#     # h_militia_healthbar = healthBar(h_militia.rect.centerx-25,h_militia.rect.centery-55,h_militia.hp, h_militia.max_hp)
#     # h_militia_armorbar = armorBar(h_militia.rect.centerx-25,h_militia.rect.centery-50,h_militia.armor, h_militia.max_armor)
#     #-----------------------------------------------------------------------
#     # h_brigand = Fighter(570,365,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand_healthbar = healthBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-55,h_brigand.hp, h_brigand.max_hp)
#     # h_brigand_armorbar = armorBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-50,h_brigand.armor, h_brigand.max_armor)
#     # # #-----------------------------------------------------------------------
#     h_landsknecht2 = Fighter (570,365,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
#     h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
#     #-----------------------------------------------------------------------
#     # h_brigand1 = Fighter(660,325,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand1_healthbar = healthBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-55,h_brigand1.hp, h_brigand1.max_hp)
#     # h_brigand1_armorbar = armorBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-50,h_brigand1.armor, h_brigand1.max_armor)
#     # # # #-----------------------------------------------------------------------
#     h_landsknecht3 = Fighter (660,325,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     h_landsknecht3_healthbar = healthBar (h_landsknecht3.rect.centerx-25,h_landsknecht3.rect.centery-55,h_landsknecht3.hp, h_landsknecht3.max_hp)
#     h_landsknecht3_armorbar = armorBar (h_landsknecht3.rect.centerx-25,h_landsknecht3.rect.centery-50,h_landsknecht3.armor, h_landsknecht3.max_armor)
#     #-----------------------------------------------------------------------
#     h_landsknecht = Fighter (750,280,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     h_landsknecht_healthbar = healthBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-55,h_landsknecht.hp, h_landsknecht.max_hp)
#     h_landsknecht_armorbar = armorBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-50,h_landsknecht.armor, h_landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     h_landsknecht1 = Fighter (840,235,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     h_landsknecht1_healthbar = healthBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-55,h_landsknecht1.hp, h_landsknecht1.max_hp)
#     h_landsknecht1_armorbar = armorBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-50,h_landsknecht1.armor, h_landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     #-----------------------------------------------------------------------
#     # h_brigand2 = Fighter(940,195,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand2_healthbar = healthBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-55,h_brigand2.hp, h_brigand2.max_hp)
#     # h_brigand2_armorbar = armorBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-50,h_brigand2.armor, h_brigand2.max_armor)
#     h_chevalier = Fighter (930,150,'chevalier',120,100,60,65,1,0,1,True,True,0,0)
#     h_chevalier_healthbar = healthBar (h_chevalier.rect.centerx-25,h_chevalier.rect.centery-65,h_chevalier.hp, h_chevalier.max_hp)
#     h_chevalier_armorbar = armorBar (h_chevalier.rect.centerx-25,h_chevalier.rect.centery-60,h_chevalier.armor, h_chevalier.max_armor)
#     #-----------------------------------------------------------------------
#     # h_landsknecht2 = Fighter (790,340,'landsknecht',90,55,40,50,2,0,1,True,True,0,0)
#     # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
#     # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman = Fighter (790,350, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman_healthbar = healthBar (h_bowman.rect.centerx-25,h_bowman.rect.top-20,h_bowman.hp, h_bowman.max_hp)
#     h_bowman_armorbar = armorBar (h_bowman.rect.centerx-25,h_bowman.rect.top-15,h_bowman.armor, h_bowman.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman1 = Fighter (695,400, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman1_healthbar = healthBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-20,h_bowman1.hp, h_bowman1.max_hp)
#     h_bowman1_armorbar = armorBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-15,h_bowman1.armor, h_bowman1.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman2 = Fighter (880,310, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman2_healthbar = healthBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-20,h_bowman2.hp, h_bowman2.max_hp)
#     h_bowman2_armorbar = armorBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-15,h_bowman2.armor, h_bowman2.max_armor)
#     #-----------------------------------------------------------------------
#     h_bowman3 = Fighter (960,260, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     h_bowman3_healthbar = healthBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-20,h_bowman3.hp, h_bowman3.max_hp)
#     h_bowman3_armorbar = armorBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-15,h_bowman3.armor, h_bowman3.max_armor)
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_hostiles = []
#     #army_hostiles.append(h_brigand)
#     #army_hostiles.append(h_brigand1)
#     army_hostiles.append(h_chevalier)
#     army_hostiles.append(h_landsknecht)
#     army_hostiles.append(h_landsknecht1)
#     army_hostiles.append(h_landsknecht2)
#     army_hostiles.append(h_landsknecht3)
#     #army_hostiles.append(h_brigand2)
#     army_hostiles.append(h_bowman)
#     army_hostiles.append(h_bowman1)
#     army_hostiles.append(h_bowman2)
#     army_hostiles.append(h_bowman3)
#
#     army_hostiles_front = army_hostiles[:5]
#
#
#     #------------------------------TotalUnitNumber----------------------------
#     total_hostiles = len(army_hostiles)
#     total_allies = len(army_player)
#     total_fighters = total_hostiles + total_allies
#
#     #------------------------------ItemsUse(Button)---------------------------
#     #inventory_button = button.Button(screen,WINDOW_SIZE[0]*0 + 110, WINDOW_SIZE[1]*0 - 6,inventory_bag,280,120,0, True, 'Inventory')
#
#     inventory_button = button.ToggleButton(screen,-65, 425,inventory_bag,260,120,0, True, 'Inventory')
#     #------------------------------ItemsUse(PotionButton)-------------------
#     potion_button = button.Button(screen, WINDOW_SIZE[0]*0.01, WINDOW_SIZE[1]*0.90, health_potion, 48,72,30, False,f'Health Potion. Restores {health_potion_restores} HP')
#     potion_button1 = button.Button(screen, WINDOW_SIZE[0]*0.06, WINDOW_SIZE[1]*0.90, defence_potion, 48,72,40, False,f'Defence Potion. Gives {defence_potion_adds} DEF/ARM')
#     potion_button2 = button.Button(screen, WINDOW_SIZE[0]*0.11, WINDOW_SIZE[1]*0.90, berserk_potion, 48,72,60, False,f'Berserk Potion. Gives {berserk_potion_adds} ATK / Removes {int(berserk_potion_adds*1)} DEF')
#
#
#     #------------------------------IconToggle(Reset)------------------------
#     restart_button = button.Button(screen, 1100, 8, retry_icon, 84,90,25, True,'Try Again')
#     skip_turn_button = button.Button(screen, WINDOW_SIZE[0]*0.92, WINDOW_SIZE[1]*0.62, skip_turn_img, 86,82,60, False,f'Skip Turn')
#     victory_button = button.Button(screen, 1170, 15, victory_icon, 86,90,25, True,'Back to Map')
#     leave_button = button.Button(screen, 1190, 0, doors_icon, 64,90,25, True,'Leave Battlefield')
#
#
#     #-----------------------------------------------------------------------
#
#     while highwaymen_battle_running:
#         #display.fill((146,244,255))
#         draw_bgBackscreen()
#         #draw_noteMap()  # location map
#         draw_bg()
#         draw_panel()
#         draw_bag()
#
#         #-----------------------------DrawingUnits/AnimatioSpeedMod------------
#         for units in army_player:
#             # militia.update(0.9)
#             # militia.draw()
#             #------------
#             landsknecht.update(1)
#             landsknecht.draw()
#             #------------
#             chevalier.update(1.3)
#             chevalier.draw()
#             #------------
#             # militia1.update(0.88)
#             # militia1.draw()
#             #------------
#             boy.update(0.88)
#             boy.draw()
#             #------------
#             landsknecht1.update(1.1)
#             landsknecht1.draw()
#             #------------
#             # militia2.update(0.84)
#             # militia2.draw()
#             #------------
#             archer.update(0.95)
#             archer.draw()
#             #------------
#             archer1.update(0.92)
#             archer1.draw()
#             #------------
#             yvan.update(1.05)
#             yvan.draw()
#
#         for hostile in army_hostiles:
#             # h_brigand.update(0.9)
#             # h_brigand.draw()
#             # #------------
#             # h_brigand2.update(0.85)
#             # h_brigand2.draw()
#             #------------
#             h_landsknecht.update(0.95)
#             h_landsknecht.draw()
#             #------------
#             h_landsknecht1.update(0.98)
#             h_landsknecht1.draw()
#             #------------
#             h_landsknecht2.update(0.94)
#             h_landsknecht2.draw()
#             #------------
#             h_landsknecht3.update(0.92)
#             h_landsknecht3.draw()
#             #------------
#             h_chevalier.update(1.25)
#             h_chevalier.draw()
#             #------------
#             # h_brigand1.update(0.9)
#             # h_brigand1.draw()
#             #------------
#             h_bowman.update(0.89)
#             h_bowman.draw()
#             #------------
#             h_bowman1.update(0.85)
#             h_bowman1.draw()
#             #------------
#             h_bowman2.update(0.92)
#             h_bowman2.draw()
#             #------------
#             h_bowman3.update(0.90)
#             h_bowman3.draw()
#         #-----------------------------HealthBar/ArmorBar-----------------------
#         #-------------Player------------------------
#         if show_indicators == True:
#             if chevalier.alive == True:
#                 chevalier_healthbar.draw(chevalier.hp)
#                 chevalier_armorbar.draw(chevalier.armor)
#             # if militia.alive == True:
#             #     militia_healthbar.draw(militia.hp)
#             #     militia_armorbar.draw(militia.armor)
#             if boy.alive == True:
#                 boy_healthbar.draw(boy.hp)
#                 boy_armorbar.draw(boy.armor)
#             if landsknecht.alive == True:
#                 landsknecht_healthbar.draw(landsknecht.hp)
#                 landsknecht_armorbar.draw(landsknecht.armor)
#             # if militia1.alive == True:
#             #     militia1_healthbar.draw(militia1.hp)
#             #     militia1_armorbar.draw(militia1.armor)
#             if landsknecht1.alive == True:
#                 landsknecht1_healthbar.draw(landsknecht1.hp)
#                 landsknecht1_armorbar.draw(landsknecht1.armor)
#             # if militia2.alive == True:
#             #     militia2_healthbar.draw(militia2.hp)
#             #     militia2_armorbar.draw(militia2.armor)
#             if archer.alive == True:
#                 archer_healthbar.draw(archer.hp)
#                 archer_armorbar.draw(archer.armor)
#             if archer1.alive == True:
#                 archer1_healthbar.draw(archer1.hp)
#                 archer1_armorbar.draw(archer1.armor)
#             if yvan.alive == True:
#                 yvan_healthbar.draw(yvan.hp)
#                 yvan_armorbar.draw(yvan.armor)
#
#             #------------------Enemy--------------------
#             if h_chevalier.alive == True:
#                 h_chevalier_healthbar.draw(h_chevalier.hp)
#                 h_chevalier_armorbar.draw(h_chevalier.armor)
#             # if h_brigand.alive == True:
#             #     h_brigand_healthbar.draw(h_brigand.hp)
#             #     h_brigand_armorbar.draw(h_brigand.armor)
#             # if h_brigand2.alive == True:
#             #     h_brigand2_healthbar.draw(h_brigand2.hp)
#             #     h_brigand2_armorbar.draw(h_brigand2.armor)
#             if h_landsknecht.alive == True:
#                 h_landsknecht_healthbar.draw(h_landsknecht.hp)
#                 h_landsknecht_armorbar.draw(h_landsknecht.armor)
#             if h_landsknecht1.alive == True:
#                 h_landsknecht1_healthbar.draw(h_landsknecht1.hp)
#                 h_landsknecht1_armorbar.draw(h_landsknecht1.armor)
#             if h_landsknecht2.alive == True:
#                 h_landsknecht2_healthbar.draw(h_landsknecht2.hp)
#                 h_landsknecht2_armorbar.draw(h_landsknecht2.armor)
#             if h_landsknecht3.alive == True:
#                 h_landsknecht3_healthbar.draw(h_landsknecht3.hp)
#                 h_landsknecht3_armorbar.draw(h_landsknecht3.armor)
#             # if h_brigand1.alive == True:
#             #     h_brigand1_healthbar.draw(h_brigand1.hp)
#             #     h_brigand1_armorbar.draw(h_brigand1.armor)
#             if h_bowman.alive == True:
#                 h_bowman_healthbar.draw(h_bowman.hp)
#                 h_bowman_armorbar.draw(h_bowman.armor)
#             if h_bowman1.alive == True:
#                 h_bowman1_healthbar.draw(h_bowman1.hp)
#                 h_bowman1_armorbar.draw(h_bowman1.armor)
#             if h_bowman2.alive == True:
#                 h_bowman2_healthbar.draw(h_bowman2.hp)
#                 h_bowman2_armorbar.draw(h_bowman2.armor)
#             if h_bowman3.alive == True:
#                 h_bowman3_healthbar.draw(h_bowman3.hp)
#                 h_bowman3_armorbar.draw(h_bowman3.armor)
#         #----------------------------------------------------------------------
#
#         #-----------------------------DamageText-----------------------------
#         damage_text_group.update()
#         damage_text_group.draw(screen)
#         #methods update and draw are parts of the sprite.
#
#         #-----------------------------Items/SkipTurn/Inventory-----------------------------
#         pos = pygame.mouse.get_pos()
#         if skip_turn_button.rect.collidepoint(pos):
#             draw_text(f'{skip_turn_button.description}', fontDMG, green, skip_turn_button.rect.x-30,skip_turn_button.rect.y+100)
#         if skip_turn_button.draw():
#             skip_turn=True
#         if battle_status != 2 and leave_button.available == True:
#             if leave_button.rect.collidepoint(pos):
#                 draw_text(f'{leave_button.description}', fontDMG, green, leave_button.rect.x-140,leave_button.rect.y+100)
#             if leave_button.draw():
#                 play_music('Map')
#                 button.wealth = button.start_wealth
#                 highwaymen_battle_running = False
#
#
#         if inventory_button.rect.collidepoint(pos):
#             draw_text(f'{inventory_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#         if inventory_button.toggled == True and battle_status ==0:
#             potion_button.available = True
#             potion_button1.available = True
#             potion_button2.available = True
#
#
#             #---------------------HealthPotion--------------------------------------
#             if potion_button.available == True:
#                 if potion_button.draw():
#                     use_health_potion = True
#                 draw_text(f'{potion_button.price}', fontBag, (255,225,100), potion_button.rect.x+5, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button.rect.collidepoint(pos):
#                     draw_text(f'{potion_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#             #-------DefencePotion--------------
#             if potion_button1.available == True:
#                 if potion_button1.draw():
#                     use_defence_potion = True
#                 draw_text(f'{potion_button1.price}', fontBag, (255,225,100), potion_button.rect.x+65, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button1.rect.collidepoint(pos):
#                     draw_text(f'{potion_button1.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#                 #-------BerserkPotion--------------
#             if potion_button2.available == True:
#                 if potion_button2.draw():
#                     use_berserk_potion = True
#                 draw_text(f'{potion_button2.price}', fontBag, (255,225,100), potion_button.rect.x+130, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button2.rect.collidepoint(pos):
#                     draw_text(f'{potion_button2.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#
#         #---------------------InventoryStock--------------------------------------
#         else:
#             potion_button.available = False
#
#         #--------------------------------------------------------------------------
#         if battle_status ==0:   #win/loose check
#
#
#             #-----------------------------PlayerAttacking---------------------------
#             for count, ally in enumerate(army_player):
#                 if current_fighter == 1+count:
#                     draw_text('^', fontActive, "#FFA500", ally.rect.centerx-20,ally.rect.y -65)
#                     if ally.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#
#                             if ally.reach == 2:
#                                 if engage == True and target != None:
#                                     # conditioned upon engage below & def attack above
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif ally.reach == 1:
#                                 if engage == True and target != None and target.reach == 1:
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             for enemy in army_hostiles_front:
#                                 if all(enemy.alive == False for enemy in army_hostiles_front):
#                                     #enemy.alive == False:
#                                     if ally.reach == 1:
#                                         if engage == True and target != None and target.reach == 2:
#                                             ally.reach = 2
#                                             ally.attack(target)
#                                             current_fighter += 1
#                                             action_cooldown = 0
#
#
#                             #-----------------------------------------SkipTurn-----------------------------------------
#                             if skip_turn == True:
#                                 current_fighter += 1
#                                 action_cooldown = 0
#                                 skip_turn_heal = 10
#                                 if ally.max_hp - ally.hp > skip_turn_heal:    #50
#                                     skip_turn_heal = skip_turn_heal
#                                 else:
#                                     skip_turn_heal = ally.max_hp - ally.hp
#                                 ally.hp += skip_turn_heal
#                                 #DamageText
#                                 damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(skip_turn_heal), green)
#                                 damage_text_group.add(damage_text)
#                             skip_turn = False
#
#                             #------------UsingItem(HealthPotion)---------------------------
#                             if use_health_potion == True and button.wealth >= potion_button.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_hp - ally.hp > health_potion_restores:    #50
#                                         heal_amount = health_potion_restores
#                                     else:
#                                         heal_amount = ally.max_hp - ally.hp
#                                     ally.hp += heal_amount
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button.price
#                                     #DamageText
#                                     damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(heal_amount), green)
#                                     damage_text_group.add(damage_text)
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_health_potion = False
#
#                             #----------------------------------------------------
#                             #------------UsingItem(DefencePotion)---------------
#                             if use_defence_potion == True and button.wealth >= potion_button1.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_armor - ally.armor > defence_potion_adds:    #50
#                                         add_defence_amount = defence_potion_adds
#                                     else:
#                                         add_defence_amount = ally.max_armor - ally.armor
#                                     ally.armor += add_defence_amount
#                                     ally.defence = 100
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button1.price     #Change price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_defence_potion = False
#
#
#                             #------------UsingItem(BerserkPotion)---------------
#                             if use_berserk_potion == True and button.wealth >= potion_button2.price:
#                                 if ally.inventory > 0:
#                                     ally.strength += berserk_potion_adds
#                                     if ally.defence < int(berserk_potion_adds):
#                                         ally.defence = 0
#                                     else:
#                                         ally.defence -= int(berserk_potion_adds)
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button2.price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                     #Change price
#                                 use_berserk_potion = False
#
#                     else:
#                         current_fighter +=1   #if dead = skip turn
#
#             #-----------------------------EnemyAttacking----------------------------
#             for count, enemy in enumerate(army_hostiles):
#                 if current_fighter == 1+ total_allies + count:   # "3 + count" - checks with the max_fighter var and number of units in army_player
#                     draw_text('^', fontActive, "#FFA500", enemy.rect.centerx-20,enemy.rect.y -65)
#                     if enemy.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#                             #------------------------------EnemyDefencePotion------------------
#                             if (enemy.armor / enemy.max_armor) <0.2 and enemy.armor < defence_potion_adds and enemy.max_armor > health_potion_restores and enemy.inventory >0:
#                                 if enemy.max_armor - enemy.armor > defence_potion_adds:
#                                     add_defence_amount = defence_potion_adds
#                                 else:
#                                     add_defence_amount = enemy.max_armor - enemy.armor
#                                 enemy.armor += add_defence_amount
#                                 enemy.defence = 100
#                                 enemy.inventory -= 1
#                                 current_fighter +=1
#                                 action_cooldown = 0
#
#
#                             #------------------------------EnemyHealthPotion------------------
#                             elif (enemy.hp / enemy.max_hp) <0.5 and enemy.inventory >0:
#                                 if enemy.max_hp - enemy.hp > health_potion_restores:
#                                     heal_amount = health_potion_restores
#                                 else:
#                                     heal_amount = enemy.max_hp - enemy.hp
#
#                                 enemy.hp += heal_amount
#                                 enemy.inventory -= 1
#
#                                 #DamageText
#                                 damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(heal_amount), green)
#                                 damage_text_group.add(damage_text)
#
#                                 current_fighter +=1
#                                 action_cooldown = 0
#
#                             #-------------------------------------------------------------------
#                             elif enemy.reach == 2:
#                                 if enemy.strength >= ally.hp and ally.alive == True:
#                                     enemy.attack(ally)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif enemy.reach == 1:
#                                 if all(ally.alive == True for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 elif all(ally.alive == False for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 2]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                             #else:
#                             #     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                             #     # enemy.hp += 10
#                             #     current_fighter += 1
#                             #     action_cooldown = 0
#                             #     # damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(10), green)
#                             #     # damage_text_group.add(damage_text)
#
#                     else:
#                         current_fighter +=1
#
#             #---------------------------------Turns----------------------------
#             # if all have had a turn, reset
#             if current_fighter > total_fighters:
#                 current_fighter = 1
#
#         #-----------------------------DefeatStatus-------------------------
#         # checking alive/dead status
#         alive_allies = 0
#         for ally in army_player:
#             if ally.alive == True:
#                 alive_allies +=1
#         if alive_allies ==0:
#             battle_status =1
#
#         #---------------------------------VictoryStatus--------------------
#         alive_enemies = 0
#         for enemy in army_hostiles:
#             if enemy.alive == True:
#                 alive_enemies +=1
#         if alive_enemies ==0:
#             battle_status =2
#
#         #-------------------Defeat/VictoryStatusDisplay-------------------
#         if battle_status !=0:
#             if battle_status ==1:
#                 draw_text(f'Defeat!', fontMenuLarge, (155,0,0), screen.get_width()*0.46,0)
#                 #-------------------ResetButton-----------------------------------
#                 if restart_button.available == True:
#                     if restart_button.draw():
#                         play_music('Battle')
#                         for ally in army_player:
#                             ally.reset()
#                         for enemy in army_hostiles:
#                             enemy.reset()
#                         button.wealth = button.start_wealth         #restart gold here
#                         current_fighter = 1
#                         action_cooldown = 0
#                         battle_status = 0
#
#                         pos = pygame.mouse.get_pos() # text over the button
#                     if restart_button.rect.collidepoint(pos):
#                         draw_text(f'{restart_button.description}', fontDMG, green, restart_button.rect.x+30,leave_button.rect.y+100)
#
#             #-------------------Defeat/VictoryStatusDisplay-------------------
#             if battle_status ==2:
#                 button.quest_highwaymen = 'locked'
#                 draw_text(f'Victory!', fontMenuLarge, green, screen.get_width()*0.46,0)
#                 if play_victory_music == True:
#                    play_music('BattleVictory')
#                 play_victory_music = False
#                 if victory_button.available == True:
#                     if victory_button.draw():
#                         button.wealth += 400
#                         button.start_wealth = button.wealth
#                         button.quest_dragonhunt = 'unlocked'
#                         print(button.start_wealth)
#                         print(button.wealth)
#                         play_music('Map')
#                         highwaymen_battle_running = False
#                     if victory_button.rect.collidepoint(pos):
#                         draw_text(f'{victory_button.description}', fontDMG, green, victory_button.rect.x-75,leave_button.rect.y+100)
#         #------------------------------End/Controls------------------------
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == VIDEORESIZE:
#                 if not fullscreen:
#                     screen = pygame.display.set_mode((event.w,event.h),0,32)
#
#             if event.type == KEYDOWN:
#                 if event.key == K_f and show_indicators == True:
#                     show_indicators = False
#                 elif event.key == K_f and show_indicators == False:
#                     show_indicators = True
#
#                 if event.key == K_o:
#                     # fullscreen = not fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     button.fullscreen = not button.fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     fullscreen = button.fullscreen
#
#                     if fullscreen:
#                         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#                     else:
#                         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#             #---------------------ToggleButton------------------------
#             inventory_button.event_handler(event) #ToggleButton
#             #---------------------ToggleButton------------------------
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 clicked = True
#             else:
#                 clicked = False
#
#         if leave_button.clicked == True or victory_button.clicked == True:
#             mouse_map_position_align(750,400)
#         #-----------------------------Action/TargetSearch-------------------
#         engage = False
#         target = None
#
#         inventory_button.draw(screen) #ToggleButton
#
#         pygame.mouse.set_visible(False)
#         pos = pygame.mouse.get_pos()
#         screen.blit(normal_icon,pos)
#
#         for count, ally in enumerate(army_player):
#             if ally.rect.collidepoint(pos) and ally.alive == True:
#                 draw_text(f'{ally.id} | HP: {ally.hp} | ARM: {ally.armor} | ATK: {ally.strength} | DEF: {ally.defence} | INV: {ally.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#         for count, enemy in enumerate(army_hostiles):
#             if enemy.rect.collidepoint(pos) and enemy.alive == True:
#                 pygame.mouse.set_visible(False)
#                 screen.blit(attack_icon,pos)
#                 draw_text(f'{enemy.id} | HP: {enemy.hp} | ARM: {enemy.armor} | ATK: {enemy.strength} | DEF: {enemy.defence} | INV: {enemy.inventory}', font, (100,0,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#
#                 # show attack icon
#                 #--------------chooseTarget&Attack-------------------------
#                 if clicked == True and enemy.alive == True:
#                     engage = True
#                     target = army_hostiles[count]
#
#
#         #-----------------------------------------------------------------------
#         #surf = pygame.transform.scale(display, WINDOW_SIZE)
#         #screen.blit(surf, (0,0))
#
#         pygame.display.update()
#         clock.tick(60)
#
#


















# def dragonhunt_battle ():
#     dragonhunt_battle_running = True
#
#     clock = pygame.time.Clock()
#     pygame.init()
#
#     pygame.mixer.set_num_channels(32)
#     pygame.mixer.pre_init(44100,-16,2,512)
#     #-----------------------------GameWindowSettings----------------------
#     pygame.display.set_caption("Dragonhunt")
#     WINDOW_SIZE = (1280,720)
#     screen = pygame.display.set_mode((1280,720),0,32)
#     #display = pygame.Surface((600,400))
#
#
#     monitor_size =[pygame.display.Info().current_w, pygame.display.Info().current_h]
#
#     fullscreen = button.fullscreen
#     #not bool(linecache.getline('genericmap.txt',1))
#     if fullscreen:
#         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#     else:
#         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#
#     #-----------------------------------Battlemap,Interface------------------------
#     bg_backscreen = pygame.image.load("BattleScreen/background.png").convert_alpha()
#     bg_backscreen = pygame.transform.scale(bg_backscreen, (int(WINDOW_SIZE[0]*1.00),(int(WINDOW_SIZE[1]*0.75))))
#
#     # note_map = pygame.image.load("BattleScreen/note_Faroak0.png").convert_alpha()
#     # note_map = pygame.transform.scale(note_map, (int(WINDOW_SIZE[0]*0.21),(int(WINDOW_SIZE[1]*0.28))))
#
#     bg_map = pygame.image.load("BattleScreen/ExtendedBattleMap.png").convert_alpha()
#     bg_map = pygame.transform.scale(bg_map, (int(WINDOW_SIZE[0]*0.70),(int(WINDOW_SIZE[1]*0.70))))
#
#     panel = pygame.image.load("BattleScreen/gamepanel0.png").convert_alpha()
#     panel = pygame.transform.scale(panel, (int(WINDOW_SIZE[0]*1.10),(int(WINDOW_SIZE[1]*1.40))))
#
#     bag_of_coins = pygame.image.load("BattleScreen/bag.png").convert_alpha()
#     bag_of_coins = pygame.transform.scale(bag_of_coins, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     #-----------------------------------Icons-------------------------------------
#     attack_icon = pygame.image.load("BattleScreen/icon_fight.png").convert_alpha()
#     attack_icon = pygame.transform.scale(attack_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#     normal_icon = pygame.image.load("BattleScreen/cursor_final.png").convert_alpha()
#     normal_icon = pygame.transform.scale(normal_icon, (int(WINDOW_SIZE[0]*0.04),(int(WINDOW_SIZE[1]*0.05))))
#
#
#     skip_turn_img = pygame.image.load("BattleScreen/skip_turn.png").convert_alpha()
#     skip_turn_img = pygame.transform.scale(skip_turn_img, (int(WINDOW_SIZE[0]*0.06),(int(WINDOW_SIZE[1]*0.05))))
#
#     #-----------------------------------Characters---------------------------------
#     # militia_image = pygame.image.load("BattleScreen/militia/idle/idle_0.png").convert_alpha()
#     # landsknecht_image = pygame.image.load("BattleScreen/landsknecht/idle/idle_0.png").convert_alpha()
#
#     #------------------------------------------------------------------------------
#     #--------------------------------Items----------------------------------------
#     inventory_bag = pygame.image.load("BattleScreen/resources/inventorybag.png").convert_alpha()
#     inventory_bag = pygame.transform.scale(inventory_bag, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     health_potion = pygame.image.load("BattleScreen/resources/health_potion.png").convert_alpha()
#     health_potion = pygame.transform.scale(health_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     defence_potion = pygame.image.load("BattleScreen/resources/reflexes_potion.png").convert_alpha()
#     defence_potion = pygame.transform.scale(defence_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     berserk_potion = pygame.image.load("BattleScreen/resources/berserk_potion.png").convert_alpha()
#     berserk_potion = pygame.transform.scale(berserk_potion, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#
#     doors_icon = pygame.image.load("BattleScreen/resources/castledoors.png").convert_alpha()
#     doors_icon = pygame.transform.scale(doors_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     retry_icon = pygame.image.load("BattleScreen/resources/try_again.png").convert_alpha()
#     retry_icon = pygame.transform.scale(retry_icon, (int(WINDOW_SIZE[0]*0.10),(int(WINDOW_SIZE[1]*0.15))))
#
#     victory_icon = pygame.image.load("BattleScreen/resources/victory.png").convert_alpha()
#     victory_icon = pygame.transform.scale(victory_icon, (int(WINDOW_SIZE[0]*0.15),(int(WINDOW_SIZE[1]*0.15))))
#
#     #------------------------------------------------------------------------------
#     screen.fill((242,238,203))
#
#     mouse_position = (0, 0)
#     #----------------------------------Music----------------------------------------
#     #open_inventory_bag = pygame.mixer.Sound('sounds/OpenInventory.mp3')
#
#     play_music('Battle1')
#
#     #------------------------   -------------------------------------------------------
#     attack_sound = pygame.mixer.Sound('BattleScreen/resources/attack_sound.wav')
#     arrow_sound = pygame.mixer.Sound('BattleScreen/resources/arrow.wav')
#     snarl_sound = pygame.mixer.Sound('BattleScreen/resources/snarl.wav')
#     stone_sound = pygame.mixer.Sound('BattleScreen/resources/throwingstone.wav')
#     flame_sound = pygame.mixer.Sound('BattleScreen/resources/flame.wav')
#     #------------------------------------ActionOrder--------------------------------
#     current_fighter = 1
#
#     action_cooldown = 0
#     action_waittime = 100
#     draw_cursor = False
#     battle_status = 0    #0 - nothing, 1 = lost, 2 = won
#
#     # if battle_status ==0:
#     #     play_music('Battle')
#     # if battle_status ==2:
#     #     pygame.mixer.music.play(0)
#     #     play_music('BattleVictory')
#     play_victory_music = True
#     if battle_status ==1:
#         play_music('BattleDefeat')
#
#     #------------------------------------BattleInterface (line 315)-------------------
#     engage = False
#     clicked = False
#     skip_turn = False
#     #total_fighters = 11
#     show_indicators = True
#
#     use_health_potion = False
#     health_potion_restores = 50
#
#     use_defence_potion = False
#     defence_potion_adds = 100
#
#     use_berserk_potion = False
#     berserk_potion_adds = 30
#
#
#     #----------------------------------ShowStats------------------------------------
#     font =pygame.font.SysFont('Times New Roman', 18)
#     fontBag = pygame.font.Font('WorldMap/ESKARGOT.ttf', 38)
#     fontDMG = pygame.font.Font('WorldMap/ESKARGOT.ttf', 26)
#     fontActive = pygame.font.Font('WorldMap/ESKARGOT.ttf', 80)
#     fontBattle = pygame.font.SysFont('Times New Roman', 70)
#     #pygame.font.Font('WorldMap/ESKARGOT.ttf', 70)
#
#
#     red = (230,16,35)
#     ginger = (245,116,34)
#     green = (0,255,0)
#     paper =  (255,150,100)
#     blue = (0,0,255)
#     lightblue = (240,248,255)
#
#
#
#
#     def draw_text(text,font,text_col,x,y):
#         img = font.render(text,True,text_col)
#         screen.blit(img,(x,y))
#     #--------------------------------------------------------------------------------
#
#     def draw_bgBackscreen ():
#         screen.blit(bg_backscreen,(0,0))
#
#     # def draw_noteMap():
#     #     screen.blit(note_map,(998,12))
#
#     def draw_bg():
#         screen.blit(bg_map,(210,40))
#
#     def draw_bag():
#         screen.blit(bag_of_coins,(0,0))
#         draw_text(f'{button.wealth}', fontBag, (255,225,100), 120, 30)
#
#     #------------------------------DrawingIndicators------------------------
#     def draw_panel():
#         screen.blit(panel,(-50,-35))
#         # for count, i in enumerate(army_player):
#         #       draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#         # for count, i in enumerate(army_hostiles):
#         #     draw_text(f'{i.id} | HP: {i.hp} | ARM: {i.armor} | ATK: {i.strength} | DEF: {i.defence} | INV: {i.inventory}', font, (100,0,0), ((panel.get_width())*0.58), (((screen.get_height() + bg_map.get_height())/2.24)+(count*16)))
#
#     def countX(lst, x):
#         return lst.count(x)
#
#     #-------------------------------------------------------------------------
#     yvan_hp = int(linecache.getline('charstats.txt',1))
#     yvan_armor = int(linecache.getline('charstats.txt',2))
#     yvan_defene = int(linecache.getline('charstats.txt',3))
#     yvan_attack = int(linecache.getline('charstats.txt',4))
#
#     #----------------------------------Charaters------------------------------
#     class Fighter():
#         def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#             self.id=id
#             self.max_hp = max_hp
#             self.hp = max_hp
#             self.max_armor = max_armor
#             self.armor = max_armor
#             self.defence = defence
#             self.start_defence = defence
#             self.strength = strength
#             self.start_strength = strength
#             self.reach = reach
#             self.special = special
#             self.max_inventory = max_inventory
#             self.inventory = max_inventory
#             self.start_resistance = resistance
#             self.resistance = resistance
#             self.start_tricks = tricks
#             self.tricks = tricks
#             self.alive = True
#             self.hostile = True
#             self.animation_list = [] #list of lists (action/img)
#             self.frame_index = 0
#             self.action = 0 #0-idle / 1-attack / 2-hurt / 3-death  updates via self.animation_list = []
#             self.update_time = pygame.time.get_ticks()  # how much time has passed
#
#             #-----------------------------Animations--------------------------------------------
#             #loading idle action images
#             temp_list = []
#             for i in range(2):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/idle/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 if self.id == 'caerbannog':
#                     img = pygame.transform.scale(img,(img.get_width(), img.get_height()))
#                 else:
#                     img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             #loading attack action images
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/attack/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 if self.id == 'caerbannog':
#                     img = pygame.transform.scale(img,(img.get_width(), img.get_height()))
#                 else:
#                     img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(1):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/hurt/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 if self.id == 'caerbannog':
#                     img = pygame.transform.scale(img,(img.get_width(), img.get_height()))
#                 else:
#                     img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#
#             temp_list = []
#             for i in range(3):
#                 img = pygame.image.load(f'BattleScreen/units/{self.id}/dead/{i}.png')
#                 img = pygame.transform.flip(img, hostile, False)
#                 if self.id == 'caerbannog':
#                     img = pygame.transform.scale(img,(img.get_width(), img.get_height()))
#                 else:
#                     img = pygame.transform.scale(img,(img.get_width()*2, img.get_height()*2))
#                 temp_list.append(img) #appends temp list to store img
#             self.animation_list.append(temp_list)
#             #-----------------------------------------------------------------------------------
#
#             self.image = self.animation_list[self.action][self.frame_index]     # to control action/images
#             # two lists (action/frames)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#
#         #---------------------------------------------------------------------
#         def update(self,animation_modifier): #animation
#             animation_cooldown = 100
#             if self.action == 0:
#                 animation_cooldown = 1000*animation_modifier
#             if self.action == 1:
#                 animation_cooldown = 150*animation_modifier
#             if self.action == 2:
#                 animation_cooldown = 300*animation_modifier
#             if self.action == 3:
#                 animation_cooldown = 250*animation_modifier
#
#             #animation_cooldown = cooldown
#             self.image = self.animation_list[self.action][self.frame_index]  #adding action
#             if pygame.time.get_ticks() - self.update_time > animation_cooldown: #if its more than 100 its time to update the animation stage
#                 self.update_time = pygame.time.get_ticks() #resets timer
#                 self.frame_index += 1
#             # if animation run out, reset
#             if self.frame_index >= len(self.animation_list[self.action]):  #adding action
#
#                 #after death unit should stay at the last frame of the dead animation sequence
#                 if self.action == 3:    #dead animation in the list.
#                     self.frame_index = len(self.animation_list[self.action])-1  #final frame
#                 else:
#                     self.idle() # sets to idle animation
#
#         #-----------------------------------Idle----------------------------
#         def idle(self):
#             self.action = 0
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def hurt(self):
#             self.action = 2
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def dead(self):
#             self.action = 3
#             self.frame_index = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Hurt----------------------------
#         def reset(self):
#             self.alive = True
#             self.inventory = self.max_inventory
#             self.hp = self.max_hp
#             self.armor = self.max_armor
#             self.defence = self.start_defence
#             self.strength = self.start_strength
#             self.frame_index = 0
#             self.action = 0
#             self.update_time = pygame.time.get_ticks()
#
#         #-----------------------------------Attack----------------------------
#         def attack(self,target):
#             rand = random.randint(-5,5)
#             damage = self.strength + rand
#             if self.special == 1:
#                 #target.armor -= 0
#                 target.hp -= damage
#             elif self.special != 1:
#                 target.armor -= int(damage*(target.defence/100))
#                 if target.armor > 0:
#                     target.hp -= int(damage*(1 - target.defence/100))
#                 if target.armor <= 0:
#                     target.hp -= int((damage*(1 - target.defence/100)-target.armor))
#                     target.armor = 0
#             # runs hurn animation
#             target.hurt()
#
#             if target.hp < 1:
#                 target.hp = 0
#                 target.alive = False
#                 # runs death animation
#                 target.dead()
#
#
#             #   if self.special != 1:
#             #       damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage-(damage*(target.defence/100)))), red)
#             #   else:
#             #       damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#             #DamageText
#             if self.special != 1:
#                 if target.armor > 1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(int(damage*(1 - target.defence/100))), red)
#                 if target.armor <=1:
#                     damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#                     #DamageText(target.rect.centerx,target.rect.y-35,str(int((damage*(1 - target.defence/100)))), red)
#             else:
#                 damage_text = DamageText(target.rect.centerx,target.rect.y-35,str(damage), red)
#
#             damage_text_group.add(damage_text)
#             #---------------------------------AttackSounds---------------------------------------
#             #attack sound # 0-standard blade; 1-arrow; 2-stone
#             if self.special == 0:
#                 pygame.mixer.Sound(attack_sound).play()
#             elif self.special == 1:
#                 pygame.mixer.Sound(arrow_sound).play()
#             elif self.special == 2:
#                 pygame.mixer.Sound(stone_sound).play()
#             elif self.special == 3:
#                 pygame.mixer.Sound(snarl_sound).play()
#             elif self.special == 4:
#                 pygame.mixer.Sound(flame_sound).play()
#             #------------------------------------------------------------------------------------
#
#
#             #animations
#             self.action = 1   # set action frames to as 1 as 1 = attack folder animation
#             self.frame_index = 0 # frame 0 in the attack folder animation
#             self.update_time = pygame.time.get_ticks()
#
#         #----------------------------------------------------------------------
#         def draw(self):
#             screen.blit(self.image, self.rect)
#
#     #-----------------------------------HealthBar--------------------------
#     class healthBar ():
#         def __init__(self, x,y, hp, max_hp):
#             self.x = x
#             self.y = y
#             self.hp = hp
#             self.max_hp = max_hp
#         def draw (self, hp):
#             self.hp = hp
#             # health ration
#             ratio = self.hp / self.max_hp
#             pygame.draw.rect(screen,red,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,green,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------ArmorBar--------------------------
#     class armorBar ():
#         def __init__(self, x,y, armor, max_armor):
#             self.x = x
#             self.y = y
#             self.armor = armor
#             self.max_armor = max_armor
#         def draw (self, armor):
#             self.armor = armor
#             # health ration
#             ratio = self.armor / self.max_armor
#             pygame.draw.rect(screen,lightblue,(self.x, self.y, 50,5))
#             pygame.draw.rect(screen,blue,(self.x, self.y, 50*ratio,5))
#
#     #-----------------------------------AttributeChangeBar-----------------
#     class DamageText(pygame.sprite.Sprite):   # sprite is updated automatically
#         def __init__(self,x,y,damage, color):
#             pygame.sprite.Sprite.__init__(self)
#             self.image = fontDMG.render(damage, True, color)
#             self.rect = self.image.get_rect()
#             self.rect.center = (x,y)
#             self.counter = 0
#
#         def update(self):
#             #move text
#             self.rect.y -=1
#             #delete after timer
#             self.counter +=1
#             if self.counter > 30:
#                 self.kill()
#
#     damage_text_group = pygame.sprite.Group()    #python list
#     #def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#     #-----------------------------------PlayerArmy--------------------------
#     militia = Fighter (350,300, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     militia_healthbar = healthBar (militia.rect.centerx-25,militia.rect.centery-55,militia.hp, militia.max_hp)
#     militia_armorbar = armorBar (militia.rect.centerx-25,militia.rect.centery-50,militia.armor, militia.max_armor)
#     #-----------------------------------------------------------------------
#     boy = Fighter (435,270, 'boy',120,60,35,40,1,3,0,True,False,0,0)
#     boy_healthbar = healthBar (boy.rect.centerx-25,boy.rect.centery-55,boy.hp, boy.max_hp)
#     boy_armorbar = armorBar (boy.rect.centerx-25,boy.rect.centery-50,boy.armor, boy.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht = Fighter (540,210,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht_healthbar = healthBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-55,landsknecht.hp, landsknecht.max_hp)
#     landsknecht_armorbar = armorBar (landsknecht.rect.centerx-25,landsknecht.rect.centery-50,landsknecht.armor, landsknecht.max_armor)
#     #-----------------------------------------------------------------------
#     landsknecht1 = Fighter (620,170,'landsknecht',90,55,45,55,1,0,1,True,False,0,0)
#     landsknecht1_healthbar = healthBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-55,landsknecht1.hp, landsknecht1.max_hp)
#     landsknecht1_armorbar = armorBar (landsknecht1.rect.centerx-25,landsknecht1.rect.centery-50,landsknecht1.armor, landsknecht1.max_armor)
#     #-----------------------------------------------------------------------
#     chevalier = Fighter (720,100,'chevalier',120,100,65,70,1,0,1,True,False,0,0)
#     chevalier_healthbar = healthBar (chevalier.rect.centerx-25,chevalier.rect.centery-65,chevalier.hp, chevalier.max_hp)
#     chevalier_armorbar = armorBar (chevalier.rect.centerx-25,chevalier.rect.centery-60,chevalier.armor, chevalier.max_armor)
#     #-----------------------------------------------------------------------
#     militia1 = Fighter (440,350, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     militia1_healthbar = healthBar (militia1.rect.centerx-25,militia1.rect.centery-55,militia1.hp, militia1.max_hp)
#     militia1_armorbar = armorBar (militia1.rect.centerx-25,militia1.rect.centery-50,militia1.armor, militia1.max_armor)
#     #-----------------------------------------------------------------------
#     militia2 = Fighter (840,110, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     militia2_healthbar = healthBar (militia2.rect.centerx-25,militia2.rect.centery-55,militia2.hp, militia2.max_hp)
#     militia2_armorbar = armorBar (militia2.rect.centerx-25,militia2.rect.centery-50,militia2.armor, militia2.max_armor)
#     #-----------------------------------------------------------------------
#     militia3 = Fighter (930,110, 'militia',60,30,35,30,1,0,1,True,False,0,0)
#     militia3_healthbar = healthBar (militia3.rect.centerx-25,militia3.rect.centery-55,militia3.hp, militia3.max_hp)
#     militia3_armorbar = armorBar (militia3.rect.centerx-25,militia3.rect.centery-50,militia3.armor, militia3.max_armor)
#     #-----------------------------------------------------------------------
#     archer = Fighter (530,115, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer_healthbar = healthBar (archer.rect.centerx-25,archer.rect.top-20,archer.hp, archer.max_hp)
#     archer_armorbar = armorBar (archer.rect.centerx-25,archer.rect.top-15,archer.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     archer1 = Fighter (440,160, 'archer',65,30,40,32,2,1,1,True,False,0,0)
#     archer1_healthbar = healthBar (archer1.rect.centerx-25,archer1.rect.top-20,archer1.hp, archer.max_hp)
#     archer1_armorbar = armorBar (archer1.rect.centerx-25,archer1.rect.top-15,archer1.armor, archer.max_armor)
#     #-----------------------------------------------------------------------
#     yvan = Fighter (350,210, 'yvan',yvan_hp,yvan_armor,yvan_defene,yvan_attack,2,2,0,True,False,0,0)
#     yvan_healthbar = healthBar (yvan.rect.centerx-25,yvan.rect.top-20,yvan.hp, yvan.max_hp)
#     yvan_armorbar = armorBar (yvan.rect.centerx-25,yvan.rect.top-15,yvan.armor, yvan.max_armor)
#     #max_hp,max_armor, defence, strength,
#
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_player = []
#     army_player.append(boy)
#     army_player.append(landsknecht)
#     army_player.append(landsknecht1)
#     army_player.append(chevalier)
#     army_player.append(archer)
#     army_player.append(archer1)
#     army_player.append(yvan)
#
#     army_player.append(militia)
#     army_player.append(militia1)
#     army_player.append(militia2)
#     army_player.append(militia3)
#
#     army_player_front = army_player[:8]
#
#     #def __init__(self, x,y,id,max_hp,max_armor, defence, strength, reach, special, max_inventory,alive,hostile,resistance,tricks):
#     #-----------------------------HostileArmy-------------------------------
#     h_dragohare = Fighter (760,230,'dragohare',400,300,85,40,3,4,0,True,True,0,0)
#     h_dragohare_healthbar = healthBar (h_dragohare.rect.centerx+90,h_dragohare.rect.centery+70,h_dragohare.hp, h_dragohare.max_hp)
#     h_dragohare_armorbar = armorBar (h_dragohare.rect.centerx+90,h_dragohare.rect.centery+75,h_dragohare.armor, h_dragohare.max_armor)
#     #-----------------------------HostileArmy-------------------------------
#     h_caerbannog = Fighter (850,280,'caerbannog',750,400,85,60,3,4,0,True,True,0,0)
#     h_caerbannog_healthbar = healthBar (h_caerbannog.rect.centerx+20,h_caerbannog.rect.centery-105,h_caerbannog.hp, h_caerbannog.max_hp)
#     h_caerbannog_armorbar = armorBar (h_caerbannog.rect.centerx+20,h_caerbannog.rect.centery-100,h_caerbannog.armor, h_caerbannog.max_armor)
#
#     # h_militia = Fighter(570,365,'militia',60,30,35,30,1,0,1,True,True,0,0)
#     # h_militia_healthbar = healthBar(h_militia.rect.centerx-25,h_militia.rect.centery-55,h_militia.hp, h_militia.max_hp)
#     # h_militia_armorbar = armorBar(h_militia.rect.centerx-25,h_militia.rect.centery-50,h_militia.armor, h_militia.max_armor)
#     #-----------------------------------------------------------------------
#     # h_brigand = Fighter(570,365,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # h_brigand_healthbar = healthBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-55,h_brigand.hp, h_brigand.max_hp)
#     # h_brigand_armorbar = armorBar(h_brigand.rect.centerx-25,h_brigand.rect.centery-50,h_brigand.armor, h_brigand.max_armor)
#     # # #-----------------------------------------------------------------------
#     # h_landsknecht2 = Fighter (570,365,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
#     # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
#     # # #-----------------------------------------------------------------------
#     # # h_brigand1 = Fighter(660,325,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # # h_brigand1_healthbar = healthBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-55,h_brigand1.hp, h_brigand1.max_hp)
#     # # h_brigand1_armorbar = armorBar(h_brigand1.rect.centerx-25,h_brigand1.rect.centery-50,h_brigand1.armor, h_brigand1.max_armor)
#     # # # # #-----------------------------------------------------------------------
#     # h_landsknecht3 = Fighter (660,325,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     # h_landsknecht3_healthbar = healthBar (h_landsknecht3.rect.centerx-25,h_landsknecht3.rect.centery-55,h_landsknecht3.hp, h_landsknecht3.max_hp)
#     # h_landsknecht3_armorbar = armorBar (h_landsknecht3.rect.centerx-25,h_landsknecht3.rect.centery-50,h_landsknecht3.armor, h_landsknecht3.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_landsknecht = Fighter (750,280,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     # h_landsknecht_healthbar = healthBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-55,h_landsknecht.hp, h_landsknecht.max_hp)
#     # h_landsknecht_armorbar = armorBar (h_landsknecht.rect.centerx-25,h_landsknecht.rect.centery-50,h_landsknecht.armor, h_landsknecht.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_landsknecht1 = Fighter (840,235,'landsknecht',90,55,40,50,1,0,1,True,True,0,0)
#     # h_landsknecht1_healthbar = healthBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-55,h_landsknecht1.hp, h_landsknecht1.max_hp)
#     # h_landsknecht1_armorbar = armorBar (h_landsknecht1.rect.centerx-25,h_landsknecht1.rect.centery-50,h_landsknecht1.armor, h_landsknecht1.max_armor)
#     # #-----------------------------------------------------------------------
#     # #-----------------------------------------------------------------------
#     # # h_brigand2 = Fighter(940,195,'brigand',50,25,30,30,1,0,1,True,True,0,0)
#     # # h_brigand2_healthbar = healthBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-55,h_brigand2.hp, h_brigand2.max_hp)
#     # # h_brigand2_armorbar = armorBar(h_brigand2.rect.centerx-25,h_brigand2.rect.centery-50,h_brigand2.armor, h_brigand2.max_armor)
#     # h_chevalier = Fighter (930,150,'chevalier',120,100,60,65,1,0,1,True,True,0,0)
#     # h_chevalier_healthbar = healthBar (h_chevalier.rect.centerx-25,h_chevalier.rect.centery-65,h_chevalier.hp, h_chevalier.max_hp)
#     # h_chevalier_armorbar = armorBar (h_chevalier.rect.centerx-25,h_chevalier.rect.centery-60,h_chevalier.armor, h_chevalier.max_armor)
#     # #-----------------------------------------------------------------------
#     # # h_landsknecht2 = Fighter (790,340,'landsknecht',90,55,40,50,2,0,1,True,True,0,0)
#     # # h_landsknecht2_healthbar = healthBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-55,h_landsknecht2.hp, h_landsknecht2.max_hp)
#     # # h_landsknecht2_armorbar = armorBar (h_landsknecht2.rect.centerx-25,h_landsknecht2.rect.centery-50,h_landsknecht2.armor, h_landsknecht2.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_bowman = Fighter (790,350, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman_healthbar = healthBar (h_bowman.rect.centerx-25,h_bowman.rect.top-20,h_bowman.hp, h_bowman.max_hp)
#     # h_bowman_armorbar = armorBar (h_bowman.rect.centerx-25,h_bowman.rect.top-15,h_bowman.armor, h_bowman.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_bowman1 = Fighter (695,400, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman1_healthbar = healthBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-20,h_bowman1.hp, h_bowman1.max_hp)
#     # h_bowman1_armorbar = armorBar (h_bowman1.rect.centerx-25,h_bowman1.rect.top-15,h_bowman1.armor, h_bowman1.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_bowman2 = Fighter (880,310, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman2_healthbar = healthBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-20,h_bowman2.hp, h_bowman2.max_hp)
#     # h_bowman2_armorbar = armorBar (h_bowman2.rect.centerx-25,h_bowman2.rect.top-15,h_bowman2.armor, h_bowman2.max_armor)
#     # #-----------------------------------------------------------------------
#     # h_bowman3 = Fighter (960,260, 'bowman',45,20,30,25,2,1,1,True,True,0,0)
#     # h_bowman3_healthbar = healthBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-20,h_bowman3.hp, h_bowman3.max_hp)
#     # h_bowman3_armorbar = armorBar (h_bowman3.rect.centerx-25,h_bowman3.rect.top-15,h_bowman3.armor, h_bowman3.max_armor)
#     #
#
#
#     # +125 HealthBar / -45  amd +5 Armor
#     #x: +90-100; y: -45
#     #-----------------------------------------------------------------------
#     army_hostiles = []
#     army_hostiles.append(h_dragohare)
#     #army_hostiles.append(h_brigand)
#     #army_hostiles.append(h_brigand1)
#     # army_hostiles.append(h_chevalier)
#     # army_hostiles.append(h_landsknecht)
#     # army_hostiles.append(h_landsknecht1)
#     # army_hostiles.append(h_landsknecht2)
#     # army_hostiles.append(h_landsknecht3)
#     # #army_hostiles.append(h_brigand2)
#     # army_hostiles.append(h_bowman)
#     # army_hostiles.append(h_bowman1)
#     # army_hostiles.append(h_bowman2)
#     # army_hostiles.append(h_bowman3)
#
#     army_hostiles_front = army_hostiles
#
#     enemy_reserves = True
#     army_hostiles_reserves = []
#     army_hostiles_reserves.append(h_caerbannog)
#
#     #------------------------------TotalUnitNumber----------------------------
#     total_hostiles = len(army_hostiles)
#     total_allies = len(army_player)
#     total_fighters = total_hostiles + total_allies
#
#     #------------------------------ItemsUse(Button)---------------------------
#     #inventory_button = button.Button(screen,WINDOW_SIZE[0]*0 + 110, WINDOW_SIZE[1]*0 - 6,inventory_bag,280,120,0, True, 'Inventory')
#
#     inventory_button = button.ToggleButton(screen,-65, 425,inventory_bag,260,120,0, True, 'Inventory')
#     #------------------------------ItemsUse(PotionButton)-------------------
#     potion_button = button.Button(screen, WINDOW_SIZE[0]*0.01, WINDOW_SIZE[1]*0.90, health_potion, 48,72,30, False,f'Health Potion. Restores {health_potion_restores} HP')
#     potion_button1 = button.Button(screen, WINDOW_SIZE[0]*0.06, WINDOW_SIZE[1]*0.90, defence_potion, 48,72,40, False,f'Defence Potion. Gives {defence_potion_adds} DEF/ARM')
#     potion_button2 = button.Button(screen, WINDOW_SIZE[0]*0.11, WINDOW_SIZE[1]*0.90, berserk_potion, 48,72,60, False,f'Berserk Potion. Gives {berserk_potion_adds} ATK / Removes {int(berserk_potion_adds*1)} DEF')
#
#
#     #------------------------------IconToggle(Reset)------------------------
#     restart_button = button.Button(screen, 1100, 8, retry_icon, 84,90,25, False,'Try Again')
#     skip_turn_button = button.Button(screen, WINDOW_SIZE[0]*0.92, WINDOW_SIZE[1]*0.62, skip_turn_img, 86,82,60, False,f'Skip Turn')
#     victory_button = button.Button(screen, 1170, 15, victory_icon, 86,90,25, True,'Back to Map')
#     leave_button = button.Button(screen, 1190, 0, doors_icon, 64,90,25, True,'Leave Battlefield')
#
#     #-----------------------------------EnemyReservesMangement----------------------
#
#
#
#     #-----------------------------------------------------------------------
#
#     while dragonhunt_battle_running:
#         #display.fill((146,244,255))
#         draw_bgBackscreen()
#         #draw_noteMap()  # location map
#         draw_bg()
#         draw_panel()
#         draw_bag()
#
#         #-----------------------------DrawingUnits/AnimatioSpeedMod------------
#         for units in army_player:
#             militia.update(0.9)
#             militia.draw()
#             #------------
#             militia1.update(0.88)
#             militia1.draw()
#             #------------
#             militia2.update(0.84)
#             militia2.draw()
#             #------------
#             militia3.update(0.84)
#             militia3.draw()
#             #------------
#             landsknecht.update(1)
#             landsknecht.draw()
#             #------------
#             chevalier.update(1.3)
#             chevalier.draw()
#             #------------
#             boy.update(0.88)
#             boy.draw()
#             #------------
#             landsknecht1.update(1.1)
#             landsknecht1.draw()
#             #------------
#             archer.update(0.95)
#             archer.draw()
#             #------------
#             archer1.update(0.92)
#             archer1.draw()
#             #------------
#             yvan.update(1.05)
#             yvan.draw()
#
#         #----------------------------EnemyUnitsDraw---------------------------
#         for hostile in army_hostiles:
#             h_dragohare.update(1.2)
#             h_dragohare.draw()
#             #------------
#             # h_brigand.update(0.9)
#             # h_brigand.draw()
#             # #------------
#             # h_brigand2.update(0.85)
#             # h_brigand2.draw()
#             #------------
#             #h_landsknecht.update(0.95)
#             # h_landsknecht.draw()
#             # #------------
#             # h_landsknecht1.update(0.98)
#             # h_landsknecht1.draw()
#             # #------------
#             # h_landsknecht2.update(0.94)
#             # h_landsknecht2.draw()
#             # #------------
#             # h_landsknecht3.update(0.92)
#             # h_landsknecht3.draw()
#             # #------------
#             # h_chevalier.update(1.25)
#             # h_chevalier.draw()
#             # #------------
#             # # h_brigand1.update(0.9)
#             # # h_brigand1.draw()
#             # #------------
#             # h_bowman.update(0.89)
#             # h_bowman.draw()
#             # #------------
#             # h_bowman1.update(0.85)
#             # h_bowman1.draw()
#             # #------------
#             # h_bowman2.update(0.92)
#             # h_bowman2.draw()
#             # #------------
#             # h_bowman3.update(0.90)
#             # h_bowman3.draw()
#         #-----------------------------HealthBar/ArmorBar-----------------------
#         #-------------Player------------------------
#         if show_indicators == True:
#             if chevalier.alive == True:
#                 chevalier_healthbar.draw(chevalier.hp)
#                 chevalier_armorbar.draw(chevalier.armor)
#             if militia.alive == True:
#                 militia_healthbar.draw(militia.hp)
#                 militia_armorbar.draw(militia.armor)
#             if militia1.alive == True:
#                 militia1_healthbar.draw(militia1.hp)
#                 militia1_armorbar.draw(militia1.armor)
#             if militia2.alive == True:
#                 militia2_healthbar.draw(militia2.hp)
#                 militia2_armorbar.draw(militia2.armor)
#             if militia3.alive == True:
#                 militia3_healthbar.draw(militia3.hp)
#                 militia3_armorbar.draw(militia3.armor)
#             if boy.alive == True:
#                 boy_healthbar.draw(boy.hp)
#                 boy_armorbar.draw(boy.armor)
#             if landsknecht.alive == True:
#                 landsknecht_healthbar.draw(landsknecht.hp)
#                 landsknecht_armorbar.draw(landsknecht.armor)
#             if landsknecht1.alive == True:
#                 landsknecht1_healthbar.draw(landsknecht1.hp)
#                 landsknecht1_armorbar.draw(landsknecht1.armor)
#             if archer.alive == True:
#                 archer_healthbar.draw(archer.hp)
#                 archer_armorbar.draw(archer.armor)
#             if archer1.alive == True:
#                 archer1_healthbar.draw(archer1.hp)
#                 archer1_armorbar.draw(archer1.armor)
#             if yvan.alive == True:
#                 yvan_healthbar.draw(yvan.hp)
#                 yvan_armorbar.draw(yvan.armor)
#
#             #------------------Enemy--------------------
#             if h_dragohare.alive == True:
#                 h_dragohare_healthbar.draw(h_dragohare.hp)
#                 h_dragohare_armorbar.draw(h_dragohare.armor)
#             # if h_chevalier.alive == True:
#             #     h_chevalier_healthbar.draw(h_chevalier.hp)
#             #     h_chevalier_armorbar.draw(h_chevalier.armor)
#             # # if h_brigand.alive == True:
#             # #     h_brigand_healthbar.draw(h_brigand.hp)
#             # #     h_brigand_armorbar.draw(h_brigand.armor)
#             # # if h_brigand2.alive == True:
#             # #     h_brigand2_healthbar.draw(h_brigand2.hp)
#             # #     h_brigand2_armorbar.draw(h_brigand2.armor)
#             # if h_landsknecht.alive == True:
#             #     h_landsknecht_healthbar.draw(h_landsknecht.hp)
#             #     h_landsknecht_armorbar.draw(h_landsknecht.armor)
#             # if h_landsknecht1.alive == True:
#             #     h_landsknecht1_healthbar.draw(h_landsknecht1.hp)
#             #     h_landsknecht1_armorbar.draw(h_landsknecht1.armor)
#             # if h_landsknecht2.alive == True:
#             #     h_landsknecht2_healthbar.draw(h_landsknecht2.hp)
#             #     h_landsknecht2_armorbar.draw(h_landsknecht2.armor)
#             # if h_landsknecht3.alive == True:
#             #     h_landsknecht3_healthbar.draw(h_landsknecht3.hp)
#             #     h_landsknecht3_armorbar.draw(h_landsknecht3.armor)
#             # # if h_brigand1.alive == True:
#             # #     h_brigand1_healthbar.draw(h_brigand1.hp)
#             # #     h_brigand1_armorbar.draw(h_brigand1.armor)
#             # if h_bowman.alive == True:
#             #     h_bowman_healthbar.draw(h_bowman.hp)
#             #     h_bowman_armorbar.draw(h_bowman.armor)
#             # if h_bowman1.alive == True:
#             #     h_bowman1_healthbar.draw(h_bowman1.hp)
#             #     h_bowman1_armorbar.draw(h_bowman1.armor)
#             # if h_bowman2.alive == True:
#             #     h_bowman2_healthbar.draw(h_bowman2.hp)
#             #     h_bowman2_armorbar.draw(h_bowman2.armor)
#             # if h_bowman3.alive == True:
#             #     h_bowman3_healthbar.draw(h_bowman3.hp)
#             #     h_bowman3_armorbar.draw(h_bowman3.armor)
#         #----------------------------------------------------------------------
#         #------------------------------------EnemyReserves-------------------------------------
#         if h_dragohare.alive == False:
#             h_caerbannog.update(1.3)
#             h_caerbannog.draw()
#             if enemy_reserves == True:
#                 army_hostiles.append(h_caerbannog)
#                 army_hostiles = army_hostiles_reserves
#                 enemy_reserves = False
#             if h_caerbannog.alive == True:
#                 h_caerbannog_healthbar.draw(h_caerbannog.hp)
#                 h_caerbannog_armorbar.draw(h_caerbannog.armor)
#
#
#         #-----------------------------DamageText-----------------------------
#         damage_text_group.update()
#         damage_text_group.draw(screen)
#         #methods update and draw are parts of the sprite.
#
#         #-----------------------------Items/SkipTurn/Inventory-----------------------------
#         pos = pygame.mouse.get_pos()
#         if skip_turn_button.rect.collidepoint(pos):
#             draw_text(f'{skip_turn_button.description}', fontDMG, green, skip_turn_button.rect.x-30,skip_turn_button.rect.y+100)
#         if skip_turn_button.draw():
#             skip_turn=True
#         if battle_status != 2 and leave_button.available == True:
#             if leave_button.rect.collidepoint(pos):
#                 draw_text(f'{leave_button.description}', fontDMG, green, leave_button.rect.x-140,leave_button.rect.y+100)
#             if leave_button.draw():
#                 play_music('Map')
#                 button.wealth = button.start_wealth
#                 dragonhunt_battle_running= False
#
#
#         if inventory_button.rect.collidepoint(pos):
#             draw_text(f'{inventory_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#         if inventory_button.toggled == True and battle_status ==0:
#             potion_button.available = True
#             potion_button1.available = True
#             potion_button2.available = True
#
#             #---------------------HealthPotion--------------------------------------
#             if potion_button.available == True:
#                 if potion_button.draw():
#                     use_health_potion = True
#                 draw_text(f'{potion_button.price}', fontBag, (255,225,100), potion_button.rect.x+5, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button.rect.collidepoint(pos):
#                     draw_text(f'{potion_button.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#             #-------DefencePotion--------------
#             if potion_button1.available == True:
#                 if potion_button1.draw():
#                     use_defence_potion = True
#                 draw_text(f'{potion_button1.price}', fontBag, (255,225,100), potion_button.rect.x+65, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button1.rect.collidepoint(pos):
#                     draw_text(f'{potion_button1.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#                 #-------BerserkPotion--------------
#             if potion_button2.available == True:
#                 if potion_button2.draw():
#                     use_berserk_potion = True
#                 draw_text(f'{potion_button2.price}', fontBag, (255,225,100), potion_button.rect.x+130, potion_button.rect.y-60)
#                 pos = pygame.mouse.get_pos()
#                 if potion_button2.rect.collidepoint(pos):
#                     draw_text(f'{potion_button2.description}', fontDMG, green, potion_button.rect.x,potion_button.rect.y-100)
#
#         #---------------------InventoryStock--------------------------------------
#         else:
#             potion_button.available = False
#
#         #--------------------------------------------------------------------------
#         if battle_status ==0:   #win/loose check
#
#             #-----------------------------PlayerAttacking---------------------------
#             for count, ally in enumerate(army_player):
#                 if current_fighter == 1+count:
#                     draw_text('^', fontActive, "#FFA500", ally.rect.centerx-20,ally.rect.y -65)
#                     if ally.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#
#                             if ally.reach == 2:
#                                 if engage == True and target != None:
#                                     # conditioned upon engage below & def attack above
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif ally.reach == 1:
#                                 if engage == True and target != None and target.reach != 2:
#                                     ally.attack(target)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             for enemy in army_hostiles_front:
#                                 if all(enemy.alive == False for enemy in army_hostiles_front):
#                                     #enemy.alive == False:
#                                     if ally.reach == 1:
#                                         if engage == True and target != None and target.reach == 2:
#                                             ally.reach = 2
#                                             ally.attack(target)
#                                             current_fighter += 1
#                                             action_cooldown = 0
#
#
#                             #-----------------------------------------SkipTurn-----------------------------------------
#                             if skip_turn == True:
#                                 current_fighter += 1
#                                 action_cooldown = 0
#                                 skip_turn_heal = 10
#                                 if ally.max_hp - ally.hp > skip_turn_heal:    #50
#                                     skip_turn_heal = skip_turn_heal
#                                 else:
#                                     skip_turn_heal = ally.max_hp - ally.hp
#                                 ally.hp += skip_turn_heal
#                                 #DamageText
#                                 damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(skip_turn_heal), green)
#                                 damage_text_group.add(damage_text)
#                             skip_turn = False
#
#                             #------------UsingItem(HealthPotion)---------------------------
#                             if use_health_potion == True and button.wealth >= potion_button.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_hp - ally.hp > health_potion_restores:    #50
#                                         heal_amount = health_potion_restores
#                                     else:
#                                         heal_amount = ally.max_hp - ally.hp
#                                     ally.hp += heal_amount
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button.price
#                                     #DamageText
#                                     damage_text = DamageText(ally.rect.centerx,ally.rect.y-35,str(heal_amount), green)
#                                     damage_text_group.add(damage_text)
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_health_potion = False
#
#                             #----------------------------------------------------
#                             #------------UsingItem(DefencePotion)---------------
#                             if use_defence_potion == True and button.wealth >= potion_button1.price:
#                                 if ally.inventory > 0:
#                                     # not healing beyond max_hp
#                                     if ally.max_armor - ally.armor > defence_potion_adds:    #50
#                                         add_defence_amount = defence_potion_adds
#                                     else:
#                                         add_defence_amount = ally.max_armor - ally.armor
#                                     ally.armor += add_defence_amount
#                                     ally.defence = 100
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button1.price     #Change price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                 use_defence_potion = False
#
#
#                             #------------UsingItem(BerserkPotion)---------------
#                             if use_berserk_potion == True and button.wealth >= potion_button2.price:
#                                 if ally.inventory > 0:
#                                     ally.strength += berserk_potion_adds
#                                     if ally.defence < int(berserk_potion_adds):
#                                         ally.defence = 0
#                                     else:
#                                         ally.defence -= int(berserk_potion_adds)
#                                     ally.inventory -= 1
#                                     button.wealth -= potion_button2.price
#
#                                     current_fighter +=1
#                                     action_cooldown = 0
#                                     #Change price
#                                 use_berserk_potion = False
#
#                     else:
#                         current_fighter +=1   #if dead = skip turn
#
#
#
#             #-----------------------------EnemyAttacking----------------------------
#             for count, enemy in enumerate(army_hostiles ):
#                 if current_fighter == 1+ total_allies + count:   # "3 + count" - checks with the max_fighter var and number of units in army_player
#                     draw_text('^', fontActive, "#FFA500", enemy.rect.centerx-20,enemy.rect.y -65)
#                     if enemy.alive == True:
#                         action_cooldown +=1
#                         if action_cooldown >= action_waittime:
#                             #------------------------------EnemyDefencePotion------------------
#                             if (enemy.armor / enemy.max_armor) <0.2 and enemy.armor < defence_potion_adds and enemy.max_armor > health_potion_restores and enemy.inventory >0:
#                                 if enemy.max_armor - enemy.armor > defence_potion_adds:
#                                     add_defence_amount = defence_potion_adds
#                                 else:
#                                     add_defence_amount = enemy.max_armor - enemy.armor
#                                 enemy.armor += add_defence_amount
#                                 enemy.defence = 100
#                                 enemy.inventory -= 1
#                                 current_fighter +=1
#                                 action_cooldown = 0
#
#
#                             #------------------------------EnemyHealthPotion------------------
#                             elif (enemy.hp / enemy.max_hp) <0.5 and enemy.inventory >0:
#                                 if enemy.max_hp - enemy.hp > health_potion_restores:
#                                     heal_amount = health_potion_restores
#                                 else:
#                                     heal_amount = enemy.max_hp - enemy.hp
#
#                                 enemy.hp += heal_amount
#                                 enemy.inventory -= 1
#
#                                 #DamageText
#                                 damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(heal_amount), green)
#                                 damage_text_group.add(damage_text)
#
#                                 current_fighter +=1
#                                 action_cooldown = 0
#
#                             #-------------------------------------------------------------------
#                             elif enemy.reach == 2:
#                                 if enemy.strength >= ally.hp and ally.alive == True:
#                                     enemy.attack(ally)
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif enemy.reach == 1:
#                                 if all(ally.alive == True for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 elif all(ally.alive == False for ally in army_player_front):
#                                     enemy.attack (random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 2]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#                                 else:
#                                     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True and ally.reach == 1]))
#                                     current_fighter += 1
#                                     action_cooldown = 0
#
#                             elif enemy.reach == 3 and enemy.id == 'dragohare':
#                                 alive_targets = sum(ally.alive == True for ally in army_player)
#                                 if alive_targets >= 6:
#                                     for i in range(6):
#                                         enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                 elif alive_targets < 6:
#                                     for j in range (alive_targets):
#                                         enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                 enemy.armor = enemy.max_armor
#                                 current_fighter += 1
#                                 action_cooldown = 0
#
#                             elif enemy.reach == 3 and enemy.id == 'caerbannog':
#                                 alive_targets = sum(ally.alive == True for ally in army_player)
#                                 if alive_targets >= 6:
#                                     for i in range(6):
#                                         enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                 elif alive_targets < 6:
#                                     for j in range (alive_targets):
#                                         enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                                 current_fighter += 1
#                                 action_cooldown = 0
#
#                             else:
#                                 current_fighter +=1
#
#                     #     enemy.attack(random.choice([ally for ally in army_player if ally.alive == True]))
#                     #     # enemy.hp += 10
#                     #     current_fighter += 1
#                     #     action_cooldown = 0
#                     #     # damage_text = DamageText(enemy.rect.centerx,enemy.rect.y-35,str(10), green)
#                     #     # damage_text_group.add(damage_text)
#
#                     else:
#                         current_fighter +=1
#
#             #---------------------------------Turns----------------------------
#             # if all have had a turn, reset
#             if current_fighter > total_fighters:
#                 current_fighter = 1
#
#         #-----------------------------DefeatStatus-------------------------
#         # checking alive/dead status
#         alive_allies = 0
#         for ally in army_player:
#             if ally.alive == True:
#                 alive_allies +=1
#         if alive_allies ==0:
#             battle_status =1
#
#         #---------------------------------VictoryStatus--------------------
#         alive_enemies = 0
#         for enemy in army_hostiles:
#             if enemy.alive == True:
#                 alive_enemies +=1
#         if alive_enemies ==0 and all(enemy.alive == False for enemy in army_hostiles_reserves):
#             battle_status =2
#
#         #-------------------Defeat/VictoryStatusDisplay-------------------
#         if battle_status !=0:
#             if battle_status ==1:
#                 draw_text(f'Defeat!', fontMenuLarge, (155,0,0), screen.get_width()*0.46,0)
#
#                 #-------------------ResetButton-----------------------------------
#                 if restart_button.available == True:
#                     if restart_button.draw():
#                         play_music('Battle1')
#                         for ally in army_player:
#                             ally.reset()
#                         for enemy in army_hostiles:
#                             enemy.reset()
#
#
#                         button.wealth = button.start_wealth         #restart gold here
#                         current_fighter = 1
#                         action_cooldown = 0
#                         battle_status = 0
#
#                         pos = pygame.mouse.get_pos() # text over the button
#                     if restart_button.rect.collidepoint(pos):
#                         draw_text(f'{restart_button.description}', fontDMG, green, restart_button.rect.x+30,leave_button.rect.y+100)
#
#             #-------------------Defeat/VictoryStatusDisplay-------------------
#             if battle_status ==2:
#                 button.quest_dragonhunt = 'locked'
#                 draw_text(f'Victory!', fontMenuLarge, green, screen.get_width()*0.46,0)
#                 if play_victory_music == True:
#                     play_music('BattleVictory')
#                 play_victory_music = False
#                 if victory_button.available == True:
#                     if victory_button.draw():
#                         button.wealth += 1000
#                         button.start_wealth = button.wealth
#                         button.quest_finale= 'unlocked'
#                         print(button.start_wealth)
#                         print(button.wealth)
#                         pyautogui.moveTo(750, 400)
#                         play_music('Outro')
#                         dragonhunt_battle_running = False
#                     if victory_button.rect.collidepoint(pos):
#                         draw_text(f'{victory_button.description}', fontDMG, green, victory_button.rect.x-75,leave_button.rect.y+100)
#         #------------------------------End/Controls------------------------
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == VIDEORESIZE:
#                 if not fullscreen:
#                     screen = pygame.display.set_mode((event.w,event.h),0,32)
#
#             if event.type == KEYDOWN:
#                 if event.key == K_f and show_indicators == True:
#                     show_indicators = False
#                 elif event.key == K_f and show_indicators == False:
#                     show_indicators = True
#
#                 if event.key == K_o:
#                     # fullscreen = not fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     button.fullscreen = not button.fullscreen
#                     # with open('genericmap.txt', 'w') as file:
#                     #     file.write(str(fullscreen))
#                     fullscreen = button.fullscreen
#
#                     if fullscreen:
#                         screen = pygame.display.set_mode(monitor_size,FULLSCREEN)
#                     else:
#                         screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),0,32)
#
#             #---------------------ToggleButton------------------------
#             inventory_button.event_handler(event) #ToggleButton
#             #---------------------ToggleButton------------------------
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 clicked = True
#             else:
#                 clicked = False
#
#         if leave_button.clicked == True or victory_button.clicked == True:
#             mouse_map_position_align(750,400)
#         #-----------------------------Action/TargetSearch-------------------
#         engage = False
#         target = None
#
#         inventory_button.draw(screen) #ToggleButton
#
#         pygame.mouse.set_visible(False)
#         pos = pygame.mouse.get_pos()
#         screen.blit(normal_icon,pos)
#
#         for count, ally in enumerate(army_player):
#             if ally.rect.collidepoint(pos) and ally.alive == True:
#                 draw_text(f'{ally.id} | HP: {ally.hp} | ARM: {ally.armor} | ATK: {ally.strength} | DEF: {ally.defence} | INV: {ally.inventory}', font, (0,100,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#         for count, enemy in enumerate(army_hostiles):
#             if enemy.rect.collidepoint(pos) and enemy.alive == True:
#                 pygame.mouse.set_visible(False)
#                 screen.blit(attack_icon,pos)
#                 draw_text(f'{enemy.id} | HP: {enemy.hp} | ARM: {enemy.armor} | ATK: {enemy.strength} | DEF: {enemy.defence} | INV: {enemy.inventory}', font, (100,0,0), ((panel.get_width())*0.01), (((screen.get_height() + bg_map.get_height())/2.24)))
#
#                 # show attack icon
#                 #--------------chooseTarget&Attack-------------------------
#                 if clicked == True and enemy.alive == True:
#                     engage = True
#                     target = army_hostiles[count]
#
#
#         #-----------------------------------------------------------------------
#         #surf = pygame.transform.scale(display, WINDOW_SIZE)
#         #screen.blit(surf, (0,0))
#
#         pygame.display.update()
#         clock.tick(60)



































