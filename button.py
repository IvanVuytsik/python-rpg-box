import pyautogui
import pygame
import self as self
import linecache
import time
# def start_wealth():
#     global start_wealth
#     start_wealth = 150
# start_wealth()
import VagrantsLot

# #-------------------------------Potions/Bombs/Charms/Scrolls--------------------------
# health_potion = False
# defence_potion = False
# berserk_potion = False
#
# antidote_potion = False
# vigor_potion = False
# celerity_potion = False
# ironskin_potion = False
# dream_potion = False
# deathkiss_potion = False
# ritual_potion = False
# poison_potion = False
# rejuvenation_potion = False
# frostshield_potion = False
# fireshield_potion = False
# energyshield_potion = False
# moonlight_potion = False
# acid_potion = False
# cleansing_potion = True
# liquidfire_potion = False
# liquidfrost_potion = False
# darkcloud_potion = False
# grenade = True
# energy_shard = False
# shrapnel_grenade = True
# earth_shard = False
#--------------------------------------Skills-------------------------------------
#haggler +
#educated +
#camp_doc +
#cartograph +
#potion_master+
#scholar +
#estates +
#duelist +
#combo +
#scout +
#thief +
#quartermaster +

#----------------------------------itemsForLists---------------------------------
#light_leather_gloves,leather_gloves,reinforced_gloves,
#light_plate_gloves,thieves_gloves,plate_gloves,tournament_gloves,war_gloves,basilisk_gloves
#light_chain_mail,light_plate_armor,light_leather,nomad_armor
#ranger_cloak,war_cloak,full_cloak
#tournament_helm,leather_hood,light_chain_helm,protector_helm
#deep_endless,spider_amulet,moon_crest
#noble_belt,duel_belt,war_belt,day_belt
#leather_pants,reinforced_pants,light_plate_pants,heavy_plate_pants,plate_pants
#war_dagger,ranger_dagger
#mercenary_sword,the_sunrise,spider_sword,short_sword
#plate_shoes,hunter_shoes,light_plate_shoes,ranger_shoes
#unity_ring,emerald_ring,minor_health_ring,minor_protection_ring,trinity_ring
#crowbar,lockmaster_tools,alchemist_kit
#metal_bow,curved_bow,peasant_bow,war_bow,redwood_bow







battle_result = 0
#----------------------------------------Income---------------------------------------
westrad_coal_mine = 'neutral'
westrad_ore_mine_0 = 'neutral'
westrad_ore_mine_1 = 'neutral'
westrad_gold_mine = 'neutral'
charlatan_silver_mine = 'neutral'
charlatan_coal_mine = 'neutral'
solomir_silver_mine = 'neutral'
solomir_gold_mine_0 = 'neutral'
solomir_gold_mine_1 = 'neutral'
solomir_gems_mine = 'neutral'
kharfajian_gems_mine_0 = 'neutral'
kharfajian_gems_mine_1 = 'neutral'
kharfajian_krystal_mine = 'neutral'



#------------------------------------------------------------------------------------
start_experience = 0
def experience():
    global experience
    experience = 0
    experience += start_experience
experience()
    # if experience >= 1000:
    #    experience -= 1000

def next_level ():
    global next_level
    next_level += experience
    if next_level >= 1000:
        next_level -= 1000

def new_level ():
    global new_level
    new_level = 0
    if start_experience >= 1000:
       new_level+=1
new_level()

start_learning_points = 0
def learning_points():
    global learning_points
    learning_points = 0
    learning_points += start_learning_points*new_level
learning_points()

# if start_experience >= next_level:
#     new_level += 1
#     next_level *= new_level

start_wealth = 50000
def wealth():
    global wealth
    wealth = 0
    wealth += start_wealth
wealth()

# start_wealth = 150
# wealth = 0
# wealth += start_wealth

PartyMaxHealth = 100
PartyStartHealth = 100
def PartyHealth():
    global PartyHealth
    PartyHealth = 0
    PartyHealth += PartyStartHealth
PartyHealth()


#-----------------------------------------Quests-------------------------------------------------
quest_new_beginnings = 'invisible'
# quest_dire_wolves = 'invisible'
# quest_highwaymen = 'invisible'
# # quest_dragonhunt = 'invisible'
# # quest_finale = 'invisible'
quest_old_ways = 'unlocked'

