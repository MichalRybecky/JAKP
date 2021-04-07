"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""

import os
import pygame

HEIGHT=900
WIDTH=500

HEIGHT_H = HEIGHT // 2
WIDTH_H = WIDTH // 2

# PyGame setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JAKP")

# Loading assets
# ked tu toho bude vela, nadzigat do samostatneho modulu
#BG = pygame.transform.scale(
#        pygame.image.load(os.path.join("bg.png")), (WIDTH, HEIGHT))


def collide(obj1, obj2) -> bool:
    """
    vracia True/False hodnotu, ci sa objekty stretli
    """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def main():
    run = True
    click = False 
    # main app loop
    while run:
        #WIN.blit(BG, (0, 0))
        pygame.draw.rect(WIN, (100, 100, 100), pygame.Rect(0, 0, WIDTH, HEIGHT))

        pos_x, pos_y = pygame.mouse.get_pos()

        # Menu Buttons
        # skarede jak noc, zatial iba pre debbugovanie
        b_size = 40
        b_size_h = b_size // 2
        b_color = (204, 204, 204)
        b_1 = pygame.Rect((WIDTH_H // 2) - b_size_h, HEIGHT_H // 2, b_size, b_size)
        b_2 = pygame.Rect(WIDTH_H - b_size_h, HEIGHT_H // 2, b_size, b_size)
        b_3 = pygame.Rect((WIDTH_H // 2 * 3) - b_size_h, HEIGHT_H // 2, b_size, b_size)

        pygame.draw.rect(WIN, b_color, b_1)
        pygame.draw.rect(WIN, b_color, b_2)
        pygame.draw.rect(WIN, b_color, b_3)

        # Button Activations
        if b_1.collidepoint(pos_x, pos_y):
            if click:
                print("si klikol, gratulka jak sa hovori")

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
