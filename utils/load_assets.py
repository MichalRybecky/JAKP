"""
Module na loadnutie assetov z assets filu,
aby sme v main.py nemali bordel
"""

import os
import pygame

from utils.load_user_settings import return_user_settings
from settings import WIDTH, HEIGHT, ICON_SIZE, ICON_SIZE_H


pygame.init()

user_settings = return_user_settings()
if user_settings["theme"] == "light": 
    BG_LOADING = pygame.image.load(os.path.join("assets", "wallpaper-loading-l.png"))
    BG = pygame.image.load(os.path.join("assets", "wallpaper-blank-w.png"))
    BG_kebab = pygame.image.load(os.path.join("assets", "kebab-l.png"))
    BG_kebab = pygame.transform.scale(BG_kebab, (500, 900))
    BG_MENY = pygame.image.load(os.path.join("assets", "premena_mien.png"))
    BG_STOCKS = pygame.image.load(os.path.join("assets", "stock_market.png"))
    FONT_COLOR = (10, 10, 10)
else:
    BG_LOADING = pygame.image.load(os.path.join("assets", "wallpaper-loading-d.png"))
    BG = pygame.image.load(os.path.join("assets", "wallpaper-blank-d.png"))
    BG_MENY = pygame.image.load(os.path.join("assets", "premena_mien-d.png"))
    BG_STOCKS = pygame.image.load(os.path.join("assets", "stock_market-d.png"))
    BG_kebab = pygame.image.load(os.path.join("assets", "kebab-d.png"))
    BG_kebab = pygame.transform.scale(BG_kebab, (500, 900))
    FONT_COLOR = (255, 255, 255)

BG_LOADING = pygame.transform.scale(BG_LOADING, (500, 900))
BG = pygame.transform.scale(BG, (500, 900))
BG_MENY = pygame.transform.scale(BG_MENY, (500, 900))
BG_STOCKS = pygame.transform.scale(BG_STOCKS, (500, 900))

MAIN_FONT = pygame.font.Font("pixel_font.ttf", 12)
BIG_FONT = pygame.font.Font("pixel_font.ttf", 20)
SMALL_FONT = pygame.font.Font("pixel_font.ttf", 8)
MENU = pygame.image.load(os.path.join("assets", "menu.png"))
MENU = pygame.transform.scale(MENU, (65, 65))
BACK = pygame.image.load(os.path.join("assets", "back.png"))
BACK = pygame.transform.scale(BACK, (65, 65))
X = pygame.image.load(os.path.join("assets", "x.png"))
X = pygame.transform.scale(X, (65, 65))
ICON = pygame.image.load(os.path.join("assets", "logo-stvorec.png"))
BUTTON = pygame.image.load(os.path.join("assets", "reconnect.png"))
BUTTON = pygame.transform.scale(BUTTON, (160, 50))

KEBAB = pygame.image.load(os.path.join("assets", "kebab_101.png"))
KEBAB = pygame.transform.scale(KEBAB, (ICON_SIZE, ICON_SIZE))
A_SORT = pygame.image.load(os.path.join("assets", "male_a.png"))
A_SORT = pygame.transform.scale(A_SORT, (ICON_SIZE, ICON_SIZE))
CASE = pygame.image.load(os.path.join("assets", "case.png"))
CASE = pygame.transform.scale(CASE, (ICON_SIZE, ICON_SIZE))
MENY = pygame.image.load(os.path.join("assets", "meny.png"))
MENY = pygame.transform.scale(MENY, (ICON_SIZE, ICON_SIZE))
MENY_M = pygame.image.load(os.path.join("assets", "meny_monochrom.png"))
MENY_M = pygame.transform.scale(MENY_M, (ICON_SIZE, ICON_SIZE))
LIFE = pygame.image.load(os.path.join("assets", "life_is_life.png"))
LIFE = pygame.transform.scale(LIFE, (ICON_SIZE, ICON_SIZE))
MATHE = pygame.image.load(os.path.join("assets", "cis_sustavy_smol.png"))
MATHE = pygame.transform.scale(MATHE, (ICON_SIZE, ICON_SIZE))
CALCUL = pygame.image.load(os.path.join("assets", "mathe_calc_smol.png"))
CALCUL = pygame.transform.scale(CALCUL, (ICON_SIZE, ICON_SIZE))
SSDLS = pygame.image.load(os.path.join("assets", "ssdls_logo.jpg"))
SSDLS = pygame.transform.scale(SSDLS, (ICON_SIZE, ICON_SIZE))
STOCKS = pygame.image.load(os.path.join("assets", "stocks.png"))
STOCKS = pygame.transform.scale(STOCKS, (ICON_SIZE, ICON_SIZE))
STOCKS_M = pygame.image.load(os.path.join("assets", "stocks_monochrom.png"))
STOCKS_M = pygame.transform.scale(STOCKS_M, (ICON_SIZE, ICON_SIZE))
