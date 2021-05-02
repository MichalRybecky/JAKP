import pygame
from settings import WIN, FPS
from utils.load_assets import BACK, BG_vsemocna_L, BG_vsemocna_D, MAIN_FONT, FONT_COLOR_L, FONT_COLOR_D
from apps.kvadraticka_rovnica import kvadraticka_app
from utils.user_settings_handling import return_user_settings

pygame.init()

font = MAIN_FONT


def vsemocna_kalkulacka_app():
    B_BACK = pygame.Rect(20, 20, 60, 60)
    kalkul_kvadraticka = pygame.Rect(110, 625, 280, 80)
    cooldown = 0
    clock = pygame.time.Clock()

    # pravdy a klamstva
    run_vsemocna = True
    click = False
    while run_vsemocna:

        user_settings = return_user_settings()

        if user_settings["theme"] == "light":
            BG_vsemocna = BG_vsemocna_L
            FONT_COLOR = FONT_COLOR_L
        else:
            BG_vsemocna = BG_vsemocna_D
            FONT_COLOR = FONT_COLOR_D

        # obrazovka + back button
        WIN.blit(BG_vsemocna, (0, 0))
        WIN.blit(BACK, (20, 20))

        kalkul_1 = font.render("Obsah a Objem", True, FONT_COLOR)
        WIN.blit(kalkul_1, (170, 170))
        kalkul_2 = font.render("Premena jednotiek", True, FONT_COLOR)
        WIN.blit(kalkul_2, (150, 290))
        kalkul_3 = font.render("Štatistika", True, FONT_COLOR)
        WIN.blit(kalkul_3, (200, 410))
        kalkul_4 = font.render("Financie", True, FONT_COLOR)
        WIN.blit(kalkul_4, (205, 530))
        kalkul_5 = font.render("Kvadratická rovnica", True, FONT_COLOR)
        WIN.blit(kalkul_5, (145, 650))

        pos_x, pos_y = pygame.mouse.get_pos()

        # events
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        # after click
        if click:

            if B_BACK.collidepoint(pos_x, pos_y) and cooldown == 0:
                run_vsemocna = False
            if kalkul_kvadraticka.collidepoint(pos_x, pos_y) and cooldown == 0:
                kvadraticka_app()

        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)
