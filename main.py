"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""
import os
import pygame

from settings import *
from utils.load_assets import *
from utils.connectivity import internet as connection_check
from utils.load_user_settings import return_user_settings
from apps.kebab import kebab_app
from apps.meny import meny_app
from apps.stocks import stocks_app


# PyGame setup
pygame.init()
pygame.display.set_caption("JAKP")
pygame.display.set_icon(ICON)


def main():
    run = True
    click = False
    exit_cooldown = 0
    clock = pygame.time.Clock()

    WIN.blit(BG_LOADING, (0, 0))
    pygame.display.update()

    internet = connection_check()
    #if not internet:
    #    MENY = MENY_M
    #    STOCKS = STOCKS_M

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
        WIN.blit(BG, (0, 0))

        # BLITING ICONS
        WIN.blit(KEBAB, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H // 3))
        WIN.blit(A_SORT, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H // 3))
        WIN.blit(CASE, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H - ICON_SIZE))
        WIN.blit(LIFE, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H - ICON_SIZE))
        WIN.blit(MATHE, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H + ICON_SIZE - 30))
        WIN.blit(CALCUL, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H + ICON_SIZE - 30))
        WIN.blit(MENY, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H * 3 // 2 + 40))
        WIN.blit(STOCKS, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H * 3 // 2 + 40))
        WIN.blit(X, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        # Button Activations
        if click:
            if B_KEBAB.collidepoint(pos_x, pos_y):
                print("KEBAB")
            elif B_A_SORT.collidepoint(pos_x, pos_y):
                print("A_SORT")
            elif B_CASE.collidepoint(pos_x, pos_y):
                print("CASE")
            elif B_LIFE.collidepoint(pos_x, pos_y):
                print("LIFE")
            elif B_MATHE.collidepoint(pos_x, pos_y):
                print("MATHE")
            elif B_CALCUL.collidepoint(pos_x, pos_y):
                print("CALCUL")
            elif B_MENY.collidepoint(pos_x, pos_y):
                meny_app()
                exit_cooldown = FPS // 3
            elif B_STOCKS.collidepoint(pos_x, pos_y):
                stocks_app()
                exit_cooldown = FPS // 3
            elif B_MENU.collidepoint(pos_x, pos_y):
                print("MENU")    
            elif B_X.collidepoint(pos_x, pos_y) and exit_cooldown == 0:
                run = False    

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

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