# unlocked_quests = []
# unlocked_quests.append(quest_old_ways)
# #unlocked_quests.extend((quest_new_beginnings,quest_dire_wolves,quest_highwaymen,quest_dragonhunt,quest_finale))
#
#-------------------------------------StoryProgression----------------------------------------
chapter_0 = True     # Homecoming
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
#-----------------------------------------------------------------------------------------
def fullscreen():
    global fullscreen
    fullscreen = False
fullscreen()

def mouse_map_align ():
    pyautogui.moveTo(750, 400)

class TroopsButton():
    def __init__(self, surface, x, y, image, size_x, size_y, price, available, description,supply,summon):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface
        self.price = price
        self.available = available
        self.description = description
        self.supply = supply
        self.summon = summon

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                time.sleep(0.1)
                action = True
                self.clicked = True
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class TechniqueButton():
    def __init__(self, surface, x, y, image, size_x, size_y, price, available, description):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.toggled = False
        self.surface = surface
        self.price = price
        self.available = available
        self.description = description

    def draw(self):
        selection_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width,self.rect.height)
        if self.available == True:
            if self.toggled == True:
                pygame.draw.rect(self.surface, "#f4e8b9", selection_rect)
            self.surface.blit(self.image, self.rect)

    def event_handler(self, event):
        if self.available == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.toggled == False:
                    if self.rect.collidepoint(event.pos):
                        self.toggled = True
                elif event.button == 1 and self.toggled == True:
                    if self.rect.collidepoint(event.pos):
                        self.toggled = False







class Button():
    def __init__(self, surface, x, y, image, size_x, size_y, price, available, description):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface
        self.price = price
        self.available = available
        self.description = description

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                time.sleep(0.1)
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class PotionButton():
    def __init__(self, surface, x, y, image, size_x, size_y, price, available, description,supply):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface
        self.price = price
        self.available = available
        self.description = description
        self.supply = supply

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                time.sleep(0.1)
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


class ScrollButton():
    def __init__(self,  x, y, image, size_x, size_y, price, available, description):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.price = price
        self.available = available
        self.description = description

    def draw(self,surface):
        action = False
        self.surface = surface
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                time.sleep(0.4)
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


class ToggleButton():
    def __init__(self, surface, x, y, image, size_x, size_y, price, available, description):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.toggled = False
        self.surface = surface
        self.price = price
        self.available = available
        self.description = description

    def draw(self, surface):
        if self.available == True:
            surface.blit(self.image, self.rect)

    def event_handler(self, event):
        if self.available == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.toggled == False:
                    if self.rect.collidepoint(event.pos):
                        self.toggled = True
                elif event.button == 1 and self.toggled == True:
                    if self.rect.collidepoint(event.pos):
                        self.toggled = False

class InvButton():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

#--------------------------------------attributes-------------------------------------
# def update_attributes ():
# strength = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',1))
# constitution = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',2))
# dexterity = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',3))
# agility = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',4))
# awareness = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',5))
# personality = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',6))
# intelligence = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',7))
# wisdom = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',8.png))
# willpower = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',9))
# luck = int(linecache.getline('MainMenuRes/char_statistic/charattributes.txt',10))

#def check_stats():
attributes = []
with open('MainMenuRes/char_statistic/charattributes.txt') as f:
    attribute = f.readlines()
count = 0
for attribute in attributes:
    count += 1

strength = int(attribute[0])
constitution = int(attribute[1])
dexterity = int(attribute[2])
agility = int(attribute[3])
awareness = int(attribute[4])
personality = int(attribute[5])
intelligence = int(attribute[6])
wisdom = int(attribute[7])
willpower = int(attribute[8])
luck = int(attribute[9])
#---------------------------------------------techniques-------------------------------------

stats_sk = []
with open('MainMenuRes/char_statistic/charskirmish.txt') as f:
    skirmish = f.readlines()
count = 0
for skirmish in stats_sk:
    count += 1

skirmish_tree = []
melee = int(skirmish[0])
ranged = int(skirmish[1])
parrying = int(skirmish[2])
athletics = int(skirmish[3])
intimidation = int(skirmish[4])
tactics = int(skirmish[5])
arming = int(skirmish[6])
siege = int(skirmish[7])
skirmish_tree.append(melee)
skirmish_tree.extend((ranged,parrying,athletics,intimidation,tactics,arming,siege))

stats_sr = []
with open('MainMenuRes/char_statistic/charsurvive.txt') as f:
    survival = f.readlines()
