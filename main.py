"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""

import os
import pygame

from utils.load_assets import *

HEIGHT = 900
WIDTH = 500

HEIGHT_H = HEIGHT // 2
WIDTH_H = WIDTH // 2
icon_size = 110

# PyGame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JAKP")
main_font = pygame.font.Font("pixel_font.ttf", 12)


def main():
    run = True
    click = False
    # main app loop
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG, (0, 0))

        # BUTTONS
        B_KEBAB = pygame.Rect((WIDTH_H - icon_size_h) // 2, HEIGHT_H // 3, icon_size, icon_size)
        B_A_SORT = pygame.Rect((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H // 3, icon_size, icon_size)
        B_CASE = pygame.Rect((WIDTH_H - icon_size_h) // 2, HEIGHT_H - icon_size, icon_size, icon_size)
        B_LIFE = pygame.Rect((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H - icon_size, icon_size, icon_size)
        B_MATHE = pygame.Rect((WIDTH_H - icon_size_h) // 2, HEIGHT_H + icon_size - 30, icon_size, icon_size)
        B_CALCUL = pygame.Rect((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H + icon_size - 30, icon_size, icon_size)
        B_MENY = pygame.Rect((WIDTH_H - icon_size_h) // 2, HEIGHT_H * 3 // 2 + 40, icon_size, icon_size)
        B_STOCKS = pygame.Rect((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H * 3 // 2 + 40, icon_size, icon_size)

        # ICONS
        WIN.blit(KEBAB, ((WIDTH_H - icon_size_h) // 2, HEIGHT_H // 3))
        WIN.blit(A_SORT, ((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H // 3))
        WIN.blit(CASE, ((WIDTH_H - icon_size_h) // 2, HEIGHT_H - icon_size))
        WIN.blit(LIFE, ((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H - icon_size))
        WIN.blit(MATHE, ((WIDTH_H - icon_size_h) // 2, HEIGHT_H + icon_size - 30))
        WIN.blit(CALCUL, ((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H + icon_size - 30))
        WIN.blit(MENY, ((WIDTH_H - icon_size_h) // 2, HEIGHT_H * 3 // 2 + 40))
        WIN.blit(STOCKS, ((WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H * 3 // 2 + 40))

        # LABELS
        # label_kebab = main_font.render("Kebab", 1, (10, 10, 10))
        # WIN.blit(
        #    label_kebab,
        #    (
        #        (WIDTH_H - (label_kebab.get_width() // 2)) // 2 + 20,
        #        (HEIGHT_H // 3) + icon_size,
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
            elif B_STOCKS.collidepoint(pos_x, pos_y):
                print("STOCKS")

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


def kebab_app():
    """
    GUI pre Kebab appku
    """
    run = True
    click = False
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG, (0, 0))
        ### Kod pod tento koment
        

        ### Kod nad tento koment
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
