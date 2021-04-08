"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""

import os
import pygame

HEIGHT = 900
WIDTH = 500

HEIGHT_H = HEIGHT // 2
WIDTH_H = WIDTH // 2

# PyGame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JAKP")
main_font = pygame.font.Font("pixel_font.ttf", 12)

# Loading assets
# ked tu toho bude vela, nadzigat do samostatneho modulu
# BG = pygame.transform.scale(
#        pygame.image.load(os.path.join("bg.png")), (WIDTH, HEIGHT))

icon_size = 110
icon_size_h = icon_size // 2
KEBAB = pygame.image.load(os.path.join("assets", "kebab_101.png"))
KEBAB = pygame.transform.scale(KEBAB, (icon_size, icon_size))


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
        # WIN.blit(BG, (0, 0))
        pygame.draw.rect(WIN, (220, 220, 220), pygame.Rect(0, 0, WIDTH, HEIGHT))

        pos_x, pos_y = pygame.mouse.get_pos()

        # kebab
        WIN.blit(KEBAB, ((WIDTH_H - icon_size_h) // 2, HEIGHT_H // 3))
        label_kebab = main_font.render("Kebab", 1, (10, 10, 10))
        WIN.blit(
            label_kebab,
            (
                (WIDTH_H - (label_kebab.get_width() // 2)) // 2 + 20,
                (HEIGHT_H // 3) + icon_size,
            ),
        )

        # stvorcove templaty pre nove appky
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H // 3, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2, HEIGHT_H - icon_size, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H - icon_size, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H - icon_size, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2, HEIGHT_H + icon_size - 30, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H + icon_size - 30, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2, HEIGHT_H * 3 // 2 + 40, icon_size, icon_size
            ),
        )
        pygame.draw.rect(
            WIN,
            (204, 204, 204),
            pygame.Rect(
                (WIDTH_H - icon_size_h) // 2 * 3, HEIGHT_H * 3 // 2 + 40, icon_size, icon_size
            ),
        )

        # Button Activations
        # if b_1.collidepoint(pos_x, pos_y):
        #    if click:
        #        print("si klikol, gratulka jak sa hovori")

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