count = 0
for survival in stats_sr:
    count += 1

survival_tree = []
acrobatics = int(survival[0])
stealth = int(survival[1])
thievery = int(survival[2])
lockpicking = int(survival[3])
deception = int(survival[4])
traps = int(survival[5])
stupefy = int(survival[6])
nature = int(survival[7])
survival_tree.append(acrobatics)
survival_tree.extend((stealth,thievery,lockpicking,deception,traps,stupefy,nature))

stats_sv = []
with open('MainMenuRes/char_statistic/charsavviness.txt') as f:
    savviness = f.readlines()
count = 0
for savviness in stats_sv:
    count += 1

savviness_tree = []
investigation = int(savviness[0])
medicine = int(savviness[1])
lore = int(savviness[2])
persuasion = int(savviness[3])
arcane = int(savviness[4])
divine = int(savviness[5])
alchemy = int(savviness[6])
engineering = int(savviness[7])
savviness_tree.append(investigation)
savviness_tree.extend((medicine,lore,persuasion,arcane,divine,alchemy,engineering))


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# def update_savviness ():
#     investigation = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',1))
#     medicine = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',2))
#     lore = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',3))
#     persuasion = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',4))
#     arcane = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',5))
#     divine = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',6))
#     alchemy = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',7))
#     engineering = int(linecache.getline('MainMenuRes/char_statistic/charsavviness.txt',8.png))
# #-----------------------------------------------------------------------------------
# def update_survival ():
#     acrobatics = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',1))
#     stealth = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',2))
#     thievery = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',3))
#     lockpicking = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',4))
#     deception = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',5))
#     traps = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',6))
#     stupefy = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',7))
#     nature = int(linecache.getline('MainMenuRes/char_statistic/charsurvive.txt',8.png))

# def update_skirmish ():
#     melee = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',1))
#     ranged = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',2))
#     parrying = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',3))
#     athletics = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',4))
#     intimidation = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',5))
#     tactics = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',6))
#     arming = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',7))
#     siege = int(linecache.getline('MainMenuRes/char_statistic/charskirmish.txt',8.png))

# def update_resistances ():
#     threshold = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',1))
#     defence = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',2))
#     arcana_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',3))
#     energy_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',4))
#     frost_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',5))
#     fire_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',6))
#     poison_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',7))

# resistance_box = []
# threshold = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',1))
# defence = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',2))
# arcana_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',3))
# energy_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',4))
# frost_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',5))
# fire_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',6))
# poison_res = int(linecache.getline('MainMenuRes/char_statistic/charres.txt',7))
# resistance_box.append(threshold)
# resistance_box.extend((defence,arcana_res,energy_res,frost_res,fire_res,poison_res))
#-----------------------------------------------------------------------------------
# def update_attack_box():
#     melee_damage = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',1))
#     ranged_damage = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',2))
#     critical_strike = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',3))
#block = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',4))
#parry = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',5))
#     leadership  = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',5))


# attack_box = []
# melee_damage = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',1))
# ranged_damage = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',2))
# critical_strike = int(linecache.getline('MainMenuRes/char_statistic/charattack.txt',3))
# attack_box.append(melee_damage)
# attack_box.extend((ranged_damage,critical_strike))
#-----------------------------------------------------------------------------------
# def update_secondary_stats ():
#     tricks = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',1))
#     supply = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',2))
#     health_points = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',3))
#     armor_points = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',4))
#     leadership  = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',5))

# tricks = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',1))
# supply = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',2))
# health_points = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',3))
# armor_points = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',4))
# # stat_distributable = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',5))
# # char_experience = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',6))
# # char_level = int(linecache.getline('MainMenuRes/char_statistic/charsecondary.txt',7))



