import inspect
import pyautogui
from button import *
import pygame, sys, random,time,os
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



def initiate_dialog (surface, dialog_n):
    dialog_n.initiate(surface)
    if dialog_n.toggled == True:
        if dialog_n.phase == 0: dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"1",0,0,None,0,0)
        if dialog_n.phase == 1:
            dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"2",0,0,None,0,0)
            #dialog_0.get_line(display,"dialog",l_portrait_img[1],"rowan",0,"5",0,25,'Deception',deception,20)
        if dialog_n.phase == 2:dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"3",0,0,None,0,0)
        if dialog_n.phase == 3:dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"1",0,0)
        if dialog_n.phase == 4:dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"4",0,0,None,0,0)
        if dialog_n.phase == 5:dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"5",0,0,None,0,0)
        if dialog_n.phase == 6:dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"2",0,0)
        if dialog_n.phase == 7:dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"3",0,0)
        if dialog_n.phase == 8:dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"4",0,0)
        if dialog_n.phase == 9:dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"6",0,0,None,0,0)
        if dialog_n.phase == 10:
            dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"5",0,0)
            dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"5_1",0,25)
        if dialog_n.phase == 11:dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"6",0,0)
        if dialog_n.phase == 12:dialog_n.get_resp(surface,"dialog",r_portrait_img[2],"captain",0,"7",0,0)
        if dialog_n.phase == 13:dialog_n.get_line(surface,"dialog",l_portrait_img[1],"rowan",0,"7",0,0,None,0,0)
        if dialog_n.phase == 14:prologue.draw_story(surface,0,0)