"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""
import os
import pygame

import utils.create_user_files
from settings import *
from utils.load_assets import *
from utils.connectivity import internet as connection_check
from utils.user_settings_handling import return_user_settings

from apps.settings_menu import settings_menu
from apps.meny import meny_app
from apps.stocks import stocks_app
from apps.kalkulacka_zivota import kalkulacka_zivota_app
from apps.kebab import kebab_app
from apps.vsemocna_kalkulacka import vsemocna_kalkulacka_app
from apps.case_inv import cases_app_inv
from apps.abeceda import abeceda_app
from apps.kalkulacka import kalkulacka_app

# Meny app importy
import http.client
import xml.etree.ElementTree as ET

# PyGame setup
pygame.init()
pygame.display.set_caption("JAKP")
pygame.display.set_icon(ICON)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def return_conversion_list(): 
    conn = http.client.HTTPSConnection("www.ecb.europa.eu")
    conn.request("GET", "/stats/eurofxref/eurofxref-daily.xml")
    res = conn.getresponse()
    data = res.read()
    root = ET.fromstring(data)
    rates = {}
    for i in root[2][0]:
        entry = i.attrib
        rates.update({entry["currency"]: float(entry["rate"])})
    return rates

def main():
    run = True
    click = False
    exit_cooldown = 0
    no_internet_label_cooldown = 0
    clock = pygame.time.Clock()


    user_settings = return_user_settings()
    if user_settings["theme"] == "light":
        BG = BG_L
        BG_LOADING = BG_LOADING_L
        FONT_COLOR = FONT_COLOR_L
    else:
        BG = BG_D
        BG_LOADING = BG_LOADING_D
        FONT_COLOR = FONT_COLOR_D

    WIN.blit(BG_LOADING, (0, 0))
    pygame.display.update()

    # Miesto pre robenie connections pre appky ktore to potrebuju
    internet = connection_check()
    if internet:
        rates = return_conversion_list()
    else:
        B_RECONNECT = pygame.Rect(WIDTH_H - 80, 30, 160, 50)
        label_no_internet = BIG_FONT.render("No internet connection", 1, (255, 0, 0))
        label_reconnect = MAIN_FONT.render("Reconnect", 1, FONT_COLOR)

    # BUTTONS INITIALIZATION
    B_KEBAB = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H // 3, ICON_SIZE, ICON_SIZE)
    B_A_SORT = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H // 3, ICON_SIZE, ICON_SIZE)
    B_CASE = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H - ICON_SIZE, ICON_SIZE, ICON_SIZE)
    B_LIFE = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H - ICON_SIZE, ICON_SIZE, ICON_SIZE)
    B_MATHE = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H + ICON_SIZE - 30, ICON_SIZE, ICON_SIZE)
    B_CALCUL = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H + ICON_SIZE - 30, ICON_SIZE, ICON_SIZE)
    B_MENY = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H * 3 // 2 + 40, ICON_SIZE, ICON_SIZE)
    B_STOCKS = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H * 3 // 2 + 40, ICON_SIZE, ICON_SIZE)
    B_X = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 60 - 20, 20, 60, 60)


    # main app loop
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        BG = BG_L if user_settings["theme"] == "light" else BG_D
        WIN.blit(BG, (0, 0))

        if not internet:
            WIN.blit(BUTTON, (WIDTH_H - 80, 30))
            WIN.blit(label_reconnect, (WIDTH_H - 60, 40))

        # BLITING ICONS
        WIN.blit(KEBAB, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H // 3))
        WIN.blit(A_SORT, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H // 3))
        WIN.blit(CASE, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H - ICON_SIZE))
        WIN.blit(LIFE, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H - ICON_SIZE))
        WIN.blit(MATHE, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H + ICON_SIZE - 30))
        WIN.blit(CALCUL, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H + ICON_SIZE - 30))
        WIN.blit(X, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        if internet:
            WIN.blit(MENY, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H * 3 // 2 + 40))
            WIN.blit(STOCKS, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H * 3 // 2 + 40))
        else:
            WIN.blit(MENY_M, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H * 3 // 2 + 40))
            WIN.blit(STOCKS_M, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H * 3 // 2 + 40))

        # Button Activations
        if click:
            if B_KEBAB.collidepoint(pos_x, pos_y):
                kebab_app()
                exit_cooldown = FPS // 3
            elif B_A_SORT.collidepoint(pos_x, pos_y):
                abeceda_app()
                exit_cooldown = FPS // 3
            elif B_CASE.collidepoint(pos_x, pos_y):
                cases_app_inv()
                exit_cooldown = FPS // 3
            elif B_LIFE.collidepoint(pos_x, pos_y):
                kalkulacka_zivota_app()
                exit_cooldown = FPS // 3
            elif B_MATHE.collidepoint(pos_x, pos_y):
                vsemocna_kalkulacka_app()
                exit_cooldown = FPS // 3
            elif B_CALCUL.collidepoint(pos_x, pos_y):
                kalkulacka_app()
                exit_cooldown = FPS // 3
            elif B_MENY.collidepoint(pos_x, pos_y):
                if internet:
                    meny_app(rates)
                    exit_cooldown = FPS // 3
                else:
                    no_internet_label_cooldown = 180
            elif B_STOCKS.collidepoint(pos_x, pos_y):
                if internet:
                    stocks_app()
                    exit_cooldown = FPS // 3
                else:
                    no_internet_label_cooldown = 180
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
                user_settings = return_user_settings()
            elif B_X.collidepoint(pos_x, pos_y) and exit_cooldown == 0:
                run = False
            if not internet:
                if B_RECONNECT.collidepoint(pos_x, pos_y):
                    internet = connection_check()
                if internet:
                    rates = return_conversion_list()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        # exit_cooldown preventuje exit po double clicku na back button z jednotlivych appiek
        if exit_cooldown > 0:
            exit_cooldown -= 1

        if no_internet_label_cooldown > 0:
            WIN.blit(label_no_internet, (WIDTH_H - 200, HEIGHT - 80))
            no_internet_label_cooldown -= 1

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
