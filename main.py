"""
JAKP

Hlavny file projektu,
menu, sluzi na spustanie modulov a submodulov
"""

import pygame
import os

HEIGHT=900
WIDTH=500

# PyGame setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JAKP")

# Loading assets
#BG = pygame.transform.scale(
#        pygame.image.load(os.path.join("bg.png")), (WIDTH, HEIGHT))

def main():
    run = True
    click = False 
    # main app loop
    while run:
        #WIN.blit(BG, (0, 0))

        pos_x, pos_y = pygame.mouse.get_pos()

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