#-----------------------------------------------------------------------------------
# def update_bonus_stats ():
#     bonus_ranged_damage = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',1))
#     bonus_melee_damage = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',2))
#     bonus_critical_strike = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',3))
#     bonus_tricks = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',4))
#     bonus_supply = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',5))
#     bonus_health_points = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',6))
#     bonus_armor_points = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',7))
#     bonus_threshold = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',8.png))
#     bonus_defence = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',9))
#     bonus_arcana_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',10))
#     bonus_energy_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',11))
#     bonus_frost_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',12))
#     bonus_fire_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',13))
#     bonus_poison_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',14))
#     bonus_melee = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',1))
#     bonus_ranged = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',2))
#     bonus_parrying = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',3))
#     bonus_athletics = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',4))
#     bonus_intimidation = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',5))
#     bonus_tactics = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',6))
#     bonus_arming = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',7))
#     bonus_siege = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',8.png))
#     bonus_acrobatics = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',9))
#     bonus_stealth = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',10))
#     bonus_thievery =int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',11))
#     bonus_lockpicking = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',12))
#     bonus_deception =int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',13))
#     bonus_traps = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',14))
#     bonus_stupefy = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',15))
#     bonus_nature = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',16))
#     bonus_investigation = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',17))
#     bonus_medicine = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',18))
#     bonus_lore = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',19))
#     bonus_persuasion = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',20))
#     bonus_arcane = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',21))
#     bonus_divine = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',22))
#     bonus_alchemy = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',23))
#     bonus_engineering = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',24))
#
# bonus_ranged_damage = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',1))
# bonus_melee_damage = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',2))
# bonus_critical_strike = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',3))
#
# bonus_tricks = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',4))
# bonus_supply = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',5))
# bonus_health_points = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',6))
# bonus_armor_points = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',7))
#
# bonus_threshold = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',8.png))
# bonus_defence = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',9))
# bonus_arcana_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',10))
# bonus_energy_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',11))
# bonus_frost_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',12))
# bonus_fire_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',13))
# bonus_poison_res = int(linecache.getline('MainMenuRes/char_statistic/charbonussecondary.txt',14))
#
# bonus_melee = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',1))
# bonus_ranged = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',2))
# bonus_parrying = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',3))
# bonus_athletics = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',4))
# bonus_intimidation = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',5))
# bonus_tactics = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',6))
# bonus_arming = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',7))
# bonus_siege = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',8.png))
# bonus_skirmish = []
# bonus_skirmish.extend((bonus_melee, bonus_ranged, bonus_parrying,
#                        bonus_athletics,bonus_intimidation, bonus_tactics,
#                        bonus_arming, bonus_siege))
# bonus_acrobatics = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',9))
# bonus_stealth = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',10))
# bonus_thievery =int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',11))
# bonus_lockpicking = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',12))
# bonus_deception =int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',13))
# bonus_traps = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',14))
# bonus_stupefy = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',15))
# bonus_nature = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',16))
# bonus_survival = []
# bonus_survival.extend((bonus_acrobatics, bonus_stealth, bonus_thievery,
#                        bonus_lockpicking,bonus_deception, bonus_traps,
#                        bonus_stupefy, bonus_nature))
# bonus_investigation = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',17))
# bonus_medicine = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',18))
# bonus_lore = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',19))
# bonus_persuasion = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',20))
# bonus_arcane = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',21))
# bonus_divine = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',22))
# bonus_alchemy = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',23))
# bonus_engineering = int(linecache.getline('MainMenuRes/char_statistic/charbonusstats.txt',24))
# bonus_savviness = []
# bonus_savviness.extend((bonus_investigation, bonus_medicine, bonus_lore,
#                         bonus_persuasion,bonus_arcane, bonus_divine,
#                         bonus_alchemy, bonus_engineering))

#-------------------------------------------------------------------------------------
# Cartographer = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',1))
# Combo = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',2))
# Educated = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',3))
# Quick_Shot = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',4))
# Camp_Doctor = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',5))
# Thief = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',6))
# Quartermaster = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',7))
# Scout = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',8.png))
# Haggler = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',9))
# Estates = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',10))
# Curse = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',11))
# Healing = str(linecache.getline('MainMenuRes/char_statistic/techniques_novice.txt',12))
# #-------------------------------------------------------------------------------------
# Snake_Eater = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',1))
# Power_Blow = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',2))
# Scholar = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',3))
# Multiple_Shot = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',4))
# Duelist = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',5))
# Bear_Trap = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',6))
# Potion_Master = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',7))
# Knock_Down = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',8.png))
# Battle_Reflex = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',9))
# Persevere = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',10))
# Moon_Shield = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',11))
# Purifier = str(linecache.getline('MainMenuRes/char_statistic/techniques_adept.txt',12))
# #-------------------------------------------------------------------------------------
# Readiness = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',1))
# Slice = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',2))
# Field_Engineer = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',3))
# Deadeye = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',4))
# Barrage = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',5))
# Shields_Up = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',6))
# War_Engineer = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',7))
# Charge = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',8.png))
# Reaper = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',9))
# Troll_Skin = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',10))
# Dream_Cloud = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',11))
# Second_Wind = str(linecache.getline('MainMenuRes/char_statistic/techniques_expert.txt',12))
# #-------------------------------------------------------------------------------------
# Backstab = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',1))
# Weak_Spot = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',2))
# Siege_Master = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',3))
# Piercing_Arrows = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',4))
# Planewalker = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',5))
# Commander = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',6))
# Master_Mechanist = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',7))
# Battle_Prudence = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',8.png))
# Channelling = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',9))
# Divine_Intervention = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',10))
# Shadows = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',11))
# Blessing = str(linecache.getline('MainMenuRes/char_statistic/techniques_master.txt',12))


