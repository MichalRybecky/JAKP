"""
Module na loadnutie assetov z assets filu,
aby sme v main.py nemali bordel
"""

import os
import pygame

from settings import WIDTH, HEIGHT, ICON_SIZE, ICON_SIZE_H

pygame.init()

MAIN_FONT = pygame.font.Font("pixel_font.ttf", 12)
BIG_FONT = pygame.font.Font("pixel_font.ttf", 20)
SMALL_FONT = pygame.font.Font("pixel_font.ttf", 8)
BG = pygame.image.load(os.path.join("assets", "wallpaper-fade.png"))
BG = pygame.transform.scale(BG, (500, 900))
MENU = pygame.image.load(os.path.join("assets", "menu.png"))
MENU = pygame.transform.scale(MENU, (60, 60))
BACK = pygame.image.load(os.path.join("assets", "back.png"))
BACK = pygame.transform.scale(BACK, (60, 60))
BACK = pygame.image.load(os.path.join("assets", "back.png"))
BACK = pygame.transform.scale(BACK, (60, 60))
X = pygame.image.load(os.path.join("assets", "x.png"))
X = pygame.transform.scale(X, (65, 65))
ICON = pygame.image.load(os.path.join("assets", "logo-stvorec.png"))


KEBAB = pygame.image.load(os.path.join("assets", "kebab_101.png"))
KEBAB = pygame.transform.scale(KEBAB, (ICON_SIZE, ICON_SIZE))
A_SORT = pygame.image.load(os.path.join("assets", "male_a.png"))
A_SORT = pygame.transform.scale(A_SORT, (ICON_SIZE, ICON_SIZE))
CASE = pygame.image.load(os.path.join("assets", "case.png"))
CASE = pygame.transform.scale(CASE, (ICON_SIZE, ICON_SIZE))
LIFE = pygame.image.load(os.path.join("assets", "life_is_life.png"))
LIFE = pygame.transform.scale(LIFE, (ICON_SIZE, ICON_SIZE))
MATHE = pygame.image.load(os.path.join("assets", "cis_sustavy_smol.png"))
MATHE = pygame.transform.scale(MATHE, (ICON_SIZE, ICON_SIZE))
CALCUL = pygame.image.load(os.path.join("assets", "mathe_calc_smol.png"))
CALCUL = pygame.transform.scale(CALCUL, (ICON_SIZE, ICON_SIZE))
MENY = pygame.image.load(os.path.join("assets", "meny_smol.png"))
MENY = pygame.transform.scale(MENY, (ICON_SIZE, ICON_SIZE))
SSDLS = pygame.image.load(os.path.join("assets", "ssdls_logo.jpg"))
SSDLS = pygame.transform.scale(SSDLS, (ICON_SIZE, ICON_SIZE))
STOCKS = pygame.image.load(os.path.join("assets", "stocks.png"))
STOCKS = pygame.transform.scale(STOCKS, (ICON_SIZE, ICON_SIZE))
