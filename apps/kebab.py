import pygame
from settings import WIN
from utils.load_assets import BG

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
