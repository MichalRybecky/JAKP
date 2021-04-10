"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""
import os
import pygame

from settings import *
from utils.load_assets import *
from utils.kebab import kebab_app
from utils.meny import meny_app


# PyGame setup
pygame.init()
pygame.display.set_caption("JAKP")


def main():
    run = True
    click = False
    # main app loop
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG, (0, 0))

        # BUTTONS
        B_KEBAB = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H // 3, ICON_SIZE, ICON_SIZE)
        B_A_SORT = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H // 3, ICON_SIZE, ICON_SIZE)
        B_CASE = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H - ICON_SIZE, ICON_SIZE, ICON_SIZE)
        B_LIFE = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H - ICON_SIZE, ICON_SIZE, ICON_SIZE)
        B_MATHE = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H + ICON_SIZE - 30, ICON_SIZE, ICON_SIZE)
        B_CALCUL = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H + ICON_SIZE - 30, ICON_SIZE, ICON_SIZE)
        B_MENY = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H * 3 // 2 + 40, ICON_SIZE, ICON_SIZE)
        B_STOCKS = pygame.Rect((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H * 3 // 2 + 40, ICON_SIZE, ICON_SIZE)

        B_X = pygame.Rect(10, 10, 60, 60)
        B_MENU = pygame.Rect(WIDTH - 60 - 10, 10, 60, 60)

        # ICONS
        WIN.blit(KEBAB, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H // 3))
        WIN.blit(A_SORT, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H // 3))
        WIN.blit(CASE, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H - ICON_SIZE))
        WIN.blit(LIFE, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H - ICON_SIZE))
        WIN.blit(MATHE, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H + ICON_SIZE - 30))
        WIN.blit(CALCUL, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H + ICON_SIZE - 30))
        WIN.blit(MENY, ((WIDTH_H - ICON_SIZE_H) // 2, HEIGHT_H * 3 // 2 + 40))
        WIN.blit(STOCKS, ((WIDTH_H - ICON_SIZE_H) // 2 * 3, HEIGHT_H * 3 // 2 + 40))

        WIN.blit(X, (10, 10))
        WIN.blit(MENU, (WIDTH - 60 - 10, 10))

        # LABELS
        # label_kebab = main_font.render("Kebab", 1, (10, 10, 10))
        # WIN.blit(
        #    label_kebab,
        #    (
        #        (WIDTH_H - (label_kebab.get_width() // 2)) // 2 + 20,
        #        (HEIGHT_H // 3) + ICON_SIZE,
        #    ),
        # )

        # Button Activations
        if click:
            print(f"si klikol: {pos_x}, {pos_y}")
            if B_KEBAB.collidepoint(pos_x, pos_y):
                print("KEBAB")
                kebab_app()
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
                print("MENY")
                meny_app()
            elif B_STOCKS.collidepoint(pos_x, pos_y):
                print("STOCKS")
            elif B_MENU.collidepoint(pos_x, pos_y):
                print("MENU")    
            elif B_X.collidepoint(pos_x, pos_y):
                run = False    

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

    pygame.quit()


if __name__ == "__main__":
    main()
