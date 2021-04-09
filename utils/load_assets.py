"""
Module na loadnutie assetov z assets filu,
aby sme v main.py nemali bordel
"""

import os
import pygame

WIDTH, HEIGHT = 900, 500

pygame.init()

icon_size = 110
icon_size_h = icon_size // 2

BG = pygame.image.load(os.path.join("assets", "wall_flat.png"))
BG = pygame.transform.scale(BG, (500, 900))
KEBAB = pygame.image.load(os.path.join("assets", "kebab_101.png"))
KEBAB = pygame.transform.scale(KEBAB, (icon_size, icon_size))
A_SORT = pygame.image.load(os.path.join("assets", "male_a.png"))
A_SORT = pygame.transform.scale(A_SORT, (icon_size, icon_size))
CASE = pygame.image.load(os.path.join("assets", "case.png"))
CASE = pygame.transform.scale(CASE, (icon_size, icon_size))
LIFE = pygame.image.load(os.path.join("assets", "life_is_life.png"))
LIFE = pygame.transform.scale(LIFE, (icon_size, icon_size))
MATHE = pygame.image.load(os.path.join("assets", "mathe.png"))
MATHE = pygame.transform.scale(MATHE, (icon_size, icon_size))
CALCUL = pygame.image.load(os.path.join("assets", "mathe_calc_smol.png"))
CALCUL = pygame.transform.scale(CALCUL, (icon_size, icon_size))
MENY = pygame.image.load(os.path.join("assets", "meny.png"))
MENY = pygame.transform.scale(MENY, (icon_size, icon_size))
SSDLS = pygame.image.load(os.path.join("assets", "ssdls_logo.jpg"))
SSDLS = pygame.transform.scale(SSDLS, (icon_size, icon_size))
STOCKS = pygame.image.load(os.path.join("assets", "stocks.png"))
STOCKS = pygame.transform.scale(STOCKS, (icon_size, icon_size))