# ---------------------------------------MapCollisions----------------------------------------
# red_image = pygame.image.load("WorldMap/redcube.png").convert_alpha()
# red_image = pygame.transform.scale(red_image, (int(WINDOW_SIZE[0]*0.02),(int(WINDOW_SIZE[1]*0.02))))
#
# RED_TILE = red_image.get_height()
#
# def load_map(path):
#     f = open(path +'.txt', 'r')
#     data = f.read()
#     f.close()
#     data = data.split('\n')
#     collisions_map = []
#     for row in data:
#         collisions_map.append(list(row))
#     return collisions_map
# collisions_map = load_map('WorldMap/WestradColMap')
#
# tile_rects = []
# y = 0
# for row in collisions_map:
#     x = 0
#     for tile in row:
#         if tile == '1':
#             display.blit(red_image, (x*RED_TILE-scroll[0],y*RED_TILE-scroll[1]))   #MapScrolling
#
#         #---------------Keeping Track of 0 tiles for collission---------------
#         if tile not in ('0'):
#             tile_rects.append(pygame.Rect(x*RED_TILE-scroll[0], y*RED_TILE-scroll[1], RED_TILE, RED_TILE))
#         x += 1
#     y +=1
#
#     for i in tile_rects:
#         pygame.draw.rect(display, (255,0,0), i)



# class WorldParty:
#     def __init__(self, max_vel, rotation_vel):
#         self.img = self.IMG
#         self.max_vel = max_vel
#         self.vel = 0
#         self.rotation_vel = rotation_vel
#         self.angle = 0
#         self.x,self.y = self.START_POS
#         self.acceleration = 0.1
#         self.rect = self.img.get_rect()
#
#     def rotate(self, left=False, right=False):
#         if left:
#             self.angle +=self.rotation_vel
#         elif right:
#             self.angle -=self.rotation_vel
#
#     def draw(self,win):
#         blit_rotate_center(win,self.img,(self.x,self.y), self.angle)
#
#     def move_forward(self):
#         self.vel = min(self.vel + self.acceleration, self.max_vel)
#         self.move()
#
#     def move_backward(self):
#         self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
#         self.move()
#
#     def move(self):
#         radians = math.radians(self.angle)
#         vertical = math.cos(radians)*self.vel
#         horizontal = math.sin(radians)*self.vel
#         self.y -= vertical
#         self.x -= horizontal
#
#     def collide(self,mask,x=0,y=0):
#         party_mask = pygame.mask.from_surface(self.img)
#         offset = (int(self.x-x), int(self.y-y))
#         poi = mask.overlap(party_mask,offset)
#         return poi
#
#     def reset(self):
#         self.x, self.y = self.START_POS
#         self.vel = 0
#         self.angle = 0
#
# class PlayerParty(WorldParty):
#     IMG = gm_party_icon
#     START_POS = (180-scroll[0],200-scroll[1])
#     def reduce_speed(self):
#         self.vel = max(self.vel - self.acceleration / 2,0)
#         self.move()
#     def bounce (self):
#         self.vel = -self.vel / 2
#         self.move()
#
# def draw(win, images, player_icon):
#     for img,pos in images:
#         win.blit(img,pos)
#     player_icon.draw(win)
#     pygame.display.update()
#
# def move_player(player_icon):
#     keys = pygame.key.get_pressed()
#     moved = False
#     if keys[pygame.K_a]:
#         player_icon.rotate(left=True)
#     if keys[pygame.K_d]:
#         player_icon.rotate(right=True)
#     if keys[pygame.K_w]:
#         moved = True
#         player_icon.move_forward()
#     if keys[pygame.K_s]:
#         moved = True
#         player_icon.move_backward()
#     if not moved:
#         player_icon.reduce_speed()

