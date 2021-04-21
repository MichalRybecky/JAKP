import pygame
from settings import WIN, FPS
from utils.load_assets import BACK, BG, MAIN_FONT, FONT_COLOR

pygame.init()

font = MAIN_FONT

def vsemocna_kalkulacka_app():

    B_BACK = pygame.Rect(20, 20, 60, 60)
    cooldown = 0
    clock = pygame.time.Clock()

    # pravdy a klamstva
    run = True
    click = False
    while run:

        # obrazovka + back button
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (20, 20))

        kalkul_1 = font.render("Obsah a Objem", True, FONT_COLOR)
        WIN.blit(kalkul_1, (170, 150))
        kalkul_2 = font.render("Premena jednotiek", True, FONT_COLOR)
        WIN.blit(kalkul_2, (150, 250))
        kalkul_3 = font.render("Štatistika", True, FONT_COLOR)
        WIN.blit(kalkul_3, (150, 350))
        kalkul_4 = font.render("Financie", True, FONT_COLOR)
        WIN.blit(kalkul_4, (150, 450))
        kalkul_5 = font.render("Kvadratická rovnica", True, FONT_COLOR)
        WIN.blit(kalkul_5, (150, 550))

        pos_x, pos_y = pygame.mouse.get_pos()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        # after click
        if click:
            if B_BACK.collidepoint(pos_x, pos_y):
                run = False

        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)
